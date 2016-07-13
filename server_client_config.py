#!/usr/bin/python2

import os,commands as c



while True:
	try:
		os.system("Xdialog --title 'Server/client Configuration' --cancel-label 'Back' --center --menubox 'Chose your option' 10 50 2 1 'Server Configuration' 2 'Client Configuration'  2>.temp")
		ch=int(c.getoutput("cat .temp|tail -1"))
	except:
		os.system("rm -f .temp")
		exit()

	if ch==1:
		os.system("./server_config.py")
	elif ch==2:
		os.system("./client_config.py")
	
