import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';  // Import useNavigate

function Signup() {
  const [formData, setFormData] = useState({
    name: '',
    age: '',
    email: '',
    password: '',
    phoneNumber: '',
    address: '',
  });

  const navigate = useNavigate();  // Create a navigate function

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:9000/signup', formData);
      console.log(response.data); // Log the response from the server

      navigate('/');  // Redirect to the home page
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Sign Up</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" name="name" placeholder="Name" onChange={handleChange} />
        <input type="number" name="age" placeholder="Age" onChange={handleChange} />
        <input type="email" name="email" placeholder="Email" onChange={handleChange} />
        <input type="password" name="password" placeholder="Password" onChange={handleChange} />
        <input type="tel" name="phoneNumber" placeholder="Phone Number" onChange={handleChange} />
        <textarea name="address" placeholder="Address" onChange={handleChange} />
        <button type="submit">Sign Up</button>
      </form>
    </div>
  );
}

export default Signup;