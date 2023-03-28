import matplotlib.pyplot as plt

from mcmc_demo0 import *
from mcmc_demo1 import *

plt.figure(figsize=(12, 5), dpi= 80, facecolor='w', edgecolor='k')

plt.subplot(1, 2, 1)
plt.plot(mcmc_log_mod.raw_beta_distr[0], mcmc_log_mod.raw_beta_distr[1])
plt.title('Simulated Raw Joint Distribution of the Coefficients', fontsize=12)
plt.xlabel('Intercept', fontsize=10)
plt.ylabel('Coefficient of Price Percentile', fontsize=10)

plt.subplot(1, 2, 2)
plt.plot(mcmc_log_mod.beta_distr[0], mcmc_log_mod.beta_distr[1])
plt.title('Simulated Joint Distribution of the Coefficients without Burn-in', fontsize=12)
plt.xlabel('Intercept', fontsize=10)
plt.ylabel('Coefficient of Price Percentile', fontsize=10)
plt.show();


plt.figure(figsize=(12, 5), dpi= 80, facecolor='w', edgecolor='k')

plt.subplot(1, 2, 1)
plt.hist(mcmc_log_mod.beta_distr[0], density=True)
plt.title(f'Simulated Distr. of Intercept with {100 * (1-cred_int_alpha)}% Cred. Int.', 
          fontsize=12)
plt.xlabel('Intercept', fontsize=10)
plt.ylabel('Density', fontsize=10)
plt.axvline(x=mcmc_log_mod.cred_ints[0,0], color='r', linestyle='dashed', linewidth=2)
plt.axvline(x=mcmc_log_mod.cred_ints[0,1], color='r', linestyle='dashed', linewidth=2)

plt.subplot(1, 2, 2)
plt.hist(mcmc_log_mod.beta_distr[1], density=True)
plt.title(f'Simulated Distr. of Price Percentile Coef. with {int(100 * (1-cred_int_alpha))}% Cred. Int.', 
          fontsize=12)
plt.xlabel('Price Percentile Coefficient', fontsize=10)
plt.ylabel('Density', fontsize=10)
plt.axvline(x=mcmc_log_mod.cred_ints[1,0], color='r', linestyle='dashed', linewidth=2)
plt.axvline(x=mcmc_log_mod.cred_ints[1,1], color='r', linestyle='dashed', linewidth=2)
plt.show();

# to make the regression line
x_ = np.arange(my_data[vars_of_interest[0]].min(), 
              my_data[vars_of_interest[0]].max(), 
              step=0.01)
x_ = x_.reshape((-1, 1))
y_ = mcmc_log_mod.predict(x_)

plt.figure(figsize=(12, 5), dpi= 80, facecolor='w', edgecolor='k')

plt.plot(x_, y_, '-', color='r')
plt.scatter(X, y)
plt.hlines(xmin=x_[0], xmax=x_[-1], y=boundary, color='g', linestyle='dashed', linewidth=2)
plt.title('Price Percentile vs. Probability of Being Chocolate', fontsize=15)
plt.xlabel('Price Percentile', fontsize=15)
plt.ylabel('Probability of Being Chocolate', fontsize=15)
plt.show();
