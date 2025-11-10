import axios from "axios";

const API_URL = "http://localhost:8000";

export const getRecommendations = async (favorites) => {
  const response = await axios.post(`${API_URL}/recommend`, { favorites });
  return response.data.recommendations;
};
