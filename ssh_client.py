#!/usr/bin/python2


import os,commands as c

while True:
	try:
		os.system("Xdialog --title 'ssh Client Configuration' --cancel-label 'back' --menubox '' 15 50 3 1 configure 2 status 3 Uninstall  2>.temp")
		ch=int(c.getoutput("cat .temp|head -1"))
	except:
		os.system("rm -f .temp")
		exit()


	if ch==1:
		x=c.getoutput("rpm -q openssh-clients")
		if x=='package openssh-clients is not installed':
			ex=os.system("yum install openssh-clients -y 1>/dev/null 2>/dev/null")
			if ex==0:
				os.system("Xdialog --title 'ssh Client Configuration' --msgbox 'ssh Client successfully configured\n\nconnect to ssh server by command \n\n#ssh user_name@(ip address of server):directory' 15 60")
			else:
				os.system("Xdialog --title 'ssh Client Configuration' --msgbox 'yum is not configured yet\n\n please configure yum first' 15 50")
				exit()
		else:
			os.system("Xdialog --title 'ssh Client configuration' --msgbox 'ssh Client already configured' 15 50")
			os.system("Xdialog --title 'ssh Client Configuration' --msgbox 'connect to ssh server by command \n\n#ssh user_name@(ip address of server):directory' 15 60")

	elif ch==2:
		
		x=c.getoutput("rpm -q openssh-clients")
		if x=='package openssh-clients is not installed':
			os.system("Xdialog --title 'ssh Client Configuration' --msgbox 'ssh Client is not configured ' 15 50")
		else:
			os.system("Xdialog --title 'ssh Client Configuration' --msgbox 'ssh Client is configured ' 15 50")

	elif ch==3:
		x=c.getoutput("rpm -q openssh-clients")
		if x=='package openssh-clients is not installed':
			os.system("Xdialog --title 'ssh client Configuration' --msgbox 'ssh client is not configured' 15 50")
		else:
			ex=os.system("Xdialog --title 'ssh Client Configuration' --yesno 'are you sure?' 15 50")
			if ex==0:
				ex=os.system("yum remove openssh-clients -y 2>.temp >/dev/null")
				
				err=c.getoutput("cat .temp|tail -1")
				if ex==0:
					os.system("Xdialog --title 'ssh Client Configuration' --msgbox 'ssh Client successfully Uninstall' 15 50")
				else:
					os.system("Xdialog --title 'ssh client Configuration' --msgbox  '"+err+"\n so it can not be uninstall' 15 70")
			else:
				pass





