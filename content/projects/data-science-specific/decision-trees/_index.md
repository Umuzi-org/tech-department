---
title: Decision Trees
ready: True
---

## Background material
- Walk through the [machine learning Kaggle tutorial](https://www.kaggle.com/learn/intro-to-machine-learning)
- Complete the DataCamp tutorial on [Tree-Based Models](https://www.datacamp.com/courses/machine-learning-with-tree-based-models-in-python)

## Assignment
Use a decision tree model to predict whether mushrooms are poisonous or edible.
1. Split your data into train and test sets.
2. Get basic descriptive statistics for the training data and check for missing and incorrect or extreme values. Get scatterplots or heatmaps showing the relationship between the variables.
3. What are the factors that predict whether a mushroom is poisonous?
4. Report the accuracy of your model on the training set and on the test set. How successful is the model - what is its precision and recall?
5. What is the prevalence of poisonous mushrooms in the dataset? How might prevalence affect the positive and negative predictive values of a test/model?

Find the data [here](agaricus-lepiota.data).

## More information on decision trees
[Coursera: Decision Trees](https://www.coursera.org/lecture/python-machine-learning/decision-trees-Zj96A)

## Description of the dataset

This dataset includes descriptions of 23 species of gilled mushrooms in the Agaricus and
Lepiota Family. Each species is identified as either edible or poisonous.

Features Information: (classes: edible=e,  poisonous=p)  
     1. cap-shape:                bell=b, conical=c, convex=x, flat=f,
                                  knobbed=k, sunken=s  
     2. cap-surface:              fibrous=f, grooves=g, scaly=y, smooth=s  
     3. cap-color:                brown=n, buff=b, cinnamon=c, gray=g, green=r,
                                  pink=p, purple=u, red=e, white=w, yellow=y  
     4. bruises?:                 bruises=t, no=f  
     5. odor:                     almond=a, anise=l, creosote=c, fishy=y, foul=f,
                                  musty=m, none=n, pungent=p, spicy=s  
     6. gill-attachment:          attached=a, descending=d, free=f, notched=n  
     7. gill-spacing:             close=c, crowded=w, distant=d  
     8. gill-size:                broad=b, narrow=n  
     9. gill-color:               black=k, brown=n, buff=b, chocolate=h, gray=g,
                                  green=r, orange=o, pink=p, purple=u, red=e,
                                  white=w, yellow=y  
    10. stalk-shape:              enlarging=e, tapering=t  
    11. stalk-root:               bulbous=b, club=c, cup=u, equal=e,
                                  rhizomorphs=z, rooted=r, missing=?  
    12. stalk-surface-above-ring: fibrous=f, scaly=y, silky=k, smooth=s  
    13. stalk-surface-below-ring: fibrous=f, scaly=y, silky=k, smooth=s  
    14. stalk-color-above-ring:   brown=n, buff=b, cinnamon=c, gray=g, orange=o,
                                  pink=p, red=e, white=w, yellow=y  
    15. stalk-color-below-ring:   brown=n, buff=b, cinnamon=c, gray=g, orange=o,
                                  pink=p, red=e, white=w, yellow=y  
    16. veil-type:                partial=p, universal=u  
    17. veil-color:               brown=n, orange=o, white=w, yellow=y  
    18. ring-number:              none=n, one=o, two=t  
    19. ring-type:                cobwebby=c, evanescent=e, flaring=f, large=l,
                                  none=n, pendant=p, sheathing=s, zone=z
    20. spore-print-color:        black=k, brown=n, buff=b, chocolate=h, green=r,
                                  orange=o, purple=u, white=w, yellow=y  
    21. population:               abundant=a, clustered=c, numerous=n,
                                  scattered=s, several=v, solitary=y  
    22. habitat:                  grasses=g, leaves=l, meadows=m, paths=p,
                                  urban=u, waste=w, woods=d
