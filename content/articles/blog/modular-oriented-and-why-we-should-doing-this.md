---
Title: Modular Oriented - And Why We Should Doing This
Date: 2020-05-22 09:56
Tags: 
- blog
- post
- tips
- opinion
- module
- framework
Description: Di dalam sebuah tim, kita mungkin memakai *framework* sebagai *standart* sistem, dan itu pasti akan sangat membantu sekali. Akan tetapi, yang saya temukan ternyata hal itu masih belum cukup untuk dikatakan efisien. Masih sering ada pekerjaan yang tidak *reusable*, artinya dia ditulis secara *inline-feature*, sehingga butuh *effort* lebih untuk mengimplementasikannya kedalam sistem lain&mdash;atau bahkan tidak bisa sama sekali. Masih sering juga terdapat lebih dari satu *flow* yang sama, namun ditulis ulang di setiap fitur, sehingga membuat *maintenance* menjadi rumit. Hingga masalah klasik seperti perbedaan *style* penulisan *code*, yang terkadang membuat bingung anggota tim.
cover_image: https://images.unsplash.com/photo-1492355040260-cd982083603e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80
---

![search-modular](https://images.unsplash.com/photo-1492355040260-cd982083603e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80)
*Photo by [Simon Goetz](https://unsplash.com/photos/feeredToXK4) on [Unsplash](https://unsplash.com/s/photos/modular)*

Saya menulis tentang `modular oriented` ini adalah karena keresahan atas masalah yang sering saya alami dulu, yaitu tentang efisiensi dalam sebuah *development* sistem / aplikasi.

Di dalam sebuah tim, kita mungkin memakai *framework* sebagai *standart* sistem, dan itu pasti akan sangat membantu sekali. Akan tetapi, yang saya temukan ternyata hal itu masih belum cukup untuk dikatakan efisien. Masih sering ada pekerjaan yang tidak *reusable*, artinya dia ditulis secara *inline-feature*, sehingga butuh *effort* lebih untuk mengimplementasikannya kedalam sistem lain&mdash;atau bahkan tidak bisa sama sekali. Masih sering juga terdapat lebih dari satu *flow* yang sama, namun ditulis ulang di setiap fitur, sehingga membuat *maintenance* menjadi rumit. Hingga masalah klasik seperti perbedaan *style* penulisan *code*, yang terkadang membuat bingung anggota tim.

Masalah-masalah tersebut terjadi karena memang setiap orang mempunyai kerangka berfikir yang berbeda. Dari sini saya menyadari tentang pentingnya dan kenapa kita harus melakukan mekanisme `modular oriented` dalam setiap *development*.

> ## *Little things that helped a lot.*

> Jika kita membuat *flow* proses di dalam sebuah fitur yang juga dibutuhkan oleh fitur-fitur lain, maka buatlah menjadi modul agar bisa diimplementasikan ke dalam fitur lain&mdash;daripada menulis ulang proses tersebut&mdash;sehingga membuat kita mudah dalam melakukan *fixing*, *update* ataupun *tracking error*.

> Jika kita tahu solusi mengatasi proses *overload* pada saat *looping massive data* yang `CRUD` ke *database*, maka buatlah menjadi modul yang *reusable*, karena orang lain mungkin akan mengalami masalah yang sama, dan kita sudah siap membantu dengan modul solusinya. Nantinya, mereka bisa belajar dari modul tersebut&mdash;atau bahkan membuatnya menjadi lebih baik. Setidaknya, kita bisa sedikit bermanfaat untuk orang lain.

...hal-hal tersebut sangatlah penting untuk diterapkan.

# Perbedaan kerangka berfikir

Satu hal yang pasti jika bekerja sebagai seorang Developer / Programmer / Software Engineer adalah kita tidak bisa bekerja secara individu. Makna dari individu disini lebih luas, bukan hanya individu seorang diri, melainkan juga individu secara kerangka berfikir. Kita bisa saja menulis ribuan baris *code* hanya untuk menyelesaikan sebuah aplikasi yang dapat berjalan dengan baik. Namun, itu bukanlah satu-satunya tujuan akhir dari sebuah *development*, melainkan itu hanya menjadi salah satu dari sekian banyak `PR` yang memang harus diselesaikan. Okelah, katakanlah kita bisa *finish production* dengan baik. Kita hanya baru saja selesai dengan satu `PR`.

Sebuah *development* tidak hanya beorientasi terhadap hasil akhir, melainkan juga berorientasi terhadap proses pengerjaannya, serta efek dan *effort* setelahnya. Developer harus memikirkan bagaimana mereka bisa menghasilkan suatu produk (aplikasi / sistem) yang baik dengan proses pengerjaan yang efisien. Efisien bisa terhadap waktu, jumlah *task*, *resource*, hingga *maintenance* dimasa mendatang [ref][10 CHALLENGES EVERY SOFTWARE PRODUCT DEVELOPER FACES](https://synoptek.com/insights/it-blogs/10-challenges-every-software-product-developer-faces/)[/ref] [ref][What is Application Lifecycle Management (ALM)?](https://stackify.com/application-lifecycle-management/)[/ref]. `PR` nya adalah, untuk mencapai target efisien tersebut tidaklah mudah. Karena kita bekerja sebagai tim, ada banyak masalah-masalah yang harus diselesaikan, misalnya; (a) kemampuan teknis tiap individu (b) setiap orang punya kerangka berfikirnya sendiri (c) tidak semua orang *open minded* (d) ada yang suka cara konvensional ada yang tidak (e) tidak semua orang setuju (f) tidak semua orang gampang paham (g) dan lain sebagainya.

Pada masa sekarang, mungkin permasalahan-permasalahan tersebut telah sedikit berkurang karena adanya *Framework*. Secara garis besar, *framework* sebenarnya diciptakan atas latar belakang `PR` yang hampir mirip, yaitu perbedaan kerangka berfikir, sehingga dengan dibuatnya *framework* diharapkan cara pikir struktural orang-orang bisa disamakan—karena mereka dipaksa untuk mengikuti suatu aturan pola tertentu [ref][The Importance of Frameworks](https://medium.com/@benyoss4/the-importance-of-frameworks-2c4a04d20ac5)[/ref]. *Framework* bukan cuma tentang *coding*, tapi juga tentang *team management*. Meskipun *framework* sangat membantu, tapi kenapa orang-orang masih belum bisa sepenuhnya menyamakan pola pikir. Masih ada saja orang yang membuat struktur sistem / *code* nya sendiri. Masih ada saja orang yang tidak mengikuti pakem yang sudah di putuskan bersama. Atau mereka mengikuti pakem, tapi tidak konsisten, alhasil membuat bingung rekan satu tim.

Kita mungkin sempat berfikir untuk menyerah menangani *problem* pola pikir ini karena masih sulit menerima perbedaan&mdash;serta sulit mengatur orang lain&mdash;akhirnya kita membiarkan hal tersebut terus berlanjut. Itu adalah hal yang wajar. Saya sendiri masih sering terjebak dalam `PR` tersebut dan masih sulit beradaptasi. Kita hanya butuh pengalaman dan banyak belajar lagi untuk bisa lebih terbuka.

# *Modular oriented is the thing we should do from now. By doing this mechanism, you can help others&mdash;indirectly, it will also help you to improve yourself.*

`modular oriented` artinya kita bekerja dengan membuat modul-modul *reusable* terhadap *flow* atau alur yang digunakan untuk memecahkan masalah. *Reusable* artinya modul tersebut dapat digunakan pada kondisi yang fleksibel di dalam sistem, serta memiliki probalitas yang kecil untuk dilakukan penyesuaian ulang apabila digunakan [ref][PROGRAMMING FUNDAMENTALS: Modular Programming](https://press.rebus.community/programmingfundamentals/chapter/modular-programming/)[/ref]. Konsep ini sudah ada sejak lama. Lalu, kenapa ini menjadi sangat penting? kenapa `modular oriented` bisa digunakan untuk mengatasi `PR` ekosistem yang tidak efisien? adalah karena manfaat kedepannya.

Apa yang akan kita lakukan dengan `modular oriented` ini adalah,

# Meminimalisir *effort development*

Salah satu tujuan utama dari adanya konsep *modular* adalah untuk membuat *effort* lebih kecil pada saat melakukan *development*&mdash;terutama untuk *after development*.

> ### *It can be done by stopping writing the same flow again*

Jangan menulis ulang&mdash;secara *inline-feature*&mdash;*flow* yang sudah kita gunakan untuk memecahkan masalah. Hal itu akan merepotkan nantinya jika kita ingin melakukan sesuatu / *update* terhadap *flow* tersebut. Secara *inline-feature* yang dimaksud gambarannya seperti ini:

```javascript
function register () {
	checkUserExists(); 	// Process to check user exist
	insertUserData(); // Process to insert user data
	generateSessionId(); // Process to generate session id
	removeOldSession(); // Process to remove last-old session
	setSessionExpired(); // Process to set session expired
	createNewSession(); // Process to create new session
	output(); // Give output
}

function login () {
	checkUserExists(); 	// Process to check user exist
	validateUserPassword(); // Process to check if user password is valid
	generateSessionId(); // Process to generate session id
	removeOldSession(); // Process to remove last-old session
	setSessionExpired(); // Process to set session expired
	createNewSession(); // Process to create new session
	output(); // Give output
}
```

Pada *code* diatas, fitur `register` dan `login` sama-sama memiliki *flow* proses `session`. Bayangkan misalnya ada lebih dari 10 fitur yang membutuhkan *flow* `session` serupa dan kita menulisnya secara *inline-feature*. Kalau ada *update* / *fixing* dalam perjalanan, kita harus memperbaikinya satu per satu di setiap fitur. Karena apabila satu *flow* tidak sesuai, maka *flow* yang lain kemungkinan besar tidak sesuai juga, karena *logic* nya sama. Hal ini sangatlah *effort* dan tidak efisien&mdash;terutama jika kita bekerja dalam tim. Kita juga akan lebih rentan terkena *typo*.

Belum lagi misalkan rekan satu tim juga melakukan hal yang sama. Lalu pada suatu kondisi, kita harus melakukan *update* terhadap fitur tersebut, tentu kita akan kerepotan&mdash;karena butuh waktu lama untuk mempelajari *flow-flow* proses yang dibuat oleh rekan tim tersebut.

> ### *Don't let yourself get stucked into that situation!*

Oleh karena itu, kita harus menulisnya secara *modular*, yakni memecahnya menjadi modul-modul.

```javascript
function createSession () {
	generateSessionId(); // Process to generate session id
	removeOldSession(); // Process to remove last-old session
	setSessionExpired(); // Process to set session expired
	createNewSession(); // Process to create new session
}

function register () {
	checkUserExists(); 	// Process to check user exist
	insertUserData(); // Process to insert user data
	createSession(); // Process to create session
	output(); // Give output
}

function login () {
	checkUserExists(); 	// Process to check user exist
	validateUserPassword(); // Process to check if user password is valid
	createSession(); // Process to create session
	output(); // Give output
}
```

Pada *code* diatas, apabila dalam perjalanan kita memiliki *problem* pada *flow* `session`, kita hanya perlu memperbaikinya di dalam modul `session` saja, sehingga *flow* yang lain tidak akan terpengaruh. Kita jadi mudah dalam melakukan *maintenance* serta memperkecil *effort* kedepannya karena acuannya menjadi satu tempat.

Selain itu, modul yang kita buat juga bisa digunakan oleh rekan tim yang lain untuk mengerjakan fitur mereka. Mereka tidak harus memikirkan ulang proses yang sudah ada, dan tidak harus kerepotan apabila terjadi perubahan. Kita bisa membantu mempermudah perkerjaan mereka. Malahan, rekan tim tersebut juga mungkin dapat memberikan masukan agar modul kita menjadi lebih baik.

Kerjasama antar tim menjadi lebih terstruktur.

> ### *That's what called&mdash;a collaboration.*

Perlu di ingat juga, tujuan dari *modular* bukan untuk membuat *development* menjadi lebih sulit. Jadi, kita harus memastikan bahwa (1) *logic* dari modul tetap *simple* (2) modulnya fleksibel (3) membuat modul hanya untuk *flow-flow* yang memang diperlukan saja (4) serta modul mudah dipahami oleh orang lain.

# Menemukan algoritma terbaik untuk diterapkan

Secara tidak langsung, `modular oriented` membuat kita terbiasa dengan kerangka berfikir orang lain&mdash;seperti kita yang terbiasa menggunakan modul-modul yang ada di internet.

Selain *development* menjadi efisien, menerapkan `modular oriented` juga tujuannya agar terbiasa menggunakan modul-modul buatan rekan tim yang lain, begitu juga sebaliknya. Dari sinilah kita akan belajar. Menurut saya, ini adalah cara terbaik untuk belajar.

```javascript
// Your own flow
function createSession () {
	generateSessionId(); // Process to generate session id
	setSessionExpired(); // Process to set session expired
	removeOldSession(); // Process to remove last-old session
	createNewSession(); // Process to create new session
}

// Your partner's modul
function createSession () {
	removeOldSession(); // Process to remove last-old session
	generateSessionId(); // Process to generate session id
	setSessionExpired(); // Process to set session expired
	createNewSession(); // Process to create new session
}
```

... *same modul with different flow*.

Kita dapat meningkatkan kemampuan dengan belajar melalui praktek, *learning by doing*. Tetapi perlu diingat, kita juga punya banyak peluang untuk melakukan kesalahan. Kita bisa salah. Untuk itu diperlukan yang namanya perbandingan. Kita perlu mempelajari algoritma orang lain untuk melihat apakah algoritma yang kita buat benar-benar efektif atau tidak&mdash;mencari tahu algoritma mana yang terbaik untuk diterapkan. Di dalam sebuah tim, hal ini akan membuat kita lebih mudah terbiasa dengan kerangka berfikir orang lain. Karena belajar dari modul untuk memecahkan masalah, maka target akan terpecah menjadi bagian-bagian yang lebih fokus&mdash;daripada harus mempelajari keseluruhan sistem dari awal.

Karena modul yang kita buat bisa dipakai oleh banyak orang sekaligus, kita akan sering menerima masukan dan lebih mudah terbuka untuk menerima pendapat. Bukan hanya kita saja yang diuntungkan, tetapi juga mereka yang menggunakan modul tersebut&mdash;karena tujuannya sama yaitu membuat modul-modul tersebut menjadi lebih baik.

# Memberikan manfaat bagi orang lain

*Scope* `modular oriented` seharusnya tidak hanya dilakukan di dalam fitur aplikasi saja, melainkan juga *scope* permasalahan yang lebih luas. Seperti contoh di awal;

> Jika kita tahu solusi mengatasi proses *overload* pada saat *looping massive data* yang `CRUD` ke *database*, maka buatlah menjadi modul.

Intinya adalah ketika kita menghadapi suatu masalah yang sulit diselesaikan, lalu kemudian kita berhasil mengatasinya, maka jangan biarkan solusi tersebut berhenti begitu saja. Mungkin saja ada orang diluar sana sedang mengalami masalah yang sama.

> ### *Don't code for yourself!*

Ada begitu banyak modul di internet yang bisa dipakai untuk menyelesaikan kasus-kasus tertentu. Bukankah kita sering menggunakannya untuk menyelesaikan pekerjaan? Bukankah kita sangat terbantu oleh modul-modul tersebut? Kita juga harus melakukan hal yang sama. Kita harus membuat setiap solusi dapat digunakan oleh orang lain dalam menyelesaikan masalah mereka.

Kita harus berfikir untuk membantu orang lain.

<hr>

![search-help](https://images.unsplash.com/photo-1531379410502-63bfe8cdaf6f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80)
*Photo by [Júnior Ferreira](https://unsplash.com/@juniorferreir_) on [Unsplash](https://unsplash.com/s/photos/help)*

`modular oriented` tidak hanya akan membuat pekerjaan menjadi lebih mudah, tetapi juga membuat kolaborasi antar tim menjadi terstruktur, dan kita bisa sedikit memberikan manfaat kepada orang lain.

`modular oriented` juga bisa menjadi solusi mengatasi `PR` untuk menciptakan lingkungan ekosistem yang efisien.


<hr>
<br>

### References











