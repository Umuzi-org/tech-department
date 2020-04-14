---
date: 2020-04-07T17:08:16+02:00
title: Java Generics
weight: 3
---

**What, Why, When?**

>
- Generics are a facility of generic programming that were added to the Java programming language in 2004.
- They were designed to extend Java's type system to allow "a type or method to operate on objects of various types while providing compile-time type safety".
- The Java collections framework supports generics to specify the type of objects stored in a collection instance.

**Type of generics.**

- A type variable is an unqualified identifier.
- Type variables are introduced by: 
  - generic class declarations, 
  - generic interface declarations, 
  - generic method declarations, 
and by generic constructor declarations.
- These all become generic when a type variable is introduced by declaring them for/within a class.

**Type safety**

- The Java language is designed to enforce type safety.
- Type safety means that a program cannot perform an operation on an object unless that operation is valid for that object.
- Type safety means that the compiler will validate types while compiling, then throw an error if you try to assign the wrong type to a variable.

**Problem when generics are not introduced.**

>      // List of object type
>      List x = new ArrayList();
>
>      x.add("text"); // A String that cannot be cast to an Integer
>
>      Integer i = (Integer)x.get(i); // Run time error



**Achieving type safety with the use of generics.**

>       // List of Integers
>       List <Integer>x = new ArrayList<Integer>();
>
>       x.add("text"); 	// A error will be thrown when trying to allocate a text.(Compile time error).
>   	x.add(7);
>
>   	Integer i = (Integer)x.get(i); 	// Run time error will be avoided.

**Compile time error vs runtime error.**

+ Compile time error is any type of error that prevents a java program compilation like:
    + a syntax error, a class not found,
    + a bad file name for the defined class,
    + a possible loss of precision when you are mixing different java data types and so on.
+ A runtime error means an error which happens, while the program is running.

**Implementing custom generics.**

+ When constructing your own generics a single letter from A-Z can be used.
+ It must be in UPPERCASE as per generics naming convention. 
+ Normally the letter E is reserved for Element.
+ The letter T can be used to indicate Type. 
+ Refer to Generics Demo 2

#### Generic class

>	                Class Container<T>{
>		                T value;
>                   }
>
>This declaration of the type can be any class
>This means anytime you create an object of Integer. This value becomes an integer. 

>   	            Class Container<T>{
>			            Object value;
>		            }
>This may cause Run Timer error. 

***Raw types in java***

* Raw types refer to using a generic type without specifying a type parameter. 
* For example, List is a raw type, while List<String> is a parameterized type. 
* When generics were introduced in JDK 1.5, raw types were retained only to maintain backwards compatibility with older versions of Java.

**Example of raw type**

* Access Link -
    [Generics Raw Types](https://www.tutorialspoint.com/java_generics/java_generics_raw_types.htm)
  * Click on live demo.
  * Execute.
  * Notice the notes under javac that provides notes of warning messages for runtime errors. 
    * (Selected compilers compiles binary like Eclipse)
* <?> Also indicates a raw type. This syntax means wildcard. 
    * It contains meta information about a class.

> **<?>** <br>
>It's not a problem when you use it with Class. Both lines work and compile:

>					Class anyType = String.class;
>					Class <?> theUnknownType = String.class;

But - if we start using it with collections, then we see strange compile time errors:

>					List<?> list = new ArrayList<Object>();  // ArrayList<?> is not allowed
>					list.add("a String");                    // doesn't compile ...
> Our List<?> is not a collection, that is suitable for just any type of object. It can only store one type: the mystic “ unkown type". Which is not a real type, for sure.
>
>
> **<?>** 
>
> - It means your Class reference can hold a reference to any Class object.

> - It's basically the same as "Class" but you're showing other people who read your code that you didn't forget about generics, you just want a reference that can hold any Class object.

> - Bruce Eckel, Thinking in Java:

> - In Java SE5, Class<?> is preferred over plain Class, even though they are equivalent and the plain Class, as you saw, doesn’t produce a compiler warning. The benefit of Class<?> is that it indicates that you aren’t just using a non-specific class reference by accident, or out of ignorance. You chose the non-specific version.


**Generics only support classes and not wrapper classes**

* int cannot be used and only Integer.
* Int is primitive. 
* Integer is a class that contains the primitive data type of int with constructor and methods. 
* As per convention you may only use classes
* Programmer defined classes can also be used. 

**Extends and super with generics.**

+ Extends will support to subclass of the Extended Class.
+ Super will support the superclass of the Extended Class.
+ Refer to Generics Demo 3.

**Food For Thought** 

History in making - [Corona Virus read more](http://www.health.gov.za/index.php/outbreaks/145-corona-virus-outbreak/465-corona-virus-outbreak)

