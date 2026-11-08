import axios from 'axios';

const hostDelFrontend = typeof window !== 'undefined' && window.location.hostname
  ? window.location.hostname
  : 'localhost';
const BASE_URL = process.env.EXPO_PUBLIC_API_URL || `http://${hostDelFrontend}:8000`;

export const api = axios.create({
  baseURL: BASE_URL,
  withCredentials: true,
});

api.interceptors.request.use((config) => {
  const token = typeof window !== 'undefined' ? window.localStorage.getItem('freshtrack_token') : null;
  if (token) {
    config.headers['Authorization'] = `Bearer ${token}`;
  }
  return config;
});

export function guardarToken(token) {
  if (typeof window !== 'undefined' && token) {
    window.localStorage.setItem('freshtrack_token', token);
  }
}

export function borrarToken() {
  if (typeof window !== 'undefined') {
    window.localStorage.removeItem('freshtrack_token');
  }
}
