---
title: simple-calculator part 2
pre: "<b>MEDIUM: </b>"
---

This a continuation of the `simple-calculator` tdd excercise. If you haven't done that yet then please do. At this point you should have a well tested `add` and `multiply` function.

This excercise will require a little OOP knowledge. Brace yourself.

## introducing the Calculator class

Update your tests so that they expect the `add` and `multiply` functions to be part of a class. Now make those tests pass.

For now on this document will just describe the features we need the Calculator to have. You need to figure out the tests and implementation yourself.

## Remember the last result

The calulater should have a function called `last` that returns the last result. Example usage:

```
calculator_instance.add(1,2)
calculator_instance.last() # should return 3
```

## Use the last result in other calculations

The `add` and `multiply` functions should allow `"LAST"` as a parameter.

Example usage:

```
calculator_instance.add(1,2)
calculator_instance.multiply("LAST",5) # should return 15
```

## Memory Slots

Allow the calculator to remember more stuff by implementing a `set_slot` function. The `set_slot` function should take a single number as an argument. That argument is called the slot number. Also implement `get_slot` for getting the value from a memory slot. Neither get_slot or `set_slot` should effect the output of `last`.

Example usage:

```
calculator_instance.add(1,2)
calculator_instance.set_slot(1)
calculator_instance.get_slot(1) # shouild return 3
calculator_instance.add(10,20)

calculator_instance.set_slot(2)
calculator_instance.get_slot(2) # shouild return 30

calculator_instance.add(100,200)
calculator_instance.get_slot(1) # shouild return 3
calculator_instance.get_slot(2) # shouild return 30
calculator_instance.last(2) # shouild return 300
```

## Allow the use of memory slots as arguments

The `add` and `multiply` functions should allow memory slots as parameters. If we were using memory slot 5 as an argument then we would represent it like this `"SLOT_5"`.

Example usage:
Following from the previous example:

```
calculator_instance.get_slot(1) # shouild return 3
calculator_instance.get_slot(2) # shouild return 30
calculator_instance.last(2) # shouild return 300

calculator_instance.add("SLOT_1",5) # should return 8
calculator_instance.multiply("SLOT_2",2) # should return 60
```
