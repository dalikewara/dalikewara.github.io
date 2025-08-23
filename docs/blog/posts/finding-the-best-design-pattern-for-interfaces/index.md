---
title: Finding The Best Design Pattern For Interfaces
description: In this post, I am looking for the best design pattern interface to meets my expectation and requirements in a various scenarios
keywords: design, interface, pattern, producer, consumer, contract
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

# Finding The Best Design Pattern For Interfaces

Design Pattern adalah sebuah konsep yang sangat berguna dalam pembuatan program. Konsep ini memastikan alur dari kode program
tetap konsisten dan terstruktur, sehingga mempermudah pekerjaan. Saya pribadi sangat menjunjung tinggi design pattern dan
menganggap bahwa konsep ini wajib sekali diterapkan dalam setiap pembuatan program. Bukan berarti saya sangat jago disini, tapi
maksud saya adalah harus ada pattern yang konsisten.

Lagipula, penerapan dari teori design pattern ini pasti berbeda-beda tiap individu. Terserah mau kita menguasai ISP
(Interface Segregation Principle), CQRS (Command Query Responsibility Segregation) atau apapun itu, pasti tiap orang berbeda
dalam hal implementasi. Ada yang strict mengikuti 1 pattern, ada yang mengadopsi lebih dari 1, ada juga yang mencampurkan beberapa
pattern, bahkan ada yang ngasal. It's ok, yang penting ada sebuah standart yang kita buat untuk diikuti. Tinggal nanti kita buat
dokumentasi menjelaskan cara kerja pattern yang kita buat, beres.

!!! warning

    Jangan mulai ngoding sebelum tahu pattern apa yang akan diterapkan!

<!-- more -->

Saya sendiri selalu mencari pattern terbaik untuk project-project yang saya buat. Saya pernah terjebak mengikuti pattern buatan
orang lain ketika sedang dalam project kolaborasi—yang design patternnya sangat ribet untuk diikuti. Saya tidak membenci cara
implementasinya, saya hanya membenci sesuatu yang ribet—apalagi jika tidak ada dokumentasinya.

Perjalanan saya dalam mencari design pattern interface terbaik ini dimulai dari konsep yang cukup simple...

> Untuk selanjutnya, saya akan pakai contoh menggunakan Golang. Nggak ada alasan khusus, saya cuma suka Golang karna simpel.
> Tapi perlu diingat, disini saya menggunakan pendekatan yang lebih universal supaya mudah dipahami, jadi agak mengesampingkan
> idiomatic di Golang

## Getting Started, The Repository Pattern

Konsep pattern ini tujuannya untuk menyediakan abstraksi atau kontrak untuk memisahkan domainnya (produser) dengan logical
bisnis utama (consumer). Pattern ini kebanyakan dipakai untuk abstraksi detail teknis sumber data (repository) seperti database,
tapi sebernarnya bisa juga dipakai untuk layer lain seperti use case, service, atau bahkan sebuah statement builder. karna intinya
sama, yaitu untuk mencerminkan sebuah kebutuhan bisnis.

Simpelnya, ada produser, consumer dan kontrak. Consumer adalah executor yang memanggil fungsi-fungsi yang disediakan oleh produser.
Produser adalah implementator yang menyediakan fungsi-fungsi untuk bisa dipanggil oleh consumer. Nah, kontrak adalah perjanjian
antara produser dan consumer untuk mengikat hubungan antara keduanya. Produser harus menyediakan fungsi-fungsinya sesuai dengan
kontrak yang telah disepakati dengan consumer, karena consumer akan melakukan proses bisnisnya berdasarkan kontrak tersebut.
Repository pattern ini adalah desain dari kontrak tersebut.

> Untuk selanjutnya saya akan pakai ketiga istilah ini: produser, consumer, kontrak

Saya akan mengambil contoh sederhana, yaitu saya akan membuat sebuah kontrak `UserRepository` untuk melakukan CRUD ke database:

``` go
type UserRepository interface {
	FindOne(queryFilter UserQueryFilter) (*User, error)
	FindAll(queryFilter UserQueryFilter) (Users, error)
	Insert(data *User) error
	Update(data *User) error
	Delete(data *User) error
}
```

Kemudian, saya akan memakai postgres sebagai databasenya, sehingga produsernya akan seperti ini:

