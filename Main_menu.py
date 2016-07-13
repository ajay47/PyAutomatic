#!/usr/bin/python2

import os,commands as c


while True:
	try:
		os.system("Xdialog --title 'Project' --cancel-label 'EXIT' --center --menubox '' 15 50 5 1 'File/Directory Management' 2 'User Mangement' 3 'Partitions' 4 'Server/Client Configuration' 5 'YUM Creation'  2>.temp")
		ch=int(c.getoutput("cat .temp|tail -1"))
	except:
		os.system("rm -f .temp")
		exit()

	if ch==1:
		os.system("./fdman.py")
	elif ch==2:
		os.system("./user_manage.py")
	elif ch==3:
		os.system("./partition.py")
	elif ch==4:
		os.system("./server_client_config.py")
	elif ch==5:
		os.system("./yum.py")
	


