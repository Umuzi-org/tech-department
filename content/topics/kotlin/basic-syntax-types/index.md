---
title: Basic Syntax & Types
ready: true
---

**BASICS - Types**

[**var us val:**](https://www.youtube.com/watch?v=Nz-lMqxfUUs)

- **val and var** both are used to declare a variable.
- **var** is like general variable and it&#39;s known as a **mutable** variable in **Kotlin** and can be assigned multiple times.
- **val** is like Final variable and it&#39;s known as **immutable** in **Kotlin** and can be initialized only single time., after it become read only. The IllegalAccessorError will occur when you try to reassign the value.
- You can enforce a type called [strongtyping](https://whatis.techtarget.com/definition/strongly-typed). This is the opposite of statically typed.

Syntaxt : var book:String = &quot;Maths&quot; // This should only be used when necessary.

**Numbers:**

- Kotlin handles numbers in a way close to Java, but not exactly the same.
- Kotlin provides the following built in types representing numbers (this is close to Java):

| **Type** | **Bit** [**Width**](https://www.youtube.com/watch?v=_SkpnG571z8) |
| --- | --- |
| Double | 64 |
| Float | 32 |
| Long | 64 |
| Int(Default data type in Kotlin) | 32 |
| Short | 16 |
| Byte | 8 |

**Characters:**

- Note that characters are not numbers in Kotlin.
- Characters are represented by the type Char.
- They cannot be treated directly as number.
- [In Java](https://www.youtube.com/watch?v=LBQrD2nkKQg) they are stored as numbers internally.
  - [https://www.youtube.com/watch?v=LBQrD2nkKQg](https://www.youtube.com/watch?v=LBQrD2nkKQg)


```
Fun check(c: Char){

If (c == 1) {

// Error : incomaptable types will occur

}

}
```


**Booleans:**

The type Boolean represents booleans, has a **true** or **false** value.

**Arrays:**

Arrays in Kotlin are represented by the array class, that has get and set functions (that turn into [] by operator overloading conventions), and size property, along with a few other useful member functions:


```
Class Array private constructor() {

val size: int

operator fun get (index : Int) T

operator fun set(index : Int, value: T ) : Unit

}
```


**Strings**

Strings represented by the type String. Strings are immutable.

They are immutable in nature.

Should be written in double quotes.

Elements of a string are characters that can be accessed by the indexing operation:


```
s[I]

A string can be iterated over with a for loop:

for (c in str){

prinln(c)

}
```
