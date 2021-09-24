---
title: vcmrefunc
description: The right way to repeat a process
author: Dali Kewara
date: 2021-09-24 12:12:44
---

[![npm package](https://nodei.co/npm/vcmrefunc.png?downloads=true&downloadRank=true&stars=true)](https://nodei.co/npm/vcmrefunc/)

[![version](https://img.shields.io/npm/v/vcmrefunc.svg?style=flat)](https://img.shields.io/npm/v/vcmrefunc.svg?style=flat)
[![build](https://img.shields.io/circleci/project/github/dalikewara/vcmrefunc.svg?style=flat)](https://img.shields.io/circleci/project/github/dalikewara/vcmrefunc.svg?style=flat)
[![language](https://img.shields.io/github/languages/top/dalikewara/vcmrefunc.svg?style=flat)](https://img.shields.io/github/languages/top/dalikewara/vcmrefunc.svg?style=flat)
[![download](https://img.shields.io/npm/dt/vcmrefunc.svg?style=flat)](https://img.shields.io/npm/dt/vcmrefunc.svg?style=flat)
[![dependents](https://img.shields.io/librariesio/dependents/npm/vcmrefunc.svg?style=flat)](https://img.shields.io/librariesio/dependents/npm/vcmrefunc.svg?style=flat)
[![issue](https://img.shields.io/github/issues/dalikewara/vcmrefunc.svg?style=flat)](https://img.shields.io/github/issues/dalikewara/vcmrefunc.svg?style=flat)
[![last_commit](https://img.shields.io/github/last-commit/dalikewara/vcmrefunc.svg?style=flat)](https://img.shields.io/github/last-commit/dalikewara/vcmrefunc.svg?style=flat)
[![license](https://img.shields.io/npm/l/vcmrefunc.svg?style=flat)](https://img.shields.io/npm/l/vcmrefunc.svg?style=flat)

# The right way to repeat a process

This module helps you to repeat a process again after it completely executed. You can specify a condition to stop the repetition immediately by giving a command `repeat(false)` inside the `repeat_function`. Also, there is an option to pass a callback that will be executed after the repetition is finished.

This is simple, easy to use, and clean code.

## Installation
NPM

```bash
npm install vcmrefunc --save
```

Browser

```bash
bower install vcmrefunc --save
```

## Initialization
NPM

```javascript
const vcmrefunc = require('vcmrefunc');
```

Browser

```html
<script src="bower_components/vcmrefunc/dist/vcmrefunc.min.js"></script>
```

## Quickstart

```javascript
vcmrefunc(delay, repeat_function, callback[optional]);
```

- Arguments
  - *number* **delay**
    - *default* 0 | miliseconds | 0 = means has no delay
  - *function* **repeat_function**
    - Has an argument `repeat`
      - *function* **repeat** [required]
  - *function* **callback** [optional]

## Usage

Here is the basic usage of `vcmrefunc`:

```javascript
vcmrefunc(0, (repeat) => {
  // Your logic here...

  repeat();
});
```

As you can see, the argument `repeat` on the `repeat_function` is used to repeat its process again until you decide to stop it. You can stop the repetition using `repeat(false)`. For example:

```javascript
var i = 0;

vcmrefunc(0, (repeat) => {
  console.log('Repeated ' + i);
  
  if (i == 4) return repeat(false);
  
  i++;

  repeat();
});
```

And you'll have output:

```bash
Repeated 0
Repeated 1
Repeated 2
Repeated 3
Repeated 4
```

Also, there is an option to pass a callback that will be executed after the repetition is finished. For example:

```javascript
var i = 0;

vcmrefunc(0, (repeat) => {
  console.log('Repeated ' + i);
  
  if (i == 4) return repeat(false);
  
  i++;

  repeat();
}, () => {
  console.log('End');
});
```

And the output will be:

```bash
Repeated 0
Repeated 1
Repeated 2
Repeated 3
Repeated 4
End
```

### Delay

If the `repeat_function` process would be repeated, the function will wait for a delay before it gets the process run again. Delay must be passed (in miliseconds) on first position of `vcmrefunc` arguments. Zero (0) delay means has no delay. Example:

```javascript
vcmrefunc(2000, (repeat) => {
  console.log('Repeated after 2 seconds');
  repeat();
});
```

### Working with asynchronous functions

You can do like this if you want to run asynchronous functions inside `repeat_function`:

```javascript
var myFunction = function (callback) {
  setTimeout(() => {
    console.log('This is my asynchronous function');
    callback();
  }, 2000);
};

var i = 0;

vcmrefunc(2000, (repeat) => {
  console.log('Repeated ' + i);
  
  myFunction(() => {
    if (i == 4) return repeat(false);

    i++;

    repeat();
  });
}, () => {
  console.log('end!');
});
```

Output:

```bash
Repeated 0
This is my asynchronous function
Repeated 1
This is my asynchronous function
Repeated 2
This is my asynchronous function
Repeated 3
This is my asynchronous function
Repeated 4
This is my asynchronous function
End
```

## Release

### Changelog
See [https://github.com/dalikewara/vcmrefunc/blob/master/CHANGELOG.md](https://github.com/dalikewara/vcmrefunc/blob/master/CHANGELOG.md).

### Credits
Copyright &copy; 2020 [Dali Kewara](https://www.dalikewara.com).

### License
[MIT License](https://github.com/dalikewara/vcmrefunc/blob/master/LICENSE)