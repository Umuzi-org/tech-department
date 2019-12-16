---
title: OOP for data science
ready: False
---

## Prerequisite

You need to complete the Multivariate Regression assignment using the salary dataset before doing this assignment ({{% contentlink "projects/data-science-specific/multivariate-linear-regression" %}}). You will use the data and the model you built in that assignment for this OOP assignment.

## Assignment
It is efficient to put machine learning models and other data science techniques into classes so that we can reuse them later and change attributes without changing the code behind these models. Independent concepts can also be put into independent classes: for example, the functioning of a cross-validate class should not affect the functioning of a linear regression class. These concepts are also referred to as high cohesion and low coupling.

1. Create a class called `Metrics` that has methods to compute the Mean Squared Error, Root Mean Squared Error, R-squared and Adjusted R-squared. Name these methods `mse`, `rmse`, `r_squared` and `adj_r_squared`. The class should have the following parameters:

- `data_dict`: dictionary containing x_train, x_test, y_train and y_test data
- `model type`: an sklearn estimator instance (e.g. LinearRegression())

2. Create a  class called `DiagnosticPlots` that has methods to plot the (1) residuals versus predicted values and (2) predicted versus observed values. These methods should be called (1) `residual_vs_predicted` and (2) `predicted_vs_observed`.

3. Use the model you built in the Multivariate Regression project to predict log-transformed salary (`log_salary`). Also create a second multiple regression model which does not include yearsrank as a feature. Save these model instances as `model1` and `model2`. Remember to scale (standardise) the features before modelling.

In other words, you should have two models:

**Model 1:**

Features: exprior, yearsworked, yearsrank,  market, degree,  otherqual,  position,  male,  Field_dummyvariable1,  Field_dummyvariable2, Field_dummyvariable3,	yearsabs

**Model 2:**

Features: exprior,	yearsworked,  market,  degree,  otherqual,  position,  male,  Field_dummyvariable1, Field_dummyvariable2, Field_dummyvariable3, yearsabs

4. Use the classes created in questions 1 and 2 to get accuracy metrics and diagnostic plots for the two models. To keep the notebook neat, your classes should be imported from separate python files.
How does the model accuracy and diagnostics for the two models compare? Which is the better regression model?

5. [OPTIONAL] Create a class called `InfluentialValues` that takes a model object (e.g LinearRegression()) as an argument and has methods for calculating and displaying the following influential values and errors: leverage, Cook's distance, standardised residuals and studentised residuals. Call these methods `leverage`, `cooks_distance`, `standardised_residuals` and `studentised_residuals`. This is easiest to do using the package `statsmethods` to create the linear regression model object. Compare the performance of the two models - does one have better predictions (i.e. more accuracy, less bias) than the other?

*Tip:* These classes should be able to work with any regression problem. You can re-use these classes in upcoming assignments when inspecting models and you can also make classes in future that can work for both regression and classification problems.
