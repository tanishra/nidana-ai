import React from 'react';
import Card from '../ui/Card';
import { FileText } from 'lucide-react';

const ExplanationPanel = ({ explanation }) => {
  if (!explanation) return null;

  // Remove markdown formatting like ** and ##
  const cleanExplanation = explanation
    .replace(/\*\*/g, '')
    .replace(/##/g, '')
    .replace(/###/g, '');

  return (
    <Card>
      <div className="flex items-center space-x-3 mb-4">
        <div className="bg-gradient-to-br from-purple-500 to-pink-500 p-2 rounded-lg">
          <FileText className="w-6 h-6 text-white" />
        </div>
        <h2 className="text-2xl font-bold text-slate-100">Clinical Explanation</h2>
      </div>

      <div className="prose prose-slate max-w-none">
        <p className="text-slate-300 leading-relaxed whitespace-pre-line text-base">
          {cleanExplanation}
        </p>
      </div>
    </Card>
  );
};

export default ExplanationPanel;