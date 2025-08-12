---
sidebar_position: 3
slug: /docs/uwais/project-structure
description: This page contains information about Uwais's project structure
keywords: [uwais, tools, ecosystem, application, project structure, clean architecture, feature driven design, domain driven design, design pattern]
---

# Project Structure

To implement the concept of Clean Architecture and Feature-Driven Design, and to keep them as simple and understandable as possible, Uwais structures the project like this:

Example (Golang):

```text
- common
    - error.go
    - fiber.go
    - mysql.go
    - response.go
- domain
    - user.go
    - product.go
- features
    - user
        - httpService_fiber_v1.go
        - repository_mysql.go
        - usecase_v1.go
    - product
    	- httpService_fiber_v1.go
        - repository_mysql.go
        - usecase_v1.go
- main.go
```

> Current version is **v4**

## Explanation

### main.[extension]

- In this file, you initialize dependencies, injections, and anything required to start and run your application
- This is the starting or entry point of your application

### domain

- The **Domain** represents your primary business model or entity
- Define your main object models or properties for your business here, including database models, DTOs (Data Transfer Objects), etc
- Keep this package as straightforward as possible. Avoid including any code that is not directly related to the model itself

### common

- In this place, you can implement various functions to assist you in performing common tasks—consider them as helpers
- Common functions can be directly called from anywhere

### features

- A **Feature** encapsulates your main business feature, logic, or service
- Here, you include everything necessary to ensure the proper functioning of the feature
- Please prioritize **Feature-Driven Design**, ensuring that features should can be easily adapted and seamlessly integrated and imported into different projects
- A standard **Feature** may comprise the following parts: `repository`, `use case`, `http/grpc/cron/etc service`. But, these are **OPTIONAL**, so feel free to adopt your own style as long as it aligns with the core concept:
    - **repository**
        - Handles communication with external data resources like databases, cloud services, or external services
        - Keep your repositories as simple as possible, avoid adding excessive logic
        - If necessary, separate operations into smaller methods
        - Changes outside the `repository` **SHOULD NOT** affect it (except changes for business domain/model/entity)
        - For config variables, database frameworks, or external clients, pass or inject them as dependencies
    - **use case**
        - Contains the main feature logic
        - Changes outside the `use case` **SHOULD NOT** affect it (except changes for business domain/model/entity and repository)
        - For config variables, external clients, or repositories, pass or inject them as dependencies
    - **http/grpc/cron/etc service**
        - Hosts feature handlers like HTTP handlers, gRPC handlers, cron jobs, or anything serving between the client and your feature or application
        - Changes outside the `service` **SHOULD NOT** affect it (except changes for business domain/model/entity, repository and use case)
        - For config variables, external clients, or use cases, pass or inject them as dependencies

### Make It Your Own

Feel free to create your own style to suit your requirements, as long as you still follow the main architecture concept.
You can create folders such as `migration` to store your database migrations, `tmp` for temporary files, or even `infra`
to house infrastructure configurations or scripts to facilitate the deployment of your project on a server or VM.
