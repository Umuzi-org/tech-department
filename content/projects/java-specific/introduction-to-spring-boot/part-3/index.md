--
title: Introduction to Spring Boot - part 3
ready: true
---

We are going to focus on creating a REST api that will serve as a end point to our sping boot java application.  

## Service 

Continuing with "introduction-to-spring-boot/part-2" for the **User** we are going to expose a **REST endpoint** to the application and we will use test to see if the application does what we want it to.

**Step 1** 

Create a Controller Class based on the spring MVC infrastructure. This will be used to expose the endpoint.
Remeber to create your Crontroller Class inside a "Controller" Package

```
package controller;

public class UserController {
}
```

**Step 2**

Add two spring annotations @RestController and @RequestMapping abouve the class declaration.

```
package controller;

								//add here.
								//add your specified route as input parameter to your annotation.
public class UserController {
}
```

@RestController declares the class as a REST Controller to the JVM.
@RequestMapping Adds a route or URL extention to reach this controller.


**Step 3** 

Add the **@Service** annotation to your UserServiceImpl class previously created in {{% contentlink "projects/java-specific/introduction-to-spring-boot/part-1" %}}.


```
				//add annotation here.
				
public class UserServiceImpl{
    addUser(name, surname) // should call insert(name, surname) from FakeRepo and print to console '[name] entered'

	removeUser(Id) // should call delete(id) from FakeRepo and print to console '[name] removed'

	getUser(Id) // should call find(id) from FakeRepo and print to console 'hello [name]'

	[name] - replaced with actual name
    }
}

```

**Step 4**

Implement all your services (methods) inside the UserService class. 
	1 - Use the @Autowired annotation to instantiate the UserService class.
	2 - Use the Put, Delete, Get spring annotations to map the respective services. 
	3 - Do not forget to mark the input parameter as a @RequestBody if you are recieving data in the body of the object.
		- If you are recieving the data as a url parameter -  mark varable as @PathVariable.
		- If you are recieving the data as a query parameter -  mark varable as a query parameter.
		

Example
```
	@PutMapping
    public ResponseEntity<String> update(@RequestBody Customer customer)                               //RequestBody
    {
        customerService.update(customer);
        ResponseEntity<String> responseEntity = new ResponseEntity("Success!", HttpStatus.NO_CONTENT);
        return responseEntity;
    }

    @DeleteMapping																						
    public ResponseEntity<String> delete(@PathVariable(value = "id")int customerId)						//PathVariable
    {
        customerService.delete(customerId);
        return new ResponseEntity("Success!", HttpStatus.OK);
    }

    @GetMapping("/{id}")																				//Query Parameter.
    public ResponseEntity<Customer> get(@PathVariable(value = "id")int customerId)
    {
        return new ResponseEntity(customerService.get(customerId), HttpStatus.OK);
    }
```
**Side Notes**
1 - Please remeber to test your end points using postman. If you need help with using postman access the using poostman link.
2 - Add at least one image of a sucessfull request using postman.
3 - The first resource link shows you everything you need to do to complete this project from start to finish if you struggle with any step.
4 - This project assumes you have set up your postgress connection as it is an extension of part1 and part2 of the Spring Boot Series. 
5 - Please create a new beanch labled **part3**
												
												**Happy Coding...**
## Resources

https://dzone.com/articles/expose-restful-apis-using-spring-boot-in-7-minutes
https://www.google.com/search?q=using+postman&oq=using+postman&aqs=chrome..69i57j0l7.2559j0j7&sourceid=chrome&ie=UTF-8#kpvalbx=_WISeXrbFAZaY1fAPp6eFmA449
https://dzone.com/articles/creating-a-rest-api-with-java-and-spring
https://github.com/nikeshpathak/customer-demo-webservice/blob/master/src/main/java/com/example/customer/demo/controller/CustomerCtrl.java
