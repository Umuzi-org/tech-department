---
title: data validation with Python and regex - string Calculator
ready: true
---

### Data Validation
##### Data validation means exactly what it sounds like—your program checks the data to make sure it meets some rules or restrictions. There are many different data validation checks that can be done. For example, we may check that:

  - data is of correct data type, for example a number and not a string
  - data does not have invalid values, such as provided zip code has a letter
  - data is not out of range, such as age given as negative number or there is division by zero
  - data meets constraints, for example given date can only be in future or message does not exceed maximum length
  - data is consistent with other data or constraint, for example student test score and student letter grade are consistent
  - data is valid, such as given filename is for an existing file
  - data is complete, such as making sure all required form fields have data

We check the data to make sure that the user did not make a mistake, accidentally or intentionally, which can prevent our program from functioning correctly or corrupt the data as this has security and data integrity implications.

#### Python regex
*Regular Expression(regex):* A regular expression (or RE) specifies a set of strings that matches it; the functions in this module let you check if a particular string matches a given regular expression (or if a given regular expression matches a particular string, which comes down to the same thing).

*Python Module:* Regular expression operations

*Usage:*
```py
import re
```

Read the Regular Expression Operations Documentation [here](https://docs.python.org/3/library/re.html), learn enough to know what regex is and to know how to go about regex-ing. You can also checkout some more material on YouTube, Google, DuckDuckGo, your choice.

Check out this [Topic]({{< ref "/topics/regular-expressions/_index.md" >}}), if you haven't.


#### Project
*Project description:* Complete the following [project](https://osherove.com/tdd-kata-1/)

* Do all the steps (1 - 9).
* Write tests every possible outcome.
