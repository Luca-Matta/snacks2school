import axios from "axios";

export function getCookie(name: string): string | null {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop()?.split(";").shift() || null;
  return null;
}

export function deleteCookie(name: string): void {
  document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:01 GMT;`;
}

export async function checkAuthStatus(): Promise<boolean> {
  try {
    console.log("Starting auth status check...");

    const token = getCookie("token");
    if (!token) {
      console.log("No auth token found");
      return false;
    }

    console.log("Token found:", token);
    return true;
  } catch (error) {
    console.error("Error checking auth status:", error);
    return false;
  }
}

export async function getCurrentUserData(): Promise<any> {
  try {
    const csrfToken = getCookie("csrftoken");

    const response = await axios.get(
      "http://localhost:8000/api/current-user-data/",
      {
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken || "",
        },
        withCredentials: true,
      }
    );

    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      console.error("Error retrieving user data:", error.response?.data);
    } else {
      console.error("Error retrieving user data:", error);
    }
    return null;
  }
}
