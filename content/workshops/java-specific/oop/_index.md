---
date: 2020-04-07T15:03:16+02:00
title: oop in java 
weight: 3
# pre: "<b>1. </b>"
---

**Object Oriented Programing referred to as ( 'OOPs' ):** 

 ***What is OOPs?***

***OOPs/ Object Oriented Programing:*** 

> - *Is a way of writing computer programs which is using the idea of "objects" to represent data and methods. comprising of The four principles of object-oriented.*


**FOUR MAIN OOP CONCEPTS IN JAVA**

> + Abstraction 
> + Encapsulation
> + Inheritance
> + Polymorphism

**Abstraction**: 
``` 
Means using simple things to represent complexity. We all know how to turn the TV on, but we don’t need to know how it works in order to enjoy it. In Java, abstraction means simple things like objects, classes,and variables represent more complex underlying code and data. This is important because it lets avoid repeating the same work multiple times.
```

> **Data Abstraction**
```
Is the property by virtue of  which only the essential details are displayed to the user. The trivial or the non-essentials units are not displayed to the user. Ex: A car is viewed as a car rather than its individual components.
```
```
May also be defined as: the process of identifying only the required characteristics of an object ignoring the irrelevant details.The properties and behaviors of an object differentiate it from other objects of similar type and also help in classifying/grouping the objects.
```


> - **Abstraction in java.** 
 - ```
     In java, abstraction is achieved by interfaces and abstract classes. We can achieve 100% abstraction using interfaces.
    ```

> **Abstract classes and Abstract methods:**

- ```
An abstract class is a class that is declared with abstract keyword.
```
- ```
An abstract method is a method that is declared without an implementation.
```
- ```
An abstract class may or may not have all abstract methods. Some of them can be concrete methods.
```
- ```
A method defined abstract must always be redefined in the subclass,thus making overriding compulsory OR either make subclass itself abstract.
```
- ```
Any class that contains one or more abstract methods must also be declared with abstract keyword.
```
- ```
There can be no object of an abstract class.That is, an abstract class can not be directly instantiated with the new operator.
```
- ```
An abstract class can have parametrized constructors and default constructor is always present in an abstract class. 
```
- ```
An abstract class can extend an abstract class constructors. 
```
