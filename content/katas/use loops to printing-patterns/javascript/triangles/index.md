---
title: Katas
pre: "<b>5. </b>"
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

## Print (triangles & squares) using loops

**1.**

Write a function that takes in number as argument and draws a right angled triangle  using the " * " characters. If the input is 4, then the output is a traingle with height 4
 
```
// JavaScript
let triangle(4) => 
expected output: RIGHT ANGLE TRIANGLE
 
 *
 **         
 ***              
 ****
```
**2.**
Write a function that takes in number as argument and draws a reflection/mirror of right angled triangle above using the " * " characters . If the input is 4, then the output is a traingle with height 4
```
// JavaScript
let triangle(5) => 
expected output: MIRROR OF RIGHT ANGLE TRIANGLE

   *
  **              
 ***
****
```
**3.**

Write a function that takes in number as argument and draws a Hollow right angled triangle above using the " * " characters . If the input is 4, then the output is a traingle with height 4

```
// JavaScript
let triangle(5) => 
expected output: HOLLOW RIGHT ANGLE TRIANGLE AND FOR ITS MIRROR.      

*
* *
*  *
*   *
******
```