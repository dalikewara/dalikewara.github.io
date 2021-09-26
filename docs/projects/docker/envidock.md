---
title: envidock
description: Envidock is a general local environment services setup using the power of Docker
author: Dali Kewara
date: 2021-09-24 18:50:50
---

# Introduction

**Envidock** is a general local environment services setup using the power of Docker.

## Usage

Clone the repo at [https://github.com/dalikewara/envidock](https://github.com/dalikewara/envidock),
then use the `docker-compose.yml` or use the `Makefile`.

## Requirements

- Docker (>=20.10.5)

## Features & Specifications

- Docker compose (3.9)
- MySQL (latest)
- Mongo (latest)
- Postgres (latest)
- Redis (latest)
- RabbitMQ (management). Latest RabbitMQ image with the management plugin enabled.

!!! note
    If you want to change the versions, change it in `docker-compose.yml` file.

## Environment variables

The setup requires environment variables listed in `.env`. You can change the values according to your needs. For production use, you may not using `.env` file, but setting all the required variables in different way manually into the system instead.

## Docker compose

The `docker-compose.yml` file provides standart way to run the environment services on Docker. You're free to customize it.

## Makefile is your friend

You can run `make` or `make info` to show information and print out available commands, just like the same as outputted bellow:

```text
AVAILABLE COMMANDS

build                Build all environment services
destroy              Destroy all environment services. This will also clear all volumes & data
up                   Create & run all environment services
down                 Remove all environment services, but leave all volumes & data untouched
stop                 Stop all environment services
start                Start all environment services
restart              Restart all environment services
clear-mongo          Clear Mongo volume & data
clear-mysql          Clear MySQL volume & data
clear-postgres       Clear Postgres volume & data
clear-redis          Clear Redis volume & data
clear-rabbitmq       Clear RabbitMQ volume & data

AVAILABLE OPTIONS

on : Affect only to specified service on commands: `build`, `up`, `stop`, `start` & `restart`
     Example: `make build on=mysql` will build & run only MySQL environment service
```

!!! note
    If you're using non Linux/Unix-like system (Windows, etc), please find it the way by yourself. If you're using Windows, you may use WSL.