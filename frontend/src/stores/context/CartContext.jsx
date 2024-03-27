import { createContext, useContext, useState } from "react";
import { useUser } from "./UserContext";

const CartContext = createContext();


export const CartProvider = ({ children }) => {
  const { userId } = useUser();
  const [cartItems, setCartItems] = useState([]);

  const addToCart = async (product) => {
    if (!product) {
      console.error('No product provided');
      return;
    }
  
    try {
      const response = await fetch('http://localhost:5000/cart', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ ...product, userId })  // Include userId in the request body
      });
  
      if (!response.ok) {
        throw new Error('Failed to add item to cart');
      }
  
      // console log data sent to the server
      console.log('Item added to cart:', product);
  
      // If you want to do something with the response, you can do it here
      const data = await response.json();
      console.log(data);
  
      // Update the cartItems state
      setCartItems(prevItems => [...prevItems, product]);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const removeFromCart = (item) => {
    setCartItems(cartItems.filter((apple) => apple !== item));
  };

  return (
    <CartContext.Provider value={{ cartItems, addToCart, removeFromCart }}>
      {children}
    </CartContext.Provider>
  );
};

export const useCart = () => {
  return useContext(CartContext);
};
