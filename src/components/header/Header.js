import React from 'react';
import styles from './Header.css';

const Header = () => {
  return (
    <div className={styles.Header}>
      <h1 className={styles.title}>Computational Modeling</h1>
      <h2 className={styles.author}>Code by Lisa Carpenter</h2>
      <p className={styles.description}>Simulations of Physical Systems from classical mechanics, electricity and magnetism, chaos, and statistical mechanics</p>
    </div>
  );
};

export default Header;
