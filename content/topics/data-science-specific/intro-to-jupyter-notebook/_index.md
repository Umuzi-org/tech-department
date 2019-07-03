---
title: Introduction to Jupyter Notebooks
ready: True
---

## Setting Up Your Environment
Download and install miniconda on your machine. This will install python
and the conda package manager for python. NB Make sure that you set the
python path! Setting the path will allow you to simply type `python`
into the terminal to open python.

You also want to install the following packages:  
-  jupyter-notebook  
-  numpy  
-  pandas  
-  matplotlib  
-  seaborn  
-  scipy  
-  scikit-learn  

You can install packages by typing `conda install name-of-package`, e.g.
`conda install numpy`.

To launch a new jupyter instance (kernel), open up a new terminal, navigate to the directory in which you want to be
and type `jupyter notebook`(and press enter). A new jupyter kernel will open in your browser. You can now open an existing
notebook (`*.ipynb`) or create a new notebook.

When you are done, click 'Close and Halt Kernel' or press `Ctrl+C` twice to shut down the kernel from the terminal.


## Assignment
Complete the Nobel Prize Winner assignment and upload it to Github.
(You will need to create a Github account if you do not already have one.)
The assignment will be given to you separately.

You may want to go through DataCamp's [Python Programming](https://www.datacamp.com/tracks/python-programming) track to get the
basic skills you will need to complete the assignment.

## Supporting Material
[Python For Data Science Cheat Sheets](http://www.utc.fr/~jlaforet/Suppl/python-cheatsheets.pdf)  
[Jupyter Notebook Keyboard Shortcuts](https://www.cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/pdf_bw/)  
[Basic Python 3 Programming for Scientists](http://www.sixthresearcher.com/didactic-materials/)  

# Best practices for writing good Jupyter Notebooks
### by Webster Gova (webster.gova@umuzi.org), edited by Michelle Hoogenhout (michelle.hoogenhout@umuzi.org)
#### For Umuzi.Org

## Why use a notebook?
### Working alone
* Keep track of your thoughts
* Make sketch notes
* Add links to resources to review later
* Example notebook: https://danielfrg.com/blog/2013/03/kaggle-bulldozers-basic-cleaning/

### Working in a team
* For code review
* For colleagues to contribute to your notebook
* To write a report on your models
* As a tutorial guide
* To communicate with external clients/entities/blog
* Example notebook:
    * https://www.kaggle.com/burhanykiyakoglu/predicting-house-prices

## Tips for effective and efficient use of (jupyter) notebooks for data science projects

### Follow standard coding practices:

* Provide comments and documentation to your code
* Stick to a consistent naming scheme! Use meaningful names: answers_to_score is clearer than score_ans, which is clearer than score_1!
* Group code in a manner that allows anyone to follow the modelling process, e.g. data exploration (summary statistics, distributions, bar graphs, scatter plots), data transformation (outlier detection, counting & dropping/replacing NaN, renaming columns/rows etc), modelling and model evaluations (model scores and error)
* Limit length of code lines
* Refactor (restructuring) code whenever necessary to keep it simple

## Make it easy for other to follow and improve your work

* Have an author name and contact details in case someone wants to ask for clarity
* The notebook should be a standalone document that does not require someone to have to know about the problem being solved or in-depth knowledge of the algorithms. This will help others follow your thought processes and understand the data transformation/data analysis being done and why certain techniques are being used, since multiple techniques exist
* Tell the story: e.g. describe the problem being solved and how the model will solve that problem
* Summarise the data's statistical characteristics (to show that your data cleaning will not introduce artefacts or new features, and to show that the data are appropriate for the model(s) you use). This includes showing the variables' distribution and central tendency, as well as amount of available data.
* Exploratory techniques for summarizing data should be used before you start formal modeling and can help development of more complex statistical models & to eliminate or sharpen potential hypotheses about the world that can be addressed by the data. You will almost always want to see graphs of variable distributions, relationships between variables and missing data patterns.
* Provide enough rationale for each coding task being carried out (you will find this information useful when you read your own notebooks later)
* Critique your own model, this will help pre-empt and address shortcomings of your model and avoid loss of confidence in your model by others

### General tips
* Keep cells of your notebook simple: don't exceed the width of your cell
* Make sure that you don't put too many unrelated functions in one cell.
* It's neater to import all packages in the first code cell of your notebook
* Ensure graphics can display inline (use matplotlib inline magic commands & semicolons)
