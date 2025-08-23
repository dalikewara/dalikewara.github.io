---
title: Finding The Best Design Pattern For Interfaces
description: In this post, I am looking for the best design pattern interface to meets my expectation and requirements in a various scenarios
keywords: design, interface, pattern, provider, consumer, contract
date: 2025-08-24
pin: false
authors:
  - dalikewara
links:
categories:
  - Design Pattern
tags:
  - design pattern
  - interface
  - coding
---

# Finding The Best Design Pattern for Interfaces

Design patterns are a super useful concept in programming. They keep your code consistent and structured, which makes your
life way easier. Personally, I'm a huge fan and think they should be a must for every project. It's not that I'm a pattern
guru; it's just about having a consistent way of doing things.

After all, everyone implements these patterns differently. Whether you're an expert in ISP (Interface Segregation Principle),
CQRS (Command Query Responsibility Segregation), or something else, each person will have their own implementation style. Some
stick strictly to one pattern, some mix a few, and some just wing it. It's all good, as long as you create a standard to follow.
Just document how your pattern works, and you're golden.

!!! warning

    Don't start coding until you know what pattern you're going to use!

<!-- more -->

I'm always on the hunt for the best pattern for my projects. I once got stuck following someone else's pattern during a
collaboration—and it was a total nightmare to follow. I didn't hate their implementation, just how complicated it was—especially
with no documentation 😭.

My journey to find the best interface design pattern started with a pretty simple concept...

!!! info

    From here on out, I'll be using Go for my examples. No special reason, I just like Go because it's simple. But keep in mind,
    I'm using a more universal approach here so it's easier to understand, so I might be skipping some of Go's specific idioms.

## 🏃‍♂️ Getting Started: The Repository Pattern

==The goal of this pattern is to provide an abstraction or a contract to separate the domain (provider) from the core business
logic (consumer)==. This pattern is mostly used to abstract technical details of data sources (repositories) like databases,
but you can also use it for other layers like use cases, services, or even a statement builder. The main point is to reflect
a business need.

Simply put, you have a provider, a consumer, and a contract. The consumer is the executor that calls the functions provided
by the provider. The provider is the implementer that provides the functions the consumer can call. The contract is the agreement
between the provider and consumer that binds them together. The provider has to provide its functions according to the contract,
because the consumer will run its business process based on that contract. The Repository pattern is the design of that contract.

!!! info

    From now on, I'll use these three terms: provider, consumer, and contract.

I'll use a simple example: I'm going to create a `UserRepository` contract to perform CRUD operations on a database.

``` go
type UserRepository interface {
	FindOne(queryFilter UserQueryFilter) (*User, error)
	FindAll(queryFilter UserQueryFilter) (Users, error)
	Insert(data *User) error
	Update(data *User) error
	Delete(data *User) error
}
```

Next, I'll use Postgres as the database, so the provider will look like this:

``` go
type userRepositoryPostgres struct {
	db *pgxpool.Pool // Example if the driver is pgxpool
}

func (u *userRepositoryPostgres) FindOne(queryFilter UserQueryFilter) (*User, error) {
	// here I'll SELECT query to Postgres
	...
}

func (u *userRepositoryPostgres) FindAll(queryFilter UserQueryFilter) (Users, error) {
	// here I'll SELECT query to Postgres
	...
}

func (u *userRepositoryPostgres) Insert(data *User) error {
	// here I'll INSERT query to Postgres
	...
}

func (u *userRepositoryPostgres) Update(data *User) error {
	// here I'll UPDATE query to Postgres
	...
}

func (u *userRepositoryPostgres) Delete(data *User) error {
	// here I'll DELETE query to Postgres
	...
}
```

> *Just think of a struct as an object.*

You can see that the `userRepositoryPostgres` object has the exact same methods and specifications as `UserRepository`. This is
because `userRepositoryPostgres` is the provider, so it has to implement all the specifications from its contract.

Now, inside the consumer, it will call the functions provided by the provider, since the provider has the actual implementation
of the CRUD process. But the consumer will orchestrate everything based on the contract. So, if I ever want to switch the provider
from Postgres to, say, MongoDB, all I have to do is create a new MongoDB provider object that implements the contract, and the consumer won't
break or throw an error. Since the contract is the same, the methods and their specifications will also be the same.

