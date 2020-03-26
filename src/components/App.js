import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import PortfolioItem from '../components/portfolio/PortfolioItem';
import PortfolioList from '../components/portfolio/PortfolioList';
import './App.css';

export default function App() {
  return (
    <Router>
      <Route exact path='/' component={PortfolioList}/>
      <Switch>
        <Route path='/:title' component={PortfolioItem} />
      </Switch>
    </Router>
  );
}
  
