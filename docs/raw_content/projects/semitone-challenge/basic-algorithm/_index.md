---
title: semitone difference - basic algorithm
pre: "<b>1. </b>"
weight: 1
ready: True
---

Make a class called JamBuddy. JamBuddy should work like this:

JS:

```
let buddy = new JamBuddy()
let notes = buddy.selectNotes()
console.log(notes) # this will print an array of two notes
correct = buddy.checkAnswer(1)
console.log(correct) # this will print True if the `1` was the correct answer
```

Python:

```
buddy = JamBuddy()
notes = buddy.select_notes()
print(notes) # this will print an array of two notes
correct = buddy.check_answer(1)
print(correct) # this will print True if the `1` was the correct answer
```

## Some finer points

For now don't worry about "flat" notes. The notes we care about are:

```
A A# B C C# D D# E F F# G G#
```

Here is an example usage:

JS:

```
let buddy = new JamBuddy()
let notes = buddy.selectNotes()
console.log(notes) # let's pretend that this outputs ['A', 'B']

let correct = buddy.checkAnswer(1)
console.log(correct) # false

correct = buddy.checkAnswer(2)
console.log(correct) # true
```

## Acceptance criteria

Make sure you do this in a TDD way. And that code sample from the top needs to run as is.

Please just supply a working class. The only place you should instantiate your class is inside your unit tests
