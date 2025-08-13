---
sidebar_position: 1
slug: /docs/umar/what-is
description: This page contains information about what Umar is
keywords: [umar, tools, ecosystem, linux, application]
---

import { symbol } from '@site/src/symbol.js';
import { link } from '@site/src/link';

# What Is Umar? 🤔

Umar is a collection of CLI commands I initially created to help me do various Linux tasks{symbol.mdash}I consider it a little Linux assistant.
Most of the time, I work on my personal laptop running Linux. It’s an OS where you’ll often deal with configuration and settings through the CLI.
At some point, I realized I was using the same commands repeatedly. Sometimes these commands weren’t simple; they needed to be chained together with
multiple other commands. So, I decided to create a tool to make those tasks easier.

:::info
Not all my needs are covered by Umar yet, as it’s still being updated every day. Whenever I find something that should be reusable,
I add it to Umar.
:::

At the moment, I have tested Umar only on Arch Linux{symbol.mdash}because that’s what I use. I think it might also work on other distros,
but I’m not entirely sure. If you look at Umar’s source code, you’ll notice that some commands are written to be compatible with other distros,
but I haven’t tested them all.

You may also notice that some Umar commands are related to MacBook devices. That’s because I currently use a MacBook Pro 2017 13-inch with Arch Linux
as my main daily OS. These commands help me configure my MacBook to work seamlessly with Arch Linux.

## Repo & License

Umar is licensed under the {link('mit')}, and its repository is available on {link('umarrepo')}.

```text
MIT License

Copyright (c) 2024 Dali Kewara

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
