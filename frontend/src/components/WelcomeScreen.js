import React, { useState } from 'react';
import axios from 'axios';
import './WelcomeScreen.css';

const API_URL = process.env.REACT_APP_API_URL || '/api';

function WelcomeScreen({ onStartSession }) {
  const [name, setName] = useState('');
  const [checkType, setCheckType] = useState('start');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!name.trim()) {
      setError('Please enter your name');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const response = await axios.post(`${API_URL}/start-session`, {
        name: name.trim(),
        check_type: checkType
      });

      onStartSession({
        sessionId: response.data.session_id,
        name: name.trim(),
        checkType: checkType,
        initialMessage: response.data.message,
        progress: response.data.progress
      });
    } catch (err) {
      setError('Failed to start session. Please try again.');
      console.error('Error starting session:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="welcome-container">
      <div className="welcome-card">
        <div className="welcome-header">
          <h1>📋 Task Tracker</h1>
          <p>Engineering Team Check-ins</p>
        </div>

        <form onSubmit={handleSubmit} className="welcome-form">
          <div className="form-group">
            <label htmlFor="name">Your Name</label>
            <input
              type="text"
              id="name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="Enter your name"
              disabled={loading}
              autoFocus
            />
          </div>

          <div className="form-group">
            <label>Check-in Type</label>
            <div className="radio-group">
              <label className="radio-option">
                <input
                  type="radio"
                  value="start"
                  checked={checkType === 'start'}
                  onChange={(e) => setCheckType(e.target.value)}
                  disabled={loading}
                />
                <span className="radio-label">
                  <span className="radio-icon">🌅</span>
                  <span>Start of Day</span>
                </span>
              </label>

              <label className="radio-option">
                <input
                  type="radio"
                  value="end"
                  checked={checkType === 'end'}
                  onChange={(e) => setCheckType(e.target.value)}
                  disabled={loading}
                />
                <span className="radio-label">
                  <span className="radio-icon">🌇</span>
                  <span>End of Day</span>
                </span>
              </label>
            </div>
          </div>

          {error && <div className="error-message">{error}</div>}

          <button type="submit" className="submit-button" disabled={loading}>
            {loading ? 'Starting...' : 'Start Check-in'}
          </button>
        </form>

        <div className="welcome-footer">
          <p>Keep it crisp and honest — this helps us support each other better! 💪</p>
        </div>
      </div>
    </div>
  );
}

export default WelcomeScreen;

