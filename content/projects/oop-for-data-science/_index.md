---
title: OOP for data science
ready: False
---

It is efficient to put machine learning models and other data science techniques into classes so that we can reuse them later and change attributes without changing the code behind these models. Independent concepts can also be put into independent classes: for example, the functioning of a cross-validate class should not affect the functioning of a linear regression class.

1. Create a cross-validate class that has two functions: train-test split and k-fold cross-validation. The class should have the following attributes:
-  `k` (the number of folds to split the data into; used for k-fold cross-validation)
- `split ratio` (the ratio for splitting the data into training and test sets, e.g. 80-20 split)

2. Create a metrics class that has functions to compute the Mean Squared Error, R-squared and Adjusted R-squared. The class should have the following attributes:

- x: 1D or 2D array of features/predictor variables
- y: 1D array containing the outcome variable
- model type (e.g. linear regression)

3. Create a linear regression model that predicts data science performance from literacy, numeracy, statistical aptitude and problem solving skills. The data can be found [here](provide link).

[Variable codebook](insert link)

4. Use your saved regression model with your cross-validation class to test the model on a (a) 80-20 split of the data, a (b) 70-30 split and a (c) 60-40 split. Save the model metrics in each case to a list or dataframe. Print the model metrics (as in question 2)- how do the different splits compare?

5. Use your saved regression model with your cross-validation class to run your model using (a) 3-fold cross-validation, (b) 5-fold cross-validation and (c) 10-fold cross-validation. Again, save your model metrics in each case. How does the model accuracy compare in each case?
