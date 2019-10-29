The decentralized [Sia](https://sia.tech) storage still limited by 40 MiB as the minimum file size (smaller files will get uploaded as 40 MiB).
This small script estimates the Sia size of the given directory (small files scaled up to 40 MiB), calculates the lost space, the average file size, and so on.

Example result:

    Size on
        Disk: 29.160 GB
        Sia:  33.967 GB

    Lost space:  4.807 GB
        +16% empty space used for scaling files up to 40MiB

    Too small files: 246
        Average: 22.404 MB

    Larger files: 169
        Average: 139.933 MB

    All files: 415
        Average: 70.265 MB
        Median: 35.369 MB