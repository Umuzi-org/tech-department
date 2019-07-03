---
title: Unit Testing
ready: True
---

## Readings:

- [pytest](https://docs.pytest.org/en/latest/)
- [Writing Tests](https://docs.python-guide.org/writing/tests/)
- [Improve your python understanding: Unit testing](https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/)

## Video:

Pytest is the nicest python testing framework currently out there, but there aren't so many
videos on it, so here are some videos on unit testing in javascript (but they provide a great explanation of
why and how you need to test your code) and unit testing with python's unittest.

- [Fun Fun Function: Unit testing in Javascript](https://youtu.be/Eu35xM76kKY)
- [unittest](https://www.youtube.com/watch?v=6tNS--WetLI)

## Data Assignment:

Write a script called `factorial.py` that takes a number and returns its factorial.
Use pytest in a separate file called test_factorial.py to test your function.

## Steps:

- Think about which tests you want to do to test that the factorial function works.
- Write the tests **first** (before creating the function).
- Test an empty function called factorial - it should fail the tests
- Add code for returning the factorial of a number - it should pass for numbers >= 1
- Add code for dealing with zero - should pass unit test for zero and for numbers >= 1
- Add code for dealing with negative numbers
- Add code for dealing with non-numeric input

Once you are done, upload your tests and function to Github.

## References:

[Factorial Numbers](https://whatis.techtarget.com/definition/factorial)
