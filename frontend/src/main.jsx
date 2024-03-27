import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import './index.css';
import { BrowserRouter } from 'react-router-dom';
import { CartProvider } from './stores/context/CartContext.jsx';
import { UserProvider } from './stores/context/UserContext'; // Import UserProvider

ReactDOM.createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <React.StrictMode>
      <UserProvider> {/* Add UserProvider */}
        <CartProvider>
          <App />
        </CartProvider>
      </UserProvider> {/* End UserProvider */}
    </React.StrictMode>,
  </BrowserRouter>
);