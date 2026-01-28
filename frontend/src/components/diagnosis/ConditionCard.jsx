import React from 'react';
import { motion } from 'framer-motion';
import Badge from '../ui/Badge';
import { getConfidenceLevel, formatPercentage } from '../../utils/helpers';
import { TrendingUp, Activity, Target } from 'lucide-react';

const ConditionCard = ({ condition, index }) => {
  const confidenceInfo = getConfidenceLevel(condition.final_confidence || condition.confidence);
  
  return (
    <motion.div
      initial={{ opacity: 0, x: -30 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ delay: index * 0.15, duration: 0.5 }}
      whileHover={{ scale: 1.02, y: -5 }}
      className="glass-card rounded-2xl p-6 border-l-4 border-blue-500 hover:shadow-2xl hover:shadow-blue-500/20 transition-all duration-300"
    >
      <div className="flex items-start justify-between mb-4">
        <div className="flex-1">
          <div className="flex items-center space-x-3 mb-3">
            <motion.div
              initial={{ scale: 0 }}
              animate={{ scale: 1 }}
              transition={{ delay: index * 0.15 + 0.2, type: "spring" }}
              className="flex items-center justify-center w-10 h-10 shadow-lg flex-shrink-0"
            >
              <span className="text-white font-bold text-lg">{index + 1}</span>
            </motion.div>
            <h3 className="text-xl font-bold text-slate-100 leading-tight">
              {condition.disease}
            </h3>
          </div>
          <Badge variant={
            confidenceInfo.label === 'High' ? 'success' : 
            confidenceInfo.label === 'Moderate' ? 'warning' : 
            'danger'
          }>
            {confidenceInfo.label} Confidence
          </Badge>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
        <motion.div 
          whileHover={{ scale: 1.05 }}
          className="bg-slate-900/60 rounded-xl p-4 border border-slate-700/50"
        >
          <div className="flex items-center space-x-2 mb-2">
            <Target className="w-4 h-4 text-blue-400" />
            <span className="text-xs text-slate-400 font-medium">Rule Confidence</span>
          </div>
          <p className="text-2xl font-bold text-blue-400">
            {formatPercentage(condition.confidence)}
          </p>
        </motion.div>

        <motion.div 
          whileHover={{ scale: 1.05 }}
          className="bg-slate-900/60 rounded-xl p-4 border border-slate-700/50"
        >
          <div className="flex items-center space-x-2 mb-2">
            <Activity className="w-4 h-4 text-cyan-400" />
            <span className="text-xs text-slate-400 font-medium">ML Adjustment</span>
          </div>
          <p className="text-2xl font-bold text-cyan-400">
            {condition.ml_adjustment > 0 ? '+' : ''}{condition.ml_adjustment}
          </p>
        </motion.div>

        <motion.div 
          whileHover={{ scale: 1.05 }}
          className="bg-slate-900/60 rounded-xl p-4 border border-slate-700/50"
        >
          <div className="flex items-center space-x-2 mb-2">
            <TrendingUp className="w-4 h-4 text-emerald-400" />
            <span className="text-xs text-slate-400 font-medium">Final Confidence</span>
          </div>
          <p className={`text-2xl font-bold ${
            (condition.final_confidence || condition.confidence) >= 70 ? 'text-green-400' :
            (condition.final_confidence || condition.confidence) >= 40 ? 'text-yellow-400' :
            'text-red-400'
          }`}>
            {formatPercentage(condition.final_confidence || condition.confidence)}
          </p>
        </motion.div>
      </div>

      {condition.matched_symptoms && condition.matched_symptoms.length > 0 && (
        <div>
          <h4 className="text-sm font-semibold text-slate-300 mb-3">Matched Symptoms:</h4>
          <div className="flex flex-wrap gap-2">
            {condition.matched_symptoms.map((symptom, idx) => (
              <Badge key={idx} variant="info">
                {symptom}
              </Badge>
            ))}
          </div>
        </div>
      )}
    </motion.div>
  );
};

export default ConditionCard;