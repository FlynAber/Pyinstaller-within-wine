# Pyinstaller within Wine for Kali

This script automates the process of installing pyinstaller within wine

## Installation
```
git clone https://github.com/FlynAber/Pyinstaller-within-wine
python3 pyinstaller-within-wine-installer.py
```

## How to use

create a python file that you wish to run on a Windows machine

Sample hello_world.py:
```
import time
print("Hello World!")
time.sleep(5)
```
Then run the command 
```
Wine /root/.wine/drive_c/Program Files/Python38-32/Scripts/pyinstaller.exe <directory to your python folder> <args>
```
**Note: args can be found with -h in place of directory**

the .exe file can be found in the folder you ran the command from in a new folder called dist
Example:
If the command is ran from /root/ then the .exe will be located in /root/dist
## Why?

Pyinstaller within wine is a good option for creating .exe files on a linux distribution.
Because Linux and Windows have different executable files, and different encoding for those exectuables, it makes it impossible for windows to read linux executables.

However, this can be overcome if a windows machine is emulated on the linux distribution, which is what Wine can do. 

By installing pyinstaller within Wine we can trick it into creating .exe files that can run on a windows machine.
