#!/usr/bin/python2

import os,commands as  c



os.system("touch /etc/yum.repos.d/package.repo")

while True:
	os.system("Xdialog --title 'yum Configurstion' --cancel-label 'back' --inputbox 'enter package id' 15 40 2>.temp")
	p_id=c.getoutput("cat .temp|head -1")
	os.system("Xdialog --title 'yum Configurstion' --cancel-label 'back' --dselect '/' 15 40 2>.temp")
	path=c.getoutput("cat .temp|head -1")
	os.system("createrepo "+path+" >/dev/null")

	f=open('/etc/yum.repos.d/package.repo','a')
	f.write("\n["+p_id+"]\nbaseurl=file://"+path+"\ngpgcheck=0\n")
	f.close()

	os.system("yum clean all 1>/dev/null 2>/dev/null")
	os.system("rm -f .temp")
	ex=os.system("Xdialog --title 'yum configuration' 'back' --yesno 'Add more package folder' 25 40 ")
	if ex==0:
		continue
	else:
		break



