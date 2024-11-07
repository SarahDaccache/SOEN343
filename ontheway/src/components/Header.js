// Header.js
import React from 'react';
import './Header.css';

const Header = () => {
  return (
    <header className="header">
      <div className="logo">On The Way!</div>
      <nav className="nav">
        <a href="#register-package" className="nav-link">Register Package</a>
        <a href="#pricing" className="nav-link">Pricing</a>
        <a href="#chatbot-assistance" className="nav-link">Chatbot Assistance</a>
        <a href="#about" className="nav-link">About</a>
        <a href="#contact" className="nav-link">Contact</a>
        <a href="#sign-in" className="nav-link sign-in-button">Sign in</a>
        <a href="#register" className="nav-link register-button">Register</a>
      </nav>
    </header>
  );
};

export default Header;
