---
title: Coding Horrors
ready: true
---


# Common TDD pitfalls.

This is a list of most common TDD pitfalls to be aware of.

## Readings
  - [Common mistkes in TDD](https://cmatskas.com/common-mistakes-in-tdd/)

## Some more TDD pitfalls
  - Avoid making tests depend on each other, either explicitly or implicitly. Dependencies among tests are a path to pain, expense, fragility, and complication. I  -have never seen an exception to this. Ever.
  - Make each test express its intent very clearly.
  - Pay attention to failure messages. Make each failure message as helpful for diagnosis as you can.
  -  Involve as little of the system as you possibly can in each test. The more parts of the system you involve in a test, the more ways it can fail, even if the functionality that the test really cares about is working.
  - Do not skimp on the refactoring. It is the refactoring that will keep your code (including the tests) easy to understand and change
  - As you write code to pass the tests, consider cheating as hard as you can. Do the stupidest (or easiest) thing you can do that will pass the tests. Later, in order to make the code less stupid, you first demonstrate its stupidity by writing a test that the stupid code can't pass.
