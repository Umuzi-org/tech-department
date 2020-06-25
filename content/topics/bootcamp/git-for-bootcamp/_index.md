---
Title: Git for Bootcamp
ready: true
---

### Using git features with Spck


### Basic Terminal Commands needed for Bootcamp
|git command|Function|
|---|---|
|`git clone` *repo url*|clones the repo to your local machine|
|`git checkout -b`*name-of-your-new-branch* |creates a new branch from the branch you had checks that branch out (this means you are now working on that branch)|
|`git status`|Returns the current working branch. If a file is in the staging area, but not committed, it shows with git status. Or, if there are no changes it’ll return nothing to commit, working directory clean.|
|`git push`|pushes the changes you have made, saved and committed locally to the remote repo|
|`git push origin` *branch name*|After branching you need to use this command to push your new branch to remote github|
|`git push --set-upstream origin` *branch name*| sets the upstream and enables you to push to the correct branch using the `git push` command|
|`git add` *file name*|adds the specified file to the stageing area so that it is ready to be committed|
`git add .`|adds all files with saved changes to staged so they are ready to commit NB! always check `git status` before using `git add .`|
|`git commit -m "*your commit message*"`|Record the changes made to the files to a local repository. For easy reference, each commit has a unique ID.It’s best practice to include a message with each commit explaining the changes made in a commit. Adding a commit message helps to find a particular change or understanding the changes. |

[Common Git Commands with Explications and examples of usage](http://guides.beanstalkapp.com/version-control/common-git-commands.html#local)