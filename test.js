// Step 1: Log in and store session cookie
async function login() {
    try {
      const response = await fetch("https://api.example.com/login", {
        method: "POST",
        credentials: "include", // Allows cookies to be stored
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: "yourUsername",
          password: "yourPassword"
        })
      });
  
      if (!response.ok) throw new Error("Login failed");
  
      console.log("Login successful!");
      fetchProtectedData(); // Call next function after login
    } catch (error) {
      console.error("Error during login:", error);
    }
  }
  
  // Step 2: Fetch data using the session cookie
  async function fetchProtectedData() {
    try {
      const response = await fetch("https://api.example.com/protected-data", {
        method: "GET",
        credentials: "include", // Ensures session cookie is sent
        headers: {
          "Content-Type": "application/json",
        }
      });
  
      if (!response.ok) throw new Error("Failed to fetch data");
  
      const data = await response.json();
      console.log("Protected Data:", data);
    } catch (error) {
      console.error("Error fetching protected data:", error);
    }
  }
  
  // Call the login function first
  login();