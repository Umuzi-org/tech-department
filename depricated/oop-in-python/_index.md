---
title: OOP in Python
todo: This should be broken down into a project with three sub-sections
---

Feeling unsure about how to approach the assignment? [Here](https://www.learnpython.org/en/Classes_and_Objects) is a quick online tutorial to get you introduced to classes.

## Assignment 1. Rolling multi-sided dice

### Description of the task

A normal die (the singular of dice) is a cube, and each face shows a number from one to six. Some games employ nonstandard dice that may have fewer (e.g. four) or more (e.g. thirteen) sides. Let’s design a general class MultiSidedDie to model multi-sided dice. We could use such an object in any number of simulation or game programs.
Each MultiSidedDie object will know two things:

1. How many sides it has
2. Its current value

When a new `MultiSidedDie` is created, specify how many sides it will have (e.g `number_of_sides`). The die can be operated on through three provided methods: roll, to set the die to a random value between 1 an `number_of_sides`, exclusively; `set_value`, to set the die to a specific value (i.e cheat); and `get_value` to see what current value is.

### Steps

1. Copy the following code into a script called `multi_sided_die.py`:

{{% code_snippet "multi_sided_die.py" %}}

2. Create class `MultiSidedDie` with attributes number of sides and value.
3. Create class methods for rolling the die, getting the value of the die and setting the value of the die.

## Assignment 2. Dice roller widget

Build an application that displays and rolls a pair of six-sided dice. Display the buttons graphically and provide two buttons, one for rolling and one for quitting the program.
Break the application down into the following programs:

### Building the Button

The buttons you will be using are not the modern ones that have a 3D look and feel. So the best that can be done, is to find out where the mouse clicked after the click has already been done. The buttons will be rectangular regions in a graphic window where user clicks can influence the behaviour of the running application. Create a class called `Button` in the script `button.py`, containing the following:

1. constructor - This initialises all the instance variables. Create a button in a window. Specify the window in which the button will be displayed, the location/size of the button, and the label that will be on the button.
2. `activate` - Set the state of the button to active.
3. `deactivate` - Set the state of the button to inactive.
4. `clicked` - Indicate when the button is clicked. If the button is active, this method will determine if the point clicked is inside the button region. The point's x and y coordinates will have to be sent as a parameter to the method.
5. `get_label` - Return the label string of the button. This is provided so that we can identify a particular button.

### Building Dice

The purpose of this class is to display the value of a die in a graphical fashion. The face of the die will be a square (via `Rectangular`) and the pips (i.e. the dots on the die) will be circles. Create a class called `DieView`, in the script `die_view.py` containing the following:

{{% code_snippet "die_view.py" %}}

1. Constructor - Create a die in a window. Specify the window, the center point of the die, and the size of the die as parameters.
2. `set_value` - Change the view to show a given value. The value to display will be passed as a parameter.
   **HINT**: The main thing in DieView is turning various pips “on” and “off” to indicate current value of the die.

### The Main Program

This script, `roller.py`, imports the Button and DieView classes from their respective modules. It creates the application window, draws the interface widgets, defines an event and can close the window. The program should get mouse clicks and process them until the user clicks Quit.

## Assignment 3: Dice Poker

### RULES OF THE GAME

- The player starts with \$100.
- Each round costs \$10 to play. This amount is subtracted from the player’s money at the start of the round.
- The player initially rolls a completely random hand (i.e. all the five dice are rolled).
- The player gets two chances to enhance the hand by re-rolling some or all of the dice.
- At the end of the hand, the player’s money is updated according to the following payout schedule:

| Hand            | Pay |
| --------------- | --- |
| Two Pairs       | 5   |
| Three of a Kind | 8   |
| Full House      | 12  |
| Four of a Kind  | 15  |
| Straight        | 20  |
| Five of a Kind  | 30  |

### Explanation of the scoring

Two pairs is two sets of pairs, for example two threes and two eights in the same hand.
A Full House is a pair and a Three of a Kind in the same hand.
Four of a kind is four of the same card, such as four eights.
A straight is five numbers in order. So this can be 12345 or 23456.
Five of a kind are five of the same number (all sixes for example).

### Instructions

Build a Dice Poker game according to the game rules above. Ultimately, we want this program to present a nice graphical interface. Our interaction will be through mouse clicks. The interface should have the following characteristics:

- The current score (amount of money) is constantly displayed.
- The program automatically terminates if the player goes broke.
- The display may choose to quit at appropriate points during play.
- The interface will present visual cues to indicate what is going on at any given moment and what the valid user responses are.

This class has to implement these operations:

1. Constructor (`__init__`) - Create the initial collection.
2. `roll` - Assign a random value to some subset of the dice while maintaining the current value of others.
3. `value` - return the current values of the five dice.
4. `score` - return the score for the dice.