But how does the consumer orchestrate this?

## With Dependency Injection, Of Course!

This is how the consumer can orchestrate the provider. ==Dependency injection is a concept where you inject dependencies from
outside using a contract as the data type or constructor==. For example, instead of calling the provider object directly inside
the consumer like this:

``` go
func UpdateUser() error {
    userRepoImpl := &userRepositoryPostgres{}
    
    // Check user exists
    user, err := userRepoImpl.FindOne({ id: 1})
    if err != nil {
        return err
    }
    if user == nil {
        return errors.New("user not found")
    }
    
    // Update user
    if err = userRepoImpl.Update(user); err != nil {
        return err
    }
    
    return nil
}
```

> *I'm just using a function approach here to make it easier to read.*

I can change it to use dependency injection like this:

``` go
func UpdateUser(userRepoImpl UserRepository) error {
    // Check user exists
    user, err := userRepoImpl.FindOne({ id: 1})
    if err != nil {
        return err
    }
    if user == nil {
        return errors.New("user not found")
    }
    
    // Update user
    if err = userRepoImpl.Update(user); err != nil {
        return err
    }
    
    return nil
}
```

### Why though? 🤔

``` go
func UpdateUser() error {
    userRepoImpl := userRepositoryPostgres{}
    
    ...
}
```

If I call the provider object directly inside the consumer like the code above, it means I'm making the consumer's business
process dependent on the provider. If I ever want to switch the provider from Postgres to MongoDB, or if there's a code change
on the provider side, I'd also have to change the code on the consumer side, or the consumer will break. The provider, in this
case, is free because it's not tied to a contract at all. This makes the contract useless because the consumer now tied to the
provider object instead of the contract. It should be the other way around: the consumer must be tied to the contract, not the
provider object.

``` go
func UpdateUser(userRepoImpl UserRepository) error {
    ...
}
```

In the code above, I'm passing `userRepoImpl` as an argument with the data type `UserRepository`, which is the contract. This is
what's called Dependency Injection. I pass the provider object as an argument to the consumer's function, but I tie that object
to the contract by making its data type or constructor `UserRepository`. So now, the consumer only knows the contract data type;
it doesn't care about the provider object. No matter how I change or replace the provider code, as long as the provider object
follows the contract, the consumer won't care and won't break because the data type and contract are guaranteed to be the same.
Most programming languages can even help validate if the object matches the contract during the compiling or building process,
so you don't have to worry about runtime errors.

### Usage differential

The way you use it is also very different with and without dependency injection. Without dependency injection, I would use the
consumer like this:

``` go
func main() {
    if err := UpdateUser(); err != nil {
        panic(err)
    }
}
```

while with dependency injection, it's like this:

``` go
func main() {
    userRepoImpl := &userRepositoryPostgres{}
    
    if err := UpdateUser(userRepoImpl); err != nil {
        panic(err)
    }
}
```

If I want to use several databases at once, I can just do this:

``` go
func main() {
    // initialize providers

    userRepoImplPostgres := &userRepositoryPostgres{}
    userRepoImplMySQL := &userRepositoryMySQL{}
    userRepoImplMongoDB := &userRepositoryMongoDB{}
    userRepoImplElasticsearch := &userRepositoryElasticsearch{}
    
    // Update user to Postgres database
    if err := UpdateUser(userRepoImplPostgres); err != nil {
        panic(err)
    }
    
    // Update user to MySQL database
    if err := UpdateUser(userRepoImplMySQL); err != nil {
        panic(err)
    }
    
    // Update user to MongoDB database
    if err := UpdateUser(userRepoImplMongoDB); err != nil {
        panic(err)
    }
    
    // Update user to Elasticsearchsearch
    if err := UpdateUser(userRepoImplElasticsearch); err != nil {
        panic(err)
    }
}
```

You can see above that I'm only using one consumer, `UpdateUser`, to update many databases, because all the providers have the
same contract. Imagine without dependency injection: I would either have to create a new consumer for each database, or I'd
have to change the consumer's code and add logic to make it compatible with each database.

I hope the example above is easy to understand 🙏.

## Now I Have a Single Fat Repository Pattern

