---
title: Statistical Thinking
ready: True
---

## Background material
- [Crash Course Statistics: Measures of Spread](https://youtu.be/R4yfNi_8Kqw)
- [Crash Course Statistics: Plots, Outliers and Justin Timberlake](https://youtu.be/HMkllhBI91Y)
- [Crash Course Statistics: Correlation Doesn’t Equal Causation](https://youtu.be/GtV-VYdNt_g)

## Tutorials

Complete the DataCamp courses [Statistical Thinking in Python Part 1](https://www.datacamp.com/courses/statistical-thinking-in-python-part-1) and [Statistical Thinking in Python Part 2](https://www.datacamp.com/courses/statistical-thinking-in-python-part-2).

## Assignment

### Instructions
In the next series of challenges, we will predict employee salaries from different employee characteristics (or features). We ask employees working in four different fields to state their salary and some background information.

Import the data [salary.csv](salary.csv) to a Jupyter Notebook. You will need the packages matplotlib, seaborn, pandas and statsmodels. A description of the variables is given in [Salary metadata.csv](Salary metadata.csv).

### Questions
1.	How many responders are there? Are there any missing values in any of the variables?
2.	What is the lowest salary and highest salary in the group?
3.	What is the mean salary for the sample? Include the standard error of the mean.
4.	What is the standard deviation for the years worked?
5.	What is the median salary for the sample?
6.	What is the interquartile range for salary in the sample?
7.	How many men are there in the sample? How many women are there in the sample? Present this information in a table.
8.	How many women are executives compared to men?
9.	Create a histogram for the variable Salary.
10.	Examine the histogram and describe the distribution for Salary.
11.	Create a bar graph to show the different average salaries of men and women. (Bonus: Add error bars to the bars showing the 95% confidence interval). What does the graph tell you about the difference between men and women’s salaries?
12.	Create a scatterplot with seaborn showing the relationship between Years Worked and Salary (don’t forget to insert a trend line).
 * What is the relationship between Years Worked and Salary?
 * Describe any patterns in the scatterplot.
 * Do you notice any unusual/extreme values that do not fit the general trend? If you see any unusual values, briefly describe them (Who are they? In what way are they different?)
13.	Using the `pearsonr` function from the scipy.stats package, calculate the Pearson correlation coefficient (and its corresponding p value) to determine the nature of the relationship between Years Worked and Salary. See `help(pearsonr)` for help on this function.
 * Interpret the size and direction of the correlation statistic.
 * Is the relationship statistically significant? Report the appropriate statistic(s) to support your answer.
