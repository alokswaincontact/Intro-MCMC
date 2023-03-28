import pandas as pd
import numpy as np

from mcmc_demo0 import *

# load in field goal data
all_data = pd.read_csv('candy-data.csv')

# list of independent variables in the model
vars_of_interest = ['pricepercent']
# name of dependent variable
target = 'chocolate'

my_data = all_data[[target] + vars_of_interest]
my_data = all_data.dropna()

# make a column vector numpy array for the dependent variable
y = np.array(my_data[target]).reshape((-1,1))
# make a column vector numpy array for the independent variable
X = np.array(my_data[vars_of_interest]).reshape((-1,len(vars_of_interest)))

# make a numpy array for the beta means priors
beta_priors = np.repeat(0.0, len(vars_of_interest)+1) 
# make a numpy array for the beta standard deviation priors
prior_stds = np.repeat(1, len(vars_of_interest))
# make a row vector numpy array for the standard deviation of the jumper distribution
jumper_stds = np.repeat(0.1, len(vars_of_interest)+1) 

# set the number of iterations to run
num_iter = 50000
# set what early portion to burn out
burn_in = 0.1
# set an alpha for the credible interval
cred_int_alpha = 0.05
# set to true to add an intercept to the data
add_intercept = True
# set the random seed
random_seed = 1

# set the decision boundary for classes
boundary = 0.5

# create an instance of the mcmc_logistic_reg
mcmc_log_mod = mcmc_logistic_reg()
# create the untrimmed distribution of beta hats
mcmc_log_mod.mcmc_solver(y, 
                         X,
                         beta_priors, 
                         prior_stds,
                         jumper_stds, 
                         num_iter,
                         add_intercept,
                         random_seed)
# create a distribution of beta_hats without the burn-in
mcmc_log_mod.trim(burn_in)
# use the median of the beta hats distributions as the coefficients for prediction
mcmc_log_mod.fit(method='median')
# create credible intervals for the 
mcmc_log_mod.credible_int(cred_int_alpha)
