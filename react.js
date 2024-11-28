import React, { useState } from 'react';
import { io } from 'socket.io-client';

function CodingChallenge() {
    const [code, setCode] = useState('');
    const [feedback, setFeedback] = useState('');

    const socket = io('ws://localhost:8000/ws/feedback/');
    
    const submitCode = () => {
        socket.emit('message', JSON.stringify({ code }));
        socket.on('feedback', (data) => setFeedback(data.feedback));
    };

    return (
        <div>
            <textarea value={code} onChange={(e) => setCode(e.target.value)} />
            <button onClick={submitCode}>Submit Code</button>
            <pre>{feedback}</pre>
        </div>
    );
}

export default CodingChallenge;
