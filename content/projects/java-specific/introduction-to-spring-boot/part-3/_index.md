---
title: Introduction to Spring Boot - part 3
ready: true
---

We are going to work on Spring boot **REST** in this project covered in {{% contentlink "topics/java-specific/introduction-to-spring-boot/part-3" %}}

Continuing with {{% contentlink "projects/java-specific/introduction-to-spring-boot/part-1" %}} we are now going to use a rest api to connect to our service. At this point we have come full circle in the life cycle of creating a rest api.

**Step 1**

You should provide api functions for the following actions

```
addUser(name, surname) - POST

removeUser(Id) - DELETE

getUserByID(Id) - GET (previously called getUser(Id))


// New functions

getAllUsers() - GET

updateExistingUserName(id, name) - PUT

```

**Step 2**

Run your application and by default it should start the server at localhost:8081 (this might differ sometimes just check your terminal where you are running the application to check the server), you should then go to any browser/postman (if you have) and hit your endpoints

**Step 3**

Write integration tests for the 4 methods in Step 1

That would be the end of your SpringBoot series. WELL DONE!!


