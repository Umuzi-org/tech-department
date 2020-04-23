---
title: Advanced algorithm
pre: "<b>3. </b>"
weight: 3
ready: true
---

Adjust your `JamBuddy` class so that it can handle flats and sharps.

Here is an example usage:

JS:

```
let buddy = new JamBuddy()
let notes = buddy.selectNotes()
console.log(notes) # let's pretend that this outputs ['A#', 'Db']

let correct = buddy.checkAnswer(1)
console.log(correct) # false

correct = buddy.checkAnswer(3)
console.log(correct) # true
```

Have fun :)

## Acceptance criteria

The usual. TDD is a must
