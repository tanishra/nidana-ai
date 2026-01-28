import React from 'react';

const Textarea = ({ value, onChange, placeholder, rows = 6, className = '' }) => {
  return (
    <textarea
      value={value}
      onChange={onChange}
      placeholder={placeholder}
      rows={rows}
      className={`
        w-full px-4 py-3 rounded-xl 
        bg-slate-800/50 border border-slate-700
        text-slate-100 placeholder:text-slate-500
        focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent
        resize-none transition-all duration-300
        backdrop-blur-sm
        ${className}
      `}
    />
  );
};

export default Textarea;