## Introduction

This code is originally from John Clements titled _Intro to Markov Chain Monte Carlo_.
It was not working and the code was divided in a piecemeal fashion across
multiple files. I fixed the issues and made it work.


## Usage example

```sh
(py38) ~/Intro-MCMC$ python main.py 
100%|████████████████████████████████████| 50000/50000 [00:52<00:00, 951.27it/s]
                           Logit Regression Results                           
==============================================================================
Dep. Variable:              chocolate   No. Observations:                   85
Model:                          Logit   Df Residuals:                       83
Method:                           MLE   Df Model:                            1
Date:                Tue, 28 Mar 2023   Pseudo R-squ.:                  0.2026
Time:                        14:18:17   Log-Likelihood:                -46.409
converged:                       True   LL-Null:                       -58.204
Covariance Type:            nonrobust   LLR p-value:                 1.193e-06
================================================================================
                   coef    std err          z      P>|z|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept       -2.3558      0.570     -4.134      0.000      -3.473      -1.239
pricepercent     4.3104      1.024      4.209      0.000       2.303       6.318
================================================================================
(py38) ~/Intro-MCMC$ 
```

## Development setup

Use _Python 3.8_

```sh
pip install -r requirements.txt
```

## Reference

- Intro to Markov Chain Monte Carlo 
  MCMC Explained and Applied to Logistic Regression 
  https://towardsdatascience.com/intro-to-markov-chain-monte-carlo-c6f217e00345

- The Ultimate Halloween Candy Power Ranking 
  https://www.kaggle.com/datasets/fivethirtyeight/the-ultimate-halloween-candy-power-ranking
