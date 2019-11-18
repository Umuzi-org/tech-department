---
title: General Clean Code Guidelines
ready: True
---

“Any fool can write code that a computer can understand. Good programmers write code that humans can understand.” ― Martin Fowler

## Obvious Function and Variable Names

When you declare a variable, give it a name that describes what values or data it holds.
When you declare a function, give it a name that describes what it does.

Example of a bad function name:
```
run_process()
```
Example of a good function name:
```
sort_files()
```
Bad variable name:
```
divs
```
Good variable name:
```
cards
```

These names should be obvious and specific. Try to look at your code from the perspective of someone who has never seen it. They should be able to tell what it does just by reading it. Consider the next developer who will work on the code as your client. Name things according to exactly what they are and what they do. If you are struggling to name a function, it may be because your function does too many different things to give it a one simple descriptive name. Which brings us to the next point...

## Functions Should do One Thing
The moment you find yourself struggling to describe what your function does in a simple sentence, your function may be too long or too busy. Describing your function should be easy. This is when you need to take the pieces of logic that do specific things in your and move them into another function. Try to keep your functions under 25 lines long.

Let's say you wrote a function that sorts files. Below is some pseudocode illustrating what a bad vs good functions structure would look like.
```md
Bad File Sorting Function()
    some code that opens the folder
    some code that looks through the files
    attempts at finding the file
    some code that filters
    the results
    some code that sorts results
    some code that prints the result after the sorting
    some logic that closes
    the folder
```
```md
Sort Files(folder)
    open the folder
    sort files in the folder
    return the sorted files

Print Files(sorted folder)
    open the sorted folder
    print the files in the folder

Good File Sorting Function()
    Sort Files(folder)
    Print Files(sorted folder)
```

As you can see, there is a lot going on in the Bad file sorting function, so it would be difficult to describe what it does in one sentence or to give it a name.

## DRY - Don't Repeat Yourself
Ideally functionality should be represented in a code-base exactly once. If you find yourself repeating certain values such as strings or numbers that won't change, rather same those values to variables. This also means you won't have to change everywhere you're using those values, you'll only need to change them where you originally assigned them to a variable.

## Flat is Better Than Nested
If you are ever tempted to put a loop inside a loop... etc. Don't.

Functions are:\
* More explicit and specific about what they actually do than a loop inside a loop.\
* Easier to test than the inner-most loop of a 5 loop stack of spaghetti-code.\
* Easier to reuse.\
* Easier to document.\

## Code Defensively
Defensive programming means anticipating things that could probably go wrong and coding to handle such situations instead of just throwing error or exception mesages. The goal is to write code that can handle real life situations: e.g. invalid input from the user.

If you don't code defensively your code might for example fail to complete its work but acts as if there is no problem leading to issues that are difficult to find and fix after you've launched your app. These bad scenarios are also called "edge cases". So think about the edge cases, assume that your user is really, really dumb and isn't following the instructions or using your program as they should. Then write your code to anticipate handle such abuse or misuse.
