import React, { useContext } from 'react';
import { useCart } from './context/CartContext';
import Navbar from './components/Navbar';
import { Link } from 'react-router-dom';  // Import Link
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { UserContext } from './context/UserContext';
import { useUser } from './context/UserContext';


const UserCart = () => {
  const { cartItems, addToCart, removeFromCart } = useCart();
  const { userId } = useUser();

  const orderButtonStyle = {
    display: 'inline-block',
    backgroundColor: '#4CAF50', /* Green */
    border: 'none',
    color: 'white',
    textAlign: 'center',
    textDecoration: 'none',
    fontSize: '16px',
    margin: '4px 2px',
    cursor: 'pointer',
    padding: '15px 32px',
    position: 'absolute',
    right: '500px',  // Position the button towards the left
    borderRadius: '5px'
  };

  console.log("CARTITEMS",cartItems);

  const navigate = useNavigate();

  const handleOrder = async () => {
    try {
      const cartItemsObject = cartItems.reduce((obj, item) => {
        obj[item.id] = item;
        return obj;
      }, {});
  
      const response = await axios.post('http://127.0.0.1:7000/order', {
        cartItems: cartItemsObject,
        userId: userId,  // Use the user ID from context
      });
      console.log(response.data);  // Log the response from the server
  
      navigate('/order');
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <>
      <Navbar />
      <div>
        <h2 className='y-cart'>Your Cart</h2>
        {cartItems.length === 0 ?
          (<p className='empty'>Your Cart is Empty</p>) :
          <div>
            {cartItems.map((item) => {
              return (
                <div className='cart-section'>
                  <div className="cart-img">
                    <img src={item.image} alt="" />
                  </div>
                  <div className="cart-details">
                    <h3>{item.product}</h3>
                    <h2>
                      {item.price}
                    </h2>
                    <h3>{item.model}</h3>
                  </div>
                  <button className='removeBtn' onClick={() => removeFromCart(item)}>Remove</button>
                </div>
              )
            })}
            <button onClick={handleOrder} style={orderButtonStyle}>Order</button>
          </div>
        }
      </div>
    </>
  )
}

export default UserCart;