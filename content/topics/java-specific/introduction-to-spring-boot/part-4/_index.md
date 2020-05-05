---
title: Introduction to Spring Boot - part 4
ready: true
---

Consuming an API refers to the process of calling an API from an application. The methods available for an application to consume an API are mapped to the API itself. For instance, if the API does not contain a GET endpoint, then the application can't consume the API using a Http(s) GET call.

You can either consume and existing SOAP service or a REST api and in this topic we are going to cover both. Lets jump into it.

# Consume a REST API

As we now know in development there is always more than one way to do something and this applies to consuming apis as well. In a spring application you can use 2 of the most popular rest clients which are:

1. HttpClient: Sends request to and gets response from server over HTTp protocol and takes care of the following as well
    - HTTP protocol interception

    - Secure HTTP connections - SSL/TLS

    - HTTP proxy server handling

    - Handles HTTP cookies

    - Connection pooling for different hosts, keep alive strategy,

    - multi-threaded request execution  

2. Rest Template: is the central Spring class for client-side HTTP access. Conceptually, it is very similar to the JdbcTemplate, JmsTemplate, and the various other templates found in the Spring Framework and other portfolio projects. This means, for instance, that the RestTemplate is thread-safe once constructed, and that you can use callbacks to customize its operations. It uses HttpClient under the hood.

Now that we have covered those its time to look into what makes up a connection

What you might need to learn first about consuming a REST api is the terminology used to describe the parts of the request

