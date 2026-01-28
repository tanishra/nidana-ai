import React from 'react';
import { AlertTriangle, Info, CheckCircle, XCircle } from 'lucide-react';
import { motion } from 'framer-motion';

const Alert = ({ type = 'info', title, children, className = '' }) => {
  const config = {
    info: {
      bg: 'bg-blue-950/50 border-blue-700/50',
      icon: Info,
      iconColor: 'text-blue-400',
      titleColor: 'text-blue-300'
    },
    warning: {
      bg: 'bg-yellow-950/50 border-yellow-700/50',
      icon: AlertTriangle,
      iconColor: 'text-yellow-400',
      titleColor: 'text-yellow-300'
    },
    success: {
      bg: 'bg-green-950/50 border-green-700/50',
      icon: CheckCircle,
      iconColor: 'text-green-400',
      titleColor: 'text-green-300'
    },
    danger: {
      bg: 'bg-red-950/50 border-red-700/50',
      icon: XCircle,
      iconColor: 'text-red-400',
      titleColor: 'text-red-300'
    },
  };

  const { bg, icon: Icon, iconColor, titleColor } = config[type];

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.3 }}
      className={`${bg} border rounded-xl p-4 backdrop-blur-sm ${className}`}
    >
      <div className="flex items-start space-x-3">
        <Icon className={`w-5 h-5 ${iconColor} mt-0.5 flex-shrink-0`} />
        <div className="flex-1">
          {title && <h4 className={`font-semibold ${titleColor} mb-1`}>{title}</h4>}
          <div className="text-sm text-slate-300">{children}</div>
        </div>
      </div>
    </motion.div>
  );
};

export default Alert;