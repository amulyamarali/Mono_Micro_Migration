import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const navigate = useNavigate(); // Add this line

  const handleSubmit = async (event) => {
    event.preventDefault();
    
    // Send login data to backend
    try {
      const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
      });
      
      if (response.ok) {
        // Login successful, handle accordingly
        console.log('Login successful');
        navigate('/actual'); // Add this line to navigate to the actual page
      } else {
        // Login failed, set error message
        setErrorMessage('Invalid email or password. Please sign up to register.');
        console.error('Login failed');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h1>FROM COMPONENT LOGIN</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Email:
          <input type="email" value={email} onChange={e => setEmail(e.target.value)} required />
        </label>
        <label>
          Password:
          <input type="password" value={password} onChange={e => setPassword(e.target.value)} required />
        </label>
        <input type="submit" value="Submit" />
        {errorMessage && <p>{errorMessage}</p>}
      </form>
    </div>
  );
}

export default Login;