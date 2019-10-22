---
title: code review process
---

## General Process

1. Recruits get given some project instructions. Like this: {{% contentlink "projects/tdd/simple-calculator-part1" %}}
2. You'll notice there is a link at the top of the project instructions. Peeps follow that link to submit their work
3. The code submissions show up in a [https://docs.google.com/spreadsheets/d/1jIWBgfh4PbZU0KpBQi_hTjSFK74CRkTQtoEcvJ1V0uA/edit#gid=2104739812&fvid=1123262740](Google sheet). This is stored on the Tech Dept Drive, send a message on the tech-team channel if you don't have access
4. You'll notice if you scroll to the left there is a column entitled "INITIAL REVIEWER", if you are intending to review someone's code then you need to put your name in this column
5. To review the code you need to make sure you understand the project instructions, clone the code, make sure it works, make sure the tests cover everything they should cover, and comment on things like good coding practices. We are currently working on some automations around this stuff but for now that's what needs to happen
6. If you are unsure about what kind of code quality we are looking for, take a look here for some ideal answers: https://github.com/Umuzi-org/automark-project-config Look at the PRs as well, there's a lot of good stuff there. If you need assistance you can ask for help on the tech-team channel and someone will jump in.
7. Now fill this in with comments about the code review: [Code review google form] (https://docs.google.com/forms/d/e/1FAIpQLScuQeCskMC7xTP1mU1CAbK0BOUqyMyLcNzX1ohRyJ_0_q019w/viewform)
8. Communicate with effected parties. Tell the recruit your feedback. If there is a RED FLAG and you need some help dealing with this recruit then let us know on the tech-team channel.

The projects that are worth reviewing first are these (in order).

- {{% contentlink "projects/tdd/simple-calculator-part1" %}}
- {{% contentlink "projects/tdd/password-checker" %}}
- {{% contentlink "projects/tdd/string-calculator" %}}
- {{% contentlink "projects/tdd/simple-calculator-part2" %}}
- {{% contentlink "projects/oop/person" %}}
- {{% contentlink "projects/oop/dice" %}}
- {{% contentlink "projects/oop/bank_accounts" %}}

Also, be a perfectionist. We want our recruits to write beautiful code

## Goals

We have a few goals for code review:

1. We need to keep track of who has submitted code and who hasn't. deadlines should be taken seriously by recruits which means that WE need to take them seriously
2. We need to know what the recruits need. If they need help then we need to help them quickly. If disciplinery action is needed then we should act fast
3. Code review aids in knowledge sharing within our team
4. Code review is a useful skill that should be taught to recruits

## Process and Roles

When deadlines are set up then a few different staff members are assigned different roles. This will be done by populating columns in the (mighty) [Coding and Data program outline spreadsheet](https://docs.google.com/spreadsheets/u/2/d/14SsiRw8sit3-IvzpntINicIWd4MG1CDOxbv14Ypsmpw/edit#gid=1404224753).

The roles are as follows:

### deadline-tracker:

- checks that people have submitted in time
- keeps track of excuses for late submissions and acts with good judgment
- can adjust deadlines if needed. MUST tell the project owner about any adjustments
- issues verbal warnings for late submissions (fills out the [verbal warning form](https://forms.gle/n41VC1PDyuGPakG79) as needed)

### junior reviewers:

- performs first and possibly second review completing the code review form listed above under general process.
- explicitly alerts senior reviewer about any RED FLAGs immediately (send a message on slack)
- if the reviewer is unhappy with the code but thinks that they can assist then they need to:
- send the recruit a summary of the problems that need to be fixed and an expected time frame (eg: fix by the end of tomorrow)
- inform the deadline-tracker
- review the re-submitted code or find another junior reviewer to do so

### senior reviewer:

- make sure that the junior reviewers understand the project submission requirements ahead of time
- deal with any RED FLAGs on a case by case basis
- re-review a few random code bases that various junior reviewers are happy with
- get a summary of common problems that came up in the review and update documentation as needed and/or create a workshop as needed
- ideally start reviewing as soon as possible in order to catch any problems that come up in the junior review process
- use the same code review form that the junior reviewers use
- send any problems found to all other reviewers involved and the recruit

## MUSTs, SHOULDs and whatnots

- every piece of code submitted by any recruit MUST be reviewed by a staff member OR by a recruit that has proven themselves at least once
- when a recruit submits code then they MUST receive their initial review comments by the end of the following day. If the cohort is large then the day after that is acceptable
- deadline-tracker SHOULD be a junior facilitator

## Using our recruits to help with code review

TODO. I think they should use the same code review form?

- Let a recruit review a few code submissions and let a junior or senior staff member check their work
- keep track of what recruits are good at code review and then dont require staff members to double check their work so much
- senior reviewers are in charge of making sure that juniors understand instructions
- junior reviewers are in charge of making sure that recruits understand instructions
