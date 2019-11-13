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

## Palindromes

Write a function that detects if an inputted string is a palindrome or not. It should return a boolean result.

```
# Python
is_palindrome("mom") # returns True
is_palindrome("Mom") # returns False
is_palindrome("rats live on no evil star") # returns True
is_palindrome("rats live on no evil star.") # returns False
```

```
// JavaScript
isPalindrome("mom") # returns true
isPalindrome("Mom") # returns false
isPalindrome("rats live on no evil star") # returns true
isPalindrome("rats live on no evil star.") # returns false
```

## compound interest

Write a function that calculates compount interest. It should return a number.

Eg if I have R100 in a bank account and I get 1% interest every month, I can see how much money I will have in my account at the end of each month like so:

Try it with a loop. Try it with recursion.

```
// JavaScript

function finalAmount(startAmount,interest,iterations){
    // clever things
}

finalAmount(100,0.01,1)    // 101.0
finalAmount(100,0.01,2)    // 102.01
finalAmount(100,0.01,3)    // 103.031
finalAmount(100,0.01,100)  // 270.481...
```

```
# Python

def final_mount(start_amount,interest,iterations):
    # clever things


final_amount(100,0.01,1)    // 101.0
final_amount(100,0.01,2)    // 102.01
final_amount(100,0.01,3)    // 103.031
final_amount(100,0.01,100)  // 270.481...
```

(life lesson: If I get 1% better every day...)

### advanced

Write a function that will figure out how many iterations are needed to meet a specific target amount. Eg: if I have R100 in a bank account and I get 1% interest every month, how many months do I have to wait before my bank acount contains R200?

There are a lot of ways to do this. Some are very inefficient (and easy to code). Some are more efficient (and hard to code). Try the easy way first. MAke it work then make it work well.

## String reverse

Make a function that can reverse a string

```
reverse("hello")  => olleh
```

## String rotate forward/backwards

```
rotate("hello",1) => elloh
rotate("hello",2) => llohe
rotate("hello",3) => lohel

rotate("hello",-1) => ohell
rotate("hello",-2) => lohel
rotate("hello",-3) => llohe
```

## Print (triangles & squares) using loops

**1.**

Write a function that takes in number as argument and prints a square
```
// JavaScript

<<<<<<< HEAD
let square(n) => 
expected output: remember to use "*" 

#####
#####
#####
#####
#####
```
**2.**
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

**3.**
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
**4.**
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
**5.**
Write a function that takes in number as argument and prints a hollow square in the center
```
// JavaScript
let square(n) => 
expected output: remember to use "*" 
#####
#   #
#   #
#   #
#####
```
**6.** 
Write a function that takes in number as argument and draws a pyramid triangle above using the " * " characters . If the input is 4, then the output is a traingle shaped as pyramid with height 4
```
// JavaScript
let triangle(5) => 
expected output: PYRAMID TRIANGLE.      
    
    *
   ***
  *****
 *******  
*********
```

**7.**
Write a function that takes in number as argument and draws a Hollow pyramid triangle above using the " * " characters . If the input is 4, then the output is a traingle shaped as pyramid with height 4
```
// JavaScript
let triangle(5) => 
expected output: HOLLOW RIGHT ANGLE TRIANGLE AND FOR ITS MIRROR.      
    
    *
   * *
  *   *
 *     *  
*********
```

**8.**
Write a function that takes in number as argument and draws the C pattern/shape
```
// JavaScript
let cPattern(5) => Expected output:

*****
*
*
*
*****
``` 
## Ceaser cipher

## fibonacci sequence
 **What is fibonacci sequence?**

> Fibonacci Sequence: is the series of numbers where the next number is found by adding up the n numbers before it.
> e.g. in this case n =2:
> sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

write a function that takes in a number argument [n] and returns fibonacci sequence of the given number [n], "series of values" 
```
//Javascript

function fibonacci(144)

Expected output:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

