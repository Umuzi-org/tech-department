---
title: Coding Horrors
ready: true
---

# Common TDD pitfalls.

- Write tests. Recruits in the past have done the mistake of not writing tests for TDD assignments, make sure you avoid this weird mistake. always write tests for your TDD projects.

This is a list of most common TDD pitfalls to be aware of:

  - Avoid making tests depend on each other, either explicitly or implicitly. Dependencies among tests are a path to pain, expense, fragility, and complication.
  - Make each test express its intent very clearly.
  - Pay attention to failure messages. Make each failure message as helpful for diagnosis as you can.
  - Involve as little of the system as you possibly can in each test. The more parts of the system you involve in a test, the more ways it can fail, even if the functionality that the test really cares about is working.
  - Do not skimp on the refactoring. It is the refactoring that will keep your code (including the tests) easy to understand and change
  - As you write code to pass the tests, consider cheating as hard as you can. Do the stupidest (or easiest) thing you can do that will pass the tests. Later, in order to make the code less stupid, you first demonstrate its stupidity by writing a test that the stupid code can't pass.
  - Naming conventions: in general, be careful with your naming conventions. make sure your naming convention consistent, names should be more descriptive.
  - Keep good directory structure and delete all junk files.
  - Avoid messy indentation (install prettier).
  - Write your tests before you write your code (Red, Green, refactor).
  - Please make sure you understand .gitignore, please don't add your node_modules to git
  - name your files according to what is inside them. E.g. if you have a file called add.js that only contains a multiply function then something is wrong.
  - Good code makes it's intentions clear. Good code is never misleading or surprising.
  - make sure you've tested every possible outcome(including exceptions) of the program, this ensures your program doesn't break because of the user's input, that is purpose of testing after all.
  - You can't define test case inside a test case.
  e.g:
    ```py
    def testOne():
      def testSomething():
        assert add("1,23,5") == 29

    ```
    instead you should put your tests into classes as methods, like so:
    ```py
    class TestOne():
      def testSomething():
        assert add("1,23,5") == 29

    ```

    _note_: The above example is written in Python, because of it's super readability.

### Some useful Readings
  1. [Common mistakes in TDD](https://cmatskas.com/common-mistakes-in-tdd/)
