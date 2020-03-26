import { models } from '../data/models';

export const usePortfolio = title => {
  const portfolioItem = models.find(item => item.title === title);

  return portfolioItem;
};
