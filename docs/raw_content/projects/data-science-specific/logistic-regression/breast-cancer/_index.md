---
title: Predict breast cancer
ready: True
---

## Assignment

Predict the class of breast cancer (malignant or 'bad' versus benign or 'good') from the features of images taken from breast samples. Ten biological attributes of the cancer cell nuclei have been calculated from the images, as described below:

|  Attribute               |     Domain |
| -------------------------| ----------------|
| 1. Sample code number            | id number|
| 2. Clump Thickness               | 1 - 10|
| 3. Uniformity of Cell Size       | 1 - 10|
| 4. Uniformity of Cell Shape      | 1 - 10|
| 5. Marginal Adhesion             | 1 - 10|
| 6. Single Epithelial Cell Size   | 1 - 10|
| 7. Bare Nuclei                   | 1 - 10|
| 8. Bland Chromatin               | 1 - 10|
| 9. Normal Nucleoli               | 1 - 10|
| 10. Mitoses                      | 1 - 10|
| 11. Class                        | (2 for benign, 4 for malignant)|

The data can be found [here](cancer.data).

At a minimum, you should complete these steps:
- Split the data into training and test sets.
- Get basic descriptive statistics for the training data and check for missing and incorrect values. Replace missing values if this makes sense to do.
- Do the necessary feature preparation and build a logistic regression model.

### Answer the following questions:

1. What are the factors that predict malignant cancer? (i.e. which variables significantly predict malignancy, *p* < 0.05)
2. Create a classification report and confusion matrix of predicted and observed values. What is the accuracy, precision, recall and F1-score of the model on the (a) training and (b) test data?
3. Plot a Receiver Operating Characteristic (ROC) curve on the test data.
4. What is overdispersion?