Okay, is the pattern above enough? Unfortunately, I don't think so. I see that the pattern is still not flexible enough. The
`UserRepository` contract might seem simple, but it's not. If you look closely, that one contract has a ton of methods with different
operations. There are methods for getting data, for inserting, updating, and deleting. ==This is called a Single Fat Interface, which
means an interface contract that's too "fat" because it has too many different operations or methods.==

### So, what's the problem here? 🤔

I have explained that a provider should always follow the contract, meaning it has to implement all the functions from that contract.
This is where the problem lies. In many development cases, this pattern always causes issues. Business needs are always changing, sometimes
almost constantly. The classic reasons are to adapt to user needs, improve performance, and for security and cost efficiency. For example,
let's say from the `UserRepository` contract, I need to move the "get user data" function to Elasticsearch, and the "insert user" function to MongoDB.
This is just an example, so don't worry if it doesn't make sense.

So, what do I have to do? Of course, I have to create three providers, right? A provider for Postgres, Elasticsearch, and MongoDB:

``` go
// Postgres provider

type userRepositoryPostgres struct {
    db interface{} // I'll mock it as an interface for now
}

func (u *userRepositoryPostgres) FindOne(queryFilter UserQueryFilter) (*User, error) {
    // here I'll SELECT query to Postgres
    ...
}

func (u *userRepositoryPostgres) FindAll(queryFilter UserQueryFilter) (Users, error) {
    // here I'll SELECT query to Postgres
    ...
}

func (u *userRepositoryPostgres) Insert(data *User) error {
    // here I'll INSERT query to Postgres
    ...
}

func (u *userRepositoryPostgres) Update(data *User) error {
    // here I'll UPDATE query to Postgres
    ...
}

func (u *userRepositoryPostgres) Delete(data *User) error {
    // here I'll DELETE query to Postgres
    ...
}

// Elasticsearch provider

type userRepositoryElasticsearch struct {
    db interface{}
}

func (u *userRepositoryElasticsearch) FindOne(queryFilter UserQueryFilter) (*User, error) {
    // here I'll get data from Elasticsearch
    ...
}

func (u *userRepositoryElasticsearch) FindAll(queryFilter UserQueryFilter) (Users, error) {
    // here I'll get all data from Elasticsearch
    ...
}

func (u *userRepositoryElasticsearch) Insert(data *User) error {
    // here I'll insert data into Elasticsearch
    ...
}

func (u *userRepositoryElasticsearch) Update(data *User) error {
    // here I'll update data in Elasticsearch
    ...
}

func (u *userRepositoryElasticsearch) Delete(data *User) error {
    // here I'll delete data from Elasticsearch
    ...
}

// MongoDB provider

type userRepositoryMongoDB struct {
    db interface{}
}

func (u *userRepositoryMongoDB) FindOne(queryFilter UserQueryFilter) (*User, error) {
    // here I'll get data from MongoDB
    ...
}

func (u *userRepositoryMongoDB) FindAll(queryFilter UserQueryFilter) (Users, error) {
    // here I'll get all data from MongoDB
    ...
}

func (u *userRepositoryMongoDB) Insert(data *User) error {
    // here I'll insert data into MongoDB
    ...
}

func (u *userRepositoryMongoDB) Update(data *User) error {
    // here I'll update data in MongoDB
    ...
}

func (u *userRepositoryMongoDB) Delete(data *User) error {
    // here I'll delete data from MongoDB
    ...
}
```

So, you can see above that I'm creating three providers, but I have to implement all the functions because I have to follow
the contract. In reality, I only want the "get data" function to go to Elasticsearch and the "insert user" function to go to MongoDB,
with the rest staying in Postgres. Since all the functions are in one single interface contract, I'm forced to implement all of
them, even though I only need a few. I could just use dummy implementations like `#!go fmt.Println("implement me!")` for the functions
I don't need, but that's really confusing, ugly, and just not acceptable. I don't like it. Why should I have to do something
that's not needed?

## 👨‍💻 Let's Change It To CQRS (Command Query Responsibility Segregation)

==From what I've read, this design pattern is about separating read operations (query) and write operations (command)==. Instead of
making one big contract for both reading and writing data, we split these two operations into two interface contracts: Query and Command,
or Reader and Writer. If I try to apply this, the `UserRepository` contract above can be made like this:

