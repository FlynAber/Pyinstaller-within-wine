import os.path

isWineInstalled = os.path.isdir("/root/.wine/drive_c/")
isWinePythonInstalled = os.path.isdir("/root/.wine/drive_c/Program Files/Python38-32")
isWinePyinstallerInstalled = os.path.isfile("/root/.wine/drive_c/Program Files/Python38-32/Scripts/pyinstaller.exe")
if isWineInstalled == True :
	print("Wine is installed")
	if isWinePythonInstalled == True :
		print("Python is installed correctly in wine")
		if (isWinePyinstallerInstalled == True) :
			print("Pyinstaller is installed correctly in wine")
		else :
			os.system("cd /root/.wine/drive_c/Program\\ Files/Python38-32 && wine python.exe Scripts/pip.exe install https://github.com/pyinstaller/pyinstaller/tarball/develop ")

	else :
		print("downloading and running python")
		os.system("wget -P /root/.wine/drive_c/ https://www.python.org/ftp/python/3.8.10/python-3.8.10.exe")
		print("Download finished.")
		print("------------Please follow the following instructions carefully!--------------")
		instructpause = input("Enter to continue...")
		print("Click Custom install \n Click next \n click install for all users (check install location is C:\Program Files\Python38-32)")
		os.system("wine /root/.wine/drive_c/python-3.8.10.exe")
		os.system("cd /root/.wine/drive_c/Program\\ Files/Python38-32 && wine python.exe Scripts/pip.exe install https://github.com/pyinstaller/pyinstaller/tarball/develop ")

else :
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
