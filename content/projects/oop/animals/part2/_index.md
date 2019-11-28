---
title: Animals Part 2. Adding Tests
ready: true
---

In this challenge you will update your current Animals project and add unit tests to the project

## Java Instructions

You'll be using JUnit.

1. Create a class called `AnimalTests`
2. Update `Animal` super class `eats()` function to return a String, "Food".
3. Update `Dog` class `sounds()` function to return a `String`, "Bark".
4. Update `Cat` class `sounds()` function to return a `String`, "Meow".

```
// Java

Dog dog = new Dog()

dog.eats()    // -> 'Food'
dog.sounds() // -> 'Barks'

Cat cat = new Cat()

cat.eat()    // -> 'Food'
cat.sounds() // -> 'Meow'
```

Now let's add our first JUnit test to our `AnimalTests`. The class should have the following methods `TestDogSound()`, `TestDogEats()`, `TestCatSound()` and `TestCatEats()`.Each method should have the @Test tag placed above it. The tests should work as follows.

```
// Java

//Dog Tests
Test -> Does dog eat Food should Pass
Test -> Does dog eat food should Fail

//Cat Tests
Cat cat = new Cat();
Test -> Does cat Barkark should Fail
Test -> Does cat Meow should Pass
Test -> Does cat eat meat should Fail
Test -> Does cat eat Food should Pass
Test -> Does cat eat food should Fail

```

### Up for a Challenge?

This section is not compulsory. If you do this we'll think you're cool.

Add some functionality to `TestDog()` and `TestCat()` so that the tests aren't case sensitive

eg:

```
Test -> Does dog eat Food -> Pass
Test -> Does dog eat food -> Pass
```
