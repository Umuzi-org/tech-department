---
title: Logging in Node and JS
ready: true
---

Through the development process logging helps us evaluate computation which we might be uncertain about, or show us what is happening during runtime where we have little control. Its like a third eye helping us see things that we might otherwise finding very difficult to see.

**Why we would like to log**

- Quick debugging of unexpected behavior during development
- Browser-based logging for analytics or diagnostics
- Logs for your server application to log incoming requests, as well as any failures that might have happened
- Optional debug logs for your library to assist the user with issues
- Output of your CLI to print progress, confirmation messages or errors

The most basic form of logging in javascript is console logging

The console object provides access to the browser's debugging console and though it might differ from browser to browser they're a set of functions common to all
see more features [here](https://developer.mozilla.org/en-US/docs/Web/API/console)
```
console.log('Logging in Node and JS');
```
**Log Levels**

What is also important to note is that logging has different levels which informs your application what sort of information it should care about so as to not make to much noise and also help in the granularity of those logs.

Example

- info
- warn
- error

But they're multiple ways and places one can log to, like output logs in a file or on a reporting tool or intecepting a request to the backend. For such activities you might need more than just console.logging and lucky for us Node provides a few options for this.

 - Middleware
    * Expressjs
 - Packages such as:
    * Winston
    * Node-Loggly
    * Morgan
    * Retrace agent for server logs



**Resources for reading**

https://www.twilio.com/blog/guide-node-js-logging

https://stackify.com/node-js-logging/