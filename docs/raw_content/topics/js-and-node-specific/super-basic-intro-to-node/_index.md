---
title: Super basic intro to Node

todo:
    - node is js on the backend
    - npm init
    - npm for installing packages
    - .gitignore node_modules/
    - running js from the command line
    - debugging js from vscode
---

Most people are introduced to JavaScript in the context of a web browser. JS adds smarts to HTML and CSS.

JS is a proper programming language so it can do a whole lot more than that. Basically it doesn't need to interact with a website in order to work. You can use it on the "back-end". It can be used to interact with filesystems and databases and all sorts of other things.

When JS is running on the backend it's usually referred to as Node. Node is really a "runtime environmnet" that can execute JS code.

Try type this into a terminal:

```
node
```

Now type

```
var greeting = "hello world";
console.log(greeting);
```

So you see you can execute JavaScript code right there in your terminal and it just works (assuing you have node installed).

Now save the helloworld code above to a file named `hello.js`. You can execute this whenever you want to by saying `node hello.js` in a terminal. Or rather `node /path/to/hello.js` if you are in a different location.

### package managers

Now one of the really super cool things about node is npm.

todo:

- talk about npm, show how to get started, install something and use it
- talk about .gitignore and node_modules
