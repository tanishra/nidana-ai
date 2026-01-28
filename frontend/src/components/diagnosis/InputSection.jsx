import React from 'react';
import Card from '../ui/Card';
import Textarea from '../ui/Textarea';
import Button from '../ui/Button';
import Alert from '../ui/Alert';
import { Stethoscope, Sparkles } from 'lucide-react';
import { motion } from 'framer-motion';

const InputSection = ({ value, onChange, onSubmit, isLoading }) => {
  return (
    <Card>
      <motion.div 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2 }}
        className="flex items-center space-x-3 mb-4"
      >
        <div className="bg-gradient-to-br from-blue-500 to-cyan-500 p-2 rounded-lg">
          <Stethoscope className="w-6 h-6 text-white" />
        </div>
        <h2 className="text-2xl font-bold text-slate-100 flex items-center gap-2">
          Patient Symptoms
          <Sparkles className="w-5 h-5 text-cyan-400" />
        </h2>
      </motion.div>

      <Alert type="info" className="mb-4">
        This tool is for <strong>testing and clinical validation only</strong>. 
        It does <strong>not provide a medical diagnosis</strong>.
      </Alert>

      <Textarea
        value={value}
        onChange={onChange}
        placeholder="Example: Patient presents with high fever (39°C), severe headache, pain behind eyes, joint pain for 3 days. Recent travel to tropical region."
        rows={6}
      />

      <div className="mt-4 flex justify-end">
        <Button 
          onClick={onSubmit} 
          disabled={isLoading || !value.trim()}
          className="min-w-[160px]"
        >
          {isLoading ? (
            <span className="flex items-center gap-2">
              <motion.div
                animate={{ rotate: 360 }}
                transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
              >
                ⚡
              </motion.div>
              Analyzing...
            </span>
          ) : (
            'Analyze Symptoms'
          )}
        </Button>
      </div>
    </Card>
  );
};

export default InputSection;