---
title: Introduction to pair programming
---

## What is it?

Pair programming is when you get two (or three) programmers to work on the same piece of code on the same computer. Only one person is coding at a time and the rest of the people are being helpful in some way.

## But why?

Think about what can happen if you have multiple brains working on th same problem. There are lots of benefits.

- the coders can all leverage their own problem-solving strengths to solve the same problem, so the problem will get solved well
- the coders will learn from each other! You get to grow and help your peers grow. How cool is that?
- the coders catch each others mistakes and assumptions before they get into the code base

## How to do it

Pair programming works best if everyone gets a turn at the keyboard, team member roles get mixed around, and communication is prioritized. There are a few different approaches to getting this right:

### Ping Pong

This kind of pair programming works best when there is a natural cadence to the coding process. Eg: Alice writes a little function, then Bob writes a little functio, etc.

This works suuuper well when it comes to Test Driven Development (we cover TDD later in the course)

### Driver-navigator

Basically in this form, one person is the driver (they drive the computer), and the other person gets to direct their efforts. The driver is writing all the code so they get to ask questions and suggest corrections if they think something is a bad idea.

### Unstructured

In the absence of a plan, this tends to happen. It sounds like a terrible idea at first (if you fail to plan, you plan to fail) but it can work pretty well in some situations.

- if the coding pair is evenly matched
- if the coding pair already know how to work together
- if the pair have compatible styles of communication and code

So while you are still learning, rather stick to one of the other styles.

## How to do it well

- take turns. Set a timer if you have to
- try to communicate constantly and clearly. Communication can be hard, value it
- always be learning. Everyone has something to teach you. If you feel frustrated by your partner's coding abilities then use this opportunity to learn how to explain yourself better (this skill will serve you well). Teamwork is really really important in life so learn how to team.

## Extra reading

https://medium.freecodecamp.org/want-to-be-a-developer-you-should-probably-be-pair-programming-2c6ec12c4866

## Practice Time!

Here are a few basic problems for ya. Try the Driver-Navigator pattern out. For now, don't worry about making any user interfaces. We are more interested in algorithmic thinking.

1. Write a function that takes one integer as a parameter and then prints that many plusses (+). Here's how you would call it:

- `print_plusses(1)` this should output "+"
- `print_plusses(3)` this should output "+++"
- `print_plusses(5)` this should output "+++++"

2. allow your program to take a second argument for the number of rows of plusses you want to draw. Think of the output as a grid. Your function takes in two parameters, the first is the number of columns and the second is the number of rows.

- `print_plusses(1,1)` this should output:

```
+
```

- `print_plusses(3,2)` this should output:

```
+++
+++
```

- `print_plusses(2,3)` this should output:

```
++
++
++
```

https://docs.google.com/document/d/1IMCAba36CxJje0xPQjAy9_p9OtCuvUPqiw7Vl3noloo/edit ??
