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

> untuk selanjutnya, saya akan pakai contoh menggunakan golang. Nggak ada alasan khusus, saya cuma suka Golang karna simpel.
> Tapi perlu diingat, disini saya menggunakan pendekatan yang lebih universal supaya mudah dipahami, jadi agak mengesampingkan
> idiomatic di Golang

## Repository Pattern

Konsep pattern ini tujuannya untuk menyediakan abstraksi atau kontrak untuk memisahkan domainnya (produser) dengan logical
bisnis utama (consumer). Pattern ini kebanyakan dipakai untuk abstraksi detail teknis sumber data (repository) seperti database,
tapi sebernarnya bisa juga dipakai untuk layer lain seperti use case, service, atau bahkan sebuah statement builder. karna intinya
sama, yaitu untuk mencerminkan sebuah kebutuhan bisnis.

Simpelnya, ada produser, consumer dan kontrak. Consumer adalah executor yang memanggil fungsi-fungsi yang disediakan oleh produser.
produser adalah produser yang menyediakan fungsi-fungsi untuk bisa dipanggil oleh consumer. Nah, kontrak adalah perjanjian
antara produser dan consumer untuk mengikat hubungan antara keduanya. Produser harus menyediakan fungsi-fungsinya sesuai dengan
kontrak yang telah disepakati dengan consumer, karena consumer akan melakukan proses bisnisnya berdasarkan kontrak tersebut.
Repository pattern ini adalah desain kontrak tersebut.

> untuk selanjutnya saya akan pakai ketiga istilah ini: produser, consumer, kontrak

Saya akan mengambil contoh sederhana, yaitu saya akan membuat sebuah kontrak UserRepository untuk melakukan CRUD ke database:

``` go
type UserRepository interface {
	FindOne(queryFilter UserQueryFilter) (*User, error)
	FindAll(queryFilter UserQueryFilter) (Users, error)
	Insert(data *User) error
	Update(data *User) error
	Delete(data *User) error
}
```

Saya akan memakai postgres sebagai databasenya, sehingga produsernya akan seperti ini:

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

Kita lihat bahwa object `userRepositoryPostgres` ini memiliki method dan spesifikasi yang sama persis dengan `UserRepository`.
Hal ini karna `userRepositoryPostgres` adalah produsernya, jadi dia harus mengimplementasi semua spesifikasi sesuai kontraknya
(`UserRepository`) dengan sama persis.

Nah, nanti di dalam consumer, fungsi-fungsi yang telah disediakan produser ini yang akan dipanggil, karena dialah yang punya hasil
implementasi nyata dari proses CRUDnya. Tapi, consumer akan mengorkestrasinya berdasarkan kontrak. Sehingga, apabila suatu saat kita
ingin mengganti produser dari postgres ke mongodb misal, kita cukup buat sebuah object produser baru yang mengemplimentasi kontrak,
dan consumer tidak akan rusak atau error. Karena kontraknya sama, yang artinya method-method dan spesifikainya pun juga pasti sama.

Tapi kemudian, bagaimana cara consumer mengorkestrasi hal ini?

## Dependency Injection

Inilah caranya agar consumer bisa mengorkestrasi produser. Dependency injection adalah sebuah konsep dimana kita menginject dependency dari luar
menggunakan sebuah kontrak sebagai tipe data atau constructor. Sebagai contoh, alih-alih kita langsung memanggil object produser didalam consumer
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

## Single Fat Repository Pattern

## CQRS (Command Query Responsibility Segregation)

## Interface Segregation Principle (ISP)

## Adapter Pattern