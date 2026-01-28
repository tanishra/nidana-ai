import React from 'react';
import { motion } from 'framer-motion';

const Button = ({ 
  children, 
  onClick, 
  variant = 'primary', 
  disabled = false,
  className = '',
  type = 'button'
}) => {
  const variants = {
    primary: 'bg-gradient-to-r from-blue-600 to-cyan-600 text-white hover:from-blue-700 hover:to-cyan-700 disabled:from-blue-800 disabled:to-cyan-800 shadow-lg shadow-blue-500/50',
    secondary: 'bg-slate-700 text-slate-100 hover:bg-slate-600 disabled:bg-slate-800 border border-slate-600',
    danger: 'bg-gradient-to-r from-red-600 to-pink-600 text-white hover:from-red-700 hover:to-pink-700 disabled:from-red-800 disabled:to-pink-800 shadow-lg shadow-red-500/50',
  };

  return (
    <motion.button
      whileHover={{ scale: disabled ? 1 : 1.05, y: disabled ? 0 : -2 }}
      whileTap={{ scale: disabled ? 1 : 0.95 }}
      transition={{ duration: 0.2 }}
      type={type}
      onClick={onClick}
      disabled={disabled}
      className={`
        px-6 py-3 rounded-xl font-semibold
        transition-all duration-300
        disabled:cursor-not-allowed disabled:opacity-50
        ${variants[variant]}
        ${className}
      `}
    >
      {children}
    </motion.button>
  );
};

export default Button;