---
title: OOP for data science
ready: False
---

## Prerequisite

You need to have completed the Multivariate Regression assignment using the salary dataset before doing this assignment ({{% contentlink "projects/data-science-specific/multivariate-linear-regression" %}}). You will use the data and the model you built in that assignment this OOP assignment.

## Assignment
It is efficient to put machine learning models and other data science techniques into classes so that we can reuse them later and change attributes without changing the code behind these models. Independent concepts can also be put into independent classes: for example, the functioning of a cross-validate class should not affect the functioning of a linear regression class.

1. Create a metrics class that has methods to compute the Mean Squared Error, R-squared and Adjusted R-squared. The class should have the following attributes:

- `x`: 1D or 2D array of features/predictor variables
- `y`: 1D array containing the outcome variable
- `model type` (e.g. linear regression)

2. Create a diagnostic_plots class that has methods to plot the (1) residuals versus predicted values and (2) predicted versus observed values.

3. [OPTIONAL] Create a class that takes a linear regression model object as an attribute and has methods for calculating and displaying the following influential values and errors: leverage, Cook's distance, standardised residuals and studentised residuals. This is easiest to do using statsmethods to create the linear regression model object.

4. Use the salary dataset and the model for predicting Salary that you built in the Multivariate Regression assignment. We are going to compare this model's performance to a new model using all the features EXCEPT yearsrank. Create this second multiple regression model now.

You should have two models:

**Model 1:**

salary ~ exprior +	yearsworked	+ yearsrank	+ market	+ degree	+ otherqual	+ position	+ male	+ Field_dummyvariable1 + Field_dummyvariable2 + Field_dummyvariable3 +	yearsabs

**Model 2:**

salary ~ exprior +	yearsworked	+ market	+ degree	+ otherqual	+ position	+ male	+ Field_dummyvariable1 + Field_dummyvariable2 + Field_dummyvariable3 + yearsabs

5. Use your newly created classes to get accuracy metrics and diagnostic plots (and influential values if you chose to calculate these) for the two models. To keep the notebook neat, your classes should be in imported from separate python files. How does the model accuracy and diagnostics for the two models compare? Which is the better regression model?
