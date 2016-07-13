#!/usr/bin/python2


import commands as c
import os
while True:
	try:
		os.system("Xdialog --title 'FTP server Configuration' --cancel-label 'back' --menubox '' 15 50 5 1 configure 2 activate 3 deactivate 4 Status 5 Uninstall 2>.temp")
		ch=int(c.getoutput("cat .temp|head -1"))
	except:
		
			os.system("rm -f .temp")
			exit()


	if ch==1:
		x=c.getoutput("rpm -q vsftpd")
		if x=='package vsftpd is not installed':
			ex=os.system("yum install vsftpd -y 1>/dev/null 2>/dev/null")
			if ex==0:
				pass
			else:
				os.system("Xdialog --title 'FTP server Configuration' --msgbox 'yum is not configured yet\n\n please configure yum first' 15 50")
				exit()
		else:
			os.system("Xdialog --title 'FTP server configuration' --msgbox 'FTP server allready configured' 15 50")
			continue

		status=c.getoutput("service vsftpd status|awk -F' ' '{print $3}'")
		if status=='stopped':
			ex=os.system("Xdialog --title 'FTP server Configuration' --yesno 'service is stopped\n\n want to start service?' 15 50")
			if ex==0:
				os.system("service vsftpd start >/dev/null")
			else:
				pass
		else:
			ex=os.system("Xdialog --title 'FTP server Configuration' --yesno 'service is active\n\nwant to stop service?' 15 50")
			if ex==0:
				os.system("service vsftpd stop >/dev/null")
			else:
				pass

		ex=os.system("Xdialog --title 'FTP server Configuration' --yesno 'want to start service at boot time' 15 50")
		if ex==0:
			os.system("chkconfig vsftpd on ")
		else:
			pass

		os.system("Xdialog --title 'FTP server Configuration' --msgbox 'place all the file & folder\nin /var/ftp to be\naccessed by anonymous user' 15 50")

	if ch==2:
	
		status=c.getoutput("service vsftpd status|awk -F' ' '{print $3}'")
		if status=='stopped':
			os.system("service vsftpd start >/dev/null")
			os.system("Xdialog --title 'FTP server Configuration' --msgbox 'FTP service successfully Actived' 15 50")
		else:
			os.system("Xdialog --title 'FTP server Configuration' --msgbox 'FTP service allready Active' 15 50")

	elif ch==3:
		status=c.getoutput("service vsftpd status|awk -F' ' '{print $5}'")
		if status=='running...':
			os.system("service vsftpd stop 2>/dev/null")
			os.system("Xdialog --title 'FTP server Configuration' --msgbox 'FTP service successfully Dectived' 15 50")
		else:
			os.system("Xdialog --title 'FTP server Configuration' --msgbox 'FTP service allready Dective' 15 50")
	elif ch==4:
		
		x=c.getoutput("rpm -q vsftpd")
		if x=='package vsftpd is not installed':
			os.system("Xdialog --title 'FTP server Configuration' --msgbox 'FTP server is not configured yet\n first configure FTP server' 15 50")
		else:
			status=c.getoutput("service vsftpd status|awk -F' ' '{print $5}'")
			if status=='running...':
				os.system("Xdialog --title 'FTP server Configuration' --msgbox 'FTP server is running...' 15 50")
			else:
				os.system("Xdialog --title 'FTP server Configuration' --msgbox 'FTP server is stop...' 15 50")
	elif ch==5:
		x=c.getoutput("rpm -q vsftpd")
		if x=='package vsftpd is not installed':
			os.system("Xdialog --title 'FTP server Configuration' --msgbox 'FTP server is not configured' 15 50")
		else:
			ex=os.system("Xdialog --title 'FTP server Configuration' --yesno 'are you sure?' 15 50")
			if ex==0:
				os.system("rpm -e vsftpd")
				os.system("Xdialog --title 'FTP server Configuration' --msgbox 'FTP server successfully Uninstall' 15 50")
			else:
				pass