``` go
type UserRepositoryQuery interface {
    FindOne(queryFilter UserQueryFilter) (*User, error)
    FindAll(queryFilter UserQueryFilter) (Users, error)
}

type UserRepositoryCommand interface {
    Insert(data *User) error
    Update(data *User) error
    Delete(data *User) error
}
```

Here, Query is the contract with functions to get user data, while Command is for creating, updating, and deleting users.
Okay, this looks pretty good and makes sense. But it seems like this pattern only solves the need to move to Elasticsearch, which
is just for the "get data" functions. It doesn't seem strong enough to solve the need to move to MongoDB 😢, because only the
"insert" function is moving to MongoDB, while "update" and "delete" are staying in Postgres.

## I Need To Separate Them Using The Interface Segregation Principle (ISP)

I think I can solve the problem above using the next design pattern, which is the Interface Segregation Principle (ISP),
one of the SOLID principles. ==This ISP pattern states that clients (in this context, producers and consumers) should not be
forced to depend on functions they don't use==. The point is, instead of creating one contract with a bunch of operations,
it's better to create several contracts, each separating its own operations. But unlike CQRS, this is more specific and
smaller. For example, I can change the `UserRepository` contract above to look like this:

``` go
type UserRepositoryFinder interface {
    FindOne(queryFilter UserQueryFilter) (*User, error)
    FindAll(queryFilter UserQueryFilter) (Users, error)
}

type UserRepositoryInserter interface {
    Insert(data *User) error
}

type UserRepositoryUpdater interface {
    Update(data *User) error
}

type UserRepositoryDeleter interface {
    Delete(data *User) error
}
```

You can see the interface above is split into four kinds of contracts: Finder, Inserter, Updater, Deleter. Finder is the
contract for all operations related to getting user data. Inserter is for adding user data, Updater for changing user data,
and Deleter for deleting user data. Since the operations are now separated, the provider implementation becomes more proper
because it's more focused. And my needs above can now be implemented.

### Let's implement the provider!

There are still three providers, one for Elasticsearch, MongoDB, and Postgres. The difference now is how the contract is implemented:

> *I'll make the Postgres provider implement all four contracts to make it easier to understand later.*

``` go
// Elasticsearch provider

type userRepositoryFinderElasticsearch struct {
    db interface{}
}

func (u *userRepositoryFinderElasticsearch) FindOne(queryFilter UserQueryFilter) (*User, error) {
    // here I'll get data from Elasticsearch
    ...
}

func (u *userRepositoryFinderElasticsearch) FindAll(queryFilter UserQueryFilter) (Users, error) {
    // here I'll get all data from Elasticsearch
    ...
}

// MongoDB provider

type userRepositoryInserterMongoDB struct {
    db interface{}
}

func (u *userRepositoryInserterMongoDB) Insert(data *User) error {
    // here I'll insert data into MongoDB
    ...
} 

// Postgres provider

type userRepositoryFinderPostgres struct {
    db interface{}
}

func (u *userRepositoryFinderPostgres) FindOne(queryFilter UserQueryFilter) (*User, error) {
    // here I'll SELECT query to Postgres
    ...
}

func (u *userRepositoryFinderPostgres) FindAll(queryFilter UserQueryFilter) (Users, error) {
    // here I'll SELECT query to Postgres
    ...
}

type userRepositoryInserterPostgres struct {
    db interface{}
}

func (u *userRepositoryInserterPostgres) Insert(data *User) error {
    // here I'll INSERT query to Postgres
    ...
} 

type userRepositoryUpdaterPostgres struct {
    db interface{}
}

func (u *userRepositoryUpdaterPostgres) Update(data *User) error {
    // here I'll UPDATE query to Postgres
    ...
}

type userRepositoryDeleterPostgres struct {
    db interface{}
}

func (u *userRepositoryDeleterPostgres) Delete(data *User) error {
    // here I'll DELETE query to Postgres
    ...
}
```

### The Breakdown!

You can see that in the Elasticsearch provider, I don't need to implement the "insert", "update", and "delete" functions because, based
on the needs above, they aren't needed. The same goes for the MongoDB provider; I don't need to implement the "get data,"
"update," and "delete" functions.

Now, all the operations are grouped and won't be dependent on each other. If I need to change a specific operation, only that
operation is changed; it won't depend on and change other operations, which minimizes work on things that aren't needed. Usage
from the consumer side also becomes more flexible.

