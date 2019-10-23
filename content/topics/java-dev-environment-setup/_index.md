---
title: Java Dev environment setup
ready: true
---

In this little tutorial we'll walk through the process of getting your dev environment ready for Java. We use a number of different tools, you'll need to get them all set up.

## VSCode

This might be the world's most popular code editor. It's very good at a lot of different things.

Install VSCode from [here](https://code.visualstudio.com/download).

VSCode has a mighty ecosystem of useful plugins. Install the Java Extension Pack. You can find more information [here](https://code.visualstudio.com/docs/languages/java).

## Gradle

Next up we'll be using Gradle as a build tool. If that sentence doesn't make too much sense right now, don't worry too much. All will become clear.

To install gradle take a look [here](https://gradle.org/install/). Make sure you get the latest version.

## Test it out

In a terminal, do the following:

```
cd /somewhere/nice
mkdir hello_java
cd hello_java
gradle init
```

Gradle will now ask you a bunch of questions.

```
Select type of project to generate:
  1: basic
  2: application
  3: library
  4: Gradle plugin
Enter selection (default: basic) [1..4] 2

Select implementation language:
  1: C++
  2: Groovy
  3: Java
  4: Kotlin
  5: Swift
Enter selection (default: Java) [1..5]

Select build script DSL:
  1: Groovy
  2: Kotlin
Enter selection (default: Groovy) [1..2] 2

Select test framework:
  1: JUnit 4
  2: TestNG
  3: Spock
  4: JUnit Jupiter
Enter selection (default: JUnit 4) [1..4] 1

Project name (default: hello_java):
Source package (default: hello_java):
```

Eventually it will output somehing like this:

```
BUILD SUCCESSFUL in 39s
2 actionable tasks: 2 executed
```

Now open up vscode and point it to the current directory with the following command:

```
code .
```

You will notice that there are a whole lot of directories and files that gradle made for you. The file hierarchy looks a little something like this:

```
├── build.gradle.kts
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew
├── gradlew.bat
├── settings.gradle.kts
└── src
    ├── main
    │   ├── java
    │   │   └── hello_java
    │   │       └── App.java    <---- here's some source code
    │   └── resources
    └── test
        ├── java
        │   └── hello_java
        │       └── AppTest.java <---- and unit tests live here
        └── resources
```

## Run the code from the command line

To run your code from the command line you can do this

```
gradle run
```

It will output something like:

```
> Task :run
Hello world.

BUILD SUCCESSFUL in 476ms
2 actionable tasks: 1 executed, 1 up-to-date
```

And to test your code, do this:

```
gradle test
```

This sould output

```
BUILD SUCCESSFUL in 455ms
3 actionable tasks: 3 up-to-date
```
