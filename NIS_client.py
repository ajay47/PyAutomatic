#!/usr/bin/python2


import os,commands as c

while True:
	try:
		os.system("Xdialog --title 'NIS Client Configuration' --cancel-label 'back' --menubox '' 15 50 3 1 configure 2 status 3 Uninstall  2>.temp")
		ch=int(c.getoutput("cat .temp|head -1"))
	except:
		os.system("rm -f .temp")
		exit()


	if ch==1:
		x=c.getoutput("rpm -q ypbind ")
		if x=='package ypbind is not installed':
			ex=os.system("yum install ypbind -y 1>/dev/null 2>/dev/null")
			os.system("Xdialog --title 'NIS Client Configuration' --msgbox 'Now you have to select \nUse NIS and then enter domain \nand server in next menu' 20 50") 
			os.system("authconfig-tui")
			os.system("Xdialog title 'NIS Client Configuration' --inputbox 'enter server ip address' 15 50 2>.temp")
			ip=c.getoutput("cat .temp|head -1")
			os.system("yum install autofs -y 2>/dev/null >/dev/null")
			f=open('/etc/auto.misc','a')
			f.write("* "+ip+":/home/&")
			f.close()

			os.system("sed -i 's/\/misc/\/home/g' /etc/auto.master")
			os.system("service autofs restart >/dev/null")
			if ex==0:
				os.system("Xdialog --title 'NIS Client Configuration' --msgbox 'NIS Client successfully configured\n\nnow you can connect to NIS server' 15 50")
			else:
				os.system("Xdialog --title 'NIS Client Configuration' --msgbox 'yum is not configured yet\n\n please configure yum first' 15 50")
				exit()
		else:
			os.system("Xdialog --title 'NIS Client configuration' --msgbox 'NIS Client allready configured' 15 50")
			os.system("Xdialog --title 'NIS Client Configuration' --msgbox 'now you can connect to NIS server' 15 50")

	elif ch==2:
		
		x=c.getoutput("rpm -q ypbind")
		if x=='package ypbind is not installed':
			os.system("Xdialog --title 'NIS Client Configuration' --msgbox 'NIS Client is not configured ' 15 50")
		else:
			os.system("Xdialog --title 'NIS Client Configuration' --msgbox 'NIS Client is configured ' 15 50")

	elif ch==3:
		x=c.getoutput("rpm -q ypbind")
		if x=='package ypbind is not installed':
			os.system("Xdialog --title 'NIS client Configuration' --msgbox 'NIS client is not configured' 15 50")
		else:
			ex=os.system("Xdialog --title 'NIS Client Configuration' --yesno 'are you sure?' 15 50")
			if ex==0:
				ex=os.system("yum remove ypbind -y 2>.temp >/dev/null")
				os.system("yum remove autofs -y 2>/dev/null >/dev/null")
				
				err=c.getoutput("cat .temp|tail -1")
				if ex==0:
					os.system("Xdialog --title 'NIS Client Configuration' --msgbox 'NIS Client successfully Uninstall' 15 50")
				else:
					os.system("Xdialog --title 'NIS client Configuration' --msgbox  '"+err+"\n so it can not be uninstall' 15 70")
			else:
				pass





