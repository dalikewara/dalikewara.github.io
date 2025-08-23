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

# Finding The Best Design Pattern For Interfaces

Design Pattern adalah sebuah konsep yang sangat berguna dalam pembuatan program. Konsep ini memastikan alur dari kode program
tetap konsisten dan terstruktur, sehingga mempermudah pekerjaan. Saya pribadi sangat menjunjung tinggi design pattern dan
menganggap bahwa konsep ini wajib sekali diterapkan dalam setiap pembuatan program. Bukan berarti saya sangat jago disini, tapi
maksud saya adalah harus ada pattern yang konsisten.

Lagipula, penerapan dari teori design pattern ini pasti berbeda-beda tiap individu. Terserah mau kita menguasai ISP
(Interface Segregation Principle), CQRS (Command Query Responsibility Segregation) atau apapun itu, pasti tiap orang berbeda
dalam hal implementasi. Ada yang strict mengikuti 1 pattern, ada yang mengadopsi lebih dari 1, ada juga yang mencampurkan beberapa
pattern, bahkan ada yang ngasal. It's ok, yang penting ada sebuah standart yang dibuat untuk diikuti. Tinggal nanti dibikin
dokumentasi menjelaskan cara kerja patternnya, beres.

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

Konsep pattern ini tujuannya untuk menyediakan abstraksi atau kontrak untuk memisahkan domainnya (provider) dengan logical
bisnis utama (consumer). Pattern ini kebanyakan dipakai untuk abstraksi detail teknis sumber data (repository) seperti database,
tapi sebernarnya bisa juga dipakai untuk layer lain seperti use case, service, atau bahkan sebuah statement builder. karna intinya
sama, yaitu untuk mencerminkan sebuah kebutuhan bisnis.

Simpelnya, ada provider, consumer dan kontrak. Consumer adalah executor yang memanggil fungsi-fungsi yang disediakan oleh provider.
provider adalah implementator yang menyediakan fungsi-fungsi untuk bisa dipanggil oleh consumer. Nah, kontrak adalah perjanjian
antara provider dan consumer untuk mengikat hubungan antara keduanya. provider harus menyediakan fungsi-fungsinya sesuai dengan
kontrak yang telah disepakati dengan consumer, karena consumer akan melakukan proses bisnisnya berdasarkan kontrak tersebut.
Repository pattern ini adalah desain dari kontrak tersebut.

> Untuk selanjutnya saya akan pakai ketiga istilah ini: provider, consumer, kontrak

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

Kemudian, saya akan memakai postgres sebagai databasenya, sehingga providernya akan seperti ini:

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

kita lihat bahwa object `userRepositoryPostgres` ini memiliki method dan spesifikasi yang sama persis dengan `UserRepository`.
Hal ini karna `userRepositoryPostgres` adalah providernya, jadi dia harus mengimplementasi semua spesifikasi sesuai kontraknya
dengan sama persis.

Nah, nanti di dalam consumer, fungsi-fungsi yang telah disediakan provider ini yang akan dipanggil, karena dialah yang punya hasil
implementasi nyata dari proses CRUDnya. Tapi, consumer akan mengorkestrasinya berdasarkan kontrak. Sehingga, apabila suatu saat saya
ingin mengganti provider dari postgres ke mongodb misal, saya cukup buat sebuah object provider baru yang mengemplimentasi kontrak,
dan consumer tidak akan rusak atau error. Karena kontraknya sama, yang artinya method-method dan spesifikainya pun juga pasti sama.

Tapi kemudian, bagaimana cara consumer mengorkestrasi hal ini?

## With The Dependency Injection, Of Course!

Inilah caranya agar consumer bisa mengorkestrasi provider. Dependency injection adalah sebuah konsep dimana kita menginject dependency dari luar
menggunakan sebuah kontrak sebagai tipe data atau constructor. Sebagai contoh, alih-alih saya langsung memanggil object provider didalam consumer
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

