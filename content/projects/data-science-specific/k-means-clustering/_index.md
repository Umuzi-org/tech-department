---
title: K-Means Clustering Assignment
ready: True
pre: "<b>MEDIUM: </b>"
ready: True
prerequisites:
  hard: ["projects/data-science-specific/statistical-thinking","projects/data-science-specific/data-visualisation","projects/data-science-specific/logistic-regression","topics/data-science-specific/clustering"]
  soft: ["topics/python-self-learning","topics/jupyter-notebooks-best-practices","topics/data-science-specific/data-science-methodology"]
tags: ["kmeans"]
---

## Pre-requisites

Read through the K-Means Tutorials at {{% contentlink "topics/data-science-specific/clustering" %}} before starting this project.

## Clustering whisky distilleries according to tasting Profiles

Data: [Whisky Tasting Profiles](whisky.csv)

Use K-Means clustering to cluster whisky distilleries by their tasting profile. Use the elbow or silhouette method to find the optimal number of clusters.

To see how successful clustering was, report relevant metrics (e.g. silhouette, adjusted rand index, etc.) and create a plot showing the different distilleries, their classes according to the k-Means clustering, and the distance between points. You can use `sklearn.manifold` to get Euclidean distances between points.

Describe the main differences between the cluster - what are the factors that differ between classes?
