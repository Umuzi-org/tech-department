---
title: SQL Database schema design
ready: True
---




In this topic, we will discuss the schema design. Here is what Wikipedia says about "Database Schema":

> The database schema of a database is its structure described in a formal language supported by the database management system. The term "schema" refers to the organization of data as a blueprint of how the database is constructed. [Wikipedia](https://en.wikipedia.org/wiki/Database_schema)

To help us understand the design process we will design an Umuzi.org physical database as an example. We will use Entity Relationship Diagram  (ERD) as a method to design our schema, I have selected [dbdiagram](https://dbdiagram.io) as a  tool to help us achieve this objective, I find the tool painless and straightforward, it provides fast feedback and I get to download a physical database right after, feel free to explore alternatives on the internet or experiment along.

This topic requires that you are a little bit familiar with [SQL](https://www.youtube.com/watch?v=27axs9dO7AE).

## The brief


As a developer working on a product you have been given a ticket that has the following requirements:
>Design a Umuzi's department database schema to handle data related to it.

The strategist on the team has added the following details to your ticket:
> The database you are about to design should handle the following queries
-  if the user has a recruit's full name he/she should be able to find which cohort the recruit belongs to.
-  if the user has a cohort name he/she should be able to find recruit(s) in it.
-  if the user has a staff member's email he/she should be able to retrieve recruits  he/she is servicing


## The steps

  Step 1:   idetify `entities` within a deparment
  ---

 Our "Umuzi" schema to include the following entities:

 - Departments
 - Cohorts
 - Recruits
 - staff

![step 1 image](./img/step_1.png)


  Step 2: Add more attributes
  ---
let establish all entities with their names and properties


![step 2 image](./img/step_2.png)

  Step 3: establish  relationships
  ---

  Each entity, attribute and relationship, should have appropriate names and that can be easily understood by the non-technical people as well. A relationship should connect entities.

 We will consider the following relationships within our  database :

- a one to one
- a one to many
- a many to many

### CASE 1 : One  to one relationship

Think on of a student who has joined a cohort,
having their name should allow a manger to retrieve his/her cohort.

The relationship is to be represented as follow:

![step 3 image](./img/one_one_rel.png)

The resulting joined table

![step 3 image](./img/one_one_result.png)

### CASE 2 : Many to one

On the other hand many recruits have been added to the same cohort, one cohort can contain many recruits, this is a `many to
one relationship`.

Our relationship representation becomes:

![step 3 image](./img/many_to_one_table.png)



### CASE 3 : Many to many relationship

 It is well known that a product at Umuzi might have one or more senior team members(staff) contributing to it. Assume you need to find out who are the seniors working on a team.

 ![step 3 image](./img/many_to_many_rel.png)

 This works for few data but what if the management require that more details about a manager performance on a project be stored as wel.
 We have a possibility to create a new table from the existing relationship, such tables ar called `bridge table`.

 ![step 3 image](./img/many_to_many_bridge.png)



Voila!

## A note about redundant records

Redundant tables and fields are a nightmare for database designers and administrators.

They draw on system resources in order to keep them secure, current and backed up. Redundant records may not seem like much when you are talking about just a dozen or so.

But in large databases where redundant fields could number thousands or millions, the computing resource overheads are substantial.

They unnecessarily increase the size of the database thus reducing efficiency and increasing the risk of data corruption.

Of course, there are times where redundancy may be necessary but this should be the exception and not the rule.

Even when redundancy is allowed, the reasons should be clearly documented to ensure removal by future database administrators when the reasons are no longer valid.

## Conclusion

Designing a database schema design is fairly a simple process, yet can prove to be complicated if the steps involved and concepts are not well implemented. This topic has defined a  database schema design, depicted entity discovery process, and finally explained the process of establishing relationships between entities.


## For more:

- To find out more about the difference between **data model** and **database schema** please click [here](https://www.quora.com/What-is-the-difference-between-a-data-model-and-database-schema)
- To find more about *database design* please click [here](https://www.guru99.com/database-design.html)
- [Learn SQL](https://www.w3schools.com/sql/sql_intro.asp).
- Find out more about relational database [here](https://dev.to/lmolivera/everything-you-need-to-know-about-relational-databases-3ejl)
- Check out [this article](https://likegeeks.com/database-design-mistakes/) on few mistakes in database design