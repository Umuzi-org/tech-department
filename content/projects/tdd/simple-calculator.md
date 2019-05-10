---
title: simple-calculator
pre: "<b>EASY: </b>"
---

We'll build a calculator to do some basic arithmetic. Please follow the instructions below. Please take all the naming conventions in this doument with a gran of salt. There are lots and lots of test frameworks in existance, each with its own conventions. Please follow whatever conventions are set out by the test tool that you are using.

Also, please dont build a frontend.

We'll follow a TDD approach. The basic approach is

1. RED: we will write ONE failing test
2. GREEN: we will make sure our test (and all tests written so far) pass
3. REFACTOR: if our code is untidy we will clean it up
4. repeat all the steps until all the functionality we need has been built and tested

## 1. Make a function that adds two numbers

First write a test function. it can be called `test_function` or something similar. It needs to make sure that the `add` function works. (of course we haven't written `add` yet. We'll write our tests first).

- write a test to demonstrate that `add(0,0)` will return 0. Run the test. It should fail. Now make the test pass by creating an `add` function.
- write a test to demonstrate that `add(-1,-1)` should return -2 then edit `add` to make your test pass
- write a test to demonstrate that`add(4,5)` should return 9 then edit `add` to make the test pass

## 2. Make sure you can add as many numbers as you want

Now write a test to make sure you can add a bunch of numbers. Eg `add(1,2,3,4)` should return 10. Think of the tests yourself

## 3. Create a multiply function that can multiply 2 numbers

`multiply(1,2)` and other similar combinations should work. Run with it

## 4. Make sure multiply can handle multiple numbers

`multiply(1,2,3,4)` should work
