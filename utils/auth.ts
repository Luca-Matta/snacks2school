import axios from "axios";

export function deleteCookie(name: string): void {
  document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:01 GMT;`;
}

const getCsrfToken = async () => {
  const response = await axios.get(
    "https://www.snacks2school.com/api/csrf-token/",
    {
      withCredentials: true,
    }
  );
  return response.data.csrfToken;
};

export async function checkAuthStatus(): Promise<boolean> {
  try {
    const token = localStorage.getItem("authToken");
    if (!token) {
      console.log("No auth token found.");
      return false;
    }

    const response = await axios.get(
      "https://www.snacks2school.com/api/check-auth-status/",
      {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${token}`,
        },
        withCredentials: true,
      }
    );

    if (response.data.isAuthenticated) {
      console.log("User is authenticated");
      return true;
    } else {
      console.log("User is not authenticated");
      return false;
    }
  } catch (error) {
    console.error("Error checking auth status:", error);
    return false;
  }
}

export async function getCurrentUserData(): Promise<any> {
  try {
    const token = localStorage.getItem("authToken");

    if (!token) {
      console.log("No auth token found.");
      return null;
    }

    const response = await axios.get(
      "https://www.snacks2school.com/api/current-user-data/",
      {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${token}`,
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

export async function getChildrenForCurrentUser(): Promise<any> {
  try {
    const token = localStorage.getItem("authToken");

    if (!token) {
      console.error("No auth token found.");
      return null;
    }

    const response = await axios.get(
      "https://www.snacks2school.com/api/children/",
      {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${token}`,
        },
        withCredentials: true,
      }
    );

    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      console.error("Error retrieving children data:", error.response?.data);
    } else {
      console.error("Error retrieving children data:", error);
    }
    return null;
  }
}
