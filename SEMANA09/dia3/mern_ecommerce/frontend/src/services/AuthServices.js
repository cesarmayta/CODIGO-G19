import { API_URL } from "../lib/Enviroments";

export const signIn = async (user) => {
  const dataUserLogin = {
    userName : user.username,
    userPassword: user.password
  }
  const response = await fetch(`${API_URL}/users/auth`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(dataUserLogin),
  });
  const data = await response.json();
  const status = response.status;
  return { data, status };
};

export const signUp = async (user) => {
  const dataNewUser = {
    userName:user.userEmail,
    userPassword:user.userPassword
  }
  const response = await fetch(`${API_URL}/users`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(dataNewUser),
  });
  const data = await response.json();
  return data;
};

export const isAuth = () => {
  const token = localStorage.getItem("token");
  if (!token) {
    return false;
  }
  const payload = token.split(".")[1];
  const jsonPayload = JSON.parse(window.atob(payload));
  if (jsonPayload.exp > new Date() / 1000) {
    return true;
  }
  return false;
};

export const signOut = () => {
  window.localStorage.removeItem("token");
  return (window.location.href = "/");
};

export const getToken = () => {
  const token = localStorage.getItem("token");
  if (!token) {
    return null;
  }
  return token;
};
