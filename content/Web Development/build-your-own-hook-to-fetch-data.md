Title: Build Your Own Hook To Access RESTful API
Tags: reactjs, hooks, javascript, typescript
Category: Web Development
Date: 2020-03-22 21:11
Slug: build-your-own-hook-to-access-restful-api
comment_id: bojwct7uay65-build-your-own-hook-to-access-restful-api
Subtitle:
Summary: This tutorial shows how to create custom hooks and then how to use the hooks to connect with RESTful servers and make REST requests.
Keywords:

Hooks are a transformative feature introduced in [Release 16.8.0](https://github.com/facebook/react/blob/master/CHANGELOG.md#1680-february-6-2019) of [React](https://reactjs.org/). Besides the builtin hooks, [you can create your own hooks](https://reactjs.org/docs/hooks-custom.html).

In this article, I am going to show you how you can build your own hooks and then, how can you use your custom hooks to fetch data. I am going to use [Create React App](https://create-react-app.dev/) and [TypeScript](https://www.typescriptlang.org/) in the following examples.

## What is a hook

A hook is nothing but a function. There is no mystery to it. It does not have any specific signature or declaration. It can take any number of arguments and can return any amount or type of values. You decide. React does not impose any requirement on you.

There is one requirement, though. A hook name should always start with `use`. For example, `useGetUserInfo` is a valid hook name. `getUserInfo` is _not_ a valid hook name.

Simply, a hook is a function whose name starts with `use`.

## Create your own hook

Let's put this to test.

Create a React project.

```bash
yarn create react-app my-app --template typescript
```

Edit `src/App.tsx`.

```typescript
const useGetMessage = (): string => {
  return "Hello World";
};

const App = () => {
  const mesg = useGetMessage();
  return <div className="App">{mesg}</div>;
};
```

In this example, I created a hook `useGetMessage`. It does not take any argument and returns a string.

I agree that it is useless, and a simple function would have sufficed. I am only making a point that _a hook is merely a function_.

## A hook that takes an argument

Let's create another hook that can take value.

```typescript
const useGetSquare = (num: number): number => {
  return num * num;
};

const App = () => {
  const square = useGetSquare(2);
  return <div className="App">{square}</div>;
};
```

Pretty simple, right?

Here we got square of the number 2 only. What if I want to get square of 3 and 4 too? Can we do this?

```typescript
const App = () => {
  return (
    <div className="App">
      {useGetSquare(2)} {useGetSquare(3)} {useGetSquare(4)}
    </div>
  );
};
```

## A hook that uses other hooks

Let's create a hook that we will use to keep track of a button click count.

Here is a naive and incorrect implementation.

```typescript
// incorrect example
const useButtonClicked = (): number => {
  let count = 0;
  count++;
  return count;
};

const App = () => {
  const count = useButtonClicked();
  const onButtonClick = () => {
    useButtonClicked();
  };
  return (
    <div className="App">
      <button onClick={onButtonClick}>Click Me</button>
      <h2>{count}</h2>
    </div>
  );
};
```

This code has some issues.

How do we increment the count inside `useButtonClicked` hook? Calling the hook from inside the `onButtonClick` method will only reset the `count` to zero.

More importantly, you can call a hook only inside a React component. `onButtonClick` is not a React component. This warning from `rules-of-hooks` explains it.

> Line 12:32: React Hook "useButtonClicked" is called in function "onButtonClick" which is neither a React function component or a custom React Hook function react-hooks/rules-of-hooks

Clearly, our approach is wrong.

We can return a method from `useButtonClicked` hook, say, `incrementCount`. Then the component can call `incrementCount` to increase the count inside the hook.

```typescript
// incorrect example
const useButtonClicked = (): [number, () => void] => {
  let count = 0;
  const incrementCount = () => {
    count++;
  };
  return [count, incrementCount];
};
```

Notice that we use an array to return the two values.

A component can use this hook like this,

```typescript
const App = () => {
  const [count, incrementCount] = useButtonClicked();
  const onButtonClick = () => {
    incrementCount();
  };

  return (
    <div className="App">
      <button onClick={onButtonClick}>Click Me</button>
      <h2>{count}</h2>
    </div>
  );
};
```

This code fixes the `rules-of-hooks` warning. But it too does not work correctly. The `count` on screen does not increase on clicking the button.

![Clicking on button does not increase the count](/images/build-your-own-hook-to-use-restful-api-button-zero.png)

If you add a `console.log` statement inside `incrementCount` to view the value of count, you will observe the `incrementCount` increases the value of `count` correctly. It is a JavaScript closure, and it has access to the `count` variable.

Unfortunately, inside the component, the `count` value is stale. It is initialized when we call `useButtonClicked`.

```typescript
const [count, incrementCount] = useButtonClicked();
```

After this initialization, this value is never updated.

The simplest solution to this issue is to use the React's `useState` hook. React team has fixed the stale value in `useState` hook. Whenever a value is updated, the component automatically gets the updated value.

In this example, we use `useState` hook inside our custom `useButtonClicked` hook.

```typescript
const useButtonClicked = (): [number, () => void] => {
  const [value, setValue] = React.useState(0);
  const incrementCount = () => {
    setValue(value + 1);
  };
  return [value, incrementCount];
};
```

This fixes the issue, and the hook works correctly.

![Result of clicking the button six times](/images/build-your-own-hook-to-use-restful-api-button-six.png)

Currently, the hook increments the count by one. Let's modify the hook so that component can decide the increment value. It requires very little change.

```typescript
const useButtonClicked = (increaseBy = 1): [number, () => void] => {
  const [value, setValue] = React.useState(0);
  const incrementCount = () => {
    setValue(value + increaseBy);
  };
  return [value, incrementCount];
};

const App = () => {
  const [count, incrementCount] = useButtonClicked(2);
...
```

The count starts from 0, then 2, then 4, and so on.

![Result of clicking the button four times](/images/build-your-own-hook-to-use-restful-api-button-eight.png)

Modify the hook so that count can start from any number the component provides, instead of just 0.

```typescript
const useButtonClicked = (increaseBy = 1, initialValue = 0): [number, () => void] => {
  const [value, setValue] = React.useState(initialValue);
...
const App = () => {
  const [count, incrementCount] = useButtonClicked(2, 10);
```

![Initial value 10 is displayed without clicking any button](/images/build-your-own-hook-to-use-restful-api-button-ten.png)

## Use a custom hook to make `GET` requests

So far, we have learned that hooks are functions. We can use a function inside another function, precisely the same way, we can use hooks inside other hooks. We can pass parameters to it, and use the return value in the components.

It is also clear to do anything non-trivial inside a custom hook, you have to use React's predefined hooks.

Armed with this knowledge, we will make a hook that will fetch user information from [Reqres](https://reqres.in/) using [`fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch).

A request can have three states,

1. it has started and is waiting for server response
1. it has successfully completed
1. it has failed

It is appropriate to use [`useReducer` hook](https://reactjs.org/docs/hooks-reference.html#usereducer) in our custom hook, instead of `useState` hook. You can read this article, ["When to use `useState` vs `useReducer` hook in React"](https://www.oncrashreboot.com/when-to-use-usestate-vs-usereducer-hook-in-react), to better understand the rationale.

### `useGetInformation` definition

In the following lines, we will define a `useGetInformation`. Consumers of the hook will pass a user ID to it. It, in turn, will return the user information, and request status, like the request is in process, or the request has failed.

The interface of the JSON object that the server will send to the hook.

```typescript
interface Info {
  id: number;
  emai: string;
  first_name: string;
  last_name: string;
  avatar: string;
}
```

Interface for the actions that the hook can perform.

```typescript
type HookAction =
  | { type: "fetching" }
  | { type: "success"; payload: Info }
  | { type: "error" };
```

Interface for the state of the hook.

```typescript
interface HookState {
  isFetching: boolean;
  isSuccessful: boolean;
  errorMessage: string;
  result: Info | null;
}
```

The default state of the hook.

```typescript
const hookInitialState: HookState = {
  isFetching: false,
  isSuccessful: false,
  errorMessage: "",
  result: null
};
```

Reducer function to update the state.

```typescript
const hookReducer = (state: HookState, action: HookAction): HookState => {
  switch (action.type) {
    case "fetching":
      return {
        ...state,
        isFetching: true,
        isSuccessful: false,
        errorMessage: "",
        result: null
      };

    case "success":
      return {
        ...state,
        isFetching: false,
        isSuccessful: true,
        result: { ...action.payload }
      };

    case "error":
      return {
        ...state,
        isFetching: false,
        isSuccessful: false,
        errorMessage: "User not found"
      };
  }
};
```

Now that we have the state, actions and a reducer, we code the hook `useGetInformation`.

    #!typescript
    const useGetInformation = (): [HookState, (id: number) => void] => {
      const [fetchState, dispatch] = React.useReducer(
        hookReducer,
        hookInitialState
      );

      const fetchInfo = (id: number) => {
        fetch(`https://reqres.in/api/users/${id}?delay=5`)
          .then(response =>
            response.status === 200
              ? Promise.resolve(response.json())
              : Promise.reject(response.status)
          )
          .then(data => {
            dispatch({
              type: "success",
              payload: { ...data.data }
            });
          })
          .catch(err => {
            dispatch({ type: "error" });
          });
      };

      const getInfoForId = (id: number) => {
        dispatch({ type: "fetching" });
        fetchInfo(id);
      };

      return [fetchState, getInfoForId];
    };

In lines, 2-5, we use React's builtin hook `useReducer`. We pass it the reducer and the default state. It returns `fetchState` and `dispatch`. The hook does not need `fetchState`, but it will expose it for the hook users. Hook users will read the value of `fetchState` and update their component. `useGetInformation` hook uses `dispatch` to update the state.

Lines 7-23 has the definition of `fetchInfo`. This method fetches user information from [Reqres](https://reqres.in/) and dispatches actions when the request fails or succeeds.

Lines 25-28 has the method `getInfoForId`. Users of the hook will use this method to pass the user ID. As soon as the ID is received, `getInfoForId` will call fetchInfo which will kick start the fetch process.

In the last line of the hook definition, 30, we return `fetchState` and `getInfoForId`.

### Example usage of `useGetInformation`

We will define a component, that will use the `useGetInformation`.

```typescript
const App = () => {
  const [
    { result, isSuccessful, isFetching, errorMessage },
    getInfoForId
  ] = useGetInformation();

  const onButtonClicked = () => {
    getInfoForId(1);
  };

  return (
    <div className="App">
      {isSuccessful && !isFetching && result && (
        <h2>First Name: {result.first_name}</h2>
      )}
      {!isSuccessful && !isFetching && errorMessage.length > 0 && (
        <h2>Error: {errorMessage}</h2>
      )}
      {isFetching && <h3>Please Wait</h3>}

      <button onClick={onButtonClicked} disabled={isFetching}>
        Get User 1 Info
      </button>
    </div>
  );
};
```

This is a simple component.

It destructures the `fetchState` returned from the `useGetInformation` hook into `{ result, isSuccessful, isFetching, errorMessage }`.

It shows the name of the user from the result, an error message in case of error, and a "Please wait" message when the request is in process.

The button is disabled when the request is in process. When the button is clicked, it passes user ID `1` to the hook.

![Please wait message while user info is fetched](/images/build-your-own-hook-to-use-restful-api-single-button-please-wait.png)![Display first name of user](/images/build-your-own-hook-to-use-restful-api-single-button-user-info.png)

Let's add two more buttons.

```typescript
  const onButton1Clicked = () => {
    getInfoForId(1);
  };

  const onButton2Clicked = () => {
    getInfoForId(2);
  };

  const onButton3Clicked = () => {
  // User with ID 100 is not present
    getInfoForId(100);
  };
...
      <button onClick={onButton1Clicked} disabled={isFetching}>
        Get User 1 Info
      </button>
      <button onClick={onButton2Clicked} disabled={isFetching}>
        Get User 2 Info
      </button>
      <button onClick={onButton3Clicked} disabled={isFetching}>
        Get Invalid User Info
      </button>
```

This is the result of clicking on the "Get Invalid User Info" button.

![Error message when an invalid user ID is passed](/images/build-your-own-hook-to-use-restful-api-three-button-error-message.png)

You can play with this code in the sandbox at [this link](https://codesandbox.io/s/relaxed-ganguly-m9prg){.ampl}.

## Wrapping up

In this tutorial, we have learned how to create custom hooks, and then we used this knowledge to create a hook that does `GET` requests to a RESTful API server. We can make similar hooks for `POST`, `PATCH` and `DELETE` requests.
