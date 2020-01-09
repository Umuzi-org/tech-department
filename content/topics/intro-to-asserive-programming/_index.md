---
title: Introduction to assertive programming
ready: True
---

You've all heard of "defensive driving", right? When driving a car you do certain things if you want to stay alive. You maintain a safe following distance, you check your mirrors and blind spot, you watch your speed. And why do you do that?

Because mistakes happen. Sometimes the road is bad, sometimes there's a cow in the road, sometimes the other drivers on the road are inatentive. Sometimes you are inattentive.

Ok. Now let's talk about code. Code is written by humans for humans. Humans are prone to human error. Humans make mistakes all the time, there will be typos, off-by-one errors, assumptions and all sorts of weird nonesense.

Assertive programming is one way to do defensive programming. It has loads of benefits.

First consider the following code:

```
assert refund_amount > 0, f"refund amound needs to be positive, this is invalid {refund_amount}"
```

This is written in Python, but other languages have their own way of doing the same kind of stuff. Basically what this does is raise/throw an Exception/Error when a certain condition is not met. The error message is nice and descriptive.

This is good for a few different things:

- sanity checking around human error and input validation
- these assertions are useful as documentation

Also, in general, the earlier you find a problem the cheaper it it to fix. This is a fact of life. Seriously.

In terms of coding, let's talk a bit more about the `refund_amount` assertion. Imagine a piece of software that is all about shopping. Occasionaly users require refunds. What might happen if somehow a negative refund amount slips into the system? It might show up as something weird on a frontend and make the end users distrust the system, then the backend devs will blame the frontend devs, maybe the accounting system will be negatively effected (of course the frontend devs will be blamed for this too, at least for a little while), the refund wont be paid to the user on time, and lotd of other aweful nasty stuff.

That one little line of code prefents all sorts of crazy stuff from happening in the code.

Assertions save lives!

## Resources

This excellent article talks about the benefits of failing fast and loudly:
https://www.martinfowler.com/ieeeSoftware/failFast.pdf

This discussion on Stackoverflow is about where assertions are inappropriate. It makes use of heavy wordds like `public methods` and stuff like that. Basically a shortcut to doing this right is thinking about who is going to see your error message and how the error message will be useful to them.
https://stackoverflow.com/questions/13832487/why-should-assertions-not-be-used-for-argument-checking-in-public-methods

## Java Resources

- https://www.geeksforgeeks.org/assertions-in-java/
