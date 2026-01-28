import React from 'react';
import { AlertTriangle, Phone } from 'lucide-react';
import { motion } from 'framer-motion';
import Card from '../ui/Card';

const EmergencyAlert = ({ redFlag, reason, recommendedAction, disclaimer }) => {
  return (
    <motion.div
      initial={{ scale: 0.9, opacity: 0 }}
      animate={{ scale: 1, opacity: 1 }}
      transition={{ duration: 0.4 }}
    >
      <Card className="border-4 border-red-500 bg-red-950/30 shadow-2xl shadow-red-500/50">
        <div className="flex items-start space-x-4">
          <motion.div 
            animate={{ 
              scale: [1, 1.1, 1],
              rotate: [0, 5, -5, 0]
            }}
            transition={{ 
              duration: 2,
              repeat: Infinity,
              repeatType: "reverse"
            }}
            className="bg-gradient-to-br from-red-600 to-red-700 p-4 rounded-xl shadow-lg shadow-red-500/50"
          >
            <AlertTriangle className="w-10 h-10 text-white" />
          </motion.div>
          <div className="flex-1">
            <h2 className="text-3xl font-bold text-red-400 mb-3">
              🚨 URGENT MEDICAL ATTENTION REQUIRED
            </h2>
            
            <div className="space-y-4">
              <div>
                <h3 className="font-semibold text-red-300 mb-1 text-lg">Red Flag Detected:</h3>
                <p className="text-red-100 text-xl font-medium">{redFlag}</p>
              </div>

              <div>
                <h3 className="font-semibold text-red-300 mb-1 text-lg">Clinical Reason:</h3>
                <p className="text-red-100">{reason}</p>
              </div>

              <div className="bg-slate-900/60 rounded-xl p-5 border-2 border-red-500/50">
                <div className="flex items-center space-x-2 mb-2">
                  <Phone className="w-6 h-6 text-red-400" />
                  <h3 className="font-semibold text-red-300 text-lg">Recommended Action:</h3>
                </div>
                <p className="text-red-100 font-medium text-lg">{recommendedAction}</p>
              </div>

              <div className="mt-4 pt-4 border-t border-red-700/50">
                <p className="text-sm text-red-300 italic">{disclaimer}</p>
              </div>
            </div>
          </div>
        </div>
      </Card>
    </motion.div>
  );
};

export default EmergencyAlert;