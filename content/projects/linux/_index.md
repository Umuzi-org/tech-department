---
title: Linux challenges

ready: true
---
# Beginner

## Task 1 : Basic Task

- Use the linux terminal to do the following :

      	1. Find the desktop folder
      	2. Create a directory and name in myProject
      	3. Change directory to myProject
      	4. Create a files and name  it  ‘ app.js ’
      	5. Change directory to Desktop and create another directory, name it myProject2
      	6. Copy ‘app.js’ from myProject to myProject2

### Resources

1. [Linux basic commands](https://www.makeuseof.com/tag/an-a-z-of-linux-40-essential-commands-you-should-know/)

## Task 2 : Absolute and Relative Paths

Create an empty file named exercise.txt and move this file to the /tmp directory, using a relative pathname from your home directory. Then, delete this file using an absolute pathname.

### Resources

1. [Paths in linux](http://www.linfo.org/path.html)
2. [Absolute and Relative Paths (video)](https://www.youtube.com/watch?v=ephId3mYu9o)

# Intermediate


## Task 3 : Cat commands

1. Create 3 files namely umuzi.txt, recruits.txt and cohort.txt.
2. Fill all 3 files with contents of your choice.
3. Write a script that concatenates the content of umuzi.txt, recruit.txt, cohort.txt and displays the result on the screen.
4. Write a script that takes the content of umuzi.txt, cohort.txt and recruits.txt to print/store the output into a new file named summary.txt.
5. Write a script that create a new file named summary.txt with new content. The script need to be careful not to override the first existing summary.txt file but should rather append the new content below the old one.

### Resources

1. [Standard File Streams (video)](https://www.youtube.com/watch?v=shFMEJJ_fpU)
2. [The cat commands](http://www.linfo.org/cat.html)

## Task 4 : The locate command

1. Write a script to help you locate a file named umuzi
2. Write a second script that will search for the same file and send the result of the search to a file named search_result.txt

### Resources

1. http://bit.ly/2GPWP9E
2. http://bit.ly/2IUg2KH

## Task 5 The locate command cont..

1. Create a file within mydocument folder, add to is a file named pad.txt
2. change the working directory to Desktop create a folder and name it work
3. copy pad.txt to the currently working directory as pad_copy.txt
4. update the database used by locate by running updatedb.
5. change the working directory to the previous one (cd -)
6. locate pad_copy.txt

Note: for each instruction write a script and save it under this task

## Task 6 Find commands
1. Write a script to find all files ending with 'pdf' on your computer
2. Write a second command that takes the result of the previous search and copy  into a folder of your choice. 
3. Write a command to display files that where modified today.

### Resources 

1. https://www.geeksforgeeks.org/find-command-in-linux-with-examples/
2. https://unix.stackexchange.com/questions/70455/how-to-run-find-exec-script



## Task 7 Text editor

1. Using nano text editor create a file named my_bio.txt
2. Save the file and close the editor
3. create a folder named my_files and move my_bio.txt within.

### Resources

1. https://www.lifewire.com/beginners-guide-to-nano-editor-3859002

# Advanced


## Task 8 User environment

1. Use echo to display Hello followed by your username. (use a bash variable!)
2. Create a variable myName with a value containing your full name.
3. Copy the value of $LANG to $MyLANG.
4. List all current shell variables.
5. Create a nodejs/python script that fetch all created variable and diplays on the creen for nodejs, in termina for python.

### Resources

1. https://dzone.com/articles/linux-environment-variables
2. https://codeburst.io/how-to-create-shortcut-commands-in-the-terminal-for-your-mac-9e016e25e4d7

## Task 9 Bash and basic scripting

1. Write a shell script that prints “Welcome to my world!” on the screen
2. Modify the shell script from point (1) to include a variable. The variable will hold the contents of the message “Welcome to my world!”
3. Store the output of the command “hostname” in a variable. Display “This script is running on _.” where “_” is the output of the “hostname” command.
4. Write a shell script to check to see if the file “file_path” exists. If it does exist, display “file_path passwords are enabled.” Next, check to see if you can write to the file. If you can, display “You have permissions to edit “file_path.””If you cannot, display “You do NOT have permissions to edit “file_path””
5. Write a shell script that displays “man”,”bear”,”pig”,”dog”,”cat”,and “sheep” on the screen with each appearing on a separate line. Try to do this in as few lines as possible.
6. write a shell script that prompts the user for a name of a file or directory and reports if it is a regular file, a directory, or another type of file. Also perform an ls command against the file or directory with the long listing option.
7. Modify the previous script to that it accepts the file or directory name as an argument instead of prompting the user to enter it.
8. Write a shell script that displays, “This script will exit with 0 exit status.” Be sure that the script does indeed exit with a 0 exit status.
9. Write a shell script that accepts a file or directory name as an argument. Have the script report if it is reguler file, a directory, or another type of file. If it is a directory, exit with a 1 exit status. If it is some other type of file, exit with a 2 exit status.

### Resources

1. https://ryanstutorials.net/bash-scripting-tutorial/bash-script.php
2. https://www.taniarascia.com/how-to-create-and-use-bash-scripts/