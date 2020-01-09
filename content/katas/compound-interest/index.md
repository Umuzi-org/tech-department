---
title: Compound interest
pre: "<b>1. </b>"
weight: 5
---

## compound Interest

**1.**
Write a function that calculates compount interest. It should return a number.

Eg if I have R100 in a bank account and I get 1% interest every month, I can see how much money I will have in my account at the end of each month like so:

Try it with a loop. Try it with recursion.

```
// JavaScript

function finalAmount(startAmount,interest,iterations){
    // clever things
}

finalAmount(100,0.01,1)    // 101.0
finalAmount(100,0.01,2)    // 102.01
finalAmount(100,0.01,3)    // 103.031
finalAmount(100,0.01,100)  // 270.481...

```

```
//py

compountInterest(principleAmount,interest,iterations):
    # clever things

Expected output:
def compountIntere(100,10,1): # 101.0
def compountIntere(100,10,2): # 102.01
def compountIntere(100,10,3): # 103.031
def compountIntere(100,10,100): =>  # 270.481...
```

### ADVANCED COMPOUND INTEREST

**2.** Write a program that will figure out how many iterations are needed to meet a specific target amount. Eg: if I have R100 in a bank account and I get 1% interest every month, how many months do I have to wait before my bank acount contains R200?

There are a lot of ways to do this. Some are very inefficient (and easy to code). Some are more efficient (and hard to code). Try the easy way first. MAke it work then make it work well.