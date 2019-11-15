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