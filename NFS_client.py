#!/usr/bin/python2


import os,commands as c

os.system("yum install nfs-utils -y >/dev/null 2>/dev/null")
os.system("Xdialog --title 'NFS Client Configuration' --inputbox 'enter server ip ' 15 50 2>.temp")
ip=c.getoutput("cat .temp|head -1")
os.system("showmount -e "+ip+" >.temp")
os.system("Xdialog --titel 'NFS client Configuration' --textbox  './.temp' 15 50")
os.system("Xdialog --title 'NFS Client Configuration' --inputbox 'Directory of server' 15 50 2>.temp")
ser_dir=c.getoutput("cat .temp|head -1")

while True:
	os.system("Xdialog --timeout 15 --title 'NFS Client Configuration' --infobox 'select mount point on your system' 15 50 ")
	ex=os.system("Xdialog --title 'NFS Client Configuration' --dselect / 25 50 2>.temp")
	if ex==0:
		client_dir=c.getoutput("cat .temp")
		os.system("mount "+ip+":"+ser_dir+" "+client_dir)
		break
	else:
		os.system("Xdialog --title 'NFS Client Configuration' --msgbox 'mount point not selectd' 15 50 ")


os.system("Xdialog --title 'NFS Client Configuration' --msgbox 'NFS client Successfully Configured' 15 50 ")

