---
title: Finding The Best Design Pattern For Interfaces
description:
keywords: design, interface, pattern
date: 2025-08-19
pin: false
authors:
  - dalikewara
links:
categories:
  - design pattern
tags:
  - design
  - pattern
  - interface
---

# Finding The Best Design Pattern For Interfaces

Design pattern adalah sebuah konsep yang sangat berguna dalam pembuatan program. Konsep ini memastikan alur dari kode program
kita tetap konsisten dan terstruktur, sehingga mempermudah pekerjaan. Saya pribadi sangat menjunjung tinggi design pattern dan
menganggap bahwa konsep ini wajib sekali diterapkan dalam setiap pembuatan program. Bukan berarti saya sangat jago disini, tapi
maksud saya adalah harus ada pattern yang konsisten.

Lagipula, penerapan dari teori design pattern ini pasti berbeda-beda tiap individu. Terserah mau kita menguasai ISP (Interface Segregation Principle),
CQRS (Command Query Responsibility Segregation) atau apapun itu, pasti tiap orang berbeda dalam hal implementasi. Ada yang strict mengikuti 1 pattern,
ada yang mengadopsi lebih dari 1, ada juga yang mencampurkan beberapa pattern, bahkan ada yang ngasal. It's ok, yang penting ada sebuah standart yang
kita buat untuk diikuti. Tinggal nanti kita buat dokumentasi menjelaskan cara kerja pattern yang kita buat, beres.

!!! warning

    Jangan mulai ngoding sebelum tahu pattern apa yang akan diterapkan!

<!-- more -->

Saya sendiri selalu mencari pattern terbaik untuk project-project yang saya buat. Saya pernah terjebak mengikuti pattern buatan orang lain
ketika sedang dalam project kolaborasi—yang design patternnya sangat ribet untuk diikuti. Saya tidak membenci cara implementasinya, saya hanya
membenci sesuatu yang ribet—apalagi jika tidak ada dokumentasinya.

Perjalanan saya dalam mencari design pattern untuk interface ini dimulai dengan konsep yang cukup simple...

> untuk selanjutnya, saya akan pakai contoh menggunakan golang. Nggak ada alasan khusus, saya cuma suka Golang.
> Tapi perlu diingat, disini saya menggunakan pendekatan yang lebih universal supaya mudah dipahami, jadi agak mengesampingkan idiomatic di Golang

## Repository Pattern

Konsep pattern ini tujuannya untuk memisahkan domain atau use case bisnis dari sumber data. logical bisnis tidak perlu tahu data kita
disimpan dimana, entah itu di database sql, nosql, file, elastic atau yang lain. Dan tidak perlu tahu juga metode eksekusi nya seperti apa,
apakah itu via query langsung ke db atau via http service. terdengar sangat bagus dan make sense bukan, jadilah berikut interface yang saya buat:

``` go
type UserRepository interface {
	FindOne(queryFilter UserQueryFilter) (*User, error)
	FindAll(queryFilter UserQueryFilter) (Users, error)
	Insert(data *User) error
	Update(data *User) error
	Delete(data *User) error
}
```

Pattern ini Simple dan mudah dimengerti. tanpa dokumentasipun, kita bisa tahu fungsi dan tujuan interface ini untuk apa, yaitu untuk melakukan CRUD ke sumber data.
Bisnis logic cukup tau kontrak interface dari UserRepository saja, yang mana mengharuskan implementator wajib memiliki method-method sesuai dengan
kontrak, yaitu: FindOne, FindAll, Insert, Update, Delete lengkap dengan dengan spesifikasinya (argument dan result). Sebagai contoh, dibawah ini
saya mencoba membuat gambaran implementator CRUD ke database postgres:

``` go
type userRepositoryPostgres struct {
	db *pgxpool.Pool // Contoh jika drivernya pakai pgxpool
}

func (u *userRepositoryPostgres) FindOne(queryFilter UserQueryFilter) (*User, error) {
	// disini kita query SELECT ke postgres
}

func (u *userRepositoryPostgres) FindAll(queryFilter UserQueryFilter) (Users, error) {
	// disini kita query SELECT ke postgres
}

func (u *userRepositoryPostgres) Insert(data *User) error {
	// disini kita query INSERT ke postgres
}

func (u *userRepositoryPostgres) Update(data *User) error {
	// disini kita query UPDATE ke postgres
}

func (u *userRepositoryPostgres) Delete(data *User) error {
	// disini kita query DELETE ke postgres
}
```

> Anggap saja struct adalah sebuah object

Kita lihat bahwa object userRepositoryPostgres ini memiliki method dan spesifikasi yang sama persis dengan interface UserRepository.
Hal ini karna userRepositoryPostgres adalah implementator dari interface UserRepository, jadi dia harus mengimplementasi semua spesifikasi
sesuai kontraknya dengan sama persis.

Nah, nanti di dalam bisnis logic, implementator ini yang akan dipanggil, karena dialah yang punya hasil implementasi nyata dari proses CRUDnya. Tapi,
bisnis logic akan mengorkestrasinya berdasarkan kontrak dari interface UserRepository. Sehingga, apabila suatu saat kita ingin mengganti implementator
dari postgres ke mongodb, kita cukup buat sebuah object baru yang mengemplimentasi kontrak interface UserRepository, maka bisnis logic tidak akan rusak atau error,
karena kontrak interfacenya sama, yang artinya method-method dan spesifikainya pun juga pasti sama.

Tapi kemudian, bagaimana cara bisnis logic mengorkestrasi hal ini?

## Dependency Injection

Inilah caranya agar bisnis logic bisa mengorkestrasi implementator. Dependency injection adalah sebuah konsep dimana kita menginject dependency dari luar
menggunakan sebuah kontrak sebagai tipe data atau constructor. Sebagai contoh, alih-alih kita langsung memanggil object implementator didalam bisnis logic
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

Kita bisa ubah supaya menggunakan dependency injection seperti ini:

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

