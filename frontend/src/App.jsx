import React from 'react';
import Navbar from './components/layout/Navbar';
import DiagnosisPage from './pages/DiagnosisPage';

function App() {
  return (
    <div className="min-h-screen">
      <Navbar />
      <DiagnosisPage />
    </div>
  );
}

export default App;