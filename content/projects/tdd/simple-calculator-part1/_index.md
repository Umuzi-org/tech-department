# SIMPLE-CALCULATOR PART 1
---
To submit this project follow the link:
[PROJECT SUBMISSION FORM](https://forms.gle/BuwjpJ6briu1ppwG9). 
If you follow a different link or do your own thing you will have to resubmit.
---
We’ll build a calculator to do some basic arithmetic. Please follow the instructions below.
Please strictly follow all naming conventions and use Jasmine testing framework to run the test for the project and follow it's conventions when writing tests.

Also, please don’t build a frontend.

We’ll follow a TDD approach. The basic approach is

    1.RED: we will write ONE failing test
    2.GREEN: we will make sure our test (and all tests written so far) pass
    3.REFACTOR: if our code is untidy we will clean it up
    4.repeat all the steps until all the functionality we need has been built and tested

## How to setup for testing:
### 1. Jasmine for NodeJS
- Install jasmine globally (npm install -g jasmine) or install jasmine as a dev dependency (npm install --save-dev jasmine).
- Initialise Jasmine in the root of your project folder (jasmine init).
- Initialise a package.json file (npm init).
- Set Jasmine as your testing framework in your package.json ("scripts": { "test": "jasmine" }).
- run your tests (npm test).

### 2. [Jasmine Standalone](https://github.com/jasmine/jasmine/releases)
- Initialise a package.json file (npm init).
- Set Jasmine as your testing framework in your package.json ("scripts": { "test": "jasmine" }).

## 1. Make a function that adds two numbers

First write a test function. it can be called test_function or something similar. It needs to make sure that the add function works. (of course we haven’t written add yet. We’ll write our tests first).

- write a test to demonstrate that add(0,0) will return 0. Run the test. It should fail. Now make the test pass by creating an add function.
- write a test to demonstrate that add(-1,-1) should return -2 then edit add to make your test pass.
- write a test to demonstrate that add(4,5) should return 9 then edit add to make the test pass.

## 2. Make sure you can add as many numbers as you want

Now write a test to make sure you can add a bunch of numbers. Eg add(1,2,3,4) should return 10. Think of the tests yourself.

## 3. Create a multiply function that can multiply 2 numbers

multiply(1,2) and other similar combinations should work. Run with it.

## 4. Make sure multiply can handle multiple numbers

multiply(1,2,3,4) should work.
