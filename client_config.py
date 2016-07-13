#!/usr/bin/python2

import os,commands as c


while True:
	try:
		os.system("Xdialog --title 'Client Configuration' --cancel-label 'Back' --center --menubox '' 20 50 6 1 'Telnet Client' 2 'FTP Client' 3 'SSH Client' 4 'NFS Client' 5 'NIS Client' 6 'ISCSI Client' 2>.temp")
		ch=int(c.getoutput("cat .temp|tail -1"))
	except:
		os.system("rm -f .temp")
		break

	if ch==1:
		os.system("./telnet_client.py")
	elif ch==2:
		os.system("./ftp_client.py")
	elif ch==3:
		os.system("./ssh_client.py")
	elif ch==4:
		os.system("./NFS_client.py")
	elif ch==5:
		os.system("./NIS_client.py")
	elif ch==6:
		os.system("./iscsi_client.py")


