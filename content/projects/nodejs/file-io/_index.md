---
title: Node & File IO
ready: true
weight: 1
pre: "<b>1: </b>"
---

You are required to create a back-end service that will help capture basic information about prospective students who come to inquire here at Umuzi. In this project you'll just be storing and retrieving information from plain old json files.

## Instructions

Create the following functionality in a TDD way.

1. Create a class called Visitor. Instances of this class should have the following properties:

- full name
- age
- date of visit
- time of visit
- comments
- name of the person who assisted the visitor

2. Create a function called `save` that saves the visitor's data to a JSON file. The file name should be named like this `visitor_{some_number}.json`. The number part of the file name should be automatically generated as you save the visitor. eg:

```
alice.save()   # results in visitor_1.json
bob.save()     # results in visitor_2.json
charlie.save() # results in visitor_3.json
```

3. Create a function called `load` that takes in a number and returns a Visitor object that was saved to file.

eg:

```
alice = load(1)
bob   = load(2)
```

## Resources

- [Accessing the file system](https://www.w3schools.com/nodejs/nodejs_filesystem.asp)
- [JSON](https://www.w3schools.com/js/js_json_intro.asp): Make sure you understand everything up to the end of "JSON Arrays"
