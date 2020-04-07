---
date: 2020-04-07T17:08:16+02:00
title: BASIC SQL
weight: 3
pre: "<b>3. </b>"
---
 
***What is SQL?***

> **SQL**
<br> 

> 
- is a database computer language, designed for the retrieval and management of data in relational databases. 
E.g MySQL, MS Access, Oracle, Sybase, Postgres and SQL server, etc. 
Most widely used query language over the databases 


**Relational Database**

> 
- A set of formally described tables from which data can be accessed or reassembled in many different ways without having to reorganize the database tables.
The standard user and application programming interface (API) of a relational database is the:  [Structured Query Language SQL](
https://www.tutorialspoint.com/Types-of-databases)

**Relational Database**


>       | PERSON   |       |Publication |
>       |__________|->---<-|____________|    Schema Model
>       |ID   |    |       |ID    |     |  (ERD-diagram,DDL)
>       |Age  |    |       |Name  |     |   
>       |Name |    |       |      |     |
>       |_____|____|       |______|_____|     
>
>       ---------------------------------------------------------------------------
>       |  Table: Person    |    |-------|   |    Table:Publication  |
>       | ID  | Name |Age   |    | 1 | 1 |   | ID    | Name          |
>       | 1   | Rolf | 28   |    | 1 | 2 |   | 1     | Social tagging| Data Table
>       | 1   | Steff| 22   |    | 2 | 2 |   | 2     | Clasification |
>       |-----|------|------|    |___|___|   |_______|_______________|
