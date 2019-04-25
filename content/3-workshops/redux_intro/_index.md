---
title: Basic introduction to Redux
---

## Redux is

- marketed as a state managment tool. It can be used to manage state an a whole lot more
- usually used with React or other frontend web framework
- concepts are similar to the Command Pattern. This is an OOP design pattern that unlocks a lot of stuff beyond simple state managment

## Resources

The basics:

- This tutorial is really good: https://redux.js.org/basics/basic-tutorial
- This logger middleware helps: https://github.com/LogRocket/redux-logger

If you want to start using redux with asyncronous code (eg ajax requests) then you'll need to use another tool:

- for simple stuff: https://github.com/reduxjs/redux-thunk
- for complicated side-effect models something like this is probably better: https://github.com/redux-saga/redux-saga

## Concepts

There are a few concepts that are super important

### Store

Lets say you are making a TODO application. This application has a beautiful frontend that automatically renders your todo items from a datastructure. Something like this:

```
const store = {
    todos : [
        {title: "get groceries", done: false},
        {title: "call mom", done: true},
        {title: "learn Redux", done: false},
        {title: "walk dog", done: false},
    ]
}
```

In redux, the store is _immutable_. We'll see what that implies when we talk about _reducers_ a little later.

Tools like React make it easy to take an application state and turn it into widgets but we wont get into that just yet. You can do this with pure vanilla JavaScript by looping over our todos and simply appending DOM elements.

### Action

An action is also a JSON object. Here are some examples:

```
{type: "ADD_TODO", title: "pay rent"}

{type: "DELETE_TODO", index: 2}

{type: "SET_DONE", index: 1, done: true}

{type: "SET_DONE", index: 1, done: false}

```

Given the example "store" we set up above can you see what effects these actions should have? What does it look like we are trying to do here?

Now there is some weird language around this. If you want Redux to execute an action then you _dispatch_ the action. Then Redux should update the _store_ through use of a _reducer_ (we'll get to those soon).

So if we wanted Redux to actually add a thing to our todo list we would do something like:

```
dispatch({type: "ADD_TODO", title: "pay rent"})
```

This is kinda a pain to write out so usually instead of doing thigs like this we make use of action creators. Eg:

```
const ADD_TODO = "ADD_TODO"

function addTodo(title){ //action creator
    // validation maybe
    return {type: ADD_TODO, title: title}
}


dispatch(addTodo("learn redux"))
```

### Reducer

Reducers are the things that execute actions on the state. Here is an example following from the above:

```
const initialState = {  // note the use of const. This is immutable
    todos : [1,2,3],
    stuff : "things"
}

function theReducer(state = initialState, action){
    // {type: ADD_TODO, title: "buy hats"}
    switch(action.type){
        case ADD_TODO:
            return {
                ...state,  // we copy all the things using some ES6 syntax
                todos: [...state.todos, {title: action.title, done:false }]
            }

            // {
            //    todos : [1,2,3,{type: ADD_TODO, title: "buy hats"}],
            //    stuff : "things"
            //}

        case DELETE_TODO:
            return { stuff }

        case SET_DONE:
            return { otherStuff }

        default:
            // nothing changes
            return state
    }
}
```

## A helloworld example

We are using ES6 syntax

## But what about KISS?

KISS == Keep It Simple, Stupid

This does seem like a complicated way to do a simple thing... Think about this:

- actions are objects. That means we can store them and track them in different ways.
- actions are executed in specific ways and have predictable results
- the hard "thinking" of your application is all held in reducers so that makes testing easy and consistent
- we have a history of every hange made to the state of an application

Look up the "Command Pattern" . Redux isn't exactly the same but very similar. Therefore there are similar applications.

- Frontend development: different buttons, inputsand widgets dispatch different actions in a predictable way
- Actions can be grouped. Meaning we can dispatch one action that dispatches a whole lot of different actions
- Macro recording. We can record the actions a user takes so that we can replay them later
- Reducers can be in a seperate code-base. we can send actions over a network and dispatch them elsewhere, we can send the same action to multiple computers to allow parallel processing
- undo/redo functionality becomes trivial
- feedback: if a number of actions need to be completed in order to complete a large task then we can track the completion of those actions and update a progress bar
- Actions can be added to a task queue instead of being dispatched immediately
- transactional behavior: you can have an action like {type: TRANSACTION_BEGIN} and then at some later stage {type: TRANSACTION_ROLLBACK} can be used to undo all the changes that happened in the transaction

## Industry

Redux is mostly used in the context of React. It is used for frontend development. But there is so much more it could do.
