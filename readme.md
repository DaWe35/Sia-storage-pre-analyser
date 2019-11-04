> The decentralized [Sia](https://sia.tech) storage still limited by 40 MiB as the minimum file size (smaller files will get uploaded as 40 MiB).

This small script estimates the Sia size of the given directory (files will rounded to 40 MiB chunks), calculates the lost space, the average file size, and so on.

## Run on Windows

- Download the [latest release](https://github.com/DaWe35/Sia-storage-pre-analyser/releases/latest/download/analyze.exe)

- Open CMD

- Type `path/to/analyze.exe "your-folder/to-analyze"`

## Run with Python 3

- First, you need to install python 3.

- Download: `git clone https://github.com/DaWe35/Sia-storage-pre-analyzer.git`

- `cd Sia-storage-pre-analyzer`

- `python analyze.py "your/input/folder"` (Python 3 required)

### Example result:

- *For additional output, use -v or --verbose flags*

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