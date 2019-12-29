---
title: OOP for data science
ready: True
---

## Prerequisite

You need to complete the Multivariate Regression assignment using the salary dataset before doing this assignment ({{% contentlink "projects/data-science-specific/multivariate-linear-regression" %}}). You will use the data and the model you built in that assignment for this OOP assignment.

## Assignment
It is efficient to put machine learning models and other data science techniques into classes so that we can reuse them later and change attributes without changing the code behind these models. Independent concepts can also be put into independent classes: for example, the functioning of a cross-validate class should not affect the functioning of a linear regression class. These concepts are also referred to as high cohesion and low coupling.

1. Create a class called `ErrorCalculator` that has methods to compute the residuals, [standardised residuals](https://www.isixsigma.com/dictionary/standardized-residual/), Mean Squared Error and Root Mean Squared Error. Name these methods `get_residuals`, `get_standardised_residuals`, `get_mse` and `get_rmse`. You can also have a method, `error_summary` that prints the average, minimum and maximum of the standardised residuals, as well as the mse and rmse.

The class should have the following parameters:

- `y`: A 1D array of the target variable, size n_observations
- `y_pred`: A 1D array of the predicted values of the target variable, size n_observations

2. Create a  class called `DiagnosticPlotter` that inherits from `ErrorCalculator` and has methods to plot the (1) residuals versus predicted values and (2) predicted versus observed values. These methods should be called (1) `residual_vs_predicted_graph` and (2) `predicted_vs_observed_graph`.

3. Use the model you built in the Multivariate Regression project to predict log-transformed salary (`log_salary`). Also create a second multiple regression model which does not include yearsrank as a feature. Save these model instances as `model1` and `model2`. Remember to scale (standardise) the features before modelling.

In other words, you should have two models:

**Model 1:**

Features: exprior, yearsworked, yearsrank,  market, degree,  otherqual,  position,  male,  Field_dummyvariable1,  Field_dummyvariable2, Field_dummyvariable3,	yearsabs

**Model 2:**

Features: exprior,	yearsworked,  market,  degree,  otherqual,  position,  male,  Field_dummyvariable1, Field_dummyvariable2, Field_dummyvariable3, yearsabs

4. Use the classes created in questions 1 and 2 to get accuracy metrics and diagnostic plots for the two models. To keep the notebook neat, your classes should be imported from separate python files.
How does the model accuracy and diagnostics for the two models compare? Which is the better regression model?

5. [OPTIONAL] Create a class called `InfluenceCalculator` that takes a model fit object as an argument and has methods for calculating and displaying leverage values and Cook's distance. Call these methods `leverage`, `cooks_distance`. This is easiest to do using the package `statsmethods` to create the linear regression model object. Are there any observations that may be influencing the models?

*Tip:* These classes should be able to work with any regression problem. You can re-use these classes in upcoming assignments when inspecting models and you can also make classes in future that can work for both regression and classification problems.
