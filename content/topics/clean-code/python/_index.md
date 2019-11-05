---
title: Clean Code for Python
ready: True
---

# Clean Code for Python

## Tabs or Spaces

`4 spaces == 1 tab`

Spaces are the preferred indentation method.
Tabs should be used solely to remain consistent with code that is already indented with tabs.
Python 3 **DISALLOWS** mixing the use of tabs and spaces for indentation.
Python 2 code indented with a mixture of tabs and spaces should be converted to using spaces exclusively.

Yes:

    # Aligned with opening delimiter.
    foo = long_function_name(var_one, var_two,
                            var_three, var_four)

    # Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
    def long_function_name(
            var_one, var_two, var_three,
            var_four):
        print(var_one)

    # Hanging indents should add a level.
    foo = long_function_name(
        var_one, var_two,
    var_three, var_four)

No:

    # Arguments on first line forbidden when not using vertical alignment.
    foo = long_function_name(var_one, var_two,
        var_three, var_four)

    # Further indentation required as indentation is not distinguishable.
    def long_function_name(
        var_one, var_two, var_three,
        var_four):
        print(var_one)

## Imports

- Imports should usually be on separate lines:

```
  Yes: import os
  import sys

  No: import sys, os
```

It's okay to say this though:

```
from subprocess import Popen, PIPE
```

- Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants. Imports should be grouped in the following order:

  1. Standard library imports.
  2. Related third party imports.
  3. Local application/library specific imports.

You should put a blank line between each group of imports.

- Absolute imports are recommended, as they are usually more readable and tend to be better behaved (or at least give better error messages) if the import system is incorrectly configured (such as when a directory inside a package ends up on sys.path):

        import mypkg.sibling
        from mypkg import sibling
        from mypkg.sibling import example

  However, explicit relative imports are an acceptable alternative to absolute imports, especially when dealing with complex package layouts where using absolute imports would be unnecessarily verbose:

      from . import sibling
      from .sibling import example

  Standard library code should avoid complex package layouts and always use absolute imports. Implicit relative imports should never be used and have been removed in Python 3.

When importing a class from a class-containing module, it's usually okay to spell this:

    from myclass import MyClass
    from foo.bar.yourclass import YourClass

If this spelling causes local name clashes, then spell them explicitly:

    import myclass
    import foo.bar.yourclass

and use `myclass.MyClass` and `foo.bar.yourclass.YourClass`.

- Wildcard imports (from <module> import \*) should be avoided, as they make it unclear which names are present in the namespace, confusing both readers and many automated tools. There is one defensible use case for a wildcard import, which is to republish an internal interface as part of a public API (for example, overwriting a pure Python implementation of an interface with the definitions from an optional accelerator module and exactly which definitions will be overwritten isn't known in advance).

When republishing names this way, the guidelines below regarding public and internal interfaces still apply.

## Strings

In Python, single-quoted strings and double-quoted strings are the same. This PEP does not make a recommendation for this. Pick a rule and stick to it. When a string contains single or double quote characters, however, use the other one to avoid backslashes in the string. It improves readability. For triple-quoted strings, always use double quote characters to be consistent with the docstring convention in [PEP 257](https://www.python.org/dev/peps/pep-0257).

    No:
    print("This is a string" + ' and also this')

    Yes:
    print("This is a string" + " and also this")

## Naming Conventions

The naming conventions of Python's library are a bit of a mess, so we'll never get this completely consistent -- nevertheless, here are the currently recommended naming standards. New modules and packages (including third party frameworks) should be written to these standards, but where an existing library has a different style, internal consistency is preferred.

### Class Names

Class names should normally use the `CapitalizedWords` convention.
The naming convention for functions may be used instead in cases where the interface is documented and used primarily as a callable.
Note that there is a separate convention for builtin names: most builtin names are single words (or two words run together), with the `CapitalizedWords` convention used only for exception names and builtin constants.

### Package and Module Names

Python packages should have short, all-`lowercase` names, although the use of \_underscores\_ is discouraged.
When an extension module written in C or C++ has an accompanying Python module that provides a higher level (e.g. more object oriented) interface, the C/C++ module has a leading underscore (e.g. \_socket).

### Function and Variable Names

Function names should be `lowercase`, with words separated by underscores as necessary to improve readability.
Variable names follow the same convention as function names.
`mixedCase` is allowed only in contexts where that's already the prevailing style (e.g. `threading.py`), to retain backwards compatibility.

### Constants

Constants are usually defined on a module level and written in `UPPERCASE` with underscores separating words. Examples include `MAX_OVERFLOW` and `TOTAL`.

### Names to Avoid

Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.
In some fonts, these characters are indistinguishable from the numerals one and zero. When tempted to use 'l', use 'L' instead.

## Comments

### Block Comments

Block comments generally apply to some (or all) code that follows them, and are indented to the same level as that code. Each line of a block comment starts with a `#` and a single space (unless it is indented text inside the comment).
Paragraphs inside a block comment are separated by a line containing a single `#`.

### Inline Comments

Use inline comments sparingly.

An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space.
Inline comments are unnecessary and in fact distracting if they state the obvious. Don't do this:

    x = x + 1                 # Increment x

But sometimes, this is useful:

    x = x + 1                 # Compensate for border

### Documentation Strings

Conventions for writing good documentation strings (a.k.a. "docstrings") are immortalized in PEP 257.

- Write docstrings for all public modules, functions, classes, and methods. Docstrings are not necessary for non-public methods, but you should have a comment that describes what the method does. This comment should appear after the def line.
- PEP 257 describes good docstring conventions. Note that most importantly, the """ that ends a multiline docstring should be on a line by itself:

```
    """Return a foobang

    Optional plotz says to frobnicate the bizbaz first.
    """
```

- For one liner docstrings, please keep the closing """ on the same line.
