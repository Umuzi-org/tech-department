---
title: Java OOP basics resources and readings
ready: true
---

## OOP Principles in Java
Object-Oriented Programming refers to languages that use objects in programming. Object-oriented programming aims to implement real-world entities like inheritance, hiding, polymorphism in programming.
The main aim of OOP is to bind together the data and the functions that operate on them so that no other part of the code can access this data except that function.

The four OOP priciples in java are:

### Abstraction
An abstraction is an idea or iated conscept which is not associated with one specific object.
In Object-oriented programming, abstraction is a process of hiding the implementation details from the user, only the functionality will be provided to the user. In other words, the user will have the information on what the object does instead of how it does it.

In Java, abstraction is achieved using Abstract classes and interfaces.[Read more](https://www.geeksforgeeks.org/abstraction-in-java-2/)

The following Java code shows how Abstraction can be implemented:

```
//abstract parent class
abstract class Animal{
    //abstract method
    public abstract void sound();
    //regular method
    public void sleep() {
    System.out.println("Zzz");
  }
}
//Dog class extends Animal class
class Dog extends Animal{

    public void sound(){
        System.out.println("Woof");
    }
    public static void main(String args[]){
        Animal obj = new Dog();
        obj.sound();
    }
}
 
``` 


### Encapsulation
Ecapsulation is known as data hiding.
It is an OOP principle which states that all the attributes and behaviours (methods and functions) of an object should be grouped together in one datatype or class.
This means that objects may be able to communicate with one another but are not allowed to know how other obpublic int

The following Java code shows how Encapsulation can be implemented:

```
public class Employee{

    //private data member  
    private String name;

    //getter method for name  
    public String getName(){
        return name;
    }
    //setter method for name  
    public void setName(String name){
        this.name=name;
    }

    public static void main(String args[]) { 
        //creating instance of the encapsulated class
        Employee e=new Employee();
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
public class Vehicle {
    void printType(){
        System.out.println("I am a Vehicle");
    }
}

public class Car extends  Vehicle {
    //Override method 
    @Override
    void printType() {
        //call method in super class
        super.printType();
        System.out.println("I am a car");
    }


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

There are two types of polymorphism in Java: compile-time polymorphism and runtime polymorphism. We can perform polymorphism in java by method overloading and method overriding.
#### Method overriding

Overriding a method is when a method in the subclass has the same name and method signature as a method in the superclass. When overriding a method you are not allowed to make the method more private. 
Example:
You cannot make a public method protected.

The following Java code shows how overriding can be implemented:
```
public class Animal {
    public void eat() {
        System.out.println("Generic animal is eating");
    }
    static class Horse extends Animal {

        //Override method
        @Override
        public void eat() {
            System.out.println("Horse is eating");
        }

        public static void main(String[] args) {
            //Create a car object
            Horse horse = new Horse();
            //call method
            horse.eat();
        }
    }
}

```
#### Method overloading

Overloading a method is when a method in the subclass has the same name but the  method signature is different from the method in the superclass.

The following Java code shows how overloading can be implemented:
```
public class Calculate{

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

    public static void main(String args[]) {
       Calculate prod_object = new Calculate();
        System.out.println(prod_object.product(10, 20));
        System.out.println(prod_object.product(10, 20, 30));
        System.out.println(prod_object.product(10.5, 20.5));
    }

}
```

Read more to gain futher undestanding on [OOP concepts](https://beginnersbook.com/2013/04/oops-concepts/)
