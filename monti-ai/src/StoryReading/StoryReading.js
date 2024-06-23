import React, { useState, useEffect } from 'react';
import axios from 'axios';

const StoryReading = () => {
  const [story, setStory] = useState([]);
  const [currentPage, setCurrentPage] = useState(0);
  const [comprehensionQuestion, setComprehensionQuestion] = useState('');
  const [userResponse, setUserResponse] = useState('');

  useEffect(() => {
    // Fetch story data from backend
    axios.get('/api/story')
      .then(response => setStory(response.data))
      .catch(error => console.error(error));
  }, []);

  const handleNextPage = () => {
    // Logic to handle comprehension checks and page navigation
    if (currentPage < story.length - 1) {
      setCurrentPage(currentPage + 1);
    } else {
      // End of story logic
    }
  };

  const handleComprehensionResponse = () => {
    // Send user response to backend for feedback
    axios.post('/api/comprehension', { response: userResponse })
      .then(feedback => {
        // Process feedback
      })
      .catch(error => console.error(error));
  };

  return (
    <div>
      <div className="story-page">
        <img src="h.png" alt="Story page" />
        <p>hello its a story</p>
      </div>
      <div className="comprehension-check">
        <p>{comprehensionQuestion}</p>
        <input 
          type="text" 
          value={userResponse} 
          onChange={(e) => setUserResponse(e.target.value)} 
        />
        <button onClick={handleComprehensionResponse}>Submit</button>
      </div>
      <button onClick={handleNextPage}>Next</button>
    </div>
  );
};

export default StoryReading;
