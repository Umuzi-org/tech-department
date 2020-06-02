---
title: Generics 
ready: true
prerequisites:
  hard: ["topics/kotlin/sealed-classes"]
  soft: []
---
## Generics
As in Java, classes in Kotlin may have type parameters:
````
class Box(t: T) {
    var value = t
    }
````
In general, to create an instance of such a class, we need to provide the type arguments:
````
val box: Box = Box(1)
````
But if the parameters may be inferred, e.g. from the constructor arguments or by some other means, one is allowed to omit the type arguments:
````
val box = Box(1) // 1 has type Int, so the compiler figures out that we are talking about Box
````
