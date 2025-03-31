import axios from "axios";

const API_URL = "https://legendary-carnival-gp75wwr5xx5cwv5j-8000.app.github.dev/api/";

export const fetchContainers = async () => {
  try {
    const response = await axios.get(`${API_URL}containers/`, { withCredentials: true });
    return response.data;
  } catch (error) {
    console.error("Ошибка при запросе контейнеров:", error);
    // return [];
  }
};

export const fetchUsers = async () => {
  try {
    const response = await axios.get(`${API_URL}users/`, { withCredentials: true });
    return response.data;
  } catch (error) {
    console.error("Ошибка при запросе пользователей:", error);
    // return [];
  }
};

export const fetchRentals = async () => {
  try {
    const response = await axios.get(`${API_URL}rentals/`, {withCredentials: true})
    return response.data
  } catch (error) {
    console.error("Ошибка при запросе аренды:", error)
    // return []
  }
}