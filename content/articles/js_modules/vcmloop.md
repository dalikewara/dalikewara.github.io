Title: vcmloop, Loop Massive Data With No Worry
Date: 2020-04-29 23:31
Tags: javascript, nodejs, module, project, open source

> Check out `vcmloop`'s latest documentation at [https://github.com/dalikewara/vcmloop](https://github.com/dalikewara/vcmloop)

[![npm package](https://nodei.co/npm/vcmloop.png?downloads=true&downloadRank=true&stars=true)](https://nodei.co/npm/vcmloop/)

[![version](https://img.shields.io/npm/v/vcmloop.svg?style=flat)](https://img.shields.io/npm/v/vcmloop.svg?style=flat#modulesbadges)
[![build](https://img.shields.io/circleci/project/github/dalikewara/vcmloop.svg?style=flat)](https://img.shields.io/circleci/project/github/dalikewara/vcmloop.svg?style=flat#modulesbadges)
[![language](https://img.shields.io/github/languages/top/dalikewara/vcmloop.svg?style=flat)](https://img.shields.io/github/languages/top/dalikewara/vcmloop.svg?style=flat#modulesbadges)
[![download](https://img.shields.io/npm/dt/vcmloop.svg?style=flat)](https://img.shields.io/npm/dt/vcmloop.svg?style=flat#modulesbadges)
[![dependents](https://img.shields.io/librariesio/dependents/npm/vcmloop.svg?style=flat)](https://img.shields.io/librariesio/dependents/npm/vcmloop.svg?style=flat#modulesbadges)
[![issue](https://img.shields.io/github/issues/dalikewara/vcmloop.svg?style=flat)](https://img.shields.io/github/issues/dalikewara/vcmloop.svg?style=flat#modulesbadges)
[![last_commit](https://img.shields.io/github/last-commit/dalikewara/vcmloop.svg?style=flat)](https://img.shields.io/github/last-commit/dalikewara/vcmloop.svg?style=flat#modulesbadges)
[![license](https://img.shields.io/npm/l/vcmloop.svg?style=flat)](https://img.shields.io/npm/l/vcmloop.svg?style=flat#modulesbadges)

# An interval-based looping method for massive data
Doing simple looping basicly doesn't have big impact to your RAM/CPU resource, but, it will if you performing heavy looping with massive data, for example 100k data or > 1m data.

Default looping method like `for`, `while`, `foreach` runs faster (has better performance), but also takes and spent more RAM/CPU resource continously along with the looping process&mdash;if you own more resource, I think it's not a big problem. Otherwise, using interval method doesn't harm RAM/CPU resource too much. It just uses a little bit of it and keeping the resource stable until the process is done. As a consequence, it runs slower than the default method&mdash;but still fast.

So, if you need to do looping with massive data and heavy process inside, using interval method should be a better solution.

### Installation
NPM

```bash
npm install vcmloop --save
```

Browser

```bash
// Bower
bower install vcmloop --save
```

### Initialization
NPM

```javascript
const vcmloop = require('vcmloop');
```

Browser

```html
// Bower
<script src="bower_components/vcmloop/dist/vcmloop.min.js"></script>
```

# Quickstart

```javascript
vcmloop(start, stop, fn, end[optional], delay[optional]);
```

- Arguments
  - *number* **start**
  - *number* **stop**
  - *function* **fn**
  - *function* **end** [optional]
  - *number* **delay** [optional]
    - *default* 0

Here is basic `vcmloop` usage:

```javascript
vcmloop(0, 5, (num) => {
  console.log(num);
});
```

You can pass an `end` argument to run once after the **synchronous** looping process is done.

```javascript
vcmloop(0, 5, (num) => {
  console.log(num);
}, () => {
  console.log('end');
});

// output:
// 0
// 1
// 2
// 3
// 4
// end
```

You can set duration or `delay` for interval process.

```javascript
vcmloop(0, 5, (num) => {
  console.log(num);
}, null, 200);
```

```javascript
vcmloop(0, 5, (num) => {
  console.log(num);
}, () => {
  console.log('end');
}, 200);
```

You may do this in an **asynchronous** looping process to make sure your code runs correctly:

```javascript
var len = 10;
var lenX = len - 1;
var start = 0;

vcmloop(start, len, (num) => {
  console.log(num);
  
  sampleFunction(sampleCallback => {
    if (num === lenX) return 'end';
  });
});
```

# Release

### Changelog
See [https://github.com/dalikewara/vcmloop/blob/master/CHANGELOG.md](https://github.com/dalikewara/vcmloop/blob/master/CHANGELOG.md).

### Credits
Copyright &copy; 2019 [Dali Kewara](https://www.dalikewara.com).

### License
[MIT License](https://github.com/dalikewara/vcmloop/blob/master/LICENSE)