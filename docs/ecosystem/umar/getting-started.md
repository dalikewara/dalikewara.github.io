---
sidebar_position: 2
slug: /docs/umar/getting-started
description: This page contains introductory information to help you get started with Umar
keywords: [umar, tools, ecosystem, linux, application, getting started]
---

# Getting Started

Before using Umar, please check your OS first. Umar was created for Linux systems, especially Arch Linux.
I highly recommend running Umar on that system.

:::warning
Although it might work on other Linux distros, macOS, or Windows WSL, I have not tested Umar extensively on those platforms.
I once tested it on Fedora 42 and Ubuntu 24.04—some commands worked, some didn’t. So, be careful when using it.
:::

:::danger
Umar doesn’t work on Windows CLI systems (such as PowerShell or Command Prompt).
:::

:::danger
If you’re not sure about what you’re doing, please don’t proceed.
:::

:::tip
If you really want to understand what Umar does, you can
always check the source code through the commands `umar r` or `umar p`. This might give you more confidence to use it next time.
:::

## Installation🔌

To install Umar, run the following command:

```bash
curl -L https://dalikewara.com/umar/install.sh | sh
```

> If the `install.sh` URL above doesn’t work, you can use this URL instead: `https://raw.githubusercontent.com/dalikewara/umar/master/install.sh`.

### Upgrade

If you already have Umar installed, simply run the following command to upgrade to the latest version:

```bash
umar u
```

## Usage 🕹

Just run this command:

```bash
umar
```

It will list all available commands you can use.