For example, previously, I only had one `UpdateUser` consumer using the `UserRepository` contract. This time, I'll change it and create
a new consumer to manage user data like this:

``` go
func FindAllUser(userRepoFinderImpl UserRepositoryFinder) (Users, error) {      
    return userRepoFinderImpl.FindAll({})
}

func InsertUser(userRepoInserterImpl UserRepositoryInserter) error {
    user := &User{
        Name: "John Doe",
    }
    
    // Insert user
    if err = userRepoInserterImpl.Insert(user); err != nil {
        return err
    }
    
    return nil
}

func UpdateUser(userRepoFinderImpl UserRepositoryFinder, userRepoUpdaterImpl UserRepositoryUpdater) error {
    // Check user exists
    user, err := userRepoFinderImpl.FindOne({ id: 1})
    if err != nil {
        return err
    }
    if user == nil {
        return errors.New("user not found")
    }
    
    // Update user
    if err = userRepoUpdaterImpl.Update(user); err != nil {
        return err
    }
    
    return nil
}

func DeleteUser(userRepoFinderImpl UserRepositoryFinder, userRepoDeleterImpl UserRepositoryDeleter) error {
    // Check user exists
    user, err := userRepoFinderImpl.FindOne({ id: 1})
    if err != nil {
        return err
    }
    if user == nil {
        return errors.New("user not found")
    }
    
    // Delete user
    if err = userRepoDeleterImpl.Delete(user); err != nil {
        return err
    }
    
    return nil
}
```

> *The `UserRepository` contract isn't used anymore because it's no longer relevant.*

Now, the consumer is super flexible; it no longer injects one big contract. All it injects are the specific operations that
the consumer needs. I can also freely change the data source business needs (not just switching databases, but also if I switch a
driver from `pgxpool` to `sqlx` or even an ORM like `goqu`) without worrying about having to implement everything I don't need. Here's
an example of using the consumer based on my needs above:

``` go
func main() {
    // Initialize Elasticsearch provider
    
    userRepoFinderImplElasticsearch := &userRepositoryFinderElasticsearch{}
    
    // Initialize MongoDB provider
    
    userRepoInserterImplMongoDB := &userRepositoryInserterMongoDB{}
    
    // Initialize Postgres provider
    
    userRepoFinderImplPostgres := &userRepositoryFinderPostgres{}
    userRepoInserterImplPostgres := &userRepositoryInserterPostgres{}
    userRepoUpdaterImplPostgres := &userRepositoryUpdaterPostgres{}
    userRepoDeleterImplPostgres := &userRepositoryDeleterPostgres{}
    
    // Insert user data into MongoDB
    if err := InsertUser(userRepoInserterImplMongoDB); err != nil {
        panic(err)
    }
    
    // Get user data from Elasticsearch
    users, err := FindAllUser(userRepoFinderImplElasticsearch)
    if err != nil {
        panic(err)
    }
    
    fmt.Println(users)
    
    // Update and delete to Postgres, but check if user exists from Elasticsearch

    if err = UpdateUser(userRepoFinderImplElasticsearch, userRepoUpdaterImplPostgres); err != nil {
        panic(err)
    }
    
    if err = DeleteUser(userRepoFinderImplElasticsearch, userRepoDeleterImplPostgres); err != nil {
        panic(err)
    }
    
    // CRUD to Postgres as in the original normal flow
    
    users, err = FindAllUser(userRepoFinderImplPostgres)
    if err != nil {
        panic(err)
    }
    
    if err = InsertUser(userRepoInserterImplPostgres); err != nil {
        panic(err)
    }
    
    if err = UpdateUser(userRepoFinderImplPostgres, userRepoUpdaterImplPostgres); err != nil {
        panic(err)
    }
    
    if err = DeleteUser(userRepoFinderImplPostgres, userRepoDeleterImplPostgres); err != nil {
        panic(err)
    }
}
```

Look how easily I can change the data source business needs above. With the same consumer and contract, all I have to do is
change the provider, and I'm done 👏.

## Let's talk About The Result object

If you notice, I've been returning a single `User` object as an example. This object actually contains user data like id,
username, email, password, etc. It's more or less like this:

``` go
type User struct {
	ID        int64
	Username  string
	Email     string
	Name      string
	Password  string
	CreatedAt time.Time
	UpdatedAt time.Time
}
```

