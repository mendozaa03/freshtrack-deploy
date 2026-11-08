import axios from 'axios';

const hostDelFrontend = typeof window !== 'undefined' && window.location.hostname
  ? window.location.hostname
  : 'localhost';
const BASE_URL = process.env.EXPO_PUBLIC_API_URL || `http://${hostDelFrontend}:8000`;

function leerStorage() {
  try { return typeof window !== 'undefined' ? window.localStorage.getItem('freshtrack_token') : null; }
  catch(e) { return null; }
}

let _token = leerStorage();

export function guardarToken(token) {
  _token = token;
  try { if (typeof window !== 'undefined' && token) window.localStorage.setItem('freshtrack_token', token); }
  catch(e) {}
}

export function borrarToken() {
  _token = null;
  try { if (typeof window !== 'undefined') window.localStorage.removeItem('freshtrack_token'); }
  catch(e) {}
}

export const api = axios.create({
  baseURL: BASE_URL,
  withCredentials: true,
});

api.interceptors.request.use((config) => {
  const token = _token || leerStorage();
  if (token) {
    config.headers['Authorization'] = `Bearer ${token}`;
  }
  return config;
});
