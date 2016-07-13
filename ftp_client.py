#!/usr/bin/python2


import os,commands as c

while True:
	try:
		os.system("Xdialog --title 'FTP Client Configuration' --cancel-label 'back' --menubox '' 15 50 4  1 configure 2 status 3 Uninstall 4 'start service' 2>.temp")
		ch=int(c.getoutput("cat .temp|head -1"))
	except:
		os.system("rm -f .temp")
		exit()


	if ch==1:
		x=c.getoutput("rpm -q ftp")
		if x=='package ftp is not installed':
			ex=os.system("yum install ftp -y 1>/dev/null 2>/dev/null")
			if ex==0:
				os.system("Xdialog --title 'FTP Client Configuration' --msgbox 'FTP Client successfully configured\n\nconnect to FTP server by command \n\n#ftp (ip address of server)' 15 50")
			else:
				os.system("Xdialog --title 'FTP Client Configuration' --msgbox 'yum is not configured yet\n\n please configure yum first' 15 50")
				exit()
		else:
			os.system("Xdialog --title 'FTP Client configuration' --msgbox 'FTP Client already configured' 15 50")
			os.system("Xdialog --title 'FTP Client Configuration' --msgbox 'FTP Client successfully configured\n\nconnect to FTP server by command \n\n#ftp (ip address of server)' 15 50")

	elif ch==2:
		
		x=c.getoutput("rpm -q ftp")
		if x=='package ftp is not installed':
			os.system("Xdialog --title 'FTP Client Configuration' --msgbox 'FTP Client is not configured ' 15 50")
		else:
			os.system("Xdialog --title 'FTP Client Configuration' --msgbox 'FTP Client is configured ' 15 50")

	elif ch==3:
		x=c.getoutput("rpm -q ftp")
		if x=='package ftp is not installed':
			os.system("Xdialog --title 'FTP client Configuration' --msgbox 'FTP client is not configured' 15 50")
		else:
			ex=os.system("Xdialog --title 'FTP Client Configuration' --yesno 'are you sure?' 15 50")
			if ex==0:
				os.system("yum remove ftp -y >/dev/null 2>/dev/null")
				os.system("Xdialog --title 'FTP Client Configuration' --msgbox 'FTP Client successfully Uninstall' 15 50")
			else:
				pass
	elif ch==4:
		ex=os.system("Xdialog --title 'FTP Client Configuration' --yesno 'start the service ?' 15 50")
		if ex==0:
			os.system("service ftp restart")
			os.system("Xdialog --title 'FTP client Configuration' --msgbox 'FTP client start successfully' 15 50")
		else:
			pass




