#!/usr/bin/python2


import os,commands as c

while True:
	try:
		os.system("Xdialog --title 'telnet Client Configuration' --cancel-label 'back' --menubox '' 15 50 3 1 configure 2 status 3 Uninstall 2>.temp")
		ch=int(c.getoutput("cat .temp|head -1"))
	except:
		os.system("rm -f .temp")
		exit()


	if ch==1:
		x=c.getoutput("rpm -q telnet")
		if x=='package telnet is not installed':
			ex=os.system("yum install telnet -y 1>/dev/null 2>/dev/null")
			if ex==0:
				os.system("Xdialog --title 'telnet Client Configuration' --msgbox 'telnet Client successfully configured\n\nconnect to telnet server by command \n\n#telnet 	(ip address of server)' 15 50")
			else:
				os.system("Xdialog --title 'telnet Client Configuration' --msgbox 'yum is not configured yet\n\n please configure yum first' 15 50")
				exit()
		else:
			os.system("Xdialog --title 'telnet Client configuration' --msgbox 'telnet Client already configured' 15 50")
			os.system("Xdialog --title 'telnet Client Configuration' --msgbox 'telnet Client successfully configured\n\nconnect to telnet server by command \n\n#telnet 	(ip address of server)' 15 50")

	elif ch==2:
		
		x=c.getoutput("rpm -q telnet")
		if x=='package telnet is not installed':
			os.system("Xdialog --title 'telnet Client Configuration' --msgbox 'telnet Client is not configured ' 15 50")
		else:
			os.system("Xdialog --title 'telnet Client Configuration' --msgbox 'telnet Client is configured ' 15 50")

	elif ch==3:
		x=c.getoutput("rpm -q telnet")
		if x=='package telnet is not installed':
			os.system("Xdialog --title 'telnet client Configuration' --msgbox 'telnet client is not configured' 15 50")
		else:
			ex=os.system("Xdialog --title 'telnet Client Configuration' --yesno 'are you sure?' 15 50")
			if ex==0:
				os.system("yum remove telnet -y >/dev/null 2>/dev/null")
				os.system("Xdialog --title 'telnet Client Configuration' --msgbox 'telnet Client successfully Uninstall' 15 50")
			else:
				pass





