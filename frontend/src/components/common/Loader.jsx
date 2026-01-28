import React from 'react';
import { Loader2 } from 'lucide-react';
import { motion } from 'framer-motion';

const Loader = ({ text = 'Analyzing clinical information...' }) => {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="flex flex-col items-center justify-center py-12"
    >
      <Loader2 className="w-12 h-12 text-clinical-primary animate-spin" />
      <p className="mt-4 text-slate-600">{text}</p>
    </motion.div>
  );
};

export default Loader;