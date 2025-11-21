import React, { useState } from 'react';
import './App.css';
import WelcomeScreen from './components/WelcomeScreen';
import ChatInterface from './components/ChatInterface';

function App() {
  const [sessionStarted, setSessionStarted] = useState(false);
  const [sessionData, setSessionData] = useState(null);

  const handleStartSession = (data) => {
    setSessionData(data);
    setSessionStarted(true);
  };

  const handleEndSession = () => {
    setSessionStarted(false);
    setSessionData(null);
  };

  return (
    <div className="App">
      {!sessionStarted ? (
        <WelcomeScreen onStartSession={handleStartSession} />
      ) : (
        <ChatInterface 
          sessionData={sessionData}
          onEndSession={handleEndSession}
        />
      )}
    </div>
  );
}

export default App;

