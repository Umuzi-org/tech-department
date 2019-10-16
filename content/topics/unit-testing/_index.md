---
title: Unit testing (language agnostic concepts)
ready: true
---

The following videos use JavaScript to demonstrate and explain some key concepts around unit testing. Even if JS is not your vibe these are worth watching.

- Lesson 1: [Why Unit Testing](https://www.youtube.com/watch?v=Eu35xM76kKY&
  list=PL0zVEGEvSaeF_zoW9o66wa_UCNE3a7BEr&index=1)
- Lesson 2: [Your first tests](https://www.youtube.com/watch?v=XsFQEUP1MxI&index=2&list=PL0zVEGEvSaeF_zoW9o66wa_UCNE3a7BEr)
- Lesson 3: [Test Runners](https://www.youtube.com/watch?v=pdx2HjFRaJY&list=PL0zVEGEvSaeF_zoW9o66wa_UCNE3a7BEr&index=3). This discussion on test runners mentions a bunch of JS stuff. But there are still many language agnostic concepts that are worth knowing about. Examples of Python test runners are unittest and pytest.

If you are actually doing JS then it's worth watching the rest of this series of videos.

This is a list of most common TDD pitfalls to be aware of:

  - Avoid writing tests after writing your code.
  - Avoid making tests depend on each other, either explicitly or implicitly. Dependencies among tests are a path to pain, expense, fragility, and complication.
  - Make each test express its intent very clearly.
  - Pay attention to failure messages. Make each failure message as helpful for diagnosis as you can.
  - Involve as little of the system as you possibly can in each test. The more parts of the system you involve in a test, the more ways it can fail, even if the functionality that the test really cares about is working.
  - Do not skimp on the refactoring. It is the refactoring that will keep your code (including the tests) easy to understand and change
  - As you write code to pass the tests, consider cheating as hard as you can. Do the stupidest (or easiest) thing you can do that will pass the tests. Later, in order to make the code less stupid, you first demonstrate its stupidity by writing a test that the stupid code can't pass.
  - Naming conventions: in general, be careful with your naming conventions. make sure your naming convention consistent, names should be more descriptive.
  - Keep good directory structure and delete all junk files.
  - Avoid messy indentation (install prettier).
