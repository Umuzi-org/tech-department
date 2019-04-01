---
title: ten-pin bowling scoring system
weight: 1
pre: "<b>1. </b>"
---

## Instructions

Write a software system for keeping track of bowling scores. You can read about traditional 10 pin bowling scoring [here](https://en.wikipedia.org/wiki/Ten-pin_bowling#Scoring).

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
