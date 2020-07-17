---
Title: What Happend to My First PHP Framework?
Date: 2020-05-01 18:54
Tags: php, module, project, open source, framework
Description: It has been long time since I published my first PHP framework `Janggelan` on GitHub. The framework was built from scratch with a core system structure inspired by Laravel and designed based on MVC concept. The goal is basicly have the framework easy to use without reducing its performance.
cover_image: https://media.giphy.com/media/uVtAU2EKHrsgifowFb/giphy.gif
---

![confusing](https://media.giphy.com/media/uVtAU2EKHrsgifowFb/giphy.gif)
*Photo by [Bounce](https://giphy.com/gifs/Bounce-TV-confused-say-what-baffled-uVtAU2EKHrsgifowFb) on [Giphy](https://giphy.com/search/confusing)*

It has been long time since I published my first PHP framework `Janggelan` on GitHub. The framework was built from scratch with a core system structure inspired by Laravel and designed based on MVC concept. The goal is basicly have the framework easy to use without reducing its performance.

As simple as making route like this:

```php
$this->request('POST /print-hello-world @Hello::world');
```

`janggelan` gives a quick access to **controller** and its **methods**. Route `/print-hello-world` on the example above will run the `world` method in the `Hello` controller.

Every framework comes with security mechanism built through inside of it. `janggelan` also provides it by giving **protecting rule** system to protect `pages`, `views` and `urls`.

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

## So, is `Janggelan` still active?

I learned some new programming languages after I committed last update to `Janggelan`'s repository, and I didn't make any activites later on it until nowadays&mdash;or even in the future because maybe I'll not continue this project.

I love `Janggelan` so much for sure. But saddest, I don't see the reason why I have to continue `Janggelan`'s development and make it to be part of future web programming. So, yes... `Janggelan` is discontinued for now.

> You can check `janggelan`'s documentation at [https://github.com/dalikewara/janggelan](https://github.com/dalikewara/janggelan)