1. `URl`: Uniform Resource Locator, is a reference to a web resource that specifies its location on a computer network. (e.g http://localhost:8080)

2. `Body`: The body of an Http call refers to data that's being sent to the API that is not displayed in the url. A body is    usually sent using
		POST-, PUT-, and PATCH-methods. The body must match what is expected in the API method. In Spring Boot, it must match the 
		@RequestBody variable.

3. `Headers`: Headers are additional information passed along in the Http request. Usual use cases for Headers are:
		   - Passing through Authentication tokens.
		   - Describing the format of the request body.

**Now Consuming an API using REST**

We are going to use the rest template to connect to out API. Imagine the API is hosted at the following url: `http://www.myapi.com`

## GET call: Used to fetch data from an API

If the GET endpoint is located at http://www.myapi.com/getendpoint and the endpoint is expecting a String variable called id, then the
GET call would look like the following:

```
RestTemplate restTemplate = new RestTemplate();
String userResourceUrl = "https://www.myapi.com/getendpoint";
ResponseEntity<String> response = restTemplate.getForEntity(userResourceUrl + "/1", String.class);

// Check if the status code is successful, since we get the entire response object
assertThat(response.getStatusCode(), equalTo(HttpStatus.OK));

```
Cause we have the entire response object we can do something a bit more cleaver when serializing objects from the response
for example

```
public class User implements Serializable {
    private long id;
 
    private String name;

	private String surname
    // standard getters and setters and constructor
}

// Now we can do a get by using getForObject() and map it to User DTO

User user = restTemplate
  .getForObject(userResourceUrl + "/1", user.class);

```

## POST call: Used to save data

If the POST endpoint is located at http://www.myapi.com/postendpoint and is expecting a model containing a name and surname String variable
then the POST call would look like the following:

```

RestTemplate restTemplate = new RestTemplate();
String userResourceUrl = "https://www.myapi.com/postendpoint";

HttpEntity<Foo> request = new HttpEntity<>(new User("Bob", "Khumalo"));
User user = restTemplate.postForObject(UserResourceUrl, request, User.class);
```

## DELETE call: Removing a record 

If the DELETE endpoint is located at https://www.myapi.com/mydeleteendpoint, the DELETE endpoint would look
like the following:

The DELETE call works similar to the GET call in the way that it passes data through to the API. The parameter is sent in the Url and not in
the request body.

```
RestTemplate restTemplate = new RestTemplate();
String userResourceUrl = "https://www.myapi.com/deleteendpoint";
long id = 2;

String entityUrl = userResourceUrl + "/" + id;
restTemplate.delete(entityUrl);

// You can do a get of the same ID afterwards to see if still exist 

```

# Consuming SOAP Webservice

This is the second kind of web service you mights be required to consume which is more involved that the REST API.

First lets learn some terminology of all the things you will working on

1. `wsdl`: web service description language -  is an XML-based file that basically tells the client application what the web service does. The WSDL file is used to describe in a nutshell what the web service does and gives the client all the information required to connect to the web service and use all the functionality provided by the web service. 

	- Below is the general structure of a WSDL file

		- Definition

		- TargetNamespace

		- DataTypes

		- Messages

		- Porttype

		- Bindings

		- service

2. `xsd`: is a file used to define what elements and attributes may appear in an XML document. It also defines the relationship of the elements and what data may be stored in them

```
<?xml version="1.0" encoding="UTF-8" standalone="no"?><wsdl:definitions xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:sch="https://medium.com/article" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="https://medium.com/article" targetNamespace="https://medium.com/article">
  <wsdl:types>
    <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" targetNamespace="https://medium.com/article">

    <xsd:element name="getArticleRequest">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="id" type="xsd:int"/>
            </xsd:sequence>
        </xsd:complexType>
    </xsd:element>

    <xsd:element name="getArticleResponse">
        <xsd:complexType>
            <xsd:sequence>
                <xsd:element name="article" type="tns:article"/>
            </xsd:sequence>
        </xsd:complexType>
    </xsd:element>
```

Second you need to download the right dependencies to generate classes from a wsdl. I wont lie the gradle configuration for this is long and complicated so I wont add it in the note but I suggest you go through this [example](https://spring.io/guides/gs/consuming-web-service/)

```
implementation ('org.springframework.boot:spring-boot-starter-web-services') {
	exclude group: 'org.springframework.boot', module: 'spring-boot-starter-tomcat'
}
implementation 'org.springframework.ws:spring-ws-core'
// For Java 11:
implementation 'org.glassfish.jaxb:jaxb-runtime'
compile(files(genJaxb.classesDir).builtBy(genJaxb))

jaxb "com.sun.xml.bind:jaxb-xjc:2.1.7"

```

To create a web service client you will need to extend WebServiceGatewaySupport and put your operations in there

```
import com.medium.user.GetUserRequest;
import com.medium.user.GetUserResponse;
import org.springframework.ws.client.core.support.WebServiceGatewaySupport;

public class UserClient extends WebServiceGatewaySupport {

    public GetUserResponse getUser(int id){
        GetUserRequest getUserRequest = new GetUserRequest();
        getUserRequest.setId(id);
        return (GetUserResponse) getWebServiceTemplate().marshalSendAndReceive(getUserRequest);
    }
}

```

Then you need to configure Marshalling, Spring Web Service uses Spring Framework’s OXM module, which has the Jaxb2Marshaller to serialize and deserialize XML requests.

```
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.oxm.jaxb.Jaxb2Marshaller;

@Configuration
public class UserConfiguration {

  @Bean
  public Jaxb2Marshaller marshaller() {
    Jaxb2Marshaller marshaller = new Jaxb2Marshaller();
    // this package must match the package in the <generatePackage> specified in
    // pom.xml
    marshaller.setContextPath("com.example.consumingwebservice.wsdl");
    return marshaller;
  }

  @Bean
  public UserClient userClient(Jaxb2Marshaller marshaller) {
    UserClient client = new UserClient();
    client.setDefaultUri("http://localhost:8080/ws");
    client.setMarshaller(marshaller);
    client.setUnmarshaller(marshaller);
    return client;
  }

}

```

## References

https://spring.io/blog/2009/03/27/rest-in-spring-3-resttemplate

http://zetcode.com/java/httpclient/

https://mkyong.com/java/java-11-httpclient-examples/

https://techndeck.com/put-request-with-json-using-java-11-httpclient-api/

https://www.dariawan.com/tutorials/java/introduction-to-java-11-standarized-http-client-api/

https://techndeck.com/delete-request-using-java-11-httpclient-api/

https://www.baeldung.com/rest-template

https://www.tutorialspoint.com/java/java_serialization.htm


https://spring.io/guides/gs/consuming-web-service/#initial

https://www.guru99.com/wsdl-web-services-description-language.html

https://fileinfo.com/extension/xsd

https://medium.com/swlh/consume-soap-web-services-with-spring-boot-4ea8e1ad7b16

https://docs.spring.io/spring-ws/site/reference/html/client.html