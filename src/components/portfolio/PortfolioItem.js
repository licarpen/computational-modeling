import React from 'react';
import styles from './PortfolioItem.css';
import PropTypes from 'prop-types';
import { usePortfolio } from '../../hooks/portfolio';
import { Link } from 'react-router-dom';

const PortfolioItem = ({ match }) => {
  const { title, image, description, script } = usePortfolio(match.params.title);

  return (
    <div className={styles.PortfolioItem}>
      <h2>{title}</h2>
      <div className={styles.links}>
        <a href={script} target='_blank' rel='noopener noreferrer' >Code</a>
        <Link className={styles.Link} to={'/'}>Back</Link>
      </div>
      <img src={image}/>
      <p className={styles.description}>{description}</p>
    </div>
  );
};

PortfolioItem.propTypes = { 
  match: PropTypes.shape({
    params: PropTypes.shape({
      title: PropTypes.string.isRequired
    }).isRequired
  }).isRequired
};

export default PortfolioItem;
