---
date: 2020-04-14T17:03:37+02:00
title: "Live coding: java-generics(Code Example)"
weight: 3
---

**CODE EXAMPLES**


```java
1.

import java.util.ArrayList;
import java.util.List;

class Container<A>
{
    A value;
}
public class GenericsDemo {
    //Constructing a Generics Class.
    
    public static void main(String[] args) {
        // List of object type
        List x = new ArrayList();

        x.add("text"); // A String that cannot be cast to an Integer
        x.add(7);

        Integer i = (Integer)x.get(1); // Run time error.
        System.out.println(i);
    }
}
```
 
```
2.

import javax.xml.namespace.QName;
import java.awt.*;

class Container2<A>
{
    // Value type declared for Generic purposes.
    A value;

    public A getValue() {
        return value;
    }

    public void setValue(A value) {
        this.value = value;
    }



    //Show method to get the name of the Generic passed to the class when instantiating the Container class.
    public void show()
    {

        System.out.println("Class Type is: " + value.getClass().getName());

    }

}
class Student{

    private String name;
    private int age;
    private double value;

    //Getters and Setter for Student attributes.
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getValue() {
        return value;
    }

    public void setValue(double value) {
        this.value = value;
    }
}

public class GenericsDemo2 {


    public static void main(String[] args) {
        //Instantiating the Container class with the type Integer.
        Container2<Integer> obj = new Container2<>();
        obj.value = 100;
        obj.show();


        //Instantiating the Container class with the type Double.
        Container2<Double> obj1 = new Container2<>();
        obj1.value = 100.00;
        obj1.show();

        //Instantiating the Container class with the type Student.
        Container2<Student> stu = new Container2<>();

        //Instantiating the Student class with values.
        Student studentInstance = new Student();
        //Inserting values into studentInstance.
        studentInstance.setValue(10000.00);
        studentInstance.setName("Hanna");
        studentInstance.setAge(24);


        //Injecting student instance into Student Object.
        stu.setValue(studentInstance);

        //Displaying the object type of the Container Class as per Instantiated Instance.
        stu.show();

        //What instance type will the next line of code show?
        System.out.println(stu.getClass().getName());

        //Will the class compile when no values are added? When a student with null values get injected into the Container class?

    }
}
```

```
3.

import java.util.ArrayList;

class Container3<A extends Number>
{
    // Value type declared for Generic purposes.
    A value;



    // Getter and Setter method for value.
    public A getValue() {
        return value;
    }

    public void setValue(A value) {
        this.value = value;
    }



    //Show method to get the name of the Generic passed to the class when instantiating the Container class.
    public void show()
    {

        System.out.println("Class Type is: " + value.getClass().getName());

    }

}

class Container4<A  extends Integer>
{
    // Value type declared for Generic purposes.
    A value;



    // Getter and Setter method for value.
    public A getValue() {
        return value;
    }

    public void setValue(A value) {
        this.value = value;
    }



    //Show method to get the name of the Generic passed to the class when instantiating the Container class.
    public void show()
    {

        System.out.println("Class Type is: " + value.getClass().getName());

    }
    public void demo(ArrayList<? super A> obj){


    }

}

public class GenericsDemo3 {
    public static void main(String[] args) {

        //Subclass Examples.
        Container3<Integer> obj = new Container3();
        obj.value = 50000;

        obj.show();

        Container3<Double> obj1 = new Container3();
        obj1.value = 100000.00;

        obj1.show();

        Container3<Long> obj2 = new Container3();
        obj2.value = 15000000000L;

        obj2.show();

        //Extending, referencing the subclass.
        //Change the data type !!!
        Container3<Number> obj3 = new Container3();
        obj3.value = 50000;

        obj3.show();

        //Superclass Examples.
        //Change the data type !!!
        Container4<Integer> obj4 = new Container4();
        obj4.value = 50000;

        ArrayList<Integer> arrayInt = new ArrayList();
        arrayInt.add(300);
        obj4.show();
        obj4.demo(arrayInt);

    }
}
```