---
title: Multivariate Linear Regression
ready: True
---

This week is all about one-hot encoding and multiple regression.

## Background materials
- [Robust One-Hot Encoding in Python](https://blog.cambridgespark.com/robust-one-hot-encoding-in-python-3e29bfcec77e)
- [Emulating R Regression Plots in Python](https://medium.com/@emredjan/emulating-r-regression-plots-in-python-43741952c034)
- [Statsmodels Regression Plot](https://www.statsmodels.org/dev/examples/notebooks/generated/regression_plots.html)
- [Building and evaluating models](https://www.ritchieng.com/machine-learning-evaluate-linear-regression-model/).
- [Test/Train Splits and Crossvalidation](https://towardsdatascience.com/train-test-split-and-cross-validation-in-python-80b61beca4b6)

## Assignment
We will predict employee salaries from different employee characteristics (or features).
Import the data [salary.csv](salary.csv) to a Jupyter Notebook. A description of the variables is given in [Salary metadata.csv](Salary metadata.csv). You will need the packages matplotlib / seaborn, pandas and statsmodels.

### Steps and questions
1. Split your data into a training and test set. Create scatterplots, histograms, and a descriptive statistics table of the variables of interest. Do any of the variables need to be transformed to be able to use them in a linear regression model? Which variables seem like good predictors of salary?
2.	One-hot encode the variable Field into three dummy variables, using HR as the reference category. You can use pandas' `get_dummies()` function for this.
3.	Produce a correlation matrix comparing the relationship of salary to the predictor variables. Is there any multicollinearity or other problems that may be a problem in the multiple regression?
4.	Use multiple linear regression to predict salary from all the variables in the training dataset. Interpret the standardised coefficients given in the statsmodels output. What are the most important features when predicting employee salary?
5.	Calculate the standardised residuals (`resid()`) and standardised predicted values (`fittedvalues()`).
6. Plot the residuals versus the predicted values using seaborn's `residplot` with fitted values as the x parameter, and the dependent variable as y, specify `lowess=True`.
  * Are there any problems with the regression?
7. Now run your model on the test set. How does your model compare when running it on the test set - what is the difference in the Root Mean Square Error (RMSE) between the training and test sets? Is there any indication that the model has been overfit or does it seem like a reasonably good model?

## References

Data is made up and inspired by Cohen, Cohen, West & Aiken. Applied Multiple Regression/Correlation Analysis for the Behavioral Sciences, 3rd Edition.
