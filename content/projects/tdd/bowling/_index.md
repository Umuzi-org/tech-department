---
title: ten-pin bowling scoring system
pre: "<b>HARD: </b>"
ready: true
---

## Take Note

This is a Test Driven Development Project. Please follow a test driven methodologies. That means that you write your test code first!

The basic idea of TDD is to write the test code before you write any actual code. So you write a test (which will fail) then you write the code that will make the test pass.

When you submit your code (on Github people!) then your tests MUST BE included in your code base.

In a professional setting, untested code is incomplete code.

In general: Follow recognized best practices around whatever language and test framework you are using. Eg: consistent naming conventions of functions, test files and literally everything else. Literally.

Also this is a team project. Do this in groups of two following a TDD ping-pong approach as described here: {{% contentlink "workshops/intro-to-pair-programming/" %}}

## Instructions

Write a software system for keeping track of bowling scores. You can read about traditional 10 pin bowling scoring [here](https://en.wikipedia.org/wiki/Ten-pin_bowling#Scoring).

Please put your tests in a directory named "tests" unless the testing framework you are using follows some other convention.

## Project Description

### Gameplay

This project is more about data, tests and algorithms than html. It needs a WORKING frontend but don't spend too much time making it beautiful. Here is how it will work:

1. As the game starts the user will be allowed to enter the names of the players eg "Uncle Bob Martin" and "Ada Lovelace"
2. The user then chooses to start the game
3. The user should be able to see the scores of all the players at all times. This includes scores for individual throws and frames, and their total scores
4. The user should be able to see whose turn it is
5. The user should be able to submit the number of pins hit on each throw. One by one. Eg, it's Uncle Bob's turn, so he throws and misses everything. The user submits a 0. The user interface shows that Bob's score is unchanged and it's still his turn. Bob throws again and hits 2 pins, the user submits a 2 and Bob's score is updated and it's still his turn. He throws again and misses. The user enters a 0. We now see that it is Ada's turn. She throws and hits all the pins because she is awesome. The user enters a 10. Ada's score is updated. Now it's Bob's turn again. Get it?

### Notes about frontends

For those of you doing this in JS: Your user interface will be a web page.

For those of you completing this in Python, don't get too fancy. Python is usually considered to be bad t user interfaces so it's really not worth learning a python frontend framework at this point. Just use the terminal. Take a look [here](http://introtopython.org/terminal_apps.html) for some details.

And everyone: Always remember [KISS](https://en.wikipedia.org/wiki/KISS_principle).

### More Outputs

We should be able to see at any point in time:

- the total score of any player
- the "leaderboard" of the current game (who is in first place, second, third etc)
- the points any person accumulated during a single turn (aka frame)
- how many turns are left
- who's turn is it now?
- whose turn is it next?

### Please don't

PLEASE DO NOT IMPLEMENT A FANCY GUI. We don't care to see the bowling pins or the ball, we don't care about physics.

## Resources and things to know

This is not a simple project. To build something awesome you should be aware of a few architectural concepts.

### Separate display logic from data logic

If your data and your gui get all mixed up then things get very hard to test. Here's an approach you might consider:

1. Think what your data should look like. What is the shape of it? Maybe you have a class called Game. And Game contains some Player objects... These things shouldn't know about HTML. For example, if you were writing a bowling server (with no front-end at all) then these data structures should be valid. Of course you would be setting up these structures in a TDD manner. Eg you could test that a Game object initializes correctly, then make that happen
2. Figure out how your data will change. The only input here is the number of pins hit on each throw. This is a simple integer. Note: we still haven't thought about HTML at this point
3. Now for some display code. Here's a pretty good example adapted from one of your predecessors:

```
function drawPlayerDetails(player) {
    document.getElementById("showDetails").innerHTML =
        "<strong>Player Name: </strong>" + player.name +
        "<br><strong>Points: </strong>" + player.totalScore +
        "<br><strong>Position: </strong>" + player.pos +
        "<br><strong>scores: </strong> [" + player.score + "]";
}
```

This function does one thing, and it does that thing well and intuitively.

### Some oop resources

- https://stackoverflow.com/questions/226977/what-is-loose-coupling-please-provide-examples
- https://medium.com/clarityhub/low-coupling-high-cohesion-3610e35ac4a6
- SOLID: https://scotch.io/bar-talk/s-o-l-i-d-the-first-five-principles-of-object-oriented-design
