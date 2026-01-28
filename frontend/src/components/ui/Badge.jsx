import React from 'react';
import { motion } from 'framer-motion';

const Badge = ({ children, variant = 'default', className = '' }) => {
  const variants = {
    default: 'bg-slate-700 text-slate-200 border-slate-600',
    success: 'bg-green-900/50 text-green-300 border-green-700',
    warning: 'bg-yellow-900/50 text-yellow-300 border-yellow-700',
    danger: 'bg-red-900/50 text-red-300 border-red-700',
    info: 'bg-blue-900/50 text-blue-300 border-blue-700',
  };

  return (
    <motion.span 
      initial={{ scale: 0.8, opacity: 0 }}
      animate={{ scale: 1, opacity: 1 }}
      transition={{ duration: 0.3 }}
      className={`
        inline-flex items-center px-3 py-1.5 rounded-full text-xs font-semibold
        border backdrop-blur-sm ${variants[variant]} ${className}
      `}
    >
      {children}
    </motion.span>
  );
};

export default Badge;