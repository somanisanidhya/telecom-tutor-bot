import React from 'react';
import { BrowserRouter as Router, Routes, Route, NavLink } from 'react-router-dom';
import Home from './pages/Home';
import Quiz from './pages/Quiz';
import { BookOpen, HelpCircle } from 'lucide-react';

function App() {
  return (
    <Router>
      <div className="app-container">
        <nav>
          <div className="logo">📡 Telecom Tutor</div>
          <div className="nav-links">
            <NavLink to="/" className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}>
              <BookOpen size={18} style={{ display: 'inline', marginRight: '6px', verticalAlign: 'text-bottom' }} />
              Chat
            </NavLink>
            <NavLink to="/quiz" className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}>
              <HelpCircle size={18} style={{ display: 'inline', marginRight: '6px', verticalAlign: 'text-bottom' }} />
              Quiz
            </NavLink>
          </div>
        </nav>

        <main className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/quiz" element={<Quiz />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
