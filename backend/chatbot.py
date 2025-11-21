from datetime import datetime

class ChatBot:
    def __init__(self, user_name, check_type='start'):
        self.user_name = user_name
        self.check_type = check_type  # 'start' or 'end'
        self.current_question_index = 0
        self.responses = {}
        
        # Define questions based on check type
        if check_type == 'start':
            self.questions = [
                {
                    "id": "energy_check",
                    "question": "0️⃣ Energy Check: What's your energy drink or vibe this morning? ☕",
                    "label": "Energy Check"
                },
                {
                    "id": "progress_yesterday",
                    "question": "1️⃣ Progress: What key tasks did you complete yesterday? 📋",
                    "label": "Yesterday's Progress"
                },
                {
                    "id": "today_focus",
                    "question": "2️⃣ Today's Focus: What are the top 1–3 priorities you're focusing on today? 🎯",
                    "label": "Today's Priorities"
                },
                {
                    "id": "blockers",
                    "question": "3️⃣ Blockers: Anything slowing you down or you need help with? 🚧",
                    "label": "Blockers"
                },
                {
                    "id": "state_of_mind",
                    "question": "4️⃣ State of Mind: One word for how you're feeling as you start the day? 💭",
                    "label": "State of Mind"
                }
            ]
            self.greeting = f"Good morning, {user_name}! 🌅 Let's do your start-of-day check-in."
        else:  # end of day
            self.questions = [
                {
                    "id": "wins",
                    "question": "1️⃣ Wins: What did you accomplish today (big or small)? 🎉",
                    "label": "Today's Wins"
                },
                {
                    "id": "learnings",
                    "question": "2️⃣ Learnings: Anything new you learned or discovered? 💡",
                    "label": "Learnings"
                },
                {
                    "id": "stuck_points",
                    "question": "3️⃣ Stuck Points: Any challenges you faced today? 🤔",
                    "label": "Challenges"
                },
                {
                    "id": "tomorrow_prep",
                    "question": "4️⃣ Tomorrow Prep: What will be your focus tomorrow? 🔜",
                    "label": "Tomorrow's Focus"
                },
                {
                    "id": "mood_check",
                    "question": "5️⃣ Mood Check: How are you ending the day? 🌙",
                    "label": "Ending Mood"
                }
            ]
            self.greeting = f"Good evening, {user_name}! 🌇 Let's wrap up your day with a quick check-out."
        
        self.total_questions = len(self.questions)
        self.started = False
    
    def get_next_question(self):
        """Get the next question to ask"""
        if not self.started:
            self.started = True
            return self.greeting
        
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            return question['question']
        
        return None
    
    def process_answer(self, answer):
        """Store the user's answer and move to next question"""
        if self.current_question_index > 0 or self.started:
            if self.current_question_index < len(self.questions):
                question = self.questions[self.current_question_index]
                self.responses[question['id']] = {
                    'label': question['label'],
                    'answer': answer,
                    'timestamp': datetime.now().isoformat()
                }
                self.current_question_index += 1
    
    def is_complete(self):
        """Check if all questions have been answered"""
        return self.current_question_index >= len(self.questions)
    
    def get_responses(self):
        """Get all collected responses"""
        return {
            'user_name': self.user_name,
            'check_type': self.check_type,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime('%H:%M:%S'),
            'responses': self.responses
        }
    
    def get_progress(self):
        """Get current progress"""
        return {
            'current': self.current_question_index,
            'total': self.total_questions
        }

