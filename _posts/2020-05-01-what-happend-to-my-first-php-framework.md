---
layout: post
title: What Happend to My First PHP Framework?
description: It has been long time since I published my first PHP framework `Janggelan` on GitHub. The framework was built from scratch with a core system structure inspired by Laravel and designed based on MVC concept. The goal is basicly have the framework easy to use without reducing its performance
---

## Overview

It has been long time since I published my first PHP
framework Janggelan on GitHub. The framework was
built from scratch with a core system structure
inspired by Laravel and designed based on MVC
concept. The goal is basically have the framework
easy to use without reducing its performance. As simple
as making route like this:

```php
$this->request('POST /print-hello-world @Hello::world');
```

Janggelan gives quick access to controller and its
methods. Route `/print-hello-world` on the example
above will run the world method in the `Hello` controller.
Every framework comes with security mechanism
built through inside it. Janggelan also provides
it by giving protecting rule system to protect
pages, views and urls.

```php
<?php return [

    // FALSE means, system will uses SESSION to store protected_rule data. Set it TRUE
    // if you want to store the data in COOKIE.
    'use_cookie' => FALSE,

    'protected_rule' => [

        // Creating 'Protected Rule' with name 'login'.
        // If the data is not valid, then redirect to Controller 'Example'
        // method 'protected.'
        'login' => [
            'on_false' => [
                'controller' => 'Example',
                'method' => 'protected'
            ],
        ],

        // Creating 'Protected Rule' with name 'protect'.
        // If the data is not valid, then redirect to View 'example'.
        'protect' => [
            'on_false' => [
                'view' => 'example',
            ],
        ],

        // Creating 'Protected Rule' with name 'myRule'.
        // If the data is not valid, then redirect to uri '/wrong'.
        'myRule' => [
            'on_false' => '/wrong'
        ],

    ]
];
```

## So, is Janggelan still active?

I learned some new programming languages after I
committed last update to Janggelan‘s repository,
and I didn’t make any activities later on it until
nowadays—or even in the future because maybe
I’ll not continue this project. I love Janggelan so
much for sure. But saddest, I don’t see the reason
why I have to continue Janggelan‘s development
and make it to be part of future web programming.
So, yes… Janggelan is discontinued for now.

> You can check Janggelan‘s documentation at [here](https://github.com/dalikewara/janggelan).