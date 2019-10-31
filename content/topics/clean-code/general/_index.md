---
title: General Clean Code Guidelines
ready: True
---

"It's easy to write code that computers understand, but hard to write code that other people understand ".

## Obvious Function and Variable Names

When you declare a variable, give it a name that describes what values or data it holds.
When you declare a function, give it a name that describes what it does.

Example of a bad function name: run_process()
Example of a good function name: sort_files()
Bad variable name: divs
Good variable name: cards

These names should be obvious. Try to look at your code from the perspective of someone who has never seen it. They should be able to tell what it does just by reading it.
Name things according to exactly what they do and what they are. If you are struggling to name a function, it may be because your function does too many different things to give it a simple descriptive name. Which brings us to the next point...

## Functions Should do One Things
The moment you find yourself struggling to describe what your function does in a simple sentence, you should know that it is too long. This is when you need to take the pieces of logic that do specific things in your and move them into another function

Bad_Function()
    some saving files logic
    some sorting files logic
    rename files logic

Good_Function()
    take_files()
    sort_files()
    rename_files()