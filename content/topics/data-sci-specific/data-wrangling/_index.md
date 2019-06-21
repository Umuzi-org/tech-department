---
title: Data Wrangling
ready: True
---

## Key concepts
- merging data frames
- filtering data frames
- manipulating rows and columns

## Tutorials
- Intro to pandas and data manipulation [here](https://www.kaggle.com/learn/pandas)
- If you'd like more, complete the DataCamp skills track [Data Manipulation with Python](https://www.datacamp.com/tracks/data-manipulation-with-python)


## Assignment

### Prerequisites
You should be familiar with data wrangling, unit testing, and functional programming techniques to complete this assignment. As far as possible, use functional programming techniques (map, reduce, apply) instead of loops when writing the functions below.

For example, to get modify every column in a data frame (to get a percentage in this case),  instead of writing:
```
for column in df:
  column = column/10*100
```

use:
```
def get_percentage(score):
  score/10*100

df.apply(get_percentage, axis = 1)
```

### Instructions

This data contains [personality scores](personality_scores.csv) for recruits, plus the [department](departments.csv) they applied for.

1. Read in the dataset [personality_scores.csv](personality_scores.csv) in this repo. Examine the data frame for duplicates (based on ID), and drop any duplicates that exist. Assert that the new data frame is the length of the unique entries of the original data frame.

2. Write functions that will (1) convert the answer on each of the personality test questions to a number, as set out in [scoring](scoring.md), and (2) calculate total scores for each of the subscales (conscientiousness, emotional stability, openness to new experience, agreeableness, extraversion). As you are doing this, first create unit tests that will test that the functions work as they should.

3. Create a function/functions that takes in subscale total, and for each subscale, creates a new column called "{subscale_name}_interpretation" (e.g., conscientiousness_interpretation) and applies the labels "low", "medium", or "high" according to a person's score on that subscale. Cut-off scores corresponding to the low, medium and high groups can be found in scoring.md.  Again, write a unit test before creating this function that tests whether the generate_score_interpretation function works.

4. Read in the data in [departments.csv](departments.csv) and merge this data frame with the personality score data frame, keeping all applicants within the department data frame. Assert that the newly created merged data frame has the same amount of rows as the department data frame, and the expected number of columns.

5. Create histograms of personality scores by department. You may need to clean some of the department names.

6. Filter the merged data frame so that you get only the ID numbers of applicants who score "low" on emotional stability, conscientiousness or agreeableness. Print the ID numbers and departments of these applicants to the screen, and also assign these applicants the tag "high_risk" in a new column.

7. Create a new data frame with a count of the number of applicants in each group ("high", "medium", "low") within each personality subscale and department. Let each department be a separate column, and each personality subscale be a separate row.
