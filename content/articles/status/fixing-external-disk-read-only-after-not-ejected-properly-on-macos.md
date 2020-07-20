---
Title: Fixing External Disk Read-Only After Not Ejected Properly on MacOS
Date: 2020-07-20 18:35
Tags: case, macos, fixing
---
Di MacOS, hardisk external saya ketika dia tidak ke-eject secara benar pasti akan menjadi read-only ketika saya koneksikan lagi. Bahkan kadang malah ga ke detect.

Untuk mengatasinya, maka saya perlu repair disk nya. Pertama, saya mencari process id atau `pid` external disk nya dengan perintah

```bash
ps aux | grep fsck
```

Setelah itu, kill proses nya

```
sudo kill -9 pid
```

Proses disk yang berjalan diatas sebenarnya adalah conflict process dari proses disk sebelum dia ke eject, jadi perlu di matikan dulu.