---
title: simple-calculator part 1
pre: "<b>EASY: </b>"
ready: true
---

The objective of this project is to build a calulator that can perform mulitiplication and addition equations on multiple integers. Do not build a Front-end(UI). Complete this project by using a TDD approach. 

The basic TDD approach is as follows:

1. RED: Write tests. It should fail initially because there isn't any code that it is testing.
2. GREEN: Write code to make the tests pass
3. REFACTOR: Make sure code is understandable and clean.

Remember to make sure your tests still pass after refactoring it.

## Set up environment

### JavaScript:

Use Jasmine to test your code. *Please do not use the SpecRunner* to test your code. Run Jasmine on the terminal.
- [Running Jasmine on the Terminal](../../../topics/jasmine-unit-tests/_index.md). Look under the heading: *Getting set up (like a boss)* for instructions to set up.

## 1. Create an add function that can add two integers

Implement the following function:
```
add()
```

The `add` function should behave like this:

```
add(1,2)
// should return 3
add(-1,-1)
// should return -2
```

## 2. Modify the add function so that it can add multiple integers.

The `add` function should now behave like this:

```
add(1,2,3,4,5)
// should return 15
```

## 3. Create a multiply function that can multiply two integers

Implement the following function:
```
mutiply()
```

The `multiply` function should behave like this:

```
multiply(1,3)
// should return 3
```


## 4. Modify the multiply function so that it can multiply multiple integers.

The `multiply` function should now behave like this:

```
mutilply(1,2,3,4,5)
// should return 120
```