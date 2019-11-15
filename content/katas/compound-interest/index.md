---
title: Compound interest
pre: "<b>1. </b>"
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

## compound Interest

**1.**
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
// Python

finalAmount(startAmount,interest,iterations):
    // clever things

=> expected output:
finalAmount(100,0.01,1)    // 101.0
finalAmount(100,0.01,2)    // 102.01
finalAmount(100,0.01,3)    // 103.031
finalAmount(100,0.01,100)  // 270.481...

```

### ADVANCED COMPOUND INTEREST

**2.** Write a function that will figure out how many iterations are needed to meet a specific target amount. Eg: if I have R100 in a bank account and I get 1% interest every month, how many months do I have to wait before my bank acount contains R200?

There are a lot of ways to do this. Some are very inefficient (and easy to code). Some are more efficient (and hard to code). Try the easy way first. MAke it work then make it work well.