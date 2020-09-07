---
_db_id: 523
content_type: topic
ready: true
title: Git feature branching
---

Git is a powerful tool and has quite a lot of flexibility around when to make branches and what the branches mean to you and your team. It's important to come up with a shared stratergy for managing branches on a team in order to keep the chaos at bay. It also it important from the perspective of CI/CD (continuous integration and continuous deployment)

Git feature branching is a very foundational branching stratergy. The reason we use it is that:

1. It will build certain good habits, such as being aware of where your branch starts and what that implies.
2. It is genuinely useful in real life projects, for example many open source projects use this
3. Many other popular branching stratergies are based on feature-branching.

## Resources

- https://bocoup.com/blog/git-workflow-walkthrough-feature-branches
- https://www.atlassian.com/agile/software-development/branching

## Some basic best practices

Always make sure you have pulled the latest `master` branch before making a new branch

Always make sure that your branch starts at the head of the master branch.

```
git checkout master
git pull
git checkout -b $YOUR_SENSIBLE_BRANCH_NAME
```

Always give your branches meaningful names. If you name your branch any variation of `my branch` or `branch 1` then you might as well name it `I am a complete noob`.

Before making a pull request then make sure your branch is up to date with the latest master branch. This is especially important when working on a team because sometimes things get merged into master that conflict with your code. If there are conflicts your code will not get merged. Period.

The first thing you need to do here is pull the latest master branch. Then you have 2 options:

This way is a plain old merge.

```
git checkout $YOUR_SENSIBLE_BRANCH_NAME
git merge master
```

Many professionals prefere a rebase. This are a little bit trickier to understand but are generally considered best practice.

```
git checkout $YOUR_SENSIBLE_BRANCH_NAME
git merge master
```

Also, please remember to push your code often. If you make a PR and your code on Github is out of date then that sucks. And if something bad happens to your computer it's important to have a backup. `git` is your code bakup.

## Making user-friendly PRs

When you make a pull request, give it a good name.

If there is an ussue or a description of what you are supposed to do then link to that. Otherwise describe what you are trying to do.

If your PR includes code that makes a change to a user interface then it's good to include a screenshot of the user interface. Sometimes it's even good to include a short video demonstrating the feature you just added so that people can see what the code does without having to run everything.