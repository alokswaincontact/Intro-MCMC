from statsmodels.discrete.discrete_model import Logit

# add an intercept since statsmodels does not
my_data['Intercept'] = 1

# fit the logistic regression model using MLE
mle_mod = Logit(my_data[target], my_data[['Intercept'] + vars_of_interest])
mle_mod_fit = mle_mod.fit(disp=False)

# print the summary
print(mle_mod_fit.summary())