import React from 'react';
import { useCart } from './context/CartContext';
import Navbar from './components/Navbar';
import { Link } from 'react-router-dom';  // Import Link

const UserCart = () => {
  const { cartItems, addToCart, removeFromCart } = useCart();

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

  console.log(cartItems);

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
            <Link to="/order" style={orderButtonStyle}>Order</Link>
          </div>
        }
      </div>
    </>
  )
}

export default UserCart;