Since our contract returns this `User` object, the consumer will always expect these fields to be available and their values
to be usable according to the data types assigned in the object. Previously, I always used a database as the data source,
which actually has a correlation. The fields from the `User` object above are a representation of the columns from the `users`
table. This means if we get data from the database, we can directly fill the field values based on the columns from the `users` table.

Now, imagine I have a consumer use case to get product data, which looks more or less like this

``` go hl_lines="12 23 24"
func FindProduct(productRepoInserterImpl ProductRepositoryFinder, userRepoFinderImpl UserRepositoryFinder) (*ProductDTO1, error) {
    // Get user data
    user, err := userRepoFinderImpl.FindOne({ id: 1})
    if err != nil {
        return err
    }
    if user == nil {
        return errors.New("user not found")
    }
    
    // Get product data
    product, err := productRepoInserterImpl.FindOne({ id: 1, userID: user.ID })
    if err != nil {
        return err
    }
    if product == nil {
        return errors.New("product not found")
    }
    
    return &ProductDTO1{
        ProductID: product.ID,
        ProductName: product.Name,
        OwnerID: user.ID,
        OwnerName: user.Name,
    }
}
```

You can see that for the product use case above, I only need the `ID` and `Name` fields from the `User` object. But in reality,
according to the `UserRepositoryFinder` contract, the single `User` object is returned, which means all fields are returned too.
But because I only need a few fields from the `User` object, I can improve it so the contract only returns a `User` object with
just the `ID` and `Name` fields.

## Specialized ISP

I'm still going to use this pattern, because according to the ISP definition above that =="clients should not be forced to depend on
functions they do not use"==, this also applies to object fields. So, for the product use case, I won't use the `UserRepositoryFinder`
contract; instead, I'll use a new contract like this:

``` go
type UserRepositoryFinderForProduct interface {
    FindOne(queryFilter UserQueryFilter) (*UserForProduct, error)
}

type UserForProduct struct {
	ID   int64
	Name string
}
```

This `UserRepositoryFinderForProduct` contract will be injected into the product use case. And this contract is specifically for
the product use case, not for others. If another use case has specific needs for the `User` object data, the method is the same:
create a new contract for that use case. By using this way, I'm implementing the ISP design pattern more completely, because now the rules
are followed for both functions and object fields.

If the user use case ever gets migrated to a separate HTTP service, the product use case will still be safe. And I don't have to make
the user service return all the fields of the single `User` object, because via HTTP, sensitive fields like `password` shouldn't be
returned in the response.

I'm calling this part Specialized ISP ✨.

## Data Transfer Object (DTO)

This is still related to what's above. Previously, I separated the result objects between the user use case and the product use case.
The result for the user use case was `User`, while for the product use case it was `UserForProduct`. This is one example of a DTO.
==The definition itself is an object used to move data between application layers and to ensure only relevant data is sent, as well
as to keep sensitive data from being exposed to layers that don't need it.==

In the use case above, you can see that I'm not returning a product object as the result, but I'm returning a `ProductDTO1` object.
Why? Because the product object might contain many fields that the client doesn't need, so they shouldn't all be returned. So, I'm applying
the DTO concept by creating a DTO object that only has the fields the client needs. The response size to the client also becomes smaller.

## The Adapter Pattern Will Be Helpful 👀

In cases of changing data source needs (from Postgres -> MongoDB, Postgres -> Elasticsearch, MongoDB -> HTTP service), what's actually changing is
just the way we query and parse the results. For example, Postgres usually uses RAW Queries, while MongoDB, Elasticsearch, and HTTP services
usually use objects. The result also usually depends on the driver/client/SDK; some use scanners, and some parse structs or objects.
The flow for each of these clients is different. But with the Specialized ISP design pattern above, this isn't a problem, because the
different flows are implemented in each provider. But this Adapter Pattern might help in some cases.

### First Case Example

The database is still Postgres, but the clients are different: one uses `pgxpool` and the other uses `sqlx`:

