---
title: Environmental Variables
---

This tutorial assumes that you are using some kind of bash derived shell. Open up your linux command prompt :)

## Shell variables

You have dealt with variables in your programming language of choice many times. Bash also has variables. You can declare them like this:

```
FOO=BAR
```

To access your variable you can do this kind of thing:

```
echo $FOO
```

You can also use bash variables within other bash operations. Eg:

```
ROOT_DIR=/path/to/some/important/directory
mkdir $ROOT_DIR
nano $ROOT_DIR/something.yaml
```

Bash has a problem with whitespace. These wont work:

```
FOO = BAR
BAZ=The quick brown fox
```

But these work:

```
FOO=BAR
BAZ="The quick brown fox"
MEH='The quick brown fox'
```

## Environmental variables

Environmental variables are shell variables that have a larger scope. Consider the following python code:

```
a = 1
# at this point in the code: only `a` is available

def foo():
    b = 2
        # at this point in the code: `a` and `b` are available, but not `c`
    def bar():
        c = 3
        # at this point in the code: `a`,`b` and `c` are all available

# at this point in the code: only `a` is available
```

Or similarly, this is the JavaScript version:

```
a = 1
# at this point in the code: only `a` is available

function foo():
    b = 2
        # at this point in the code: `a` and `b` are available, but not `c`
    function bar():
        c = 3
        # at this point in the code: `a`,`b` and `c` are all available

# at this point in the code: only `a` is available
```

## .bashrc
