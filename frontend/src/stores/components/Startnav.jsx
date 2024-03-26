import React from "react";
import { Link } from "react-router-dom";

import { useCart } from "../context/CartContext";

const Navbar = () => {

  const { cartItems } = useCart()

  return (
    <div className="navbar-section">

      <div className="navSection">
        <Link to='/' className="custom-link">
          <div className="title">
            <h2>E-Mart</h2>
          </div>
        </Link>

        {/* <div className="search">
          <input type="text" placeholder="Search..." />
        </div> */}
        {/* <div className="user">
          <div className="user-detail">SignIN/SignUp</div>
        </div> */}
        <Link to="/login" className="custom-link">
          <h3>Login</h3>
        </Link>
        <Link to="/signup" className="custom-link">
          <h3>Signup</h3>
        </Link>
        <Link to='/cart'>
          <div className="cart">Cart
            <span>
              {cartItems.length}
            </span>
          </div>
        </Link>
      </div>
    </div >
  );
};

export default Navbar;