``` go
type userRepositoryPostgres struct {
	db *pgxpool.Pool // Contoh jika drivernya pakai pgxpool
}

func (u *userRepositoryPostgres) FindOne(queryFilter UserQueryFilter) (*User, error) {
	// disini saya query SELECT ke postgres
	...
}

func (u *userRepositoryPostgres) FindAll(queryFilter UserQueryFilter) (Users, error) {
	// disini saya query SELECT ke postgres
	...
}

func (u *userRepositoryPostgres) Insert(data *User) error {
	// disini saya query INSERT ke postgres
	...
}

func (u *userRepositoryPostgres) Update(data *User) error {
	// disini saya query UPDATE ke postgres
	...
}

func (u *userRepositoryPostgres) Delete(data *User) error {
	// disini saya query DELETE ke postgres
	...
}
```

> Anggap saja struct adalah sebuah object

Kita lihat bahwa object `userRepositoryPostgres` ini memiliki method dan spesifikasi yang sama persis dengan `UserRepository`.
Hal ini karna `userRepositoryPostgres` adalah produsernya, jadi dia harus mengimplementasi semua spesifikasi sesuai kontraknya
dengan sama persis.

Nah, nanti di dalam consumer, fungsi-fungsi yang telah disediakan produser ini yang akan dipanggil, karena dialah yang punya hasil
implementasi nyata dari proses CRUDnya. Tapi, consumer akan mengorkestrasinya berdasarkan kontrak. Sehingga, apabila suatu saat saya
ingin mengganti produser dari postgres ke mongodb misal, saya cukup buat sebuah object produser baru yang mengemplimentasi kontrak,
dan consumer tidak akan rusak atau error. Karena kontraknya sama, yang artinya method-method dan spesifikainya pun juga pasti sama.

Tapi kemudian, bagaimana cara consumer mengorkestrasi hal ini?

## With The Dependency Injection, Of Course!

Inilah caranya agar consumer bisa mengorkestrasi produser. Dependency injection adalah sebuah konsep dimana kita menginject dependency dari luar
menggunakan sebuah kontrak sebagai tipe data atau constructor. Sebagai contoh, alih-alih saya langsung memanggil object produser didalam consumer
seperti ini:

> Disini saya pakai pendekatan fungsi saja supaya lebih mudah dibaca

``` go
func UpdateUser() error {
    userRepoImpl := userRepositoryPostgres{}
    
    // Check user exists
    user, err := userRepoImpl.FindOne({ id: 1})
    if err != nil {
        return err
    }
    if user  nil {
        return errors.New("user not found")
    }
    
    // Update user
    if err = userRepoImpl.Update(user); err != nil {
        return err
    }
    
    return nil
}
```

Saya bisa ubah supaya menggunakan dependency injection seperti ini:

``` go
func UpdateUser(userRepoImpl UserRepository) error {
    // Check user exists
    user, err := userRepoImpl.FindOne({ id: 1})
    if err != nil {
        return err
    }
    if user  nil {
        return errors.New("user not found")
    }
    
    // Update user
    if err = userRepoImpl.Update(user); err != nil {
        return err
    }
    
    return nil
}
```

### Why though?

``` go
func UpdateUser() error {
    userRepoImpl := userRepositoryPostgres{}
    
    ...
}
```

Jika saya langsung memanggil object produser kedalam consumer seperti diatas, itu artinya saya membuat proses bisnis
consumer menjadi ketergantungan terhadap produser. Jika suatu saat saya mau mengganti produser dari postgres ke mongodb, atau
misal ada perubahan kodingan disisi produser, maka saya juga harus merubah kodingan di sisi consumer, kalau tidak maka consumer
akan error. Produser disini seolah-olah diberi kebebasan karna sama sekali tidak terikat dengan kontrak. Itu artinya kontrak
menjadi tidak berguna karna consumer sekarang taunya object produser bukannya si kontrak. Padahal harusnya sebaliknya, consumer
hanya perlu tau kontrak, tidak perlu tau object produser.

``` go
func UpdateUser(userRepoImpl UserRepository) error {
    ...
}
```

pada kode diatas, saya menaruh `userRepoImpl` sebagai argument dengan type data `UserRepository`, yang mana adalah si kontrak.
Inilah yang namanya Dependency Injection. Object produser saya lewatkan sebagai argument dari fungsi consumer, tapi saya mengikat
object tersebut dengan kontrak dengan membuat tipe data atau constructornya nya adalah `UserRepository`. Sehingga, sekarang consumer
taunya hanya tipe data kontrak tersebut, tidak peduli object produsernya. Mau saya merubah atau mengganti kode produser kayak
gimanapun, selama object produsernya mengikuti kontrak, consumer tidak perduli dan tidak akan error, karna sudah dipastikan tipe
data dan kontraknya akan selalu sama. Kebanyakan bahasa pemrograman juga bisa membantu memvalidasi kecocokan object dengan kontrak
pada proses compiling atau build, sehingga tidak perlu khawatir lagi terjadi runtime error.

