---
title: ten-pin bowling scoring system
weight: 1
pre: "<b>1. </b>"
---

## Take Note

This is a Test Driven Development Project. Please follow a test driven methodologies. That means that you write your test code first!

The basic idea of TDD is to write the test code before you write any actual code. So you write a test (which will fail) then you write the code that will make the test pass.

When you submit your code (on Github people!) then your tests MUST BE included in your code base.

In a professional setting, untested code is incomplete code.

In general: Follow recognised best practices around whatever language and test framework you are using. Eg: consistent naming conventions of functions, test files and literally everything else. Literally.

## Instructions

Write a software system for keeping track of bowling scores. You can read about traditional 10 pin bowling scoring [here](https://en.wikipedia.org/wiki/Ten-pin_bowling#Scoring).

Please put your tests in a directory named "tests" (unless the testing framework you are using follows some other convention(which is unlikely)).

### Initial inputs:

The names of the players eg "Uncle Bob Martin" and "Ada Lovelace"

### Gameplay

Once the game has started, the players take turns until the game is concluded. Each player gets to throw the bowling ball up to three times during their turn. Each time they throw they can knock down up to a maximum of 10 pins.

PLEASE DO NOT IMPLEMENT A FANCY GUI. we dont care to see the bowling pins or the ball, we dont care about physics.

The only input that will matter here is the number of pins knocked over.

### Outputs

We should be able to access at any point in time:

- the total score of any player
- the "leaderboard" of the current game (who is in first place, second, third etc)
- the points any person accumulated during a single turn (aka frame)
- how many turns are left
- who's turn is it now?
- whose turn is it next?
