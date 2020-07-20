---
Title: Fixing External Disk Read-Only After Not Ejected Properly on MacOS
Date: 2020-07-20 18:35
Tags: case, macos, fixing
---
![macos-disk-not-ejected-properly](https://lh3.googleusercontent.com/pw/ACtC-3f_Z0u7xgSAmynttDAGq6-GNH3_BVn5f2NCCxCSUHSKCp6YcyVAOM6pVOeidO6GItzSJ0UzuQa9jgD0baOPNZrkSpQzM7nQ-VTyA06ca18vOvIoXHkrvFMocHIXKuy0uGOnhFdIc_PpYOR25BnyrkYu=w720-h290-no)

Di MacOS, hardisk external saya ketika dia tidak ke-eject secara benar pasti akan menjadi read-only ketika saya koneksikan lagi. Bahkan kadang malah ga ke detect.

Untuk mengatasinya, maka saya perlu repair disk nya. Pertama, saya mencari process id atau `pid` external disk nya dengan perintah

```bash
ps aux | grep fsck
```

![macos-get-disk-pid](https://lh3.googleusercontent.com/pw/ACtC-3ckWSGs6gL1v0_t2W10HQO_Se8lQE3z-BHHXNbOhKb-5Qd2LtKniZ5tZmBuzLyEE2Mwv4JHaV2iLuSU_kvYrA-OsUyzngAK3T-rEhVuCh_qBq5S8QUv6Bmad-c9Z8d2dtn_tNPjsm25S3_0brhlOzCE=w1164-h150-no)

Setelah itu, kill proses nya

```bash
sudo kill -9 pid
```

![macos-kill-pid](https://lh3.googleusercontent.com/pw/ACtC-3cv7V-4atL8jqyHC3b-9Nm3Fz-CDt_BtCSpkX4Se-RcwRUIAPMI8qcqIhFwY64brCRMngowjSLr_4eYYxGQIXLCX6WR2Nn6f7b6CI1qG8srIqyfrMCuGoIodBfR8a10ecG-a5pmS3RX_Jjrd29JoW-4=w738-h154-no)

Proses disk yang berjalan diatas sebenarnya adalah conflict process dari proses disk sebelum dia ke eject, jadi perlu di matikan dulu.