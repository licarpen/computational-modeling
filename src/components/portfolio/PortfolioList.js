import React from 'react';
import styles from './PortfolioList.css';
import { Link } from 'react-router-dom';
import { models } from '../../data/models';
import Footer from '../footer/Footer';

const PortfolioList = () => {
  const portfolioItemElements = models.map(item => (
    <li key={item.title} className={styles.card}>
      <Link className={styles.Link} to={`/${item.title}`}>
        <h2 className={styles.title}>{item.title}</h2>
        <div className={styles.imgDiv}>
          <img src={item.imageSmall} alt={item.title}/>
        </div>
      </Link>
    </li>
    
  ));

  return (
    <>
      <ul className={styles.PortfolioList}>
        {portfolioItemElements}
      </ul>
      <Footer />
    </>
  );
};

export default PortfolioList;
