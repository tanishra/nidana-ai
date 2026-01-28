import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const diagnosePatient = async (text) => {
  try {
    const response = await api.post('/diagnose', { text });
    return response.data;
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};

export const submitDoctorFeedback = async (feedbackData) => {
  try {
    const response = await api.post('/feedback', feedbackData);
    return response.data;
  } catch (error) {
    console.error('Feedback API Error:', error);
    throw error;
  }
};

export default api;