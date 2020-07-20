---
title: Make a simple GUI
pre: "<b>1. </b>"
weight: 2
ready: True
prerequisites:
  hard: ["projects/semitone-challenge/basic-algorithm"]
  soft: []
available_options: ["javascript", "any_frontend_framework"]
submission_type: continue_repo
from_repo: "projects/semitone-challenge/basic-algorithm"
---

Create a basic web site that a user can use to interact with the JamBuddy class.

If you are required to do this ni a web framework then do so, otherwise create a simple `index.html` page that a user can just open in their browser.

- Make a button with the text "Get random notes". If the user clicks on this button then the selectNotes function should be called and the notes should be displayed on the screen.
- make an input box where the user can enter their answer.
- create a button with the text "Submit answer". If the user clicks this button then the checkAnswer function should be called.
  - if the answer is correct then display the message "You got it right .Well Done!"
  - if the answer is incorrect then display the message "Wrong answer! Try again"

## Acceptance criteria

TDD is a must. Yes, you need to even unit test your DOM manipulations
