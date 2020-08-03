---
title: Intro to Redux for home automation
available_flavours:
  - javascript
  - typescript
content_type: project
ready: true
prerequisites:
  hard:
    - topics/redux-intro
submission_type: repo
tags:
  - redux
  - thunks
  - combineReducers
---

Redux is generally explained in the context of frontend frameworks. Lots of people think that it is a React thing. Lots of people are wrong... Redux is quite a versatile tool. It can even be used in the absence of a frontend.

In this project we'll be thinking about how we could use redux for a little bit of Internet of things home automation. Fo shizzle. It's that awesome.

Once you have these foundations out of the way you can move onto integrating redux into a frontend. But let's get the foundations out of the way first.

## Instructions

### The basics

Take a little time to google IoT home automation and come up with a list of things you might want to automate in your home once you are a wealthy and successful professional coder. Arrange all the different things you might want to automate into a state object. Here's an example:

```
state = {
    loungeLighting: "dim",
    discoBallOn: true,
    alarmClockTime : "07:00",
    nowPlaying: "https://www.youtube.com/watch?v=oHg5SJYRHA0",

}
```

Ok, run with it a little bit. What other things would you want to control?

The next step is to try to figure out what actions a user could take in order to update the state, and then to create some action creators for those.

Eg:

```
function setNowPlaying(videoLink){
    return {
        type: SET_NOW_PLAYING,
        videoLink
    }
}
```

Now implement your reducers.

Make sure you can dispatch your actions in order to update the state.

Once you have this down. it would probably be wise to make a PR. Rapid feedback for the win!

### Combine Reducers

Often Redux is tied to pretty complicated applications. There are often many pages, widgets and whatnots that need to be controlled. As things get complicated your reducer can get really really big.

That's why redux has a thing called CombineReducers, it lets you split things up a bit.

Create a few seperate reducers to control different things. You could have a sperate reducer per room, or you could have a sperate reducer for each major function (eg: you could have a "lighting" reducer that controls the lights for the whole house).

Demonstrate your understanding of combineReducers.

This would be a good time to make another PR.

### Thunks

Now one super cool thing about redux is that you dont really have to dispatch actions one at a time. You can have an action with side effects, and those side effects can dispatch other actions!

There are two main ways to handle side effects in redux. Thunks and Sagas. Thunks are the easy way, and they are worth understanding before movin onto sagas.

Your mission is to create a few more actions that use Thunks to combine a few of your existing actions. For example you might have an action with type `GOOD_MORNING` that starts playing soothing morning tunes and turns the kettle on. You might have another action of type `PARTY_MODE` that dimms the lights, turns on the disco ball, and changes the volume of the door bell.

What combinations of actions would you want to trigger?

## Did you know?

Did you know Tilde uses Redux? Open up the developer console (F12 usually) and you'll be able to see how your interactions dispatch actions and update the state. Most of the state looks quite intense, look for `Entities` inside the state and see if you can recognise what's going on in there and how it relates to what you are seeing on your board.
