import { createLogger } from "redux-logger";
import { createStore, applyMiddleware } from "redux";

// Actions and action creators

const UP = "UP";
export function increment() {
  return {
    type: UP
  };
}

const DOWN = "DOWN";
export function decrement() {
  return {
    type: DOWN
  };
}

// initial state and reducer

const initialState = {
  total: 0
};

function counterReducer(state = initialState, action) {
  switch (action.type) {
    case UP:
      return { total: state.total + 1 };
    case DOWN:
      return { total: state.total - 1 };
    default:
      return state;
  }
}

// create the store

const loggerMiddleware = createLogger();

export const store = createStore(
  counterReducer,
  applyMiddleware(
    loggerMiddleware // neat middleware that logs actions
  )
);
