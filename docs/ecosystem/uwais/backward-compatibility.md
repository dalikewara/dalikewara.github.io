---
sidebar_position: 3
slug: /docs/uwais/backward-compatibility
description: This page contains information about Uwais's backward compatibility
keywords: [uwais, tools, ecosystem, application, project structure, clean architecture, feature driven design, domain driven design, design pattern, backward compatibility]
---

# Backward Compatibility

Uwais maintains backward compatibility by separating the version of the source/app from the version of the generated project structure.
With this approach, Uwais can introduce future changes without breaking any existing generated project structures.

## Source or App Version

This refers to the version of the Uwais source code. You should always update Uwais to the latest version to receive the newest fixes and features.
Don’t worry, upgrading Uwais will not break your generated project structure; it will remain automatically compatible.

## Project Structure Version

This refers to the version of the generated project structure. Different versions may produce different structures, which helps ensure backward compatibility.

> The current default project structure version is `v4`.
