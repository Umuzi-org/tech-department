---
date: 2020-04-07T17:08:16+02:00
title: java collections
weight: 3
---

>   **List**

```
import java.util.*;
public class Lists {
    //Store lists of objects.
    //Duplicates are allowed
    //Objects remain in the order of insertion
    //You can manually sort the list by writing a custom function if you want to.
    //Elements in a list are indexed with a "Integer"
    //Checking for for a particular item in a list you have to go down a list like you manually on a written list.
    //- This makes checking for a item by insertion value slow.
    //Looking for a item by index is fast as the index is sorted in numerical order.
    //Iterating through list is fast. As fast as looping through anything sorted can be.

    //If you only want to add or remove a item to the end of the list use the ArrayList as this only adds items using
    //- the add function that adds items to the end of the list.
    List<String> list1 = new ArrayList<String>();

    //Removing or adding elsewhere in a list?
    List<String> list2 = new LinkedList<String>();



}

```

>   **Map**

```

import java.util.*;
public class Maps {
    //These apply to ann instances of the Maps.

    //Stores Key Value Pairs.
    //Like lookup table where you can store values with a key(Integer, String, etc).
    //- You then can use the key to retrieve another object.
    //Maps are optimized to retrieve a value by key, fast.
    //If the key is a integer and they be stored as a consecutive list rather use a List.
    //If the keys are unordered then use a map.
    //Iterating over a map value is slow due to the objects in the maps being unordered or sorted.
    //Maps are not optimized for Iteration. Hence they dont extend the Iterator class.
    //If you want to add objects of a class you created yourself.
    //- The objects have to implement the hashcode() and equals() methods.
    //- So that the set knows if two objects are the same or not.

    // Keys are not in any particular order, and order is liable to change.
    //Order may be random.
    //Most light weight
    Map<String, String> mapHashMap = new HashMap<String, String>();

    //Keys are sorted in natural order
    //(A,B,C ... 1,2,3)
    //Must implement comparable for custom objects.
    //Uses a tree structure.
    Map<String, String> mapTreeMap = new TreeMap<String, String>();

    //Keys remain in order added.
    Map<String, String> mapLinkedHashMap = new LinkedHashMap<String, String>();
}

```
> **QUEUES**

```
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;

public class Queues {

    //The Queue is used to insert elements at the end of the queue and removes from the beginning of the queue. It follows FIFO concept.
  // The Java Queue supports all methods of Collection interface including insertion, deletion etc.
  //add(value) - places given value at back of queue
  //remove() - removes value from front of queue and returns it.
  //Throws a NoSuchElementException if queue is empty.
  //peek() - returns front value from queue without removing it.
  //returns null if empty.
  //size() - returns number of elements in queue.
  //isEmpty() - returns true if queue has not elements.
  public static void main(String[] args) {
      Queue<Integer> queue1 = new LinkedList<Integer>();
      queue1.add(42);
      queue1.add(-3);
      queue1.add(17); //front [42, -3, 17] back
      System.out.println(queue1.remove()); //42


          System.out.println(queue1);

      }
}
```
>  **Queues-Example**

```
import java.util.LinkedList;
import java.util.Queue;

public class QueuesExample
{
    public static void main(String[] args)
    {
        Queue<Integer> q = new LinkedList<>();

        // Adds elements {0, 1, 2, 3, 4} to queue
        for (int i=0; i<5; i++)
            q.add(i);

        // Display contents of the queue.
        System.out.println("Elements of queue-"+q);

        // To remove the head of queue.
        int removedele = q.remove();
        System.out.println("removed element-" + removedele);

        System.out.println(q);

        // To view the head of queue
        int head = q.peek();
        System.out.println("head of queue-" + head);

        // Rest all methods of collection interface,
        // Like size and contains can be used with this
        // implementation.
        int size = q.size();
        System.out.println("Size of queue-" + size);
    }
}
```

>  **Queues-Example2**

