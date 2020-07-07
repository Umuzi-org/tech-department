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

- ##### This is how it works in the industry:
    - The Product Owner is responsible for maximizing the value of the product resulting from work of the Development Team. How this is done may vary widely across organizations, Scrum Teams, and individuals.

    - The Development Team consists of professionals who do the work of delivering a potentially releasable Increment of "Done" product at the end of each Sprint. A "Done" increment is required at the Sprint Review. Only members of the Development Team create the Increment. Optimal Development Team is allowed to have not less than 3 and not more than 9 team members to be able to execute tasks efficiently.

    - The Scrum Master is responsible for promoting and supporting Scrum as defined in the Scrum Guide. Scrum Masters do this by helping everyone understand Scrum theory, practices, rules, and values.The Scrum Master is a servant-leader for the Scrum Team.

- ##### This is how we follow Scrum at Umuzi:
    - Product Owner also acts as a stakeholder for the product. This person is in charge of deciding what the MVP, and different versions of the product look like. They are also responsible for ensuring the backlog is in correct order. 

    - Team Members consist of developers, designers, and anyone who's doing that actual production of work. Responsible for working with the Product Owner to break down tasks & reach completion on different ticket items.

    - Scrum Master is the facilitator of the scrum process. Helps the team to be productive and acheive their goal by making sure that the resources are available and there are no blockers in acheiving the goal, the team becomes independent over time.


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

#### Common 'column labels' found in product teams at Umuzi: 

  - **Backlog:** items in the backlog represent the conceived work for the team over the next 2-3+ sprints. Tickets need to be looked over by the team during the "Storytime" meeting to make sure that the objectives are clear. Attach all resources to the ticket whether they are points of reference, design documents, etc. Name the tickets so there is no confusion as to what is being accomplished. Add every requirement to the checklist and be specific.
  - **This Sprint:** here tickets are in the queue for the team's current sprint.
  The team commits to completing a given amount of tickets in the coming sprint during the "Planning" meeting.
  - **In Progress:** in this column tickets are assigned to individuals who will be actively workeing on them.
  - **Code Review:** tickets here are reviewed by team mates first. If the pull request is approved by a team member, it can either be merged straight away or given a final review by a senior member. If not, changes will be requested and the procedure will continue until the code is ready to be merged.
  - **Staging/Prototyping:** Tickets here are being checked to make sure that the user experiences what the ticket was set out to accomplish. If there's bugs or missing functionality, send it back to development.
  - **Done/Complete:** This column is for complete work. Issues cannot be moved to the Done/Complete column until the code is at least merged into the master branch.

  **Please note:** The columns described here are useful for this discussion, columns in project boards tend to be named differently and if you are new to Scrum then these columns will work well for you. Please make sure you understand the general procedure outlined here, then adapt it for your team.

#### GIT Feature Branching

We follow feature branching when working in a team. This basically means that:

- before any coding occurs, pull down the latest version from "origin/master".
- when a dev starts working on a new issue, they should make a new branch. The branch should have a sensible name
- if the dev is writing code, they should be committing and pushing code. They should push every day that they made progress! Please insist on this,you will meet resistence and you will need to stand your ground.
- Once the developer has made some changes worth committing then they make a PR.

PRs should:

- have meaningful names
- be as small as possible so that whoever is doing the review can do a good job
- PRs are created when there is code to be merged.