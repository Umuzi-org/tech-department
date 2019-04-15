

# Nodejs Challenges


## Task 1 : Http server (http, get, serve static files)   


- Make a copy of your game and rename the copy to nodeApp.
-  Setup a node server with express within nodeApp folder  to serve your game on port 8080 to  https://localhost:8080 or localhost:8080

### Resources

NB: The list of provided resources is not exhaustive feel free to check arround (google...) for more.

- [Basic node server](https://nodejs.org/en/docs/guides/getting-started-guide/)
- [Express documentation](https://expressjs.com/)
- [Static files](https://expressjs.com/en/starter/static-files.html)
- [Express, node overview](https://www.tutorialspoint.com/nodejs/nodejs_express_framework.htm)




## Task 2: Request handling (basic routing, post, form, middleware)

- Set-up a node server  within a second folder (with a name of your choice)
- Create a form with a public folder, similar to this [one](https://ibm.co/2DecgXY) (do not mind the style). 
- The form is to be served on  https://localhost:8000/form
- Upon submission the form should collect all data and submit them to a screen within a JSON format

### Resources

- [Basic routing](https://expressjs.com/en/starter/basic-routing.html)
- [Express Middleware](https://expressjs.com/en/guide/using-middleware.html)
- [More about middleware](http://bit.ly/2Ivqojf)
- [About bodyParser](http://bit.ly/2PaKoZD)

## Task 3: HTML template engine  (Javascript templates, fetch, api)

- Setup a sever within a third folder
- Create a single page website which provide weather to visitors. 
- The site should be similar to this [one](https://cdn-images-1.medium.com/max/1400/0*e-_dbhFTqw7WMHwg.png) , however you are required to used PUG as template and ES6 
- The site url to be served by entering the following url: localhost:8880/weather

### Resources

- [About javascript template engines (Short explanation)](https://stackoverflow.com/questions/9547028/what-is-a-template-engine)
- [More on Javascript templates](https://www.sitepoint.com/overview-javascript-templating-engines/)
- [API](https://medium.freecodecamp.org/what-is-an-api-in-english-please-b880a3214a82)
- [Fetch](https://scotch.io/tutorials/how-to-use-the-javascript-fetch-api-to-get-data)


## Task 4: A registration restful API ( API end-point, routing, MongoDB, database schema)

- Setup a server within a fourth folder - name it as you wish.
- You are required to create a back-end service that will help capture basic informations about prospective student who come to inquire here at Umuzi. 
- Captured information should include the following: Visitor’s **Name and surname**, **age, **date** and **time**, **subject of inquiry**and **the name of the person who assisted the visitor**. 
- The back-end service to provide the following end points:
    1. **/addNewProspect**(add a new prospect)
    2. **/deleteProspect:id** (delete a single prospect)
    3. **/deleteAllProspects** (delete all prospects)
    4. **/viewProspects** (view all prospects)
    5. **/viewProspect:id** (view a single prospect)
    6. **/updateProspect:id **(Update a single prospect)
- The service to use Mongodb database and Mongoose schema.

### Resources 

- [About restful API](https://searchmicroservices.techtarget.com/definition/RESTful-API)
- [Build a restful API with node](https://medium.com/@purposenigeria/build-a-restful-api-with-node-js-and-express-js-d7e59c7a3dfb )

- [Test your API-ends](https://www.getpostman.com/)