```

import java.util.LinkedList;
import java.util.Queue;

/*
 *  Example of element() and peek() methods.
 */

public class QueuesExample2
{

    public static void main( String[] args )
    {
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(200);
        queue.add(300);
        queue.add(400);
        queue.add(500);

        System.out.println("queue : " + queue + "\n");

        /*
         * Retrieves, but does not remove, the head of this queue. This method
         * differs from peek only in that it throws an exception if this queue
         * is empty.
         */
        Integer element = queue.element();

        System.out.println("element : " + element);
        System.out.println("queue : " + queue + "\n");

        /*
         * Retrieves, but does not remove, the head of this queue, or returns
         * null if this queue is empty.
         */

        element = queue.peek();
        System.out.println("element : " + element);
        System.out.println("queue : " + queue + "\n");

    }
}
```

>  **Sets**

```
import java.util.*;

public class Sets {
    //Applies to all instances of the set Interface.

    //Only store unique items.
    //Which removes duplicates.
    //Not indexed, unlike lists. So you cannot locate a particular item on the list by its stored position.
    //Sets are optimized for finding a object by its inserted value.
    //Making it very fast to check if a particular object exists.
    //If you want to add objects of a class you created yourself.
    //- The objects has to implement the hashcode() and equals() methods.
    //- So that the set knows if two objects are the same or not.

    //Order is unimportant and okay if it changes!
    //Hash set is not ordered.
    //Order may be random.
    //Most light weight
    Set<String> stringHashSet = new HashSet<String>();

    //Sorted in natural order? Use Tree Set.
    //(A,B,C ... 1,2,3) these are naturally comparable (methods are pre-written)
    //You must implement comparable for custom objects.
    //Uses a tree structure.
    Set<String> stringTreeSet = new TreeSet<String>();

    //Elements remain in order they were added.
    Set<String> set3 = new LinkedHashSet<String>();


}
```

>  **SortedMaps**

```
import java.util.Iterator;
import java.util.Map;
import java.util.Set;
import java.util.SortedMap;
import java.util.TreeMap;

public class SortedMaps
{
    public static void main(String[] args)
    {
        SortedMap<Integer, String> sm = new TreeMap<Integer, String>();
        sm.put(new Integer(2), "practice");
        sm.put(new Integer(3), "quiz");
        sm.put(new Integer(5), "code");
        sm.put(new Integer(4), "contribute");
        sm.put(new Integer(1), "geeksforgeeks");
        Set s = sm.entrySet();

        // Using iterator in SortedMap
        Iterator i = s.iterator();

        // Traversing map. Note that the traversal
        // produced sorted (by keys) output .
        while (i.hasNext())
        {
            Map.Entry m = (Map.Entry)i.next();

            int key = (Integer)m.getKey();
            String value = (String)m.getValue();

            System.out.println("Key : " + key +
                    "  value : " + value);
        }
    }
}
```
> **SortedSets**

```

import java.util.Comparator;
import java.util.SortedSet;
import java.util.TreeSet;
public class SortedSets {

        public static void main(String[] args) {
            SortedSet<Person> personsById = new TreeSet<>(
                    Comparator.comparing(Person::getId));

            personsById.add(new Person(1, "X"));
            personsById.add(new Person(2, "Z"));
            personsById.add(new Person(3, "A"));
            personsById.add(new Person(4, "C"));
            personsById.add(new Person(4, "S")); // A duplicate Person

            System.out.println("Persons by  Id:");
            personsById.forEach(System.out::println);

            SortedSet<Person> personsByName = new TreeSet<>(
                    Comparator.comparing(Person::getName));
            personsByName.add(new Person(1, "X"));
            personsByName.add(new Person(2, "Z"));
            personsByName.add(new Person(3, "A"));
            personsByName.add(new Person(4, "C"));

            System.out.println("Persons by  Name: ");
            personsByName.forEach(System.out::println);

        }

    }

    class Person {
        private int id;
        private String name;

        public Person(int id, String name) {
            this.id = id;
            this.name = name;
        }

        public int getId() {
            return id;
        }

        public void setId(int id) {
            this.id = id;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        @Override
        public boolean equals(Object o) {
            if (!(o instanceof Person)) {
                return false;
            }

            // id must be the same for two Persons to be equal
            Person p = (Person) o;
            if (this.id == p.getId()) {
                return true;
            }

            return false;
        }

        @Override
        public int hashCode() {
            return this.id;
        }

        @Override
        public String toString() {
            return "(" + id + ", " + name + ")";
        }
    }
```
> [Java Collections101_Sorted_Set](http://www.java2s.com/Tutorials/Java/Java_Collection/0110__Java_Sorted_Set.htm)

