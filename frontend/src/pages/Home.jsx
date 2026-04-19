import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import { Send } from 'lucide-react';

const Home = () => {
  const [messages, setMessages] = useState([
    { role: 'bot', text: 'Hello! I am your AI Telecom Tutor. Ask me anything about telecommunications.' }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = { role: 'user', text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await axios.post('http://localhost:8000/ask', { query: userMessage.text });
      setMessages((prev) => [...prev, { role: 'bot', text: response.data.answer }]);
    } catch (error) {
      setMessages((prev) => [...prev, { role: 'bot', text: 'Sorry, I encountered an error. Please ensure the backend is running.' }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-messages">
        {messages.map((msg, idx) => (
          <div key={idx} className={`message-bubble ${msg.role === 'user' ? 'message-user' : 'message-bot'}`}>
            {msg.text}
          </div>
        ))}
        {loading && (
          <div className="message-bubble message-bot">
            <div className="spinner"></div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>
      
      <form className="input-area" onSubmit={handleSend}>
        <input
          type="text"
          className="input-field"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your question..."
          disabled={loading}
        />
        <button type="submit" className="btn-primary" disabled={loading}>
          <Send size={18} />
          Send
        </button>
      </form>
    </div>
  );
};

export default Home;
