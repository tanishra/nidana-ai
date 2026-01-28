import React, { useState } from 'react';
import Card from '../ui/Card';
import Button from '../ui/Button';
import Alert from '../ui/Alert';
import { UserCheck, Send } from 'lucide-react';

const DoctorFeedback = ({ conditions }) => {
  const [formData, setFormData] = useState({
    rankingQuality: 'good',
    acceptedCondition: '',
    missedCondition: '',
    overconfident: false,
    underconfident: false,
    feedbackNotes: ''
  });

  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    
    console.log('Feedback submitted:', formData);
    
    setSubmitted(true);
    setTimeout(() => {
      setSubmitted(false);
      setFormData({
        rankingQuality: 'good',
        acceptedCondition: '',
        missedCondition: '',
        overconfident: false,
        underconfident: false,
        feedbackNotes: ''
      });
    }, 3000);
  };

  return (
    <Card className="border-t-4 border-purple-500">
      <div className="flex items-center space-x-3 mb-6">
        <div className="bg-gradient-to-br from-purple-500 to-pink-500 p-2 rounded-lg">
          <UserCheck className="w-6 h-6 text-white" />
        </div>
        <h2 className="text-2xl font-bold text-slate-100">
          Doctor Feedback
        </h2>
      </div>

      {submitted ? (
        <Alert type="success" title="Feedback Submitted">
          Thank you for your clinical review. Your feedback helps improve the system.
        </Alert>
      ) : (
        <form onSubmit={handleSubmit} className="space-y-5">
          <div>
            <label className="block text-sm font-semibold text-slate-300 mb-2">
              How would you rate the AI's ranking?
            </label>
            <select
              value={formData.rankingQuality}
              onChange={(e) => setFormData({ ...formData, rankingQuality: e.target.value })}
              className="w-full px-4 py-3 rounded-xl bg-slate-800/50 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-purple-500 transition-all"
            >
              <option value="good">Good</option>
              <option value="acceptable">Acceptable</option>
              <option value="poor">Poor</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-semibold text-slate-300 mb-2">
              Which condition best matched your clinical judgment? (optional)
            </label>
            <input
              type="text"
              value={formData.acceptedCondition}
              onChange={(e) => setFormData({ ...formData, acceptedCondition: e.target.value })}
              className="w-full px-4 py-3 rounded-xl bg-slate-800/50 border border-slate-700 text-slate-100 placeholder:text-slate-500 focus:outline-none focus:ring-2 focus:ring-purple-500 transition-all"
              placeholder="e.g., Dengue Fever"
            />
          </div>

          <div>
            <label className="block text-sm font-semibold text-slate-300 mb-2">
              Was any important condition missed? (optional)
            </label>
            <input
              type="text"
              value={formData.missedCondition}
              onChange={(e) => setFormData({ ...formData, missedCondition: e.target.value })}
              className="w-full px-4 py-3 rounded-xl bg-slate-800/50 border border-slate-700 text-slate-100 placeholder:text-slate-500 focus:outline-none focus:ring-2 focus:ring-purple-500 transition-all"
              placeholder="e.g., Malaria"
            />
          </div>

          <div className="flex flex-col sm:flex-row gap-4">
            <label className="flex items-center space-x-3 cursor-pointer group">
              <input
                type="checkbox"
                checked={formData.overconfident}
                onChange={(e) => setFormData({ ...formData, overconfident: e.target.checked })}
                className="w-5 h-5 text-purple-500 bg-slate-800 border-slate-600 rounded focus:ring-2 focus:ring-purple-500"
              />
              <span className="text-sm text-slate-300 group-hover:text-slate-100 transition-colors">AI was overconfident</span>
            </label>

            <label className="flex items-center space-x-3 cursor-pointer group">
              <input
                type="checkbox"
                checked={formData.underconfident}
                onChange={(e) => setFormData({ ...formData, underconfident: e.target.checked })}
                className="w-5 h-5 text-purple-500 bg-slate-800 border-slate-600 rounded focus:ring-2 focus:ring-purple-500"
              />
              <span className="text-sm text-slate-300 group-hover:text-slate-100 transition-colors">AI was underconfident</span>
            </label>
          </div>

          <div>
            <label className="block text-sm font-semibold text-slate-300 mb-2">
              Additional clinical notes (optional)
            </label>
            <textarea
              value={formData.feedbackNotes}
              onChange={(e) => setFormData({ ...formData, feedbackNotes: e.target.value })}
              rows={4}
              className="w-full px-4 py-3 rounded-xl bg-slate-800/50 border border-slate-700 text-slate-100 placeholder:text-slate-500 focus:outline-none focus:ring-2 focus:ring-purple-500 resize-none transition-all"
              placeholder="Any additional observations or suggestions..."
            />
          </div>

          <div className="flex justify-end">
            <Button type="submit" className="flex items-center space-x-2">
              <Send className="w-4 h-4" />
              <span>Submit Feedback</span>
            </Button>
          </div>
        </form>
      )}
    </Card>
  );
};

export default DoctorFeedback;