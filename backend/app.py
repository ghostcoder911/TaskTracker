from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import ChatBot
from sheets_api import SheetsAPI
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Initialize components
sheets_api = SheetsAPI()
active_sessions = {}

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

@app.route('/api/start-session', methods=['POST'])
def start_session():
    """Initialize a new chat session"""
    data = request.json
    user_name = data.get('name', '').strip()
    check_type = data.get('check_type', 'start')  # 'start' or 'end'
    
    if not user_name:
        return jsonify({"error": "Name is required"}), 400
    
    session_id = f"{user_name}_{datetime.now().timestamp()}"
    chatbot = ChatBot(user_name, check_type)
    active_sessions[session_id] = {
        'chatbot': chatbot,
        'user_name': user_name,
        'check_type': check_type,
        'started_at': datetime.now().isoformat()
    }
    
    # Get first message
    initial_message = chatbot.get_next_question()
    
    return jsonify({
        "session_id": session_id,
        "message": initial_message,
        "progress": chatbot.get_progress()
    })

@app.route('/api/send-message', methods=['POST'])
def send_message():
    """Process user's message and return bot's response"""
    data = request.json
    session_id = data.get('session_id')
    user_message = data.get('message', '').strip()
    
    if not session_id or session_id not in active_sessions:
        return jsonify({"error": "Invalid session"}), 400
    
    session = active_sessions[session_id]
    chatbot = session['chatbot']
    
    # Process user's answer
    chatbot.process_answer(user_message)
    
    # Check if conversation is complete
    if chatbot.is_complete():
        # Save to Google Sheets
        try:
            sheets_api.save_checkin(
                user_name=session['user_name'],
                check_type=session['check_type'],
                responses=chatbot.get_responses()
            )
            
            # Clean up session
            del active_sessions[session_id]
            
            return jsonify({
                "message": "✅ All done! Your responses have been saved. Have a great day! 🌟",
                "completed": True,
                "progress": {"current": chatbot.total_questions, "total": chatbot.total_questions}
            })
        except Exception as e:
            return jsonify({
                "message": f"⚠️ Responses saved locally, but there was an issue with Google Sheets: {str(e)}",
                "completed": True,
                "progress": {"current": chatbot.total_questions, "total": chatbot.total_questions}
            })
    
    # Get next question
    next_message = chatbot.get_next_question()
    
    return jsonify({
        "message": next_message,
        "completed": False,
        "progress": chatbot.get_progress()
    })

@app.route('/api/cancel-session', methods=['POST'])
def cancel_session():
    """Cancel an active session"""
    data = request.json
    session_id = data.get('session_id')
    
    if session_id in active_sessions:
        del active_sessions[session_id]
    
    return jsonify({"message": "Session cancelled"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

