---
title: Introduction to Spring Boot - part 1
ready: true
prerequisites:
  hard: ["projects/java-specific/introduction-to-spring-boot/"]
  soft: []
---

We covered a very large part of the Spring Boot framework at a high level on the reading material but I hope you went through the resource as well. This project will be very simple but focusing on all the building blocks. **HAVE FUN!!**

**Step 1** - Create a java application and import 'org.springframework.boot:spring-boot-starter-web' into your build.gradle file to convert it to a Spring Boot application

**Step 2** - Ensure that your Main class is configure correctly for a Spring Boot application. Hint: @SpringBootApplication

**Step 3** - Create a Model called User

```
class User {
    private long Id;
    private String name;
    private String surname;

    // add constructor, getter and setter
}
```

**Step 4** Create an interface called FakeRepoInterface with the following methods

```
insertUser(id, name, surname)

findUserById(id)

deleteUser(id)

```

**Step 5** - Create a class called FakeRepo wrap it with the @Repository annotation which implements the FakeRepoInterface, in this class you will mimic an actual repository by provide implementation
for the following methods

```
Create an object array of type User

insertUser(id, name, surname) // should store the name and surname in the 'User' Object Array

findUserById(id) // returns name and surname of the specified id from the 'User' Object Array

deleteUser(id) // remove the object with id from the User Object Array
```

**Step 6** - Create an Interface called (UserService) with the following methods they can be type void for now

```
addUser(name, surname)

removeUser(Id)

getUser(Id)
```

**Step 7** - Create a class called UserServiceImpl which implements the interface in [step 4] and must do the following

Use (dependency injection) for including FakeRepo inside UserServiceImpl **DO NOT USE THE NEW KEYWORD**

```
addUser(name, surname) // should call insert(name, surname) from FakeRepo and print to console '[name] entered'

removeUser(Id) // should call delete(id) from FakeRepo and print to console '[name] removed'

getUser(Id) // should call find(id) from FakeRepo and print to console 'hello [name]'

[name] - replaced with actual name
```

**Step 8** - Write tests for

- addUser(name, surname)
- removeUser(Id)
- getUser(Id)
