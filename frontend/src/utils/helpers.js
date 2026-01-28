export const getConfidenceLevel = (confidence) => {
  if (confidence >= 70) return { label: 'High', color: 'bg-green-100 text-green-800 border-green-200' };
  if (confidence >= 40) return { label: 'Moderate', color: 'bg-yellow-100 text-yellow-800 border-yellow-200' };
  return { label: 'Low', color: 'bg-red-100 text-red-800 border-red-200' };
};

export const getConfidenceColor = (confidence) => {
  if (confidence >= 70) return 'text-green-600';
  if (confidence >= 40) return 'text-yellow-600';
  return 'text-red-600';
};

export const formatPercentage = (value) => {
  return `${Math.round(value)}%`;
};