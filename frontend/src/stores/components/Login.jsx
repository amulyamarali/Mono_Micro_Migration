// import React from 'react'

// function Login() {
//   return (
//     <div>
//       <h1>FROM COMPONENT LOGIN</h1>
//     </div>
//   )
// }

// export default Login


import React, { useState } from 'react';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    // Handle login logic here
    console.log(`Email: ${email}, Password: ${password}`);
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
      </form>
    </div>
  );
}

export default Login;
