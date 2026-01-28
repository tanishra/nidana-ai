import React, { useState } from 'react';
import Container from '../components/layout/Container';
import InputSection from '../components/diagnosis/InputSection';
import EmergencyAlert from '../components/diagnosis/EmergencyAlert';
import ResultsSection from '../components/diagnosis/ResultsSection';
import ExplanationPanel from '../components/diagnosis/ExplanationPanel';
import FollowUpIndicator from '../components/diagnosis/FollowUpIndicator';
import DoctorFeedback from '../components/diagnosis/DoctorFeedback';
import Loader from '../components/common/Loader';
import Alert from '../components/ui/Alert';
import { diagnosePatient } from '../services/api';

const DiagnosisPage = () => {
  const [inputText, setInputText] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async () => {
    if (!inputText.trim()) return;

    setIsLoading(true);
    setError(null);
    setResponse(null);

    try {
      const result = await diagnosePatient(inputText);
      setResponse(result);
    } catch (err) {
      setError('Failed to analyze. Please check your connection and try again.');
      console.error('Diagnosis error:', err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Container className="py-24 space-y-6">
      <InputSection
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        onSubmit={handleSubmit}
        isLoading={isLoading}
      />

      {isLoading && <Loader />}

      {error && (
        <Alert type="danger" title="Error">
          {error}
        </Alert>
      )}

      {response && (
        <>
          {response.urgent ? (
            <EmergencyAlert
              redFlag={response.red_flag}
              reason={response.reason}
              recommendedAction={response.recommended_action}
              disclaimer={response.disclaimer}
            />
          ) : (
            <>
              <ResultsSection conditions={response.possible_conditions} />
              
              <ExplanationPanel explanation={response.explanation} />
              
              <FollowUpIndicator required={response.follow_up_required} />

              {response.disclaimer && (
                <Alert type="info">
                  {response.disclaimer}
                </Alert>
              )}

              {response.possible_conditions && response.possible_conditions.length > 0 && (
                <DoctorFeedback conditions={response.possible_conditions} />
              )}
            </>
          )}
        </>
      )}
    </Container>
  );
};

export default DiagnosisPage;