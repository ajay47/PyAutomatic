#!/usr/bin/python2


import os,commands as c

while True:
	try:
		os.system("Xdialog --title 'ISCSI Client Configuration' --cancel-label 'back' --menubox '' 15 50 3 1 configure 2 status 3 Uninstall  2>.temp")
		ch=int(c.getoutput("cat .temp|head -1"))
	except:
		os.system("rm -f .temp")
		exit()


	if ch==1:
		x=c.getoutput("rpm -q iscsi-initiator-utils")
		if x=='package iscsi-initiator-utils is not installed':
			ex=os.system("yum install iscsi-initiator-utils -y 1>/dev/null 2>/dev/null")
			if ex==0:	
				os.system("service iscsid restart 2>/dev/null")
				os.system("chkconfig iscsid on")
				os.system("Xdialog --titel 'ISCSI Client Configuration' --inputbox 'enter server ip address' 15 50 2>.temp")
				ip=c.getoutput("cat .temp")
				os.system("iscsiadm --mode dicoverydb --type sendtargets --portal "+ip+" --discover >.temp 2>/dev/null")
				iqn=("cat .temp|awk -F' ' '{print $2}'")
				os.system("iscsiadm --mode node --targetname "+iqn+" --portal "+ip+" --login")					
				
				os.system("Xdialog --title 'ISCSI Client Configuration' --msgbox 'ISCSI Client successfully configured' 15 60")
			else:
				os.system("Xdialog --title 'ISCSI Client Configuration' --msgbox 'yum is not configured yet\n\n please configure yum first' 15 50")
				exit()
		else:
			os.system("Xdialog --title 'ISCSI Client configuration' --msgbox 'ISCSI Client already configured' 15 50")

	elif ch==2:
		
		x=c.getoutput("rpm -q iscsi-initiator-utils")
		if x=='package iscsi-initiator-utils is not installed':
			os.system("Xdialog --title 'ISCSI Client Configuration' --msgbox 'ISCSI Client is not configured ' 15 50")
		else:
			os.system("Xdialog --title 'ISCSI Client Configuration' --msgbox 'ISCSI Client is configured ' 15 50")

	elif ch==3:
		x=c.getoutput("rpm -q iscsi-initiator-utils")
		if x=='package iscsi-initiator-utils is not installed':
			os.system("Xdialog --title 'ISCSI client Configuration' --msgbox 'ISCSI client is not configured' 15 50")
		else:
			ex=os.system("Xdialog --title 'ISCSI Client Configuration' --yesno 'are you sure?' 15 50")
			if ex==0:
				ex=os.system("yum remove iscsi-initiator-utils -y 2>.temp >/dev/null")
				
				err=c.getoutput("cat .temp|tail -1")
				if ex==0:
					os.system("Xdialog --title 'ISCSI Client Configuration' --msgbox 'ISCSI Client successfully Uninstall' 15 50")
				else:
					os.system("Xdialog --title 'ISCSI client Configuration' --msgbox  '"+err+"\n so it can not be uninstall' 15 70")
			else:
				pass





