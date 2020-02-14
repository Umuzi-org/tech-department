---
title: SQL Extended
---

We have had many sessions about JDBC Templates, JPA and Hibernate, so I would hope that you now have a clue of what we are talking about.

Remember the scripts you submitted for this https://umuzi-org.github.io/tech-department/projects/sql/ project now we are going to do this through JAVA.

## Part1

1. I would like to use vanilla java **(no Springboot)** connect to your database and perform the queries in part2 but only number [1-7]
2. I would like you to use Springboot JDBC templates to connect to your database and perform the queries in part2 but only number [1-9]
3. Lastly I would like you to use Hibernate + JPA to connect to your database and perform the queries in part2 [1-17]

**Part 2 of this project should be tested scenario by scenario**


## Part 2: Querying a database

Save all of your instructions in a script file - you will submit this file on Gnomio and github.

1. SELECT ALL records from table Customers.

2. SELECT records only from the name column in the Customers table.

3. Show the name of the Customer whose CustomerID is 1.

4. UPDATE the record for CustomerID = 1 on the Customer table so that the name is “Lerato Mabitso”.

5. DELETE the record from the Customers table for customer 2 (CustomerID = 2).

6. Select all unique statuses from the Orders table and get a count of the number of orders for each unique status.

7. Return the MAXIMUM payment made on the PAYMENTS table.

8. Select all customers from the “Customers” table, sorted by the “Country” column.

9. Select all products with a price BETWEEN R100 and R600.

10. Select all fields from “Customers” where country is “Germany” AND city is “Berlin”.

11. Select all fields from “Customers” where city is “Cape Town” OR “Durban”.

12. Select all records from Products where the Price is GREATER than R500.

13. Return the sum of the Amounts on the Payments table.

14. Count the number of shipped orders in the Orders table.

15. Return the average price of all Products, in Rands and in Dollars (assume the exchange rate is R12 to the Dollar).

16. Using INNER JOIN create a query that selects all Payments with Customer information.

17. Select all products that have turnable front wheels.