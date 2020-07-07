---
title: Mock Interview Prep
ready: true
tags: ["work readyness"]
---

### Introduction
This little exercise will take you through the basic git mechanisms you need to know about in order to be productive. By the end of this exercise you’ll be able to create and manage your own git repos

## Creating and managing your own repo
Note: you can do all of this stuff from the command line! You should be using linux. Open up a terminal and do the following:

Your initial commit
Create a directory named git-basic-exercises
cd into your new directory
look at what’s inside using ls -a. It should be empty
initialize your git repo using git init. Then check ls -a again. Can you spot the difference?
check the status of your repo by typing git status
type in touch README.md. This creates a new blank file. Then check ls -a and git status again.
type in git log. The output should make sense to you
Now add your readme file to your git staging area. Hint: use the git add command
Then check your git status again. Can you see the difference?
Try to unstage your file and check your git status again
Ok, now for your first commit: Make sure your readme file is staged then type in git commit -m "initial commit" Your output should be something like this:
 [master (root-commit) 2103b64] initial commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
type in git log isn’t that nice? press q to exit
more commits!
type in nano README.md. This will open up a text editor. Type in some stuff and then press ctrl x to exit. Then y then enter. This will save your changes
type in cat README.md. This will print your file to the console
take a look at the git stats again and make sure you understand it
commit your changes to your repo. Your commit should have the message "second commit"
make some more changes to your readme and make a "third commit"
check this out
type in git log. You should see all your commits there. It should look something like this:
commit a57585d3cf93e64c04e62e58dfe8151d191503cf (HEAD -> master)
Author: Sheena O'Connell <sheena.oconnell@gmail.com>
Date:   Tue Apr 23 15:07:40 2019 +0200

    third commit

commit a48c005c761902395cf9a50f13ddbffeee4f5537
Author: Sheena O'Connell <sheena.oconnell@gmail.com>
Date:   Tue Apr 23 15:07:12 2019 +0200

    second commit

commit 2103b6418ecf4f70effabb639cfad6ac9d57c089
Author: Sheena O'Connell <sheena.oconnell@gmail.com>
Date:   Tue Apr 23 14:43:51 2019 +0200

    initial commit
Each commit has a “hash”. That’s the weird alphanumeric string thingy.

Copy the commit hash for your second commit. You can just select it with your mouse and right click and choose ‘copy’
press q to exit the log view. You should now be back at the terminal
type in git checkout and then paste in the commit hash and press enter
cat README.md It’s like going back in time
git checkout master
cat README.md Now we are up to date
You can jump to any commit using git checkout. You can checkout a branch, a commit hash, or a tag. We didn’t explore tags here.

When you checkout a branch, you checkout the latest commit on that branch.

branching

