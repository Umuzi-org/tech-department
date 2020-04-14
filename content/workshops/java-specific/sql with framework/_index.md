---
date: 2020-04-07T17:08:16+02:00
title: basic SQL with Framework
weight: 3
# pre: "<b>2. </b>"
---
 
***What is SQL?***

> **SQL**
<br> 

> 
- Is a database computer language, designed for the retrieval and management of data in relational databases. 
E.g MySQL, MS Access, Oracle, Sybase, Postgres and SQL server, etc.Most widely used query language over the databases 
- SQL stands for Structured Query Language
- SQL lets you access and manipulate databases
- SQL became a standard of the American National Standards Institute (ANSI) in 1986, and of the International Organization for Standardization (ISO) in 1987



**Relational Database**

> 
- A set of formally described tables from which data can be accessed or reassembled in many different ways without having to reorganize the database tables.
The standard user and application programming interface (API) of a relational database is the:  [Structured Query Language SQL](
https://www.tutorialspoint.com/Types-of-databases)

**Relational Database**


>       |  PERSON  |       |Publication |
>       |-----|----|->---<-|------|-----|    Schema Model
>       |ID   |    |       |ID    |     |  (ERD-diagram,DDL)
>       |Age  |    |       |      |     |   
>       |Name |    |       |Name  |     |
>       |-----|----|       |------|-----|     
>       ---------------------------------------------------------------------------
>       |  Table: Person    |    |-------|   |    Table:Publication  |
>       |-----|------|------|    |---|---|   |-----------------------|
>       | ID  | Name |Age   |    | 1 | 1 |   | ID    | Name          |
>       | 1   | Rolf | 28   |    | 1 | 2 |   | 1     | Social tagging| Data Table
>       | 1   | Steff| 22   |    | 2 | 2 |   | 2     | Clasification |
>       |-----|------|------|    |---|---|   |-------|---------------|

<br>

**(RDBMS) What is it used for?**

- Allows users to:
    + Access data in the RDBMS  
    + Describe users to describe the data.
    + Define the data and manipulate the data. 
    + Embed within other languages using 
    + SQL Modules.
    + SQL Libraries.
    + SQL Pre compilers.
- Allows users to:
    + create and drop databases and tables.
    + create view, stored procedure, functions in a database.
    + set permissions on tables, procedures and views.

**SQL Syntaxes and Data Types**

- [SQL-Quick ref (Syntax:)](https://www.w3schools.com/sql/sql_quickref.asp)
- [SQL-Quick ref (Data Types:)](https://www.tutorialspoint.com/sql/sql-data-types.htm)

**SQL Operators**

- Reserved word or a character used primarily in an SQL statement.
  - Types of Operators:
  - Arithmetic operators
  - Comparison operators
  - Logical operators
- [Negation operators](https://www.tutorialspoint.com/sql/sql-operators.htm)

**SQL Expressions** <br/> 

* Expression is a combination of one or more values, operators and SQL functions that evaluate to a value.
* SQL EXPRESSIONs are like formulae and they are written in query language.
* You can also use them to query the database for a specific set of data.

  - **Types of Expressions in SQL:**
    - Boolean
    - Numeric
    - Date

  - **Example of Expressions in SQL:**
    - SELECT * FROM CUSTOMERS WHERE SALARY = 10000;

  >       +----+-------+-----+---------+----------+
  >       | ID | NAME  | AGE | ADDRESS | SALARY   |
  >       +----+-------+-----+---------+----------+
  >       |  7 | Muffy |  24 | Indore  | 10000.00 |
  >       +----+-------+-----+---------+----------+

  - **Numeric Expression in SQL:**
    - SELECT (15 + 6) AS ADDITION;
  
  >      +----------+
  >      | ADDITION |
  >      +----------+
  >      |       21 |
  >      +----------+  

  - **Built-in functions like avg(), sum(), count(), etc.**	
    - SELECT COUNT(*) AS "RECORDS" FROM CUSTOMERS;

  >      +---------+
  >      | RECORDS |
  >      +---------+
  >      |       7 |
  >      +---------+

  - **Date Expressions.**	
    - SELECT COUNT(*) AS "RECORDS" FROM CUSTOMERS;
    - SELECT GETDATE();

  >     +---------------------+	    +-------------------------+
  >     | Current_Timestamp   |     |       GETDATE           |
  >     +---------------------+     +-------------------------+
  >     | 2009-11-12 06:40:23 |     | 2009-10-22 12:07:18.140 |
  >     +---------------------+     +-------------------------+

**SQL Modules (In Java).**
  
- A module consists of a group of procedures, which are called from the host programming language. 
- Each procedure contains a single SQL statement, and data is passed to and from the procedure through parameters.
- A module can be thought of as an object library that is linked to the application code. However, exactly how the procedures and the rest of the application are linked is - implementation-dependent.


**SQL Module using jOOQ.**

- You use jOOQ's code generator to connect to your database and generate Java classes that model your database tables and columns.
- Instead of writing SQL String statements with plain JDBC, you will use those generated Java classes to write your SQL queries.
- Can be used as a command line command in a supported IDE (Eclipse) or as a Maven plugin.  <br>
LINK -> [jOOQ + Sql-Module](https://www.jooq.org/doc/3.9/manual-single-page/)

#### SQL Module using jOOQ with Maven.

**Typical Maven Dependencies for jOOQ.**

    <dependency>                     | <dependency>                | <dependency>   
    <groupId>org.jooq</groupcfactId> | <groupId>org.jooq</groupId> | <groupId>org.jooq</groupId>
    <artifactId>jooq</artifactId>    | <version>3.12.4</version>   | <artifactId>jooq-codegen</artifactId> 
    <version>3.12.4</version>        | </dependency>               | <version>3.12.4</version> 
    </dependency>                    |                             | </dependency>
  
**jOOQ - Command Line.**

   - ***In SQL:***                          

    - SELECT 1 FROM DUAL
    - SELECT 1 FROM DUAL
    - UPDATE t SET v = 1

   - **Using jOOQ:**

    - create.selectOne().fetch()
    - create.selectOne().fetch();
    - create.update(T).set(T.V, 1).execute();

   - **jOOQ - As a string builder.**

    - // Fetch a SQL string from a jOOQ Query in order to manually execute it with another tool.
    - // For simplicity reasons, we're using the API to construct case-insensitive object references, here.
    - String sql = create.select(field("BOOK.TITLE"), field("AUTHOR.FIRST_NAME"), field("AUTHOR.LAST_NAME"))<br>
          .from(table("BOOK"))<br>
          .join(table("AUTHOR"))<br>
          .on(field("BOOK.AUTHOR_ID").eq(field("AUTHOR.ID"))<br>
          .where(field("BOOK.PUBLISHED_IN").eq(1948))<br> 
          .getSQL();

**Why use SQL Modules like jOOQ.** 
 
 - *jOOQ is different*
   - SQL was never meant to be abstracted. To be confined in the narrow boundaries of heavy mappers, hiding the beauty and simplicity of relational data. SQL was never meant to be object-oriented. SQL was never meant to be anything other than... SQL!
   - The dynamic SQL building power may be one of the biggest advantages of using a runtime query model like the one offered by jOOQ. Queries can be created dynamically, of arbitrary complexity.
   - jOOQ being close to the metal is that jOOQ supports many advanced or rarely used SQL features
   - The jOOQ DSL provides an easy and type safe way to query your data. This gives jOOQ an advantage over other low level approaches such as (god forbid) raw JDBC or Spring JDBC templates. 

**SQL Modules using Stored Procedure.** 

  - A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again.
  - You can also pass parameters to a stored procedure, so that the stored procedure can act based on the parameter value(s) that is passed.

**Stored Procedure Syntax.**

  - CREATE PROCEDURE procedure_name<br>
    - AS<br>
    - sql_statement<br>
    - GO;<br>
  - EXEC procedure_name;

**Stored Procedure example.**

  - CREATE PROCEDURE SelectAllCustomers
    - AS
    - SELECT * FROM Customers
    - GO;
  - EXEC SelectAllCustomers;

**Stored Procedure With Multiple Parameters**

- CREATE PROCEDURE SelectAllCustomers @City nvarchar(30), 
  @PostalCode nvarchar(10)
  - AS
  - SELECT * FROM Customers WHERE City = @City AND 
  <br>PostalCode = @PostalCode
  - GO;
- EXEC SelectAllCustomers @City = "London", @PostalCode = "WA1 1DP";


##### End of SQL Basics Part1...

![alt text](https://www.azquotes.com/picture-quotes/quote-art-has-always-been-this-pure-interrogation-rhetorical-question-less-the-rhetoric-whatever-samuel-beckett-123-66-83.jpg)














