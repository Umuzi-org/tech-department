---
title: Introduction to Spring Boot - part 4
ready: true
---

Consuming an API refers to the process of calling an API from an application. The methods available for an application to consume
an API are mapped to the API itself. For instance, if the API does not contain a GET endpoint, then the application can't consume the 
API using a Http GET call.

## REST Terminology

`Body`: The body of an Http call refers to data that's being sent to the API that is not displayed in the url. A body is usually sent using
		POST-, PUT-, and PATCH-methods. The body must match what is expected in the API method. In Spring Boot, it must match the 
		@RequestBody variable.

`Headers`: Headers are additional information passed along in the Http request. Usual use cases for Headers are:
		   - Passing through Authentication tokens.
		   - Describing the format of the request body.

## Consuming an API using REST

Imagine the API is hosted at the following url: `https://www.myapi.com`

# GET call: Used to fetch data from an API

If the GET endpoint is located at https://www.myapi.com/mygetendpoint and the endpoint is expecting a String variable called id, then the
GET call would look like the following:

```
	// HttpClient allows us to make calls to API's
	HttpRequest request = HttpRequest.newBuilder()
		.GET() // The type of Http Request
		.uri(URI.create("https://www.myapi.com/mygetendpoint?id=myUserId")) // The Uri of the API
		.setHeader("Authentication", "Bearer userAuthenticationToken") // add request header
		.build();

	HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString()); // Shows the results of the Http Request

```

# POST call: Used to save data

If the POST endpoint is located at https://www.myapi.com/mypostendpoint and is expecting a model containing a name and surname String variable
then the POST call would look like the following:

```

	var values	=	new HashMap<String, String>() {{
						put("name", "John");
						put ("surname", "Doe");
					}};

	var objectMapper = new ObjectMapper();
	String requestBody = objectMapper.writeValueAsString(values); // Converting the HashMap to a String

	HttpClient client = HttpClient.newHttpClient();
	HttpRequest request = HttpRequest.newBuilder()
			.uri(URI.create("https://www.myapi.com/mypostendpoint"))
			.POST(HttpRequest.BodyPublishers.ofString(requestBody)) // requestBody refers to the data passed through in the POST call
			.build();

	HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

```

# PUT call: Create or Update a resource

If the PUT endpoint is located at https://www.myapi.com/myputendpoint and is expecting a model as a body, the PUT endpoint would look
like the following:


```

	String inputJson =	"{\n" +
						"  \"name\": \"put_test_employee\",\n" +
						"  \"salary\": \"1123\",\n" +
						"  \"age\": \"23\"\n" +
						"}";

	var client = HttpClient.newHttpClient();
 
	var request = HttpRequest.newBuilder()
		.uri(URI.create("https://www.myapi.com/myputendpoint"))
		.header("Content-Type", "application/json") // Describes the format of the body data
		.PUT(HttpRequest.BodyPublishers.ofString(inputJson))
		.build();
  
	var response = client.send(request, HttpResponse.BodyHandlers.ofString());

```

# PATCH call: Making partial changes to existing data

If the PATCH endpoint is located at https://www.myapi.com/mypatchendpoint and is expecting a model as a body, the PATCH endpoint would look
like the following:

```

	String inputJson =	"{\n" +
						"  \"name\": \"put_test_employee\",\n" +
						"  \"salary\": \"1123\",\n" +
						"  \"age\": \"23\"\n" +
						"}";

	var client = HttpClient.newHttpClient();

	HttpRequest request = HttpRequest.newBuilder()
	   .uri(URI.create("https://www.myapi.com/mypatchendpoint"))
	   .header("Content-type", "application/json")
	   .PATCH(BodyPublishers.ofString(inputJson))
	   .build();

	var response = client.send(request, HttpResponse.BodyHandlers.ofString());

```

# DELETE call: Removing a record 

If the DELETE endpoint is located at https://www.myapi.com/mydeleteendpoint, the DELETE endpoint would look
like the following:

The DELETE call works similar to the GET call in the way that it passes data through to the API. The parameter is sent in the Url and not in
the request body.

```
 
	var request = HttpRequest.newBuilder()
		.uri(URI.create("https://www.myapi.com/mydeleteendpoint/IdVariable"))
		.header("Content-Type", "application/json")
		.DELETE()
		.build();
 
	var client = HttpClient.newHttpClient();
 
	var response = client.send(request, HttpResponse.BodyHandlers.ofString());

```

## References

http://zetcode.com/java/httpclient/
https://mkyong.com/java/java-11-httpclient-examples/
https://techndeck.com/put-request-with-json-using-java-11-httpclient-api/
https://www.dariawan.com/tutorials/java/introduction-to-java-11-standarized-http-client-api/
https://techndeck.com/delete-request-using-java-11-httpclient-api/
