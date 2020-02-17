---
date: 2019-03-19T16:50:16+02:00
title: Version Control & Scrum using Trello & Github
weight: 15
---

## Definition of Scrum

A framework within which people can address complex adaptive problems, while productively and creatively delivering products of the highest possible value.

## The Scrum Team

The Scrum Team consists of a Product Owner, the Development Team, and a Scrum Master. Scrum Teams are self-organizing and cross-functional. Self-organizing teams choose how best to accomplish their work, rather than being directed by others outside the team. Cross-functional teams have all competencies needed to accomplish the work without depending on others not part of the team.

Scrum Teams deliver products iteratively and incrementally, maximizing opportunities for feedback. Incremental deliveries of "Done" product ensure a potentially useful version of working product is always available.

## Scrum roles

- This is how it works in the industry:
    - The Product Owner is responsible for maximizing the value of the product resulting from work of the Development Team. How this is done may vary widely across organizations, Scrum Teams, and individuals.The Product Owner is responsible for maximizing the value of the product resulting from work of the Development Team. How this is done may vary widely across organizations, Scrum Teams, and individuals.

    - The Development Team consists of professionals who do the work of delivering a potentially releasable Increment of "Done" product at the end of each Sprint. A "Done" increment is required at the Sprint Review. Only members of the Development Team create the Increment. Optimal Development Team is allowed to have not less than 3 and not more than 9 team members to be able to execute tasks efficiently.

    - The Scrum Master is responsible for promoting and supporting Scrum as defined in the Scrum Guide. Scrum Masters do this by helping everyone understand Scrum theory, practices, rules, and values.The Scrum Master is a servant-leader for the Scrum Team. The Scrum Master helps those outside the Scrum Team understand which of their interactions with the Scrum Team are helpful and which aren’t. The Scrum Master helps everyone change these interactions to maximize the value created by the Scrum Team.

- This is how we follow Scrum at Umuzi:
    - Product Owner
  The stakeholder for the product. This person is in charge of deciding what the MVP, and different versions of the product look like. They are also responsible for ensuring the backlog is in correct order. 

  - Team Member
  Developers, designers, and anyone who's doing that actual production of work. Responsible for working with the Product Owner to break down tasks & reach completion on different ticket items.

  - Scrum Master
  The facilitator of the scrum process. If this person is doing their job right, the team becomes independent over time.


## Scrum Meetings

### Planning

- When:
  At the beginning of the sprint
- What:
  The team commits to a set of tickets for the sprint that they think they can complete.
- Why:
  Gives a goal to work towards, ensures that there is a select pool of tickets that the team can then have the freedom to choose as they please.

### Storytime

- When:
  As needed. 2-3+ sprint's worth of tickets should be in the backlog at all times.
- What:
  The team hashes out different story point from the product manager, converting them into tickets that are an appropriate size with unambiguous requirements.
- Why:
  So every ticket is clear on what needs to be accomplished.

### Review

- When:
  At the end of every sprint
- What:
  Team demos all work done for an audience including, but not limited to, stakeholders & team members
- Why:
  It's not only nice to show off work, but it ensures that everything is actually working in harmony.

### Retro

- When:
  After the end of every sprint
- What:
  The team, with the intention of improving the scrum process, covers the following issues together
  What went well
  What went poorly
  What can be done to improve
- Why:
  The scrum process should be adaptable to the organization's needs. This also allows all members of the team to participate and own the process.

### Standup

- When:
  Every day
- What:
  Team answers following questions in order - What did I do to advance the team's goals in the sprint yesterday? - What is impeding me from working on the team's goals for this sprint?
  All other discussions are tabled for smaller groups afterwards
- Why:
  Helps to adapt to problems that come up, and to initiate conversation about different topics.

## General issue board procedure

Every time you move a ticket from one column to another, you make a PR and assign a team member for the first review on your code. If the code has no bugs or errors then the ticket moves to final code review so it can be merged.If there are any changes requested comments are made on the PR and then the ticket is moves to reveiw changes requested. Tickets that are merged move to the Done column.
Attach all resources to the ticket whether they are points of reference, design documents, etc.
Name the tickets so there is no confusion as to what is being accomplished.
Add every requirement to the checklist, and be specific. Check off requirements as you finish work on them in development.

### Backlog

Items in the backlog represent the conceived work for the team over the next 2-3+ sprints.
Before items are able to be moved into the "To Do" column, they need to be looked over by the team during the "Storytime" meeting to make sure that the objectives are clear.
Various labeling/measuring can take place on these tickets, like adding the feature they're associated with, the estimated work hours to complete the feature, and more.

### This Sprint

Tickets in this sprint are in the queue for the team's current sprint.
The team commits to completing a given amount of tickets in the coming sprint during the "Planning" meeting.

### Today

Tickets moved to today are being actively worked on by the person assigned to them.

#### Git Action

Before any coding occurs, pull down the latest version from "origin/master". Then, after coding is finished, create a new branch with a name corresponding to your ticket. Commit, push to origin, and create a pull request in Github.

### Code Review

Tickets in 'First review needed' are having their associated code (or design) reviewed. A team member will look at the pull request on Github and see that the code is well formed, doesn't have obvious bugs and accomplishes what it set out to do, it is either moved to 'Final Review needed' or merged straight away. If necessary, changes are suggested, and the ticket is moved 'Review: changes requested'.

#### Git Action

If the code passes review, the pull request is approved and the branch is merged into master.

### Quality Assurance

Tickets in quality assurance are being checked to make sure the user experiences what the ticket was set out to accomplish. If there's bugs or missing functionality, send it back to development.

#### Git Action

Pull the merge commit from origin/master for testing.

### Done:

Tickets here are done.
