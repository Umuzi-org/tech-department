---
title: Java OOP basics resources and readings
ready: true
---


[What is Object Oriented Programming?](https://medium.com/learn-how-to-program/chapter-3-what-is-object-oriented-programming-d0a6ec0a7615)

## Four main OOP priciples in java:

### Abstraction
In Object-oriented programming, abstraction is a process of hiding the implementation details from the user, only the functionality will be provided to the user. In other words, the user will have the information on what the object does instead of how it does it.

An every day example of abstraction is driving a car. When you turn on the ignition you just turn a key, the car does a whole lot of things under the hood. The starter motor and carberator is abstracted. You don't need to know how that stuff works in order to work a car.

In Java, abstraction is achieved using Abstract classes and interfaces.[Read more](https://www.geeksforgeeks.org/abstraction-in-java-2/)

The following Java code shows how Abstraction can be implemented:

```
abstract class Bike{  
  abstract void run();  
} 

class Honda4 extends Bike{  
    void run(){
        System.out.println("running safely");
    }
} 

class Main{
    public static void main(String args[]){  
        Bike obj = new Honda4();  
        obj.run();  
    }  
}   

``` 


### Encapsulation
Encapsulation is known as data-hiding.
It is an OOP principle which states that all the attributes and behaviours (methods and functions) of an object should be grouped together in one datatype or class.
This means that objects may be able to communicate with one another but are restricted to access some of the object's components directly.
Publicly accessible methods are generally provided in the class so-called [accessors and mutators.](https://www.cs.colostate.edu/~cs161/Fall12/labs/lab2/bookgetset.html)) 

[Read more on encapsulation.](https://www.geeksforgeeks.org/encapsulation-in-java/)

The following Java code shows how Encapsulation can be implemented:

```
class Employee{

    //private data member
    private String name;

    public void setName(String empName){
        this.name  = empName;
    }

    //getter method for name  
    public String getName(){
        return name;
    }

}

class Main{
    public static void main(String args[]) {
        //creating instance of the encapsulated class
        Employee e = new Employee();
        //setting value in the name member
        e.setName("Mbali");
        //getting value of the name member
        System.out.println(e.getName());

    }
} 
```
[Abstraction vs Encapsulation](https://1.bp.blogspot.com/-ECYNAUTGGMk/WPQeY4EpFtI/AAAAAAAAIX8/j-Ji8N_mDz8-d72SasgNPnQD-nIlw-kiACLcB/s1600/Abstraction%2Bvs%2BEncapsulation%2B2.jpg)

### Inheritance
This OOP principle allows one class to inherit all the attributes and behaviors of another class.
Inheritance has a hierarchy  relationship between superclasses (base classes )and subclasses

The following Java code shows how Inheritance can be implemented:
```
//superclass
class Vehicle {
    void printType(){
        System.out.println("I am a Vehicle");
    }
}

class Car extends  Vehicle {
    //Override method
    @Override
    void printType() {
        //call method in super class
        super.printType();
        System.out.println("I am a car");
    }
}
class Main{
    public static void main(String[] args) {
        //Create a car object
        Car car = new Car();
        //call method
        car.printType();
    }
}

```

### Polymorphism
Polymorphism in Java is a concept by which we can perform a single action in different ways. Polymorphism is derived from 2 Greek words: poly and morphs. The word "poly" means many and "morphs" means forms. So polymorphism means many forms.

There are two types of polymorphism in Java: compile-time polymorphism and run-time polymorphism. We can perform polymorphism in java by method overloading and method overriding. [Read more.](https://stackify.com/oop-concept-polymorphism/) 
#### Method overriding

Overriding a method is when a method in the subclass has the same name and method signature as a method in the superclass. When overriding a method you are not allowed to make the method more private. 

Example:
You cannot make a public method protected.

The following Java code shows how overriding can be implemented:
```
public class Fruit {
    public void print() {
        System.out.println("I am a fruit");
    }
}
class Apple extends Fruit {

    //Override method
    @Override
    public void print() {
        System.out.println("I am an Apple");
    }

}
class Main{
public static void main(String[] args) {
    //Create an animal object
    Fruit fruit = new Fruit();
    //Create horse object
    Apple apple = new Apple()
    fruit.print();
    //call method
    apple.print();
}
}

```
#### Method overloading

Overloading a method is when a method in the subclass has the same name but the  method signature is different from the method in the superclass.[Read more](https://beginnersbook.com/2013/05/method-overloading/)

The following Java code shows how overloading can be implemented:
```
class Calculate{

    public int product (int x, int y) {
        return (x * y);
    }

    // Overloaded. This product method  takes three int parameters
    public int product(int x, int y, int z) {
        return (x * y * z);
    }

    // Overloaded. This product method takes two double parameters
    public double product(double x, double y) {
        return (x * y);
    }
}

class Main {
    public static void main(String args[]) {
        Calculate prod_object = new Calculate();
        System.out.println(prod_object.product(10, 20));
        System.out.println(prod_object.product(10, 20, 30));
        System.out.println(prod_object.product(10.5, 20.5));
    }
}
```

## Important links 
Read more to gain further understanding on [OOP concepts](https://beginnersbook.com/2013/04/oops-concepts/).

[Here](https://stackify.com/oops-concepts-in-java/) is another useful link.

[Java oops concepts] (https://www.javatpoint.com/java-oops-concepts) by Java T Point.