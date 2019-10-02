---
title: Data Validation
ready: false
---

### Data Validation
Data validation means exactly what it sounds like, your program checks the data to make sure it meets some rules or restrictions. Validation and verification are two ways to check that the data entered into a computer is correct, because data entered incorrectly is of little use. There are many different data validation checks that can be done.

### Types of validation
There are a number of validation types that can be used to check the data that is being entered.

| Validation type | How it works                                                                        | Example usage                                                                                         |   |   |
|-----------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|---|---|
| **Check digit**     | The last one or two digits in a code are used to check the other digits are correct | Bar code readers in  supermarkets use check digits                                                    |   |   |
| **Format check**    | Checks the data is in the  right format                                             | A National Insurance number is in the form LL 99 99 99 L  where L is any letter and 9  is any number. |   |   |
| **Length check**    | Checks the data isn't too short or too long                                         | A password which needs to be six letters long                                                         |   |   |
| **Lookup table**    | Looks up acceptable values in a table                                               | There are only seven possible days of the week                                                        |   |   |
| **Range check**     | Checks that a value falls  within the specified range                               | Number of hours worked must be  less than 50 and more than 0                                          |   |   |
| **Spell check**     | Looks up words in a dictionary                                                      | When word processing                                                                                  |   |   |
| **Presence check**  | Checks that data has been entered into a field                                      | In most databases a key field cannot be left blank                                                    |   |   |


We check the data to make sure that the user did not make a mistake, accidentally or intentionally, which can prevent our program from functioning correctly or corrupt the data as this has security and data integrity implications.

### Data Validation
Verification is performed to ensure that the data entered exactly matches the original source.

### Methods of verification
There are two main methods of verification:

- **Double entry** - entering the data twice and comparing the two copies. This effectively doubles the workload, and as most people are paid by the hour, it costs more too.
- **Proofreading data** - this method involves someone checking the data entered against the original document. This is also time-consuming and costly.
