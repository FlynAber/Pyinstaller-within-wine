# Pyinstaller within Wine for Kali

This script automates the process of installing pyinstaller within wine

## Installation
```
git clone https://github.com/FlynAber/Pyinstaller-within-wine
python3 pyinstaller-within-wine-installer.py
```

## Why?

Pyinstaller within wine is a good option for creating .exe files on a linux distribution.
Because Linux and Windows have different executable files, and different encoding for those exectuables, it makes it impossible for windows to read linux executables.

However, this can be overcome if a windows machine is emulated on the linux distribution, which is what Wine can do. 

By installing pyinstaller within Wine we can trick it into creating .exe files that can run on a windows machine.