### Usage differential

Secara penggunaan antara pakai Dependency Injection dan tidak juga sangat berbeda. Tanpa dependency injection, saya pakai
consumernya seperti ini:

``` go
func main() {
    if err : UpdateUser(); err ! nil {
        panic(err)
    }
}
```

sedangkan kalau pakai Dependency Injection seperti ini:

``` go
func main() {
    userRepoImpl := userRepositoryPostgres{}
    
    if err := UpdateUser(userRepoImpl); err != nil {
        panic(err)
    }
}
```

kalau saya mau pakai beberapa database sekaligus, saya tinggal buat seperti ini:

``` go
func main() {
    userRepoImplPostgres := userRepositoryPostgres{}
    userRepoImplMySQL := userRepositoryMySQL{}
    userRepoImplMongo := userRepositoryMongo{}
    userRepoImplElastic := userRepositoryElastic{}
    
    // Update user ke database postgres
    if err := UpdateUser(userRepoImplPostgres); err != nil {
        panic(err)
    }
    
    // Update user ke database MySQL
    if err := UpdateUser(userRepoImplMySQL); err != nil {
        panic(err)
    }
    
    // Update user ke database Mongo
    if err := UpdateUser(userRepoImplMongo); err != nil {
        panic(err)
    }
    
    // Update user ke Elasticsearch
    if err := UpdateUser(userRepoImplElastic); err != nil {
        panic(err)
    }
}
```

Kita bisa lihat diatas saya cuma pakai 1 consumer yang sama yaitu `UpdateUser` untuk update ke banyak database, karna semua
produser diatas kontraknya sama. Bayangkan kalau tanpa pakai Dependency Injection, maka saya harus antara membuat ulang consumer
baru untuk masing-masing database, atau saya harus merubah kodingan consumer dan menambahkan logic agar bisa kompatible terhadap
masing-masing database.

Semoga dapat dimengerti ya dengan contoh diatas.

## Now I Have A Single Fat Repository Pattern

Ok sekarang, apakah pattern diatas sudah cukup? Sayangnya saya rasa belum. Saya melihat bahwa pattern diatas masih belum cukup
fleksibel. Kontrak `UserRepository` diatas memang terlihat simpel, tapi sebenarnya tidak. Kalau kalian sadar, 1 kontrak tersebut
memiliki banyak sekali method dengan tugas yang berbeda-beda. Ada method buat get data, ada yang buat insert, update dan delete.
Ini dinamakan dengan istilah Single Fat Interface, artinya suatu kontrak interface yang sangat gemuk karna memiliki beragam tugas
atau method yang berbeda-beda.

### So, what's the problem here?

Diatas saya menjelaskan bahwa sebuah produser harus selalu mengukuti kontrak, artinya dia harus mengimplementasi semua fungsi-fungsi
dari kontrak tersebut. Disinilah masalahnya. Dalam banyak kasus pengembangan, pattern ini selalu menimbulkan masalah. Kebutuhan bisnis
selalu berubah-ubah, bahkan kadang hampir setiap saat. Alasan klasisknya ya karna menyesuaikan kebutuhan user, performance improvement,
securtity dan cost efisiensi. Sebagai contoh, anggaplah bahwa dari kontrak `UserRepository`, saya butuh merubah get data user ke elastic,
dan insert user ke mongo. Ini contoh saja jangan pikirkan make sense atau tidaknya. Maka, apa yang harus saya lakukan? tentunya saya
harus membuat 3 produser kan? produser untuk postgres, elastic dan mongo:

