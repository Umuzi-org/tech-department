---
title: Jasmine Unit testing
ready: True
---

Jasmine is a unit testing framework we like a lot. Techically it's a Behavior Driven Development (BDD) framework.

## Getting started

### Getting set up (the noob method)

There are a few different ways to get started with Jasmine. Let's go with the technically simplest one first:

... TODO

### Getting set up (like a boss)

Open up a terminal. Now execute each of the following commands:

```
mkdir my_jasmine_goodies
cd my_jasmine_goodies
npm init
npm add jasmine
npx jasmine init
npx jasmine examples
```

Take a moment to Google npm and npx if these concepts are new to you.

Now, in your editor of choice (vscode, subline, atom...), open up `package.json`. There should be something that looks like this:

```
"scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
```

Edit it to look like this:

```
"scripts": {
    "test": "jasmine"
  },
```

To run your tests you can now just do this:

```
npm test
```

Base your project structure off the example code that jasmine created for you.

## Linkz

- The official tutorial is very thorough: https://jasmine.github.io/tutorials/your_first_suite

## Advanced topics

Now that you have the basics down, here are a few more advanced ways to use Jasmine.

### Testing the DOM

Say you have some code that does some DOM manipulation. There are tools that exit that make this pretty straight-forward.

```
npm add jsdom
```

Now

{{% code_snippet "dom_manipulation.js" %}}

### Spies

Spies (often referred to as mocks in other languages and tools) are used to allow a kind of dependency injection within your tests. Here is a basic example of how it works:

{{% code_snippet "spies.js" %}}

Of course this is just the tip of the ice berg. But it gives a a basic intro. Spies are detailed in the official tutorial.

### Spy on the filesysytem

Use this. The official docs are nice.

https://github.com/tschaub/mock-fs