Jika saya langsung memanggil object provider kedalam consumer seperti diatas, itu artinya saya membuat proses bisnis
consumer menjadi ketergantungan terhadap provider. Jika suatu saat saya mau mengganti provider dari postgres ke mongodb, atau
misal ada perubahan kodingan disisi provider, maka saya juga harus merubah kodingan di sisi consumer, kalau tidak maka consumer
akan error. provider disini seolah-olah diberi kebebasan karna sama sekali tidak terikat dengan kontrak. Itu artinya kontrak
menjadi tidak berguna karna consumer sekarang taunya object provider bukannya si kontrak. Padahal harusnya sebaliknya, consumer
hanya perlu tau kontrak, tidak perlu tau object provider.

``` go
func UpdateUser(userRepoImpl UserRepository) error {
    ...
}
```

pada kode diatas, saya menaruh `userRepoImpl` sebagai argument dengan type data `UserRepository`, yang mana adalah si kontrak.
Inilah yang namanya Dependency Injection. Object provider saya lewatkan sebagai argument dari fungsi consumer, tapi saya mengikat
object tersebut dengan kontrak dengan membuat tipe data atau constructornya nya adalah `UserRepository`. Sehingga, sekarang consumer
taunya hanya tipe data kontrak tersebut, tidak peduli object providernya. Mau saya merubah atau mengganti kode provider kayak
gimanapun, selama object providernya mengikuti kontrak, consumer tidak perduli dan tidak akan error, karna sudah dipastikan tipe
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
    userRepoImpl := &userRepositoryPostgres{}
    
    if err := UpdateUser(userRepoImpl); err != nil {
        panic(err)
    }
}
```

kalau saya mau pakai beberapa database sekaligus, saya tinggal buat seperti ini:

``` go
func main() {
    // inisialisasi providers

    userRepoImplPostgres := &userRepositoryPostgres{}
    userRepoImplMySQL := &userRepositoryMySQL{}
    userRepoImplMongo := &userRepositoryMongo{}
    userRepoImplElastic := &userRepositoryElastic{}
    
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

kita bisa lihat diatas saya cuma pakai 1 consumer yang sama yaitu `UpdateUser` untuk update ke banyak database, karna semua
provider diatas kontraknya sama. Bayangkan kalau tanpa pakai Dependency Injection, maka saya harus antara membuat ulang consumer
baru untuk masing-masing database, atau saya harus merubah kodingan consumer dan menambahkan logic agar bisa kompatible terhadap
masing-masing database.

Semoga dapat dimengerti ya dengan contoh diatas.

## Now I Have A Single Fat Repository Pattern

Ok sekarang, apakah pattern diatas sudah cukup? Sayangnya saya rasa belum. Saya melihat bahwa pattern diatas masih belum cukup
fleksibel. Kontrak `UserRepository` diatas memang terlihat simpel, tapi sebenarnya tidak. Kalau kita sadar, 1 kontrak tersebut
memiliki banyak sekali method dengan operasi yang berbeda-beda. Ada method buat get data, ada yang buat insert, update dan delete.
Ini dinamakan dengan istilah Single Fat Interface, artinya suatu kontrak interface yang sangat gemuk karna memiliki beragam operasi
atau method yang berbeda-beda.

### So, what's the problem here?

Diatas saya menjelaskan bahwa sebuah provider harus selalu mengukuti kontrak, artinya dia harus mengimplementasi semua fungsi-fungsi
dari kontrak tersebut. Disinilah masalahnya. Dalam banyak kasus pengembangan, pattern ini selalu menimbulkan masalah. Kebutuhan bisnis
selalu berubah-ubah, bahkan kadang hampir setiap saat. Alasan klasisknya ya karna menyesuaikan kebutuhan user, performance improvement,
securtity dan cost efisiensi. Sebagai contoh, anggaplah bahwa dari kontrak `UserRepository`, saya butuh merubah get data user ke elastic,
dan insert user ke mongo. Ini contoh saja jangan pikirkan make sense atau tidaknya. Maka, apa yang harus saya lakukan? tentunya saya
harus membuat 3 provider kan? provider untuk postgres, elastic dan mongo:

``` go

// provider postgres

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

// provider elastic

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

// provider mongo

type userRepositoryMongo struct {
    db interface{}
}

func (u *userRepositoryMongo) FindOne(queryFilter UserQueryFilter) (*User, error) {
    // disini saya get data dari mongo
	...
}

func (u *userRepositoryMongo) FindAll(queryFilter UserQueryFilter) (Users, error) {
    // disini saya get all data dari mongo
	...
}

func (u *userRepositoryMongo) Insert(data *User) error {
    // disini saya insert data ke mongo
	...
}

func (u *userRepositoryMongo) Update(data *User) error {
    // disini saya update data ke mongo
	...
}

func (u *userRepositoryMongo) Delete(data *User) error {
    // disini saya delete data ke mongo
	...
}
```

Nah, kita bisa lihat diatas saya membuat 3 provider, tapi saya harus mengimplementasi semua fungsi-fungsinya karna memang
harus mengikuti kontrak. Padahal, saya hanya ingin fungsi get data saja yang ke elastic dan fungsi insert ke mongo, sisanya
masih tetap ke postgres. Karena semua fungsinya berada dalam 1 kontrak interface yang sama, maka mau tidak mau saya harus
tetap mengimplementasi semua fungsi-fungsi nya, meskipun sebenearnya saya hanya butuh sebagian saja. Saya bisa saja melakukan
dummy implementasi dengan memakai misal `fmt.Println("implement me!")` untuk fungsi-fungsi yang tidak dibutuhkan, tapi ini sangat
membingungkan, jelek dan tidak acceptable. Saya tidak suka. Kenapa saya harus mengerjakan sesuatu yang tidak dibutuhkan? 

## Let's Change It To CQRS (Command Query Responsibility Segregation)

Dari yang saya baca, konsep design pattern ini adalah untuk memisahkan operasi baca (query) dan tulis (command). Alih-alih
membuat 1 kontrak besar untuk read data dan write data sekaligus, kita pisahkan kedua operasi tersebut menjadi dua kontrak interface `Query` dan `Command`,
atau `Reader` dan `Writer`. Kalau saya coba terapkan, kontrak `UserRepository` diatas bisa dibuat seperti ini:

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

Disini Query adalah kontrak yang berisi fungsi-fungsi untuk get data user, sedangkan Command untuk create, update dan delete user. Ok
terlihat cukup bagus dan make sense. Cuman sepertinya pattern ini hanya bisa mensolve kebutuhan perpindahan ke elastic saja, yang mana hanya untuk
fungsi get data. Tapi sepertinya tidak cukup kuat untuk mensolve kebutuhan perpindahan ke Mongo. Karna yang pindah ke Mongo hanya fungsi insert
saja, Update dan Delete masih ke postgres.

## I Need To Separate Them Using The Interface Segregation Principle (ISP)

Kayaknya Masalah diatas bisa saya solve dengan memakai design pattern selanjutnya yang ini, yaitu Interface Segregation Principle (ISP),
salah satu bagian dari SOLID principle. Pattern ISP ini menyatakan bahwa klien (dalam konteks ini adalah producer dan consumer) tidak
boleh dipaksa untuk bergantung pada fungsi-fungsi yang tidak mereka gunakan. Jadi intinya, daripada saya membuat 1 kontrak dengan berbagai macam operasi,
lebih baik saya membuat beberapa kontrak dengan memisahkan operasinya masing-masing. Namun tidak seperti CQRS, melainkan lebih kecil dan spesifik lagi.
Sebagai contoh, kontrak `UserRepository` diatas saya bisa ubah menjadi seperti ini:

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

kita lihat interface diatas dibagi menjadi 4 macam kontrak: `Finder`, `Inserter`, `Updater`, `Deleter`. Finder disini adalah
kontrak untuk semua operasi yang berhubungan dengan mendapatkan data user. Inserter untuk yang behubungan dengan menambah data user,
Updater untuk merubah data user dan Deleter untuk menghapus data user. Karna operasi-operasinya sekarang sudah dipisah, maka implementasi
providernya menjadi lebih proper karna jadi terfokus. Dan kebutuhan saya diatas jadi bisa diimplementasi.

### Let's implement the provider!

Tetap ada 3 provider, masing-masing untuk elastic, mongo dan postgres. Bedanya sekarang implementasi kontraknya sebagai berikut:

> Saya akan buat untuk provider postgres mengimplementasi ke 4 kontrak diatas agar memudahkan pemahaman lebih lanjut

``` go

// provider elastic

type userRepositoryFinderElastic struct {
    db interface{}
}

func (u *userRepositoryFinderElastic) FindOne(queryFilter UserQueryFilter) (*User, error) {
    // disini saya get data dari elastic
	...
}

func (u *userRepositoryFinderElastic) FindAll(queryFilter UserQueryFilter) (Users, error) {
    // disini saya get all data dari elastic
	...
}

// provider mongo

type userRepositoryInserterMongo struct {
    db interface{}
}

func (u *userRepositoryInserterMongo) Insert(data *User) error {
    // disini saya insert data ke mongo
	...
} 

// provider postgres

type userRepositoryFinderPostgres struct {
    db interface{}
}

func (u *userRepositoryFinderPostgres) FindOne(queryFilter UserQueryFilter) (*User, error) {
    // disini saya query SELECT ke postgres
	...
}

func (u *userRepositoryFinderPostgres) FindAll(queryFilter UserQueryFilter) (Users, error) {
    // disini saya query SELECT ke postgres
	...
}

type userRepositoryInserterPostgres struct {
    db interface{}
}

func (u *userRepositoryInserterPostgres) Insert(data *User) error {
    // disini saya query INSERT ke postgres
	...
} 

type userRepositoryUpdaterPostgres struct {
    db interface{}
}

func (u *userRepositoryUpdaterPostgres) Update(data *User) error {
    // disini saya query UPDATE ke postgres
	...
}

type userRepositoryDeleterPostgres struct {
    db interface{}
}

func (u *userRepositoryDeleterPostgres) Delete(data *User) error {
    // disini saya query DELETE ke postgres
	...
}
```

### The breakdown!

kita bisa lihat, pada provider elastic, saya tidak perlu implement fungsi Insert, Update dan Delete, karna berdasarkan kebutuhan
diatas ini tidak diperlukan. Begitu juga dengan provider mongo, saya tidak perlu implement fungsi get data, update dan delete.

Sekarang semua operasi-operasi nya sudah dikelompokan dan tidak akan saling ketergantungan. Jika butuh perubahan pada operasi tertentu,
maka hanya operasi itulah yang diubah, tidak boleh ikut bergantung dan merubah operasi yang lain, sehingga meminimalisir pekerjaan
pada hal-hal yang tidak diperlukan. Secara penggunaan dari sisi consumer juga jadi lebih fleksibel.

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
adalah semua operasi-operasi yang memang dibutuhkan oleh si consumer saja. Selain itu, saya juga bisa dengan leluasa
mengubah-ubah kebutuhan bisnis sumber data secara spesifik (tidak hanya ganti database, tapi berlaku juga misal saya ganti driver dari
`pgxpool` ke `sqlx` atau bahkan orm seperti `goqu`) tanpa khawatir harus mengimplementasi semua yang tidak dibutuhkan.
Berikut adalah contoh penggunaan consumer sesuai kebutuhan saya diatas:

``` go
func main() {
    // Inisialisasi Elastic provider
    
    userRepoFinderImplElastic := &userRepositoryFinderElastic{}
    
    // Inisialisasi Mongo provider
    
    userRepoInserterImplMongo := &userRepositoryInserterMongo{}
    
    // Inisialisasi Postgres provider
    
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
}
```

Lihatlah betapa mudahnya saya mengubah-ubah kebutuhan bisnis sumber data diatas. Hanya dengan consumer dan kontrak yang sama, cukup
ubah providernya saja, beres.

## I Can't Find That The Pattern Can Be Used When talking About The Result

## Specialized ISP

## Adapter Pattern Will Be Helpful

Dalam kasus perubahan kebutuhan sumber data: dari postgres -> mongo, postgres -> elastic, mongo -> http service, ini
sebenarnya yang berubah hanyalah cara query dan parsing resultnya saja. Misal postgres biasa pakai RAW Query sedangkan mongo, elastic dan http service
biasa pakai object. Result juga biasanya tergantung driver/client/sdk, ada yang pakai scanner ada juga yang parsing struct atau object.
Memang sih flow masing-masing client tersebut beda-beda caranya. Tapi dengan design pattern Specialized ISP diatas hal ini bukan menjadi suatu masalah,
karna perbedaan flow tersebut diimplemntasinya di masing-masing provider. Tapi mungkin pattern ini bisa membantu dalam beberapa kasus.

### First Case Example

Database nya sama pakai postgres, tapi client nya beda, yang satu pakai `pgxpool` yang satu pakai `sqlx`:

``` go hl_lines="14 15 16 17 38 39 40"
// provider postgres pakai pgxpool

type userRepositoryFinderPGXPool struct {
    db interface{}
}

func (u *userRepositoryFinderPGXPool) FindOne(queryFilter UserQueryFilter) (*User, error) {
    if queryFilter.ID < 1 {
        return nil, nil
    }
    
    var user User
    
    // context disini hanya contoh saja, idiomatic di Golang ini ditaruh sebagai first argument: `ctx context.Context`
	if err := u.db.QueryRow(context.Background(), `SELECT name, created_at, updated_at FROM users WHERE id = $1`, queryFilter.ID).Scan(&user.Name, &user.CreatedAt, &user.UpdatedAt); err != nil {
	    return nil, err
	}
	
	user.SetFormattedCreatedAt()
	user.SetFormattedUpdatedAt()
	
	return &user, nil
}

// provider postgres pakai sqlx

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

Dari kode diatas bisa dilihat bahwa secara flow yang berbeda hanya yang di highlight saja, selain itu flownya sama antara keduanya.
Bukankah akan lebih baik jika tidak perlu menulis ulang flow yang sama tersebut?

### Second Case example

misal saya punya fungsi untuk create order. Didalam proses create order tersebut, ada proses insert data order dan update stock product.
Kemudian, anggap saja saya butuh untuk menggunakan Transaction supaya data ordernya valid, kurang lebih seperti ini providernya:

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

lalu di sisi consumer:

> Anggap saja kontraknya adalah `OrderRepositoryInserter` dan `ProductRepositoryUpdater`

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

Nah, ini baru masalah serius, karna disitu saya memakai object/interface transaction `pgx.Tx` dari client `pgxpool` secara langsung dan menginject objectnya sebagai depedency ke argument
fungsi `InsertTx` dan `UpdateTx`. Serta di dalam consumernya sendiri saya memanggil `tx.Rollback()` dan `tx.Commit()`, yang mana method ini berasal dari object
`pgx.Tx` tadi. Itu artinya, saya telah membuat baik kontrak, provider maupun consumer nya punya ketergantungan dengan object external `pgxpool` dan `pgx.Tx`.
Secara otomatis ini akan menggugurkan konsep design pattern yang sudah dibuat diatas, karna design pattern nya itu tidak boleh punya ketergantungan apapun dengan object external.
Kalau saya mau ubah dari `pgxpool` ke `sqlx`, maka saya sudah pasti harus merubah kontrak, provider dan consumer, mengganti object transaksi dari `pgxpool` ke `sqlx`.
Harusnya tidak boleh seperti itu.

### Now we get the usage of this pattern

Nah, disinilah peran Adapter Pattern dibutuhkan, karena tujuan pattern ini adalah untuk mengubah sebuah object/interface menjadi kontrak interface standart baru yang diharapkan oleh klien.
Artinya, kita mengubah object/interface `pgxpool` dan `sqlx` menjadi sebuah interface yang kita buat sendiri sebagai standart. Contoh, proses sumber data selalu punya operasi read dan write.
Kita bisa bikin kontrak standart untuk itu:

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

Nanti, di sisi provider, argument yang diinject adalah kontrak dari adapter ini, contoh:

``` go
type orderRepositoryInserterPGXPool struct {
    db SourceAdapter
}

func (u *orderRepositoryInserterPGXPool) BeginTx() (SourceAdapterTx, error) {
    return u.db.BeginTx()
}

func (u *orderRepositoryInserterPGXPool) InsertTx(tx SourceAdapterTx, order *Order) error {
    ...
}
```

Dengan begini, masalah ketergantungan terselesaikan. Jika saya ubah dari `pgxpool` ke `sqlx`, saya hanya perlu membuat para client tersebut
mengimplementasi kontrak `SourceAdapter`, maka consumer diatas tidak akan error dan tidak ada yang perlu diubah. Metodenya sama persis dengan
design pattern yang awal-awal diatas, cuman bedanya disini kita pakai istilah Adapter Pattern. Contoh:

``` go
type pgxPoolAdapter struct {
	db *pgxpool.Pool
}

func (p *pgxPoolAdapter) BeginTx() (SourceAdapterTx, error) {
    // Contoh supaya pgxpool mereturn `(SourceAdapterTx, error)` sesuai kontrak
    
	tx, err := u.db.BeginTx(context.Background(), pgx.TxOptions{})
	if err != nil {
	    return nil, err
	}
	
	return &pgxPoolAdapterTx{ tx: tx }, nil
}

func (p *pgxPoolAdapter) QueryOne(query interface{}, args ...interface{}) (SourceRow, error) {
    // implement supaya pgxpool mengolah argument `query interface{}, args ...interface{}` dan mereturn `(SourceRow, error)` sesuai kontrak
	...
}

func (p *pgxPoolAdapter) QueryAll(query interface{}, args ...interface{}) (SourceRows, error) (SourceAdapterRows, SourceAdapterErr) {
    // implement supaya pgxpool mengolah argument `query interface{}, args ...interface{}` dan mereturn `(SourceAdapterRows, error)` sesuai kontrak
	...
}

func (p *pgxPoolAdapter) Exec(query interface{}, args ...interface{}) (SourceResult, error) {
    // implement supaya pgxpool mengolah argument `query interface{}, args ...interface{}` dan mereturn `(SourceResult, error)` sesuai kontrak
	...
}

func NewPGXPoolAdapter(db *pgxpool.Pool) SourceAdapter {
	return &pgxPoolAdapter{
		db: db,
	}
}
```

### There is also drawbacks for this

Kekurangannya, kita jadi harus coding untuk implementasi merubah object external tersebut agar mengikuti kontrak Adapter Pattern yang kita buat.
Ini biasanya butuh extra effort. Karena kan flownya beda-beda setiap client jadi penyesuaiannya juga beda-beda, agak tricky. Kadang kita juga 
harus memikirkan gimana membuat sebuah Adapter Pattern yang kompatible untuk semua sdk/client.

Saya bisa bilang pattern ini opsional saja. Tapi begitu kita sudah buat implementasi provider adapternya maka selanjutnya akan lebih mudah.
karna akan jadi banyak hal yang bisa terstandarisasi kedepannya, sehingga akan memudahkan migrasi dan mengadopsi peruibahan-perubahan dengan
mudah tanpa harus merubah proses bisnis. Issue pada contoh kasus pertama diatas juga bisa diselesaikan dengan Adapter Pattern.

## The Final Take, For The Current Moment

Akhirnya, untuk saat ini, design pattern interface terbaik yang saya pakai untuk memenuhi ekspektasi dan kebutuhan saya diatas adalah
Dependency Injection dan Specialized ISP. Saya merasa pattern ini sudah cukup balance antara complexity dan simplicity, cukup
fleksibel dan pastinya masih sangat humanable untuk dibaca. Untuk Adapter Pattern ini opsional, tapi karna saya berencana untuk
membuat reusable adapter dalam berbagai driver database, jadi saya akan pakai pattern ini kedepannya, toh juga tidak akan mengganggu
design pattern utama.

Jadi, final design pattern yang saya ambil adalah Dependency Injection + Specialized ISP + Adapter Pattern. Sekian terima kasih,
semoga bisa membantu.

Untuk todo example di Uwais, saya masih akan pakai basic Repository pattern karna buat contoh project generator tidak perlu
design pattern yang kompleks. Nanti biar developernya yang mengganti sesuai selera.