``` go
type userRepositoryPostgres struct {
    db interface{} // saya mock jadi interface saja
}
 
func (u *userRepositoryPostgres) FindOne(queryFilter UserQueryFilter) (*User, error) {
    // disini saya query SELECT ke postgres
	...
}
 
func (u *userRepositoryPostgres) FindAll(queryFilter UserQueryFilter) (Users, error) {
    // disini saya query SELECT ke postgres
	...
}

func (u *userRepositoryPostgres) Insert(data *User) error {
    // disini saya query INSERT ke postgres
	...
}
 
func (u *userRepositoryPostgres) Update(data *User) error {
    // disini saya query UPDATE ke postgres
	...
}
  
func (u *userRepositoryPostgres) Delete(data *User) error {
    // disini saya query DELETE ke postgres
	...
}

type userRepositoryElastic struct {
    db interface{}
}

func (u *userRepositoryElastic) FindOne(queryFilter UserQueryFilter) (*User, error) {
    // disini saya get data dari elastic
	...
}

func (u *userRepositoryElastic) FindAll(queryFilter UserQueryFilter) (Users, error) {
    // disini saya get all data dari elastic
	...
}

func (u *userRepositoryElastic) Insert(data *User) error {
    // disini saya insert data ke elastic
	...
}

func (u *userRepositoryElastic) Update(data *User) error {
    // disini saya update data ke elastic
	...
}

func (u *userRepositoryElastic) Delete(data *User) error {
    // disini saya delete data ke elastic
	...
}

type userRepositoryMongo struct {}

func (u *userRepositoryMongo) FindOne(queryFilter UserQueryFilter) (*User, error) {}

func (u *userRepositoryMongo) FindAll(queryFilter UserQueryFilter) (Users, error) {}

func (u *userRepositoryMongo) Insert(data *User) error {}

func (u *userRepositoryMongo) Update(data *User) error {}

func (u *userRepositoryMongo) Delete(data *User) error {}
```

Nah, kalian bisa lihat diatas saya membuat 3 produser, tapi saya harus mengimplementasi semua fungsi-fungsinya karna memang
harus mengikuti kontrak. Padahal, saya hanya ingin fungsi get data saja yang ke elastic dan fungsi insert ke mongo, sisanya
masih tetap ke postgres. Karena semua fungsinya berada dalam 1 kontrak interface yang sama, maka mau tidak mau saya harus
tetap mengimplementasi semua fungsi-fungsi nya, meskipun sebenearnya saya hanya butuh sebagian saja. Saya bisa saja melakukan
dummy implementasi dengan memakai misal `fmt.Println("implement me!")` untuk fungsi-fungsi yang tidak dibutuhkan, tapi ini sangat
membingungkan, jelek dan tidak acceptable. Saya tidak suka. Kenapa saya harus mengerjakan sesuatu yang tidak dibutuhkan? 

## Let's Change It To CQRS (Command Query Responsibility Segregation)

Masalah diatas, bisa saya solve dengan memakai design pattern selanjutnya yang ini, yaitu CQRS (Command Query Responsibility Segregation).
Inti dari pattern ini adalah alih-alih saya membuat 1 kontrak dengan berbagai macam tugas, sekarang saya membuat beberapa kontrak dengan
memisahkan tugasnya masing-masing. Sebagai contoh, kontrak `UserRepository` diatas saya bisa ubah menjadi seperti ini:

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

Kita lihat diatas dibagi menjadi 4 macam kontrak: `Finder`, `Inserter`, `Updater`, `Deleter`. Finder disini adalah
kontrak untuk semua tugas yang berhubungan dengan mendapatkan data user. Inserter untuk yang behubungan dengan menambah data user,
Updater untuk merubah data user dan Deleter untuk menghapus data user. Karna tugas-tugasnya sekarang sudah dipisah, maka implementasi
produsernya menjadi lebih proper karna jadi terfokus.

### Let's implement the producer!

Tetap ada 3 produser, masing-masing untuk elastic, mongo dan postgres. Bedanya sekarang implementasi kontraknya sebagai berikut:

> Saya akan buat untuk producer postgres mengimplementasi ke 4 kontrak diatas agar memudahkan pemahaman lebih lanjut

``` go

// Producer elastic

type userRepositoryFinderElastic struct {}

func (u *userRepositoryFinderElastic) FindOne(queryFilter UserQueryFilter) (*User, error) {}

func (u *userRepositoryFinderElastic) FindAll(queryFilter UserQueryFilter) (Users, error) {}

// Producer mongo

type userRepositoryInserterMongo struct {}

func (u *userRepositoryInserterMongo) Insert(data *User) error {} 

// Producer postgres

type userRepositoryFinderPostgres struct {}

func (u *userRepositoryFinderPostgres) FindOne(queryFilter UserQueryFilter) (*User, error) {}

func (u *userRepositoryFinderPostgres) FindAll(queryFilter UserQueryFilter) (Users, error) {}

type userRepositoryInserterPostgres struct {}

func (u *userRepositoryInserterPostgres) Insert(data *User) error {} 

type userRepositoryUpdaterPostgres struct {}

func (u *userRepositoryUpdaterPostgres) Update(data *User) error {}

type userRepositoryDeleterPostgres struct {}

func (u *userRepositoryDeleterPostgres) Delete(data *User) error {}
```

### The breakdown!

