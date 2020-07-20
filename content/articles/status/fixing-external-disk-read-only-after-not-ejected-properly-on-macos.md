---
Title: Fixing External Disk Read-Only After Not Ejected Properly on MacOS
Description: Di MacOS, hardisk external saya pada saat dia tidak ke eject secara
  benar pasti akan menjadi read-only ketika saya koneksikan lagi. Bahkan kadang
  malah ga ke detect (unmounted).
cover_image: https://lh3.googleusercontent.com/pw/ACtC-3f_Z0u7xgSAmynttDAGq6-GNH3_BVn5f2NCCxCSUHSKCp6YcyVAOM6pVOeidO6GItzSJ0UzuQa9jgD0baOPNZrkSpQzM7nQ-VTyA06ca18vOvIoXHkrvFMocHIXKuy0uGOnhFdIc_PpYOR25BnyrkYu=w720-h290-no
Date: 2020-07-20 18:35
Tags: case, macos, fixing, apple, disk
---
![macos-disk-not-ejected-properly](https://lh3.googleusercontent.com/pw/ACtC-3f_Z0u7xgSAmynttDAGq6-GNH3_BVn5f2NCCxCSUHSKCp6YcyVAOM6pVOeidO6GItzSJ0UzuQa9jgD0baOPNZrkSpQzM7nQ-VTyA06ca18vOvIoXHkrvFMocHIXKuy0uGOnhFdIc_PpYOR25BnyrkYu=w720-h290-no)

Di **MacOS**, *hardisk external* saya pada saat dia tidak ke *eject* secara benar pasti akan menjadi *read-only* ketika saya koneksikan lagi. Bahkan kadang malah ga ke *detect* (*unmounted*).

Untuk mengatasinya, maka saya perlu *repair disk* nya. Pertama saya koneksikan *disk external* nya, kemudian mencari *process id* atau `pid` *external disk* nya dengan perintah:

```bash
ps aux | grep fsck
```

![macos-get-disk-pid](https://lh3.googleusercontent.com/pw/ACtC-3ckWSGs6gL1v0_t2W10HQO_Se8lQE3z-BHHXNbOhKb-5Qd2LtKniZ5tZmBuzLyEE2Mwv4JHaV2iLuSU_kvYrA-OsUyzngAK3T-rEhVuCh_qBq5S8QUv6Bmad-c9Z8d2dtn_tNPjsm25S3_0brhlOzCE=w1164-h150-no)

Setelah itu, *kill* proses nya.

```bash
sudo kill -9 pid
```

![macos-kill-pid](https://lh3.googleusercontent.com/pw/ACtC-3cv7V-4atL8jqyHC3b-9Nm3Fz-CDt_BtCSpkX4Se-RcwRUIAPMI8qcqIhFwY64brCRMngowjSLr_4eYYxGQIXLCX6WR2Nn6f7b6CI1qG8srIqyfrMCuGoIodBfR8a10ecG-a5pmS3RX_Jjrd29JoW-4=w738-h154-no)

Proses *disk* yang berjalan diatas sebenarnya adalah *conflict process* dari `pid` *disk* lama sebelum dia ke *eject*. Karena *conflict*, maka di *background* mencoba untuk membentuk 2 `pid` atas 1 koneksi *external disk* yang sama. Jadi, perlu di matikan dulu yang lama.

Kalau muncul pesan seperti ini,

![macos-disk-repair-error-notice](https://lh3.googleusercontent.com/pw/ACtC-3dmBRgFe-nXSj2u4RJb2j2EuxOd56xq-3wJPu5Wz7PdBoQNT3OFJhAufmhsM0VJ_7l3mJU0q5X7NkvBKlxKg41a7Nsx_VpGypcqEPKSWLBLGBKMtjZxGC5FdPeS_uzJrwfJGICQzyi5a1LVFP9iSOxD=w854-h332-no)

klik `ok` saja. Biasanya kalau *external disk* saya tidak ke *detect*, setelah proses *kill* `pid` tadi maka *external disk* akan otomatis ke *mount*. Hal ini dikarenakan `pid` yang *conflict* tadi sudah dihapus, sehingga `pid` asli dari *disk* yang sedang *connect* sekarang bisa berjalan.

Terakhir adalah *repair disk*. Saya biasanya menggunakan aplikasi *default* `Disk Utility`. Sebelum di *repair*, saya *unmount* dulu semua partisinya.

![macos-disk-repair-disk](https://lh3.googleusercontent.com/pw/ACtC-3dh5UlO9qtLErcIzALYLtJy1pzEPgMqyWb3-wbpHJsY3nToQdKPbOj88l4vRorD1IfMt77gqJ3WOMouozAM_kG2jZdf_JqMKgDadcMNoVX8TxqlPxXAsz2TWEHk58vuCy51As6o33u28NmKgiN8UKIa=w1860-h1142-no)

Setelah itu, tinggal menunggu selesai. Apabila proses *repair* selesai, saya cabut dan koneksikan kembali *external disk* nya. Sudah normal.

Sumpah, ini *annoying* sekali. Masalahnya *hardisk external* saya isinya banyak dan pas *repair* lama banget. ***C'mon Apple!***