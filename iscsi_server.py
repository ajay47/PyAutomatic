#!/usr/bin/python2

import os,commands as c

while True:
	try:
		os.system("Xdialog --title 'ISCSI server Configuration' --cancel-label 'back' --menubox '' 15 50 6 1 configure 2 activate 3 deactivate 4 Status 5 'Add partition to share' 6 Uninstall 2>.temp")
		ch=int(c.getoutput("cat .temp|tail -1"))
	except:
		
		os.system("rm -f .temp")
		exit()

	if ch==1:
		x=c.getoutput("rpm -q scsi-target-utils")
		if x=='package scsi-target-utils is not installed':
			ex=os.system("yum install scsi-target-utils -y 1>/dev/null 2>/dev/null")
			if ex==0:
				pass
			else:
				os.system("Xdialog --title 'ISCSI server Configuration' --msgbox 'yum is not configured yet\n\n please configure yum first' 15 50")
				exit()
		else:
			os.system("Xdialog --title 'ISCSI server configuration' --msgbox 'ISCSI server allready configured' 15 50")
			#continue
	
		status=c.getoutput("service tgtd status|awk -F' ' '{print $3}'")
		if status=='stopped':
			ex=os.system("Xdialog --title 'ISCSI server Configuration' --yesno 'service is stopped\n\n want to start service?' 15 50")
			if ex==0:
				os.system("service tgtd start >/dev/null")
			else:
				pass
		else:
			ex=os.system("Xdialog --title 'ISCSI server Configuration' --yesno 'service is active\n\nwant to stop service?' 15 50")
			if ex==0:
				os.system("service tgtd stop >/dev/null")
			else:
				pass
		ex=os.system("Xdialog --title 'ISCSI server Configuration' --yesno 'want to start service at boot time' 15 50")
		if ex==0:
			os.system("chkconfig tgtd on ")
		else:
			pass
		os.system("iptables -A INPUT -p tcp --dport 3260 -j ACCEPT")
		os.system("Xdialog --title 'ISCSI server zconfiguration' --msgbox 'Add raw partition to share...' 15 50")
	

	if ch==2:
	
		status=c.getoutput("service tgtd status|awk -F' ' '{print $3}'")
		if status=='stopped':
			os.system("service tgtd start >/dev/null")
			os.system("Xdialog --title 'ISCSI server Configuration' --msgbox 'ISCSI service successfully Actived' 15 50")
		else:
			os.system("Xdialog --title 'ISCSI server Configuration' --msgbox 'ISCSI service allready Active' 15 50")

	elif ch==3:
		status=c.getoutput("service tgtd status|awk -F' ' '{print $6}'")
		if status=='running...':
			os.system("service tgtd stop >/dev/null")
			os.system("Xdialog --title 'ISCSI server Configuration' --msgbox 'ISCSI service successfully Dectived' 15 50")
		else:
			os.system("Xdialog --title 'ISCSI server Configuration' --msgbox 'ISCSI service allready Dective' 15 50")
	elif ch==4:
		x=c.getoutput("rpm -q scsi-target-utils")
		if x=='package scsi-target-utils is not installed':
			os.system("Xdialog --title 'ISCSI server Configuration' --msgbox 'ISCSI server is not configured yet\n first configure ISCSI server' 15 50")
		else:
			status=c.getoutput("service tgtd status|awk -F' ' '{print $6}'")
			if status=='running...':
				os.system("Xdialog --title 'ISCSI server Configuration' --msgbox 'ISCSI server is running...' 15 50")
			else:
				os.system("Xdialog --title 'ISCSI server Configuration' --msgbox 'ISCSI server is stopped...' 15 50")

	elif ch==5:
		os.system("Xdialog --title 'ISCSI server Configuration' --inputbox 'partition name' 15 50 2>.temp")
		part=c.getoutput("cat .temp|head -1")
		os.system("Xdialog --title 'ISCSI server Configuration' --inputbox 'enter IQN' 15 50 2>.temp")
		iqn=c.getoutput("cat .temp|head -1")
		f=open('/etc/tgt/targets.conf','a')
		f.write("\n<target iqn."+iqn+">\nbacking-store "+part+"\n</target>\n")
		f.close()
		os.system("service tgtd restart >/dev/null")

	elif ch==6:
		x=c.getoutput("rpm -q scsi-target-utils")
		if x=='package scsi-target-utils is not installed':
			os.system("Xdialog --title 'ISCSI server Configuration' --msgbox 'ISCSI server is not configured' 15 50")
		else:
			ex=os.system("Xdialog --title 'ISCSI server Configuration' --yesno 'are you sure?' 15 50")
			if ex==0:
				os.system("rpm -e scsi-target-utils")
				os.system("Xdialog --title 'ISCSI server Configuration' --msgbox 'ISCSI server successfully Uninstall' 15 50")
			else:
				pass

