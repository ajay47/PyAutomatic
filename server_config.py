#!/usr/bin/python2

import os,commands as c


while True:
	try:
		os.system("Xdialog --title 'Server Configuration' --cancel-label 'Back' --center --menubox '' 20 50 6 1 'Telnet server' 2 'FTP server'  3 'NFS server'  4 'ISCSI server' 2>.temp")
		ch=int(c.getoutput("cat .temp|tail -1"))
	except:
		os.system("rm -f .temp")
		break

	if ch==1:
		os.system("./telnet.py")
	elif ch==2:
		os.system("./ftp_server.py")
	elif ch==3:
		os.system("./nfs.py")
	
	elif ch==4:
		os.system("./iscsi_server.py")


