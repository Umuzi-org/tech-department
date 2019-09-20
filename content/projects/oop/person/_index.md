---
title: Person
ready: true
---

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
let person = new Person('Ryan',30,'male',['being a hardarse','agile', 'ssd hard drives'] )
let greeting = person.hello()
console.log(greeting)
```

This should output:

```
Hello, my name is Ryan and I am 30 years old. My interests are being a hardarse, agile and ssd hard drives.
```

In OOP this is known as abstraction. We created a simple model of a more complex thing. We only represent the attributes and functionality that we need.

When an object instance is created from a class, the class's constructor function is run to create it. This process of creating an object instance from a class is called instantiation — the object instance is instantiated from the class. `person` is an instance of `Person`