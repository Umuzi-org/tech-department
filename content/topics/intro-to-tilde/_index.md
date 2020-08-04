---
_db_id: 399
content_type: topic
title: Introduction to Tilde
---

Welcome to Tilde. We built it with love.

If you are new to dev stuff, it's going to look a little weird. Don't worry. Before you get too deep into how we actually use this thing, it'll be good for you to know a bit about the principles and practices that inspired the design.

The first thing to know is that software development on a team is hard. And most techies work on a team. Back in the early days of software development things sucked. A lot. Software projects generally just failed, even big ones backed by people with really solid technical skills. Projects were mostly either late, broken, over-budget or the features were just wrong. If you want success in this line of work, knowing how to use tech is just the tip of the iceberg lettice.

So after lots of suffering, the software industry started figuring out ways of working that are actually effective. There are loads and loads of things to be said about those methods. But the main thing to know is that we designed Tilde in such a way as to get you to practice those methods. The way you'll be working through this course is really quite similar to how industry giants build epic software.

Basically, Tilde is basen on a thing called Kanban. Read this excellent article to understand what Kanban is all about: https://kanbanize.com/kanban-resources/getting-started/what-is-kanban

Ok cool! So Tilde is basically a kanban board. Each card you see on the board is a piece of work that you need to get done.

There are 3 main kinds of cards:

TOPICS: These are self-study materials. You can use the buttons to move them around. Most topics dont need to have any kind of review process. You just move them when you are ready by using the buttons on the cards.

WORKSHOPS: You can't move these yourself, only staff members can move them. An example of a workshop might be a presentation given by a staff member. When a staff member moves one of your WORKSHOP cards it basically means that you attended an event.

PROJECTS: These ones are the most complicated... This is the lifecycle of the basic project:

1. You choose to start a project. In the background, Tilde creates a repo for you on Github. Make sure you watch your email, github will send you an invitation email
2. You need to do your project work on the repo, but you can't commit straight to the master branch. This is how industry does it. You need to make a branch and once you have made progress you need to make a Pull Request (PR) on Github. If you are given a project with multiple parts or multiple questions, you can make multiple branches and multiple PRs.
3. Your PR wil be reviewed by other coders, once 2 people have approved your PR then it can get merged into the master branch.
4. Once your master branch completely meets the project requirements, then you need to move it to the Review column. This lets us know that you are confident that your repo's master branch is up to scratch.
5. Now there is another kind of review that happens. Your project submission will be marked as either:
   - RED FLAG: you dont want this. The most common cause of red flags is submitting empty master branches. Please be super careful here and ask if you are unsure
   - NOT YET COMPETENT: We think you are on the right track but your code needs a bit more work
   - COMPETENT: Wooo! You're done
   - EXCELLENT: Double wooo!

## IMPORTANT

You will be expected to review each other's work from time to time. Reviewing code is your top priority. If everyone puts effort into helping each other grow then everyone will grow quickly.

If you haven't been asked to review any code then just do your thang :)

We keep track of how good you are at reviewing code. For example, if you say something is COMPETENT and a staff member thinks it's a RED FLAG then that will be bad for you.

Try to do the best job you can as a reviewer when you are asked to review.

## Extra reading

Here's a bit more information about how to prioritise your activities and why:

{{% contentlink path="topics/agile-triage" %}}