``` go hl_lines="15 16 17 38 39 40"
// Postgres provider using pgxpool

type userRepositoryFinderPGXPool struct {
    db interface{}
}

func (u *userRepositoryFinderPGXPool) FindOne(queryFilter UserQueryFilter) (*User, error) {
    if queryFilter.ID < 1 {
        return nil, nil
    }
    
    var user User
    
    // context here is just an example, in idiomatic Go it's placed as the first argument: `ctx context.Context`
	if err := u.db.QueryRow(context.Background(), `SELECT name, created_at, updated_at FROM users WHERE id = $1`, queryFilter.ID).Scan(&user.Name, &user.CreatedAt, &user.UpdatedAt); err != nil {
		return nil, err
	}
	
	user.SetFormattedCreatedAt()
	user.SetFormattedUpdatedAt()
	
	return &user, nil
}

// Postgres provider using sqlx

type userRepositoryFinderSQLX struct {
    db interface{}
}

func (u *userRepositoryFinderSQLX) FindOne(queryFilter UserQueryFilter) (*User, error) {
    if queryFilter.ID < 1 {
        return nil, nil
    }
    
    var user User
    
    if err = u.db.Get(&user, `SELECT name, created_at, updated_at FROM users WHERE id = $1`, queryFilter.ID); err != nil {
        return nil, err
    }
	
	user.SetFormattedCreatedAt()
	user.SetFormattedUpdatedAt()
	
	return &user, nil
}
```

From the code above, you can see that the only parts of the flow that are different are the highlighted ones; the rest of
the flow is the same. Wouldn't it be better if we didn't have to rewrite the same flow?

### Second Case example

Let's say I have a function to create an order. In the process of creating the order, there's a process to insert order data
and update product stock. Now, let's say I need to use a Transaction to make sure the order data is valid. The provider
would look something like this:

``` go
type orderRepositoryInserterPGXPool struct {
    db *pgxpool.Pool
}

func (u *orderRepositoryInserterPGXPool) BeginTx() (pgx.Tx, error) {
    return u.db.BeginTx(context.Background(), pgx.TxOptions{})
}

func (u *orderRepositoryInserterPGXPool) InsertTx(tx pgx.Tx, order *Order) error {
    ...
}

type productRepositoryUpdaterPGXPool struct {
    db *pgxpool.Pool
}

func (p *productRepositoryUpdaterPGXPool) UpdateTx(tx pgx.Tx, product *Product) error {
    ...
}
```

and on the consumer side:

> *Let's assume the contracts are `OrderRepositoryInserter` and `ProductRepositoryUpdater`.*

``` go
func CreateOrder(orderRepoImplInserter OrderRepositoryInserter, productRepoImplUpdater OrderRepositoryUpdater) error {
    tx, err := orderRepoImplInserter.BeginTx()
    if err != nil {
        return err
    }
    
    defer tx.Rollback()
    
    // Insert order
    
    if err = orderRepoImplInserter.InsertTx(tx, &Order{}); err != nil {
        return err
    }
    
    // Update product stock
    
    if err = productRepoImplUpdater.UpdateTx(tx, &Product{}); err != nil {
        return err
    }
    
    if err = tx.Commit(); err != nil {
        return err
    }
    
    return nil
}
```

Now, this is a serious problem, because I'm using the `pgx.Tx` transaction object/interface from the `pgxpool` client directly and
injecting its object as a dependency to the `InsertTx` and `UpdateTx` function arguments. And inside the consumer itself, I'm calling
`tx.Rollback()` and `tx.Commit()`, which are methods from the `pgx.Tx` object. This means I've made the contract, provider, and consumer
all dependent on the external `pgxpool` and `pgx.Tx` objects. This automatically invalidates the design pattern concepts we've built above,
because the pattern shouldn't have any dependencies on external objects. If I want to switch from `pgxpool` to `sqlx`, I'll definitely
have to change the contract, provider, and consumer, and replace the transaction object from `pgxpool` with `sqlx`. It shouldn't be
like that.

### Now we get the usage of this pattern

==This is where the Adapter Pattern comes in handy, because its purpose is to transform an object/interface into a new standard interface
contract that the client expects==. This means we're turning the `pgxpool` and `sqlx` objects/interfaces into a standard interface that we
create ourselves. For example, a data source process always has read and write operations. We can create a standard contract for that:

