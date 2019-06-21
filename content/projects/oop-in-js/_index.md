---
date: 2019-03-19T16:50:16+02:00
title: OOP in Js
weight: 15
---


## Assignment 1: Basics

Assignment Description

Create a class called Person which defines the generic data and functionality of a person. Now as we know there are a lot of things involved with a Person e.g (age,gender,their address, height, shoe size, passport number, etc). but in this case we are only interested in showing their name, age, gender, and interests, and we also want to be able to write a short introduction about them based on this data, and get them to say Hello. This is known as abstraction in OOP ,creating a simple model of a more complex thing, which represents its most important aspects in a way that is easy to work with for our program's purposes.

Remember!
From your Person class, you will create object instances — objects that contain the data and functionality defined in the class.

E.g) Class: Person 
Name
Surname
Age
Gender
Interests: an array of activities/interests
Full Name: returns the person’s Name + Surname
Greeting: “Hello I’m +Name!”

Object: FirstPerson
Name: Nosipho
Surname: Masondo
Age: 8
Gender: Female
Interests: Dancing,Singing
Greeting: “Hello I’m Nosipho”

Object: SecondPerson
Name: Thando
Surname: Ngwane
Age:16
Gender: Male
Interests: playing games,drawing
Method: I am Thando Ngwane I am 16 and my interests are playing games and and drawing.


When an object instance is created from a class, the class's constructor function is run to create it. This process of creating an object instance from a class is called instantiation — the object instance is instantiated from the class.

In JavaScript we use special functions called constructor functions to define objects and their features.They are useful because you'll often come across situations in which you don't know how many objects you will be creating; constructors provide the means to create as many objects as you need in an effective way, attaching data and functions to them as required.

I hope this information is useful!




## Assignment 2: Dice
You’ve all seen dice before. A die (singular for dice) usually has 6 sides, but can have more. Eg 20 sided dice are a thing.

A die has a value (eg if 1 dot is showing then the value is 1). When a die is rolled then it’s value randomly changes. A six sided die has a ⅙ chance of landing on any of the sides. 

A weighted die is less random. A weighted die has a higher chance of landing on a specific number (or specific numbers).

Draw a class diagram to represent the above
Write the code

Dice are made in a factory. A factory can only make one kind of die. Eg there could be a factory that only makes 6 sided dice, and another factory that only makes 20 sided dice.

Factories are imperfect, sometimes there are manufacturing flaws. Every factory has a possibility of creating a weighted die by mistake. 

 3. Create a DiceFactory class. It should have a method called makeDie that outputs a single die instance

Since dice factories are imperfect, their outputted dice need to be tested. A dice tester can test one die at a time. It tests the die by rolling it a bunch of times and checking that the results are properly random. A dice tester can only test one kind of die, for example one dice tester might only test 6 sided dice, and another might only test 20 sided dice. 

4. Write a class to represent a DiceTester. It should have a method called testDie that has a single die as an input and returns True if the die is fair. If the wrong kind of Die is input then the DiceTester should be able to detect that and log an error.



## Assignment 3: Compound interest
A Bank Account has a balance, an interest rate and a monthly fee.

For example if a person has an interest rate of 12% (which is totally unrealistic but make the numbers easier) and they have R1000 in their bank account then they will receive (R1000 x 12% / 12) after one month of saving. That means they earned R10 in interest. Now if their monthly fee on that account is R50 then their final balance after 1 month is R1000+R10-R50 = R960.

The balance of a bank account can also change if a deposit or withdrawal is made. Money can also be transferred between bank accounts.

A bank account also has a type, for example Cheque, Savings or Credit Card. Bank accounts belong to People. One person can own multiple bank accounts.  

A bank account also has a number that uniquely identifies it within the bank. If I wanted to transfer money from my bank account to yours then all I should need is your bank account number.

Draw a UML diagram that depicts all the classes described above
Write code to match your UML 
