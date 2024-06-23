import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import StoryReading from './StoryReading/StoryReading';

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">

        <p1>
          m o n t i 🧸
        </p1>
      </header>

      <div>
        <StoryReading></StoryReading>
      </div>
    

    </div>

  );
}

export default App;