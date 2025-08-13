---
sidebar_position: 2
slug: /docs/uwais/getting-started
description: This page contains introductory information to help you get started with Uwais
keywords: [uwais, tools, ecosystem, application, getting started, clean architecture, project structure, feature driven design, domain driven design, design pattern]
---

import { linkCustom } from '@site/src/link.js';

# 🏃‍♂️ Getting Started

## Requirements

Before installing, make sure your system meets these requirements:

- Operating systems that support `/bin/sh` with **POSIX** standards. **Linux** and **MacOS** should work without issues as they support it by default. For **Windows** users, consider using WSL instead
- curl
- git

:::info
Currently, I am working on migrating Uwais's code from pure POSIX shell script to Rust. It will be available in the next version of Uwais, which is v2.
The new Uwais will have a different installation approach to ensure cross-platform compatibility. Don’t worry, I will keep the existing flow and mechanism
so it will be automatically compatible with the new version. If you already have an older Uwais installed, you won’t need to do anything except upgrade to
the latest version.
:::

## Installation 🔌

To install Uwais, run the following command:

```bash
curl --proto '=https' --tlsv1.2 -L https://dalikewara.com/uwais/install.sh | sh
```

> If the `install.sh` URL above doesn’t work, you can use this URL instead: `https://raw.githubusercontent.com/dalikewara/uwais/master/install.sh`.

:::tip
If you’re concerned about safety and security, you can download the {linkCustom('install.sh', 'https://dalikewara.com/uwais/install.sh')} file first and execute it manually.
Or, you can view the `install.sh` source code at {linkCustom('https://raw.githubusercontent.com/dalikewara/uwais/master/install.sh', 'https://raw.githubusercontent.com/dalikewara/uwais/master/install.sh')}.
:::

### Upgrade

If you already have Uwais installed, simply run the following command to upgrade to the latest version:

```bash
uwais update
```

## Usage 🕹

Just run this command:

```bash
uwais
```

It will list all available commands you can use.
