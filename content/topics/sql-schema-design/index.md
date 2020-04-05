---
title: SQL
ready: True
---

# Database schema design


In this topic, we will discuss the schema design. Here is what Wikipedia says about "Database Schema":

> The database schema of a database is its structure described in a formal language supported by the database management system. The term "schema" refers to the organization of data as a blueprint of how the database is constructed. [Wikipedia](https://en.wikipedia.org/wiki/Database_schema)

To help us understand the design process we will design an Umuzi.org physical database as an example. We will use Entity Relationship Diagram  (ERD) as a method to design our schema, I have selected [dbdiagram](https://dbdiagram.io) as a  tool to help us achieve this objective, I find the tool painless and straightforward, it provides fast feedback and I get to download a physical database right after, feel free to explore alternatives on the internet or experiment along.

## The brief


As a developer working on a product you have been given a ticket that has the following requirements:
>Design a department database schema to handle data related to it.

## The steps

  Step 1:   idetify `entities` within a deparment
  ---

 Our "Department" schema to include the following entities:

 - Departments
 - Cohorts
 - Recruits
 - staffs
[step 1 image](./img/step_1.png)


  Step 2: Each attribute in a given entity should have a unique name
  ---
let establish all entities with their names and properties
```
 DEPARTMENT
    -DEP_ID
    -DEP_NAME

COHORT
    -COHORT_ID
    -COHORT_NAME
    -COHORT_START_DATE
    -COHORT_END_DATE


STAFF
    -STAF_ID
    -STAFF_TYPE
    -STAF_FULL_NAME
    -STAF_EMAIL
    -STAF_DEPARTMENT

RECRUIT
    -RECRUIT_ID
    -RECRUIT_FULL_NAME
    -RECRUIT_DEPARTMENT
    -RECRUIT-COHORT
    -RECRUIT_PORTFOLIO_LINK
```
[step 2 image](./img/step_2.png)

  Step 3: establish  relationships
  ---

  Each entity, attribute and relationship, should have appropriate names and that can be easily understood by the non-technical people as well. A relationship should not be connected directly to each other, a relationship should connect entities.

 our entities within the "department schema" have the following relationships:

- Each department has a one or more staff member, a staff member is part of only one department at a time
- each cohort is linked to one or more department(s)
- each cohort has one or more recruits

We will consider only this scenario for now.

[step 3 image](./img/step_3.png)

Voila!

## Conclusion

Designing a database schema design is fairly a simple process, yet can prove to be complicated if the steps involved and concepts are not well implemented. This topic has defined a  database schema design, depicted entity discovery process, and finally explained the process of establishing relationships between entities.


## For more:


- To find out more about the difference bettwen **data model** and **database schema** please click [here](https://www.quora.com/What-is-the-difference-between-a-data-model-and-database-schema)
- To find more about *database design* please click [here](https://www.guru99.com/database-design.html)
- Find out more about relational database [here](https://dev.to/lmolivera/everything-you-need-to-know-about-relational-databases-3ejl)