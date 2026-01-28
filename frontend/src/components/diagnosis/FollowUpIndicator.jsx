import React from 'react';
import Alert from '../ui/Alert';

const FollowUpIndicator = ({ required }) => {
  if (!required) return null;

  return (
    <Alert type="warning" title="Additional Information May Help">
      More information may help improve diagnostic accuracy. Consider gathering additional patient history or conducting follow-up assessment.
    </Alert>
  );
};

export default FollowUpIndicator;