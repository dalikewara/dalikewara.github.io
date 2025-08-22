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
kita tetap konsisten dan terstruktur, sehingga mempermudah segala hal yang berhubungan dengan pengembangan. Saya pribadi sangat
menjunjung tinggi design pattern dan menganggap bahwa konsep ini wajib sekali diterapkan dalam setiap pembuatan program. Bukan
berarti saya sangat jago disini, tapi maksud saya adalah harus ada pattern yang konsisten.

<!-- more -->

Lagipula, penerapan dari teori design
pattern ini pasti berbeda-beda tiap individu. Terserah mau kita menguasai ISP (Interface Segregation Principle), CQRS (Command Query Responsibility Segregation)
atau apapun itu, pasti tiap orang berbeda dalam hal implementasi. Ada yang strict mengikuti 1 pattern, ada yang mengadopsi lebih dari 1, ada juga yang
mencampurkan beberapa pattern, bahkan ada yang ngasal. It's ok, yang penting ada sebuah standart yang kita buat untuk diikuti. Tinggal nanti kita buat
dokumentasi menjelaskan cara kerja pattern yang kita buat, beres.

!!! warning

    Jangan mulai ngoding sebelum kita tahu pattern apa yang akan kita buat!

Saya sendiri selalu mencari pattern terbaik untuk project-project yang saya buat. Saya juga pernah terjebak mengikuti pattern buatan orang lain
ketika sedang dalam project kolaborasi—yang design patternnya sangat ribet untuk diikuti. Saya tidak membenci cara implementasinya, saya hanya
membenci sesuatu yang ribet—apalagi jika tidak ada dokumentasinya.

Perjalanan saya dalam mencari design pattern untuk interface ini dimulai dengan konsep yang cukup simple berikut:

> untuk selanjutnya, saya akan pakai contoh menggunakan golang

## Repository Pattern

Konsep pattern ini tujuannya untuk memisahkan domain atau use case bisnis dari sumber data. logical bisnis tidak perlu tahu data kita
disimpan dimana, entah itu di database sql, nosql, file, elastic atau yang lain. Dan tidak perlu tahu juga metode eksekusi nya seperti apa,
apakah itu via query langsung ke db atau via http service. terdengar bagus dan make sense bukan, jadilah berikut implementasi konsep yang saya buat:

``` go
type UserRepository interface {
	FindOneCtx(ctx context.Context, queryFilter UserQueryFilter) (*User, error)
	FindAllCtx(ctx context.Context, queryFilter UserQueryFilter) (Users, error)
	InsertCtx(ctx context.Context, data *User) error
	UpdateCtx(ctx context.Context, data *User) error
	DeleteCtx(ctx context.Context, data *User) error
}
```

Simple dan mudah dimengerti. tanpa dokumentasipun, kita bisa tahu fungsi dan tujuan interface ini untuk apa, yaitu untuk melakukan CRUD ke sumber data.
Kalau di golang, implementasinya juga sangat simple:

``` go
type userRepository struct {
	db interface{} // Contoh jika pakai database
}

func (u *userRepository) FindOneCtx(ctx context.Context, queryFilter UserQueryFilter) (*User, error) {
	panic("implement me")
}

func (u *userRepository) FindAllCtx(ctx context.Context, queryFilter UserQueryFilter) (Users, error) {
	panic("implement me")
}

func (u *userRepository) InsertCtx(ctx context.Context, data *User) error {
	panic("implement me")
}

func (u *userRepository) UpdateCtx(ctx context.Context, data *User) error {
	panic("implement me")
}

func (u *userRepository) DeleteCtx(ctx context.Context, data *User) error {
	panic("implement me")
}

func NewUserRepository(db interface{}) UserRepository {
	return &userRepository{
		db: db,
	}
}
```