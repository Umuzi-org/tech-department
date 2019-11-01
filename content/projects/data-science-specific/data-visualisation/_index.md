---
title: Data Visualisation Projects
ready: True
---

## Background

Make sure you have gone through at least one of the tutorial listed in
{{% contentlink "topics/data-science-specific/data-visualisation" %}}


## Assignment 1
Once you have completed the course, complete the DataCamp project
[Exploring the Evolution of Linux](https://www.datacamp.com/projects/111).  

## Assignment 2:
Complete the data visualisation assignment on Financial Services Use in Tanzania

The [training](training.csv) dataset contains demographic information and what financial services are used by approximately 10,000 individuals across Tanzania. This data was extracted from the FSDT Finscope 2017 survey and prepared specifically for this challenge. A more detailed description of variables from the Finscope survey are explained in {{% contentlink "projects/data-science-specific-data-visualisation/mobile-money-viz" %}}.

Each individual is classified into four mutually exclusive categories:

- No_financial_services: Individuals who do not use mobile money, do not save, do not have credit, and do not have insurance
- Other_only: Individuals who do not use mobile money, but do use at least one of the other financial services (savings, credit, insurance)
- Mm_only: Individuals who use mobile money only
- Mm_plus: Individuals who use mobile money and also use at least one of the other financial services (savings, credit, insurance)

This dataset is the geospatial mapping of all cash outlets in Tanzania in 2012. Cash outlets in this case included commercial banks, community banks, ATMs, microfinance institutions, mobile money agents, bus stations and post offices. This data was collected by FSDT.


## Instructions:

1. Examine the dataset. Are there any missing observations or columns where the data do not seem valid?  

2. Get basic descriptive statistics for the dataset.

3. Create appropriate graphs to visually represent the relationship between financial services accessed (non-mobile, mobile, both) and age, gender, marital status, land ownership and type of income.  

4. Create appropriate graphs to visually represent the relationship between how often mobile services are used and age, gender, marital status, land ownership and type of income.

5. Create a map to visually explore geographic distribution of mobile services coverage with respect to type of income.

6. What can you conclude about use of financial services in Tanzania? Which demographic and geographic factors are associated with mobile money use?

**Advanced**: [Here](https://kyso.io/KyleOS/cufflinks-intro?utm_campaign=News&utm_medium=Community&utm_source=DataCamp.com%20add%20to%20curriculum%20visualisation) is a great walk-through of different types of plots in [Plotly](https://plot.ly/python/) with [Cufflinks](https://plot.ly/ipython-notebooks/cufflinks/).

### Submission
Create a repo on Github to complete this assignment. Start a new notebook and commit your notebook changes to Github. Once you are done, create an html report from the notebook.
