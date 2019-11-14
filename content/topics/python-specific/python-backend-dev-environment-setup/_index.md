---
title: Python backend dev environment setup
ready: true
---

### What you need

This page is here to help you get set up on your local machine. These are very important tools we use at Umuzi and eventually at the workplace.

#### Installations

Setting up your environment needs you to to install a bunch of stuff. A good programmer knows his stuff, knows what he's installing and doesn't just jump into code. You will need the following:

- [VScode](https://code.visualstudio.com/docs/setup/linux): Visual Studio Code is an IDE developed by Microsoft for Windows, Linux and macOS. An integrated development environment is a software application that provides comprehensive facilities to computer programmers for software development.</br>
An IDE normally consists of at least a source code editor, build automation tools, and a debugger. What makes an IDE so useful is the I: integrated. You could use just about anything for a development environment and many people use a variety of basic, individual programs in place of an IDE but an integrated environment gives you the ability to do everything in a single editor.  
- [python3.7](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/): You will need to install the latest version of python3.7.* . Why Python? because it's friggin awesome. You can use Python for developing desktop GUI applications, websites and web applications. Also, Python, as a high level programming language, allows you to focus on core functionality of the application by taking care of common programming tasks.


#### How to run things on the terminal

The terminal is an interface in which you can type and execute text based commands. It can be much faster to complete some tasks using a Terminal than with graphical applications and menus. Another benefit is allowing access to many more commands and scripts. A common terminal task of installing an application can be achieved within a single command, compared to navigating through the Software Centre or Synaptic Manager. Press *Ctrl + Alt + T* to open the terminal when using Ubuntu/Linux-mint

##### Running Python
- Say you've created a `hello.py` script with a bunch of return statements.
- Create a folder on your computer to use for your Python programs, such as `~/pythonpractice`, and save your `hello.py` program in that folder.
- Open up the terminal program. In KDE, open the main menu and select "Run Command..." to open Konsole. In GNOME, open the main menu, open the Applications folder, open the Accessories folder, and select Terminal.
- Type `cd ~/pythonpractice` to change directory to your `pythonpractice` folder, and hit Enter.
- Don't forget to make the script executable by chmod +x.
- Type `python ./hello.py` to run your program!
**Note**: If you have both Python version 2.6.1 and Python 3.7.* installed (Very possible if you are using Ubuntu, and ran `sudo apt-get install python3` to have python3 installed), you should run python3 hello.py

##### Running programs

**Side Note**: update and upgrade your computer every chance you get, I do it every week. On your terminal run `sudo apt update` to update your machine, and if you need to upgrade the machine along with the apps, please run `sudo apt upgrade`

- After installing from the terminal some programs can allow you to open them from the terminal. So instead of navigating everywhere in your computer you can just type the alias of that program. e.g. Since we installed VScode on our machines, a simple way to open it is to go into the terminal and type in `code`. code is an alias created by the terminal as a short cut for the program.

There are are many other examples of alias that the terminal uses for programs and commands. Also check this topic on how you can use an [alias](https://shapeshed.com/unix-alias/)
