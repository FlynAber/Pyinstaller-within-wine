import os

install = input("Would you like to install Pyinstaller within wine? This is a lengthy process. (Y/N) (Note: this is required for the Payload generator)")

if (install.lower() == "y") :
	print("Adding Architecture i386")
	os.system("sudo dpkg --add-architecture i386")
	print("updating apt lists")
	os.system("sudo apt-get update")
	print("installing wine and wine32")
	os.system("sudo apt-get install wine wine32")
	os.system("wine init")
	print("downloading and running python")
	os.system("wget -P /root/.wine/drive_c/ https://www.python.org/ftp/python/3.8.10/python-3.8.10.exe")
	print("Download finished.")
	print("------------Please follow the following instructions carefully!--------------")
	instructpause = input("Enter to continue...")
	print("Click Custom install \n Click next \n click install for all users (check install location is C:\Program Files\Python38-32)")
	os.system("wine /root/.wine/drive_c/python-3.8.10.exe")
	os.system("cd /root/.wine/drive_c/Program\\ Files/Python38-32 && wine python.exe Scripts/pip.exe install https://github.com/pyinstaller/pyinstaller/tarball/develop ")
