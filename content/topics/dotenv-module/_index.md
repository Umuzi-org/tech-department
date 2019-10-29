---
title: Introduction to Dotenv module 
ready: true

---

## What is an environment variable?

An [environment variable](https://en.wikipedia.org/wiki/Environment_variable) is a variable whose value is set outside the program, typically through functionality built into the operating system or microservice. An environment variable is made up of a name/value pair, and any number may be created and available for reference at a point in time.

```
//example 
NAME_OF_PLACE=Umuzi

```

## How does dotenv help you?

Using environment variables is one technique to make your app easier to configure by separating infrequently changing data from your code. [Dotenv](https://www.npmjs.com/package/dotenv) module loads environment variables from a .env file that you create and adds them to the [process.env](https://nodejs.org/docs/latest/api/process.html#process_process_env) object that is made available to the application

```
//.env
MODE=development
DB_HOST=localhost
DB_PORT=27017
DB_USER=root
DB_PASS=235b599a53bd46c3fb89999b1389ba83

```


```
//server.js
console.log(process.env.MODE); //development
console.log(process.env.DB_HOST); //localhost
console.log(process.env.DB_PORT); //27017
console.log(process.env.DB_USER); //root
console.log(process.env.DB_PASS); //235b599a53bd46c3fb89999b1389ba83

```

## How do I use dotenv?

- Create project directory and name it whatever you want.
- cd into the directory you created and run
```
npm init -y
npm install --save dotenv

``` 
- Create a .env file and add your settings.

```
//.env

BASE_URL=https://umuzi.org
API_KEY=000FBAA4558FF565851A3E104017AB1A
SERVER_PORT=3000
USER=umuziadmin
OBJ={key1:"value1", key2:"value2",key3:"value3",key4:"value4"}
BOOL=true
NUM=123456
STRING= Dumela Lefatshe
NULL=null
UNDEFINED=undefined
ARRAY=[1,2,3,4,5,6]

```

#### &nbsp; Usage

- Create a .js file and start using the module
```
//index.js

require('dotenv').config();

const url = process.env.BASE_URL;
const apiKey = process.env.API_KEY;
const port = process.env.SERVER_PORT;
const user = process.env.USER;
const obj = process.env.OBJ;
const boolean = process.env.BOOL;
const number = process.env.NUM;
const string = process.env.STRING;
const null1 = process.env.NULL;
const undefined1 = process.env.UNDEFINED;
const array = process.env.ARRAY;

console.log(url);
console.log(apiKey);
console.log(port);
console.log(user); //lol, this one seems to return the name of pc owners.
console.log(obj);
console.log(number);
console.log(string);
console.log(boolean);
console.log(null1 == null ? true : false);
console.log(array);

```

What if you need this environment variables in multiple places? If you do reference the variables everywhere that you need them it could make refactoring and maintenance more difficult than if they are in one place. 

#### &nbsp; You can use a Javascript config file to get around this.

```
//config.js

require('dotenv').config();

module.exports = {
    url : process.env.BASE_URL,
    apiKey : process.env.API_KEY,
    port : process.env.SERVER_PORT,
    user : process.env.USER,
    obj : process.env.OBJ,
    boolean : process.env.BOOL,
    number : process.env.NUM,
    string : process.env.STRING,
    null1 : process.env.NULL,
    undefined1 : process.env.UNDEFINED,
    array : process.env.ARRAY
};

```

Now you can import this configs from any place in your code.

```
//index.js, doSomething.js, anotherJsFile.js, etc

const configs = require('/path/to/js/config/file');

console.log(configs.url);
console.log(configs.apiKey);
console.log(configs.user);
console.log(configs.obj);

```
##### What’s the value in this technique?

- it is easy
- clarity on how all environment variables are being mapped
- you can rename variables to more readable properties
- you can add other configuration properties from non-environment variables

## &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; OR

```
//config.js

const dotenv = require('dotenv');
const result = dotenv.config();

if (result.error) {
  throw result.error;
}

const { parsed: envs } = result; 

module.exports = envs;

```

```
//index.js, doSomething.js, anotherJsFile.js, etc

const { url, apiKey, port, user, obj } = require('/path/to/js/config/file');

console.log(url);
console.log(apiKey);
console.log(user);
console.log(obj);

```
## &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; OR

Dotenv has the option of preloading the environment variables outside your code. Preload your variables and eliminate the code that reads the .env file from your code. Less code is fewer lines that could break or be maintained.
![alt text](https://imgflip.com/s/meme/Roll-Safe-Think-About-It.jpg)

This technique removes any need for code that uses require on dotenv. This includes the ``` dotenv.config()``` or  ``` require('dotenv').config() ``` code mentioned previously in this article. You can run your node app using the — require ( -r ) command line option to preload dotenv. The following command will preload all environment variables from the file .env using dotenv and make them available in your app.


```
node -r dotenv/config server.js

```
Now you can access all environment variables in the .env without requiring dotenv in your code, use  ```process.env.NAME_OF_VARAIBLE``` to access the variables.

## Best practices

> Be careful to add .env to your .gitignore file and commit that change before you add your .env. Otherwise, you run the risk of committing an early version of your .env to source control.

```
//.gitignore

.env

```

## Resources 

https://www.npmjs.com/package/dotenv

https://medium.com/chingu/an-introduction-to-environment-variables-and-how-to-use-them-f602f66d15fa

https://medium.com/chingu/protect-application-assets-how-to-secure-your-secrets-a4165550c5fb