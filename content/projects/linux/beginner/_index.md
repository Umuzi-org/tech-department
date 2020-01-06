---
title: Beginner Linux challenges
ready: true
---

### Submission guidelines

While you work through this project you will save your script commands in a number of files called shell scripts, name them by task and sub task number i.e. 1-2,  they have the extension .sh. You'll be handing those in later. In general we use a tool called Git and a platform called Github for project submissions but this will be covered later in the course.

### Task 1 : Basic Task

Open a linux terminal. Now do the following from the command line.

1. type in `ls` and press enter. What do you see? What does this mean?
2. type in `pwd` and press enter. What do you see? What does this mean?
3. Make a new directory called `workspace` then `cd` into your new directory
4. type in `ls` and press enter. What do you see? What does this mean?
5. Make a new file called `README.md` (you can use the `touch` command to do this)
6. Make a copy of `README.md`, name your copy `CHANGELOG.md`

#### Resources

1. [Linux basic commands](https://www.makeuseof.com/tag/an-a-z-of-linux-40-essential-commands-you-should-know/)

### Task 2 : Absolute and Relative Paths

Create an empty file named `exercise.md` and move this file to the `/tmp` directory, using a relative pathname. Then, delete this file using an absolute pathname.

### Resources

1. [Paths in linux](http://www.linfo.org/path.html)
2. [Absolute and Relative Paths (video)](https://www.youtube.com/watch?v=ephId3mYu9o)

### Task 3 : cat commands

1. Create 3 files namely `umuzi.md`, `recruits.md` and `cohort.md`.
2. Fill all 3 files with contents of your choice. Maybe some nice poems about you MUB experience.
3. Write a script that concatenates the content of `umuzi.md`, `recruit.md`, `cohort.md` and displays the result on the screen.
4. Write a script that takes the content of `umuzi.md`, `cohort.md` and `recruits.md` to print/store the output into a new file named `summary.md`.
5. use the command line to append the words "The End" to `summary.md`. Be careful not to overwrite the exiting contend

#### Resources

1. [Standard File Streams (video)](https://www.youtube.com/watch?v=shFMEJJ_fpU)
2. [The cat commands](http://www.linfo.org/cat.html)

### Task 4 : The locate command

1. Write a script to help you `locate` a file named `umuzi`
2. Write a second script that will search for the same file and send the result of the search to a file named `search_result.md`

#### Resources

1. http://bit.ly/2GPWP9E
2. http://bit.ly/2IUg2KH

### Task 5 The locate command cont..

1. Create a file within `Documents` directory, add to is a file named `pad.md`
2. change the working directory to Desktop, then create a folder and name it `work`
3. copy `pad.md` to the currently working directory as `pad_copy.md`
4. update the database used by locate by running `locate updatedb`.
5. change the working directory to the previous one (`cd -`)
6. use `locate` to find `pad_copy.md`

Note: for each instruction write a script and save it under this task

### Task 6 Find commands

1. Write a script to find all files ending with 'pdf' on your computer
2. Write a second command that takes the result of the previous search and copy into a folder of your choice.
3. Write a command to display files that where modified today.

#### Resources

1. https://www.geeksforgeeks.org/find-command-in-linux-with-examples/
2. https://unix.stackexchange.com/questions/70455/how-to-run-find-exec-script

### Task 7 Text editor

1. Using `nano` text editor create a file named `my_bio.md`
2. Save the file and close the editor
3. Create a folder named `my_files` and move `my_bio.md` within.

#### Resources

1. https://www.lifewire.com/beginners-guide-to-nano-editor-3859002
