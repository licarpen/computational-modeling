import React from 'react';
import styles from './Header.css';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <div className={styles.Header}>
      <Link className={styles.Link} to={'/'}>
        <h1 className={styles.title}>Computational Modeling</h1>
        <h2 className={styles.author}>Code by Lisa Carpenter</h2>
        <p className={styles.description}>Simulations of physical systems from classical mechanics, electricity and magnetism, chaos, and statistical mechanics</p>
      </Link>
    </div>
  );
};

export default Header;
