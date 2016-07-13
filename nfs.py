#!/usr/bin/python2

from os import system
import os
import commands

system("Xdialog --msgbox 'Welcome to NFS Server Configuration' 0 0")


while True:
	
	system("Xdialog --menubox 'Select your choice' 15 50 3 1 'Install NFS server' 2 'Select directories to share and clients' 3 'Exit' 2> .tempnfs")

	try:
		choice = int(commands.getoutput("cat .tempnfs"))

	except ValueError:
		exit()


	if choice == 1:		# Install NFS server
		commands.getoutput("yum install nfs-utils > .tempnfs")
		system("Xdialog --textbox .tempnfs 10 50")
		system("service nfs restart > /dev/null")
		system("Xdialog --msgbox 'NFS server installed and service started' 10 50")
	

	elif choice == 2:       # Select directories to share and client ip addresses
		system("Xdialog --inputbox 'Enter no of dir to share' 20 40 1 2> .tempnfs")
		try:
			shares=int(commands.getoutput("cat .tempnfs"))
		except :
			system("Xdialog --msgbox 'Enter correct no of directories' 20 20")

		for i in range(0,shares):
			system("Xdialog --dselect / 0 0 2> .tempnfs")
			dirname=commands.getoutput("cat .tempnfs")
			print dirname
			system("Xdialog --inputbox 'Enter ip of client' 0 0 2> .tempnfs")
			ipadd=commands.getoutput("cat .tempnfs")
			f=open('/etc/exports','a')
			f.write("\n"+dirname+" "+ipadd+"(sync)")
			f.close()
			os.chmod(dirname,0776)
			system("exportfs -r")
			
		system("Xdialog --msgbox 'Directories shared successfully' 0 0")


	elif choice == 3:      # Exits
		exit()