``` go
type SourceAdapter interface {
    BeginTx() (SourceAdapterTx, error)
    QueryOne(query interface{}, args ...interface{}) (SourceRow, error)
    QueryAll(query interface{}, args ...interface{}) (SourceRows, error)
    Exec(query interface{}, args ...interface{}) (SourceResult, error)
}

type SourceAdapterTx interface {
    Commit() error
    Rollback() error
    QueryOne(query interface{}, args ...interface{}) (SourceRow, error)
    QueryAll(query interface{}, args ...interface{}) (SourceRows, error)
    Exec(query interface{}, args ...interface{}) (SourceResult, error)
}

type SourceRow interface {
    Scan(dest ...interface{}) error
}

type SourceRows interface {
    Next() bool
    Scan(dest ...interface{}) error
}

type SourceResult interface {
    RowsAffected() int64
}
```

Then, on the provider side, the argument being injected is this adapter's contract, for example:

``` go
type orderRepositoryInserter struct {
    db SourceAdapter
}

func (u *orderRepositoryInserter) BeginTx() (SourceAdapterTx, error) {
    return u.db.BeginTx()
}

func (u *orderRepositoryInserter) InsertTx(tx SourceAdapterTx, order *Order) error {
    ...
}
```

With this, the dependency problem is solved. We don't need to specify the suffix `PGXPool` anymore, because now the provider doesn't care,
it is now tied to the `SourceAdapter`. If I switch from `pgxpool` to `sqlx`, all I need to do is make those clients implement
the `SourceAdapter` contract, and the consumer above won't break and nothing needs to be changed. The method is exactly the same
as the initial design pattern, just with a different name: Adapter Pattern. Example:

``` go
type pgxPoolAdapter struct {
	db *pgxpool.Pool
}

func (p *pgxPoolAdapter) BeginTx() (SourceAdapterTx, error) {
    // I make pgxpool returns `(SourceAdapterTx, error)` according to the contract
    
	tx, err := u.db.BeginTx(context.Background(), pgx.TxOptions{})
	if err != nil {
		return nil, err
	}
	
	return &pgxPoolAdapterTx{ tx: tx }, nil
}

func (p *pgxPoolAdapter) QueryOne(query interface{}, args ...interface{}) (SourceRow, error) {
    // I'll make pgxpool processes the `query interface{}, args ...interface{}` argument and returns `(SourceRow, error)` according to the contract
	...
}

func (p *pgxPoolAdapter) QueryAll(query interface{}, args ...interface{}) (SourceRows, error) (SourceAdapterRows, SourceAdapterErr) {
    // I'll make pgxpool processes the `query interface{}, args ...interface{}` argument and returns `(SourceAdapterRows, error)` according to the contract
	...
}

func (p *pgxPoolAdapter) Exec(query interface{}, args ...interface{}) (SourceResult, error) {
    // I'll make pgxpool processes the `query interface{}, args ...interface{}` argument and returns `(SourceResult, error)` according to the contract
	...
}

func NewPGXPoolAdapter(db *pgxpool.Pool) SourceAdapter {
	return &pgxPoolAdapter{
		db: db,
	}
}
```

### There are also drawbacks for this

The downside is that we have to code the implementation to transform these external objects to follow the Adapter Pattern contract
we've made. This usually takes extra effort, because each client's flow is different, so the adjustments are also different and a
bit tricky. Sometimes we also have to think about how to create a single Adapter Pattern that's compatible with all SDKs/clients.

I'd say this pattern is optional. But once we've implemented the provider adapter, it will be easier later on. Many things can be
standardized in the future, which will make migrations and adapting to changes easy without having to change the business process.
The issue in the first case example above can also be solved with the Adapter Pattern.

## The Final Take 🚀, For The Current Moment

Finally, for now, the best interface design pattern that I use to meet my expectations and needs above is Dependency Injection + Specialized ISP + DTO.
I feel like this pattern is a good balance between complexity and simplicity, is flexible enough, and is definitely still very human-readable.
The Adapter Pattern is optional, but since I plan to create reusable adapters for various database drivers, I'll be using this pattern in the future,
and it won't interfere with the main design pattern.

So, the final design pattern I'm choosing is Dependency Injection + Specialized ISP + Adapter Pattern + DTO. That's all, thank you, I hope this post
helps you.

!!! note

    For the [Uwais](/docs/uwais/) todo example, I'll still be using the basic Repository pattern because a complex design pattern isn't necessary for a project generator
    example. The developers can change it later to their liking.
