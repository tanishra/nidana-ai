import React from 'react';
import { motion } from 'framer-motion';

const Card = ({ children, className = '', animate = true }) => {
  const Component = animate ? motion.div : 'div';
  const animationProps = animate ? {
    initial: { opacity: 0, y: 20 },
    animate: { opacity: 1, y: 0 },
    transition: { duration: 0.5, ease: "easeOut" }
  } : {};

  return (
    <Component
      {...animationProps}
      className={`glass-card rounded-2xl shadow-2xl p-6 ${className}`}
    >
      {children}
    </Component>
  );
};

export default Card;