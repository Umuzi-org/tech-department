---
title: Expose a JSON API
ready: true
weight: 4
pre: "<b>4: </b>"

prerequisites:
  hard:
    [
      "projects/nodejs/sql",
      "topics/js-and-node-specific/apis-with-node",
      "projects/nodejs/file-io",
    ]
  soft: []
tags: ["node", "api", "express"]
story_points: 5

available_options: ["javascript"]
submission_type: continue_repo
from_repo: projects/nodejs/file-io
---

There is no need to create a new git repo for this code submission. This is a continuation of your previous work.

## Instructions

Use Express to expose the following JSON endpoints.

- `/addNewVisitor`: create a new Visitor in the database
- `/deleteVisitor:id`: delete a single Visitor from the database
- `/deleteAllVisitors`: delete all Visitors
- `/viewVisitors`: view all Visitors
- `/viewVisitor:id`: view a single Visitor
- `/updateVisitor:id`: Update a single Visitor

### Resources

- {{% contentlink path="topics/apis/basics" %}}
- {{% contentlink path="topics/js-and-node-specific/apis-with-node" %}}
