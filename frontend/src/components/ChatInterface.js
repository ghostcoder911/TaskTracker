import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import './ChatInterface.css';

const API_URL = process.env.REACT_APP_API_URL || '/api';

function ChatInterface({ sessionData, onEndSession }) {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [loading, setLoading] = useState(false);
  const [completed, setCompleted] = useState(false);
  const [progress, setProgress] = useState(sessionData.progress || { current: 0, total: 5 });
  const messagesEndRef = useRef(null);
  const inputRef = useRef(null);

  useEffect(() => {
    // Add initial bot message
    setMessages([
      {
        type: 'bot',
        text: sessionData.initialMessage,
        timestamp: new Date()
      }
    ]);
  }, [sessionData.initialMessage]);

  useEffect(() => {
    // Scroll to bottom when messages change
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  useEffect(() => {
    // Focus input when not loading
    if (!loading && !completed) {
      inputRef.current?.focus();
    }
  }, [loading, completed]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!inputValue.trim() || loading || completed) return;

    const userMessage = inputValue.trim();
    
    // Add user message to chat
    setMessages(prev => [...prev, {
      type: 'user',
      text: userMessage,
      timestamp: new Date()
    }]);

    setInputValue('');
    setLoading(true);

    try {
      const response = await axios.post(`${API_URL}/send-message`, {
        session_id: sessionData.sessionId,
        message: userMessage
      });

      // Add bot response
      setMessages(prev => [...prev, {
        type: 'bot',
        text: response.data.message,
        timestamp: new Date()
      }]);

      // Update progress
      if (response.data.progress) {
        setProgress(response.data.progress);
      }

      // Check if completed
      if (response.data.completed) {
        setCompleted(true);
      }
    } catch (err) {
      console.error('Error sending message:', err);
      setMessages(prev => [...prev, {
        type: 'error',
        text: 'Sorry, there was an error. Please try again.',
        timestamp: new Date()
      }]);
    } finally {
      setLoading(false);
    }
  };

  const handleNewCheckIn = () => {
    onEndSession();
  };

  return (
    <div className="chat-container">
      <div className="chat-card">
        <div className="chat-header">
          <div className="chat-header-info">
            <h2>{sessionData.name}</h2>
            <p>{sessionData.checkType === 'start' ? '🌅 Morning Check-in' : '🌇 Evening Check-out'}</p>
          </div>
          <div className="progress-indicator">
            <span>{progress.current} / {progress.total}</span>
          </div>
        </div>

        <div className="progress-bar">
          <div 
            className="progress-fill" 
            style={{ width: `${(progress.current / progress.total) * 100}%` }}
          />
        </div>

        <div className="messages-container">
          {messages.map((message, index) => (
            <div key={index} className={`message ${message.type}-message`}>
              <div className="message-content">
                {message.text}
              </div>
              <div className="message-time">
                {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
              </div>
            </div>
          ))}
          {loading && (
            <div className="message bot-message">
              <div className="message-content">
                <div className="typing-indicator">
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        {!completed ? (
          <form onSubmit={handleSubmit} className="input-container">
            <input
              ref={inputRef}
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              placeholder="Type your response..."
              disabled={loading}
              className="message-input"
            />
            <button 
              type="submit" 
              disabled={loading || !inputValue.trim()}
              className="send-button"
            >
              ➤
            </button>
          </form>
        ) : (
          <div className="completion-actions">
            <button onClick={handleNewCheckIn} className="new-checkin-button">
              Start New Check-in
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

export default ChatInterface;

