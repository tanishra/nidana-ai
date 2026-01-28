import React from 'react';
import Card from '../ui/Card';
import ConditionCard from './ConditionCard';
import Alert from '../ui/Alert';
import { ClipboardList } from 'lucide-react';

const ResultsSection = ({ conditions }) => {
  if (!conditions || conditions.length === 0) {
    return (
      <Card>
        <Alert type="info">
          No strong matches found. More information may be required for accurate analysis.
        </Alert>
      </Card>
    );
  }

  return (
    <Card>
      <div className="flex items-center space-x-3 mb-6">
        <div className="bg-gradient-to-br from-emerald-500 to-teal-500 p-2 rounded-lg">
          <ClipboardList className="w-6 h-6 text-white" />
        </div>
        <h2 className="text-2xl font-bold text-slate-100">Possible Conditions</h2>
      </div>

      <div className="space-y-4">
        {conditions.map((condition, index) => (
          <ConditionCard key={index} condition={condition} index={index} />
        ))}
      </div>
    </Card>
  );
};

export default ResultsSection;