---
title: Person
ready: true
---

## Project structure

### Java

The code you push to git should have the following structure:

```
├── build.gradle
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew
├── gradlew.bat
├── settings.gradle
└── src
    ├── main
        └── java
            ├── Person.java       <-------- names are important
            └── MainProgram.java  <-------- names are important

```

Please refer to the following to find out more: {{% contentlink "topics/java-specific/project-submission-requirements" %}}

## Instructions

Please follow TDD when implementing this code if you have covered TDD in your course.

Create a `class` called `Person` which defines the generic data and functionality of a human.

A class is a collection of attributes and functions. Different languages use different terminology for these things, but the bacic concepts are the same.

Give your `Person` class should have the following attributes:

- name
- age
- gender
- interests. This is a list or array of strings

Give your `Person` class a `hello` function:

Example usage:

```
// JavaScript:

let person = new Person('Ryan',30,'male',['being a hardarse','agile', 'ssd hard drives'] )
let greeting = person.hello()
console.log(greeting)
```

```
# Python

person = Person('Ryan',30,'male',['being a hardarse','agile', 'ssd hard drives'] )
greeting = person.hello()
print(greeting)
```

```
// Java

Person person = new Person(
    "Ryan",30,"male",
    new String[] {"being a hardarse", "agile", "ssd hard drives"})
String greeting = person.hello()
System.out.println(greeting)
```

This should output:

```
Hello, my name is Ryan and I am 30 years old. My interests are being a hardarse, agile and ssd hard drives.
```

In OOP this is known as abstraction. We created a simple model of a more complex thing. We only represent the attributes and functionality that we need.

When an object instance is created from a class, the class's constructor function is run to create it. This process of creating an object instance from a class is called instantiation — the object instance is instantiated from the class. `person` is an instance of `Person`
