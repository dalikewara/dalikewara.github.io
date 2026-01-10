---
title: 🏃‍♂️ Getting Started
description: This page shows the steps to get started before using Uwais
keywords: uwais, installation
---

# 🏃‍♂️ Getting Started

## Requirements

Uwais has been fully migrated to Rust starting from version `v2.0.0`. This ensures seamless compatibility with all major operating systems (Linux, Windows, macOS).

However, the legacy version is still available for download. If you specifically need to use the old version, please ensure you meet these requirements, as it was built using POSIX shell scripts:

- Operating systems that support `/bin/sh` with POSIX standards. Linux and MacOS should work without issues as they support it by default. For Windows users, consider using WSL instead
- curl
- git

## Installation

### Linux and MacOS

To install Uwais, run the following command:

``` bash
curl --proto '=https' --tlsv1.2 -L https://dalikewara.com/uwais/install.sh | sh
```

> If the `install.sh` URL above doesn’t work, you can use this URL instead: `https://raw.githubusercontent.com/dalikewara/uwais/master/install.sh`.

!!! tip

    If you’re concerned about safety and security, you can download the [install.sh](../../uwais/install.sh) file first and execute it manually.
    Or, you can view the `install.sh` source code at [https://raw.githubusercontent.com/dalikewara/uwais/master/install.sh](https://raw.githubusercontent.com/dalikewara/uwais/master/install.sh).
  
### Windows

If you are using WSL or a tool like Git Bash, you can use the `curl` command mentioned above. Alternatively, you can download the installer from the [GitHub release Page](https://github.com/dalikewara/uwais/releases). The installer file is the one ending with `windows-installer.exe`.

### Manual Installation

If you prefer to install Uwais manually, download the archive for your operating system from the [GitHub release Page](https://github.com/dalikewara/uwais/releases). Once extracted, you will find an executable file. You should place this file in a directory included in your system's PATH (e.g., `/usr/local/bin` on Linux) so it can be easily accessed from the command line.

### Upgrade

If you already have Uwais installed, simply run the following command to upgrade to the latest version:

``` bash
uwais update
```

> If you are upgrading from version `v1.1.2`, you must run `uwais update` twice to reach the latest version (`v2.0.0+`). This is necessary because the first run updates you to the final legacy version (`v1.2.0`), which includes the migration scripts required for the transition. The second run then performs the actual upgrade to the new Rust-based version (`v2.0.0+`).

## Usage

Simply run:

``` bash
uwais
```

This will list all available commands and usage info.
