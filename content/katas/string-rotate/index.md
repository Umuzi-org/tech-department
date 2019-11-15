---
title: String rotate
pre: "<b>4. </b>"
weight: 5
---

This section just has a bunch of little excersises. For the most part they are language agnostic puzzles that can be used in a bunch of different ways:

- recruits can use them to practice on their own
- whiteboarding excercises
- pair programming excercises
- practicing tdd

**Guidelines**
Make sure you can do this stuff without relying heavily on the built in functions. Eg if the goal is to find the maximum number in the list, using the `max` function wont teach you a thing. This is about algorithmic thinking. The mental capabilities you will build by doing these excercises are much more important than memorising built in functions. You should end up with skills you can apply to problems in other languages.

**NOTE** all the string excercises listed should be adapted to work with arrays as well


## String rotate forward/backwards

Write a function that takes in string argument and n (number) argument and the rotate the given string to nth position

```
rotate("hello",1) => elloh
rotate("hello",2) => llohe
rotate("hello",3) => lohel

rotate("hello",-1) => ohell
rotate("hello",-2) => lohel
rotate("hello",-3) => llohe
```