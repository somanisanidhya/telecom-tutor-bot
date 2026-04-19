import React, { useState } from 'react';
import axios from 'axios';
import { Settings, CheckCircle } from 'lucide-react';

const Quiz = () => {
  const [questions, setQuestions] = useState([]);
  const [currentIdx, setCurrentIdx] = useState(0);
  const [loading, setLoading] = useState(false);
  const [selectedOpt, setSelectedOpt] = useState(null);
  const [showAnswer, setShowAnswer] = useState(false);
  const [score, setScore] = useState(0);
  const [quizFinished, setQuizFinished] = useState(false);

  const fetchQuiz = async () => {
    setLoading(true);
    setQuizFinished(false);
    setScore(0);
    setCurrentIdx(0);
    setSelectedOpt(null);
    setShowAnswer(false);
    
    try {
      const resp = await axios.post('http://localhost:8000/quiz', { topic: 'telecommunications' });
      setQuestions(resp.data.questions || []);
    } catch (err) {
      alert("Failed to load quiz. Backend might be down or not configured correctly.");
    } finally {
      setLoading(false);
    }
  };

  const handleOptionClick = (optId) => {
    if (showAnswer) return;
    setSelectedOpt(optId);
  };

  const checkAnswer = () => {
    if (!selectedOpt) return;
    setShowAnswer(true);
    if (selectedOpt === questions[currentIdx].correct_option_id) {
      setScore(s => s + 1);
    }
  };

  const nextQuestion = () => {
    if (currentIdx < questions.length - 1) {
      setCurrentIdx(i => i + 1);
      setSelectedOpt(null);
      setShowAnswer(false);
    } else {
      setQuizFinished(true);
    }
  };

  if (loading) {
    return (
      <div className="quiz-container" style={{ justifyContent: 'center' }}>
        <div className="spinner" style={{ width: '40px', height: '40px', borderWidth: '4px' }}></div>
        <p style={{ marginTop: '20px' }}>Generating AI Quiz based on your context...</p>
      </div>
    );
  }

  if (questions.length === 0) {
    return (
      <div className="quiz-container" style={{ justifyContent: 'center' }}>
        <div className="quiz-header">
          <h2>Ready to Test Your Knowledge?</h2>
          <p>Generate a quiz based on the telecommunications context database.</p>
        </div>
        <button className="btn-primary" onClick={fetchQuiz} style={{ padding: '12px 24px', fontSize: '1.1rem' }}>
          <Settings size={20} />
          Generate Quiz
        </button>
      </div>
    );
  }

  if (quizFinished) {
    return (
      <div className="quiz-container" style={{ justifyContent: 'center' }}>
        <CheckCircle size={64} color="var(--secondary)" style={{ marginBottom: '20px' }} />
        <h2>Quiz Completed!</h2>
        <p style={{ fontSize: '1.2rem', margin: '15px 0' }}>Your score: {score} / {questions.length}</p>
        <button className="btn-primary" onClick={fetchQuiz}>Retake New Quiz</button>
      </div>
    );
  }

  const currentQ = questions[currentIdx];

  return (
    <div className="quiz-container">
      <div className="quiz-header">
        <p>Question {currentIdx + 1} of {questions.length}</p>
      </div>
      
      <div className="quiz-card">
        <div className="quiz-question">{currentQ.question}</div>
        <div className="quiz-options">
          {currentQ.options.map((opt) => {
            let className = "quiz-option";
            if (showAnswer) {
              if (opt.id === currentQ.correct_option_id) className += " correct";
              else if (opt.id === selectedOpt) className += " wrong";
            } else if (opt.id === selectedOpt) {
              className += " selected";
            }
            
            return (
              <div key={opt.id} className={className} onClick={() => handleOptionClick(opt.id)}>
                <div style={{ fontWeight: '500', width: '24px' }}>{opt.id.toUpperCase()}.</div>
                <div>{opt.text}</div>
              </div>
            );
          })}
        </div>
        
        <div className="quiz-actions">
          {!showAnswer ? (
            <button className="btn-primary" onClick={checkAnswer} disabled={!selectedOpt}>
              Confirm Answer
            </button>
          ) : (
            <button className="btn-primary" onClick={nextQuestion}>
              {currentIdx < questions.length - 1 ? 'Next Question' : 'Finish Quiz'}
            </button>
          )}
        </div>
      </div>
    </div>
  );
};

export default Quiz;
