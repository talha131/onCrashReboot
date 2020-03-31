Title: Conditional Spread Syntax In JavaScript
Tags: javascript, tip,
Category: Web Development
Date: 2020-03-31 10:00
Slug: conditional-spread-syntax-in-javascript
comment_id: ae9irtbcsq3w-conditional-spread-syntax-in-javascript
Subtitle:
Summary: Spread operator is a powerful feature of JavaScript. In this article, I explain the idiomatic style of applying this operator conditionally.
Keywords:

[Spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax), in JavaScript, lets you expand arrays, objects and even strings succinctly. It is one of the features in JavaScript that I miss the most when working in other programming languages.

In this article, I will show how you can expand any JavaScript literal **conditionally**.

## Conditionally expand an object

Idiomatic syntax is

```javascript
{ ...(condition && object) }
```

### Explanation

Consider these two objects

```javascript
const obj1 = { isDev: true };
const obj2 = { name: "Talha", user: "talha131" };
```

You can merge them together like so,

```javascript
const objMerged = { ...obj1, ...obj2 };
```

Say I add a boolean variable `expand`. `obj2` should be expanded only when `expand` is true.

```javascript
let expand = true;
let objMerged = { ...obj1, ...(expand && obj2) };
```

`objMerged` value is

```json
{
  "isDev": true,
  "name": "Talha",
  "user": "talha131"
}
```

Try false.

```javascript
expand = false;
objMerged = { ...obj1, ...(expand && obj2) };
```

`objMerged` value is

```json
{
  "isDev": true
}
```

## Conditionally expand a string to an object

Idiomatic syntax is

```javascript
[...(condition && string)];
```

### Explanation

When you apply the spread operator on a string inside `{}`, it returns an object.

```javascript
const str = "abc";
const eg = { ...str };
```

`eg` value is

```json
{
  0: "a",
  1: "b",
  2: "c"
}
```

Therefore, you can use the same syntax that you use for conditionally expanding an object.

```javascript
expand = false;
let expandedStr = { ...(expand && str) };
```

## Conditionally expand an array

Idiomatic syntax is

```javascript
[...(condition ? array : [])];
```

### Explanation

Consider these two arrays

```javascript
const arr1 = [1, 3, 5];
const arr2 = [2, 4, 6];
```

You can merged these arrays like this,

```javascript
const arrayMerged = [...arr1, ...arr2];
```

Say I add a boolean variable `expand`. `arr2` should be expanded only when `expand` is true.

```javascript
let expand = true;
const arrayMerged = [...arr1, ...(expand && arr2)];
```

Unfortunately, **this will not work** if condition, `expand`, is false. You will get the error.

> error: TypeError: false is not iterable

The reason is in case of array and string, the `...` operator requires an iterable. When the condition is false, the `()` expression is empty, in turn, the `...` operator complains, "Where is my iterable?"

Therefore, the correct syntax is

```javascript
const arrayMerged = [...arr1, ...(expand ? arr2 : [])];
```

The ternary operator provides an empty array for the failing case.

## Conditionally expand a string to an array

Idiomatic syntax is

```javascript
[...(condition ? string : [])];
```

### Explanation

When you apply the spread operator on a string inside `[]`, it returns an array.

```javascript
const str = "abc";
const eg = [...str];
```

Value of `eg` is `[ "a" , "b" , "c" ]`.

Therefore, just like an array, if you try to use logical and operator `&&`, you will get the error.

```javascript
// incorrect
const eg = [...(false && "hello")];
```

The correct syntax is

```javascript
expand = false;
let expandedStr = [...(expand ? str : [])];
```

Here `expandedStr` will evaluate to an empty array `[]`.

## Warp Up

You can see a working examples and run them at [this link](https://playcode.io/533547).

```javascript
// Objects

const obj1 = { isDev: true };
const obj2 = { name: "Talha", user: "talha131" };

let expand = true;
let objMerged = { ...obj1, ...(expand && obj2) };
console.log("Expand Objects true");
console.log(objMerged);

expand = false;
objMerged = { ...obj1, ...(expand && obj2) };
console.log("Expand Objects false");
console.log(objMerged);

// Arrays

const arr1 = [1, 3, 5];
const arr2 = [2, 4, 6];

expand = true;
let arrayMerged = [...arr1, ...(expand ? arr2 : [])];
console.log("Expand Arrays true");
console.log(arrayMerged);

expand = false;
arrayMerged = [...arr1, ...(expand ? arr2 : [])];
console.log("Expand Arrays false");
console.log(arrayMerged);

// String to array

const str = "abc";

expand = true;
let expandedStr = [...(expand ? str : [])];
console.log("Expand string to array true");
console.log(expandedStr);

expand = false;
expandedStr = [...(expand ? str : [])];
console.log("Expand string to array false");
console.log(expandedStr);

// String to object

expand = true;
expandedStr = { ...(expand && str) };
console.log("Expand string to object true");
console.log(expandedStr);

expand = false;
expandedStr = { ...(expand && str) };
console.log("Expand string to object false");
console.log(expandedStr);
```

It's output is

```shell
Expand Objects true
{
  isDev: true ,
  name: "Talha" ,
  user: "talha131"
}

Expand Objects false
{
  isDev: true
}

Expand Arrays true
[ 1, 3, 5, 2, 4, 6 ]

Expand Arrays false
[ 1, 3, 5 ]

Expand string to array true
[ "a", "b", "c" ]

Expand string to array false
[ ]

Expand string to object true
{
  0: "a" ,
  1: "b" ,
  2: "c"
}

Expand string to object false
{ }
```
