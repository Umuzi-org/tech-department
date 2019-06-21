---
title: MySQL Assesment
---
## NCIT Units

## Instructions
- Save all of your instructions in a script file - you will submit this file on Gnomio and github.
- save it as `MySql Assessment 114048 & 114049 Part 1``

Download MySQL and install on Ubuntu; also install the MySQLdb library in python (using conda or pip install).
The MySQLdb package will allow you to use python to interface with your MySQL database.


## Questions

1. Open a mySQL connection in python.
2. Create a database called "Umuzi".

3. Create the following tables
    - Customers
    - Employees
    - Orders
    - Payments
    - Products

4. Create a Primary key for each table with auto-increment (make sure you correctly specify the data types, e.g. the ID field should be `int`).
5. Create a Foreign key for the tables.

Create a query that will:

6. INSERT the following records to the tables described above.

### Customer Table

| CustomerID | FirstName | LastName | Gender | Address | Phone | Email | City | Country |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1	| John | Hibert | Male | 284 chaucer st| 084789657 (int 10)	| john@gmail.com (varchar 100) | Johannesburg | South Africa  |
| 2 | Thando | Sithole | Female | 240 Sect 1 | 0794445584 | thando@gmail.com (varchar 100) | Cape Town | South Africa |
| 3 | Leon | Glen | Male | 81 Everton Rd,Gillits | 0820832830 | Leon@gmail.com (varchar 100) | Durban | South Africa |
| 4 | Charl | Muller | Mal | 290A Dorset Ecke | +44856872553 | Charl.muller@yahoo.com (varchar 100) | Berlin | Germany |
| 5 | Julia | Stein | Female | 2 Wernerring | +448672445058 | Js234@yahoo.com (varchar 100) | Frankfurt | Germany |



### Employees Table

| EmployeeID | FirstName | Last Name  |  Email |  Job Title |
| --- | --- | --- | --- | --- |  
| 1 (int) | Kani (varchar 50) | Matthew (varchar 50) | mat@gmail.com (varchar 100) | Manager |
| 2 (int) | Lesly (varchar 50) | Cronje (varchar 50) | LesC@gmail.com (varchar 100) | Clerk |  
| 3 (int) | Gideon (varchar 50) | Maduku (varchar 50) | m@gmail.com (varchar 100) | Accountant |


### Orders Table

| OrderId | Order | Date Required | Date Shipped | Status |  
| --- | --- | --- | --- |--- |  
| 1 (int) | 01-09-2018 (datetime) | 05-09-2018 | 02-09-2018 | Not shipped |
| 2 (int) | 01-09-2018 (datetime) | 04-09-2018 | 03-09-2018 | Shipped |  
| 3 (int) | 01-09-2018 (datetime) | 03-09-2018 | 02-09-2018 | Not shipped |  

### Payments Table

| CustomerId | PaymentDate | Amount |    
| --- | --- | --- |  
| 1 (int) | 01-09-2018 (datetime) | R100.00 (decimal) |  
| 2 (int) | 01-09-2018 (datetime) | R250.75 (decimal) |  

### Products Table

| ProductId | ProductName | Description | BuyPrice |  
| --- | --- | --- | --- |  
| 1 (int) | Harley Davidson Chopper | This replica features working kickstand, front suspension, gear-shift lever | R150.75 (decimal) |
| 2 (int) | Classic Car | Turnable front wheels, steering function | R550.75 (decimal) |  
| 3 (int) | Sports car | Turnable front wheels, steering function | R700.60 (decimal) |
