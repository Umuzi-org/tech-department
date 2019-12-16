---
title: Level 1 programming katas
ready: true
---

The following exercises are put together to help you practise kotlin. These will give you the opportunity to practise the language and familiarise yourself with the syntax of the language
as well as give you the opportunity to test your knowledge.

You can practise basic practices here: [Online Kotlin Compiler](https://play.kotlinlang.org/#eyJ2ZXJzaW9uIjoiMS4zLjYxIiwicGxhdGZvcm0iOiJqYXZhIiwiYXJncyI6IiIsImpzQ29kZSI6IiIsIm5vbmVNYXJrZXJzIjp0cnVlLCJ0aGVtZSI6ImlkZWEiLCJjb2RlIjoiLyoqXG4gKiBZb3UgY2FuIGVkaXQsIHJ1biwgYW5kIHNoYXJlIHRoaXMgY29kZS4gXG4gKiBwbGF5LmtvdGxpbmxhbmcub3JnIFxuICovXG5cbmZ1biBtYWluKCkge1xuICAgIHByaW50bG4oXCJIZWxsbywgd29ybGQhISFcIilcbn0ifQ==).

Before starting the exercises, read through the following [article](https://kotlinlang.org/docs/reference/coding-conventions.html) to familiarise yourself with the coding conventions of Kotlin.

Be sure to follow these conventions when completing these exercises.

## Note 
The online compiler will display code in the console with the println(String parameter) method. use this method to display your answers in the online terminal.

## Exercise: Greetings

In Kotlin there are 3 basic ways of concatenating Strings. Write a function greetings() that accepts a String argument and prints a greeting message to the console.

You must use the plus() method, the "+" operator and String templates to display the text in the following manner:

eg: `greetings("Tshepo")` should output 

-- Greetings Tshepo --

3 times.

## Exercise: DivisibleByFive
 
Write a function `divisibleByFive()` that accepts an Integer as an argument and returns a boolean value describing whether or not the number add is in fact divisible by 5.
The function should print to the console what the remainder value is when the argument is divided by 5.

Make sure to print to the console the boolean value received from the function.

eg. divisibleByFive(6) should return the following:

-- 1 --
-- false --

## Exercise: Draw a square

Write a function called `drawSquare()` that takes in an Integer as a argument and outputs a square drawn in the console that has a side length that equals the integer input.

eg. drawSquare(2) should output the following:

```
##
##
```

eg `drawSquare(4)` should output

```
####
####
####
####
```

## Exercise: Find the longest string in an array.

Create a function call `findLongest()` that accepts a String array as an input and outputs the longest String in the array.

eg. `findLongest(arrayOf("lion", "dog", "cat", "whale"))` should output the following:

```
whale
```

If there are multiple words of the same length, all the words should be printed to the console.

eg. `findLongest(arrayOf("lion", "dog", "cat", "whale", "hyena"))` should output the following:

```
whale
hyena
```

## Exercise: Divide each item in the array by 2 and combine list

Create a function called `halfAndCombine()` that accepts an array of Integers and outputs each value divided by 2 and then join the new list to the old list.

eg. `halfAndCombine(arrayOf(2,4,6))` should output

````````````````
[2,4,6,1,2,3]
````````````````

## Exercise: Convert every 2nd item in String array to uppercase and then concatenate each character

Create a function called `convertAndConcatenate()` that converts every 2nd character to uppercase and then joins each character to create 1 String value.

eg. `convertAndConcatenate(arrayOf('l','i','o','n','s'))` should print the following:

``````
lIoNs
``````

## Next Steps

Well done for getting this far! These excercises practiced some really fundamental skills. You should be familiar with some loops, if statements, comparisons, and the syntax of functions. But even though we have hit the end of this project there is a LOT left for you to learn and practice.

Make sure you really understand all the code you wrote here. You can't build a house without a foundation. You need a solid foundational skills so you can be a pro!

So keep practicing. Practice in your free time, practice if you are ahread of schedule with one of your projects, practice if you need a break from another task. Push yourself and be awesome! You can even practice with a pen and paper if you don't have access to a computer at home.

Remember that you are here to become a professional! Professionals take ownership of their own learning and skills, and professionals help the people around them to become successful.

Here are some resources you can use to continue this journey:

- https://adriann.github.io/programming_problems.html : this has lots of cool little excercises. They're mostly pretty small, you could do a few every day if you wanted to. Even one per day would be a winner
- https://www.codewars.com: you should know about this already, it's legit!

Have fun :)



