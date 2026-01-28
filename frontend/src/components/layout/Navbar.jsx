import React from 'react';
import { Activity, Sparkles } from 'lucide-react';
import { motion } from 'framer-motion';

const Navbar = () => {
  return (
    <motion.nav 
      initial={{ y: -100, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.6, ease: "easeOut" }}
      className="fixed top-0 left-0 right-0 z-50 glass-navbar"
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center space-x-3">
            <motion.div 
              whileHover={{ rotate: 360, scale: 1.1 }}
              transition={{ duration: 0.6 }}
              className="bg-gradient-to-br from-blue-500 to-cyan-500 p-2.5 rounded-xl shadow-lg shadow-blue-500/50"
            >
              <Activity className="w-6 h-6 text-white" />
            </motion.div>
            <div>
              <h1 className="text-lg font-bold gradient-text flex items-center gap-2">
                Clinical Decision Support
                <Sparkles className="w-4 h-4 text-cyan-400" />
              </h1>
              <p className="text-xs text-slate-400">AI-Powered Medical Analysis</p>
            </div>
          </div>
          
          <div className="flex items-center space-x-4">
            <span className="text-sm text-slate-300 hidden sm:block font-medium">
              Doctor Portal
            </span>
            <motion.div 
              whileHover={{ scale: 1.1 }}
              className="h-10 w-10 rounded-full bg-gradient-to-br from-blue-500 to-cyan-500 flex items-center justify-center text-white text-sm font-bold shadow-lg shadow-blue-500/50"
            >
              MD
            </motion.div>
          </div>
        </div>
      </div>
    </motion.nav>
  );
};

export default Navbar;