Kalian bisa lihat, pada produser elastic, saya tidak perlu implement fungsi Insert, Update dan Delete, karna berdasarkan kebutuhan
diatas ini tidak diperlukan. Begitu juga dengan produser mongo. Sekarang semua tugas-tugas nya sudah dikelompokan dan tidak akan
saling ketergantungan. Jika butuh perubahan pada tugas tertentu, maka hanya tugas itulah yang diubah, tidak boleh ikut bergantung dan
merubah tugas yang lain, sehingga meminimalisir pekerjaan pada hal-hal yang tidak diperlukan. Secara penggunaan dari sisi consumer
juga jadi lebih fleksibel.

Sebagai contoh, sebelumnya saya hanya mempunyai 1 consumer `UpdateUser` dengan memakai kontrak `UserRepository`. Kali ini saya akan
mengubahnya dan membuat consumer baru untuk melakukan management data user sebagai berikut:

> Mulai dari sekarang, kontrak `UserRepository` tidak terpakai lagi karena sudah tidak relevan

``` go
func FindAllUser(userRepoFinderImpl UserRepositoryFinder) (Users, error) {        
    return userRepoFinderImpl.FindAll({})
}

func InsertUser(userRepoInserterImpl UserRepositoryInserter) error {
    user := User{
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
    if user  nil {
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
    if user  nil {
        return errors.New("user not found")
    }
    
    // Delete user
    if err = userRepoDeleterImpl.Delete(user); err != nil {
        return err
    }
    
    return nil
}
```

Dengan demikian, sekarang consumer nya menjadi sangat fleksibel, tidak lagi menginject 1 kontrak besar. Semua yang diinject
adalah semua tugas-tugas yang memang dibutuhkan oleh si consumer saja. Selain itu, saya juga bisa dengan leluasa
mengubah-ubah kebutuhan bisnis sumber data secara spesifik tanpa khawatir harus mengimplementasi semua yang tidak dibutuhkan.
Berikut adalah contoh penggunaan consumer sesuai kebutuhan saya diatas:

``` go

// Elastic producer

userRepoFinderImplElastic := &userRepositoryFinderElastic{}

// Mongo producer

userRepoInserterImplMongo := &userRepositoryInserterMongo{}

// Postgres producer

userRepoFinderImplPostgres := &userRepositoryFinderPostgres{}
userRepoInserterImplPostgres := &userRepositoryInserterPostgres{}
userRepoUpdaterImplPostgres := &userRepositoryUpdaterPostgres{}
userRepoDeleterImplPostgres := &userRepositoryDeleterPostgres{}

// Insert data user ke mongo

if err := InsertUser(userRepoInserterImplMongo); err != nil {
    panic(err)
}

// Get data user dari elastic

users, err := FindAllUser(userRepoFinderImplElastic)
if err != nil {
    panic(err)
}

fmt.Println(users)

// Update dan delete ke postgres, tapi check user exists dari elastic

if err = UpdateUser(userRepoFinderImplElastic, userRepoUpdaterImplPostgres); err != nil {
    panic(err)
}

if err = DeleteUser(userRepoFinderImplElastic, userRepoDeleterImplPostgres); err != nil {
    panic(err)
}

// CRUD ke postgres seperti normal flow diawal

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
```

Lihatlah betapa mudahnya saya mengubah-ubah kebutuhan bisnis sumber data diatas. Hanya dengan consumer dan kontrak yang sama, cukup
ubah-ubah implementasi produsernya saja, beres.

## I Can't Find That The Pattern Can Be Used When talking About The Result

## I Need To Separate Them Using The Interface Segregation Principle (ISP)

## Adapter Pattern Will Be Helpful

## The Final Take

Akhirnya, untuk sekarang, design pattern interface yang saya pakai untuk memenuhi ekspektasi dan kebutuhan saya diatas adalah
Dependency Injection + mix antara CQRS dan ISP. Saya merasa pattern ini cukup balance antara complexity dan simplicity, cukup
fleksibel dan pastinya masih sangat humanable untuk dibaca. Untuk Adapter Pattern ini opsional, tapi karna saya berencana untuk
membuat reusable adapter dalam berbagai driver database, jadi saya akan pakai pattern ini kedepannya, toh juga tidak akan mengganggu
design pattern utama.

Jadi, final design pattern yang saya ambil adalah Dependency Injection + Mix CQRS & ISP + Adapter pattern. Sekian terima kasih,
semoga bisa membantu.

!!! info

    Untuk todo example di Uwais, saya masih akan pakai basic Repository pattern karna buat contoh project generator tidak perlu
    design pattern yang kompleks. Nanti biar developernya yang mengganti sesuai selera.
