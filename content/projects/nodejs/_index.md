---
title: Nodejs Challenges
todo: [

    "add more introductory node exercises. consider: https://zellwk.com/blog/crud-express-mongodb/ and then expose crud json api"
]
---

## Note

These are NodeJS challenges. Your main focus here is to make sure your Node code is good. You will not be evaluated on the prettiness of your frontend. Your frontend just needs to work.

## Task 1 : Http server (http, get, serve static files)

Create an HTML form with the following fields:

- email address
- comments. This is a text box

Create a basic express js application and serve your form as a static file. The url should be `http://localhost:[YOUR_PORT]/comment`

The default port when running an express app is 8080. So your url will probably look like this: [http://localhost:8080/comment](http://localhost:8080/comment)

### Resources

NB: The list of provided resources is not exhaustive feel free to check around (google...) for more.

- [Basic node server](https://nodejs.org/en/docs/guides/getting-started-guide/)
- [Express documentation](https://expressjs.com/)
- [Static files](https://expressjs.com/en/starter/static-files.html)
- [Express, node overview](https://www.tutorialspoint.com/nodejs/nodejs_express_framework.htm)

## Task 2: Request handling (basic routing, post, form, middleware)

Add a submit button to your form. When the user clicks that button then do the following:

- collect the form data and write it to the log (`console.log`) on the backend. Meaning you should be calling the `console.log` within your express code
- redirect the user to a new page at `http://localhost:[YOUR_PORT]/thanks` that just says "Thanks for the comment"

### Resources

- [Basic routing](https://expressjs.com/en/starter/basic-routing.html)
- [Express Middleware](https://expressjs.com/en/guide/using-middleware.html)
- [More about middleware](http://bit.ly/2Ivqojf)
- [About bodyParser](http://bit.ly/2PaKoZD)

## Task 3: HTML template engine (Javascript templates, fetch, api)

Create a new express js project called weather station

- create a new page on your site at the url `http://localhost:[YOUR_PORT]/weather`
- use the PUG template engine and ES6 to render a web page. The site should be similar to this [one](https://cdn-images-1.medium.com/max/1400/0*e-_dbhFTqw7WMHwg.png)
- Your web page should display real data. Do do so you will make use of the following JSON api:

Note that when you submit this task, it should be in a new git repository.

### Resources

- [About javascript template engines (Short explanation)](https://stackoverflow.com/questions/9547028/what-is-a-template-engine)
- [More on Javascript templates](https://www.sitepoint.com/overview-javascript-templating-engines/)
- [API](https://medium.freecodecamp.org/what-is-an-api-in-english-please-b880a3214a82)
- [Fetch](https://scotch.io/tutorials/how-to-use-the-javascript-fetch-api-to-get-data)

## Task 4: A registration restful API ( API end-point, routing, MongoDB, database schema)

You are required to create a back-end service that will help capture basic information about Visitorive students who come to inquire here at Umuzi.

Start off by defining your MongoDB schema. Make use of Mongoose. Create an ?? called Visitor that allows you to store the following info:

- id
- visitor name
- name of the person who assisted the visitor
- visitor's age
- date of visit
- time of visit
- comments

Next up create some JSON endpoints:

- `/addNewVisitor`: create a new Visitor in the database
- `/deleteVisitor:id`: delete a single Visitor from the database
- `/deleteAllVisitors`: delete all Visitors
- `/viewVisitors`: view all Visitors
- `/viewVisitor:id`: view a single Visitor
- `/updateVisitor:id`: Update a single Visitor

### Resources

- [About restful API](https://searchmicroservices.techtarget.com/definition/RESTful-API)
- [Build a restful API with node](https://medium.com/@purposenigeria/build-a-restful-api-with-node-js-and-express-js-d7e59c7a3dfb)
- [Test your API-end points ](https://www.getpostman.com/)
