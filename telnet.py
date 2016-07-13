#!/usr/bin/python2

import os
import commands
while True:
	try:
		os.system("Xdialog --menubox SERVERS 15 50 40 1 'TELNET Server' 2 'APACHE Server' 3 'NIS Server' 4 Back 2>ch.txt")

		ch=int(commands.getoutput("cat ch.txt"))
	except:
		os.system("rm -f ch.txt")
		exit()
			
	while True:
		if ch==1 :		
			os.system("Xdialog --menubox TELNET 15 50 40 1 Server 2 Client 3 'Add User' 4 Exit 2>ch1.txt")
	
			ch1=int(commands.getoutput("cat ch1.txt"))
			if ch1==1 :
				os.system('yum install telnet-server -y 2>/dev/null > /dev/null')
				f=open("/etc/xinetd.d/telnet","r")
				filedata=f.read()
				f.close()
				newdata=filedata.replace("yes","no")
				f=open("/etc/xinetd.d/telnet","w")
				f.write(newdata)
				f.close()
				os.system("Xdialog --inputbox 'Enter y to restart the service: ' 15 50 2>yn.txt")
				yn=commands.getoutput("cat ch1.txt")
				if yn=="y" :
					os.system("service xinetd restart > /dev/null")		
					os.system("Xdialog --infobox 'Server Configured' 15 50")
				u=raw_input()
				os.system("clear")
			elif ch1==2 :
				os.system('yum install telnet -y 2>/dev/null > /dev/null')
				ip=raw_input("Enter the IP address ")
				user=raw_input("Enter the name of the user ")
				passw=raw_input("Enter the password ")
				os.system("echo '" + user + "\n" + passw + "\n' | telnet " + ip) 
			elif ch1==3 :
				os.system("Xdialog --inputbox 'Enter the name of the new user: ' 15 50 2>us.txt")
				user=commands.getoutput("cat us.txt")
				os.system('useradd ' + user)
				os.system("Xdialog --inputbox 'Enter the password: ' 15 50 2>ps.txt")
				passw=commands.getoutput("cat ps.txt")
				os.system('echo ' + passw + ' | passwd ' + user + ' --stdin')
				os.system("Xdialog --infobox 'User Added' 15 50")
				u=raw_input()
				os.system("clear")
			elif ch1==4:
				break
			else :
				os.system("Xdialog --infobox 'Invalid Option' 15 50")
		if ch==2 :
			os.system("Xdialog --menubox APACHE 15 50 4 1 Server 2 Client 3 Exit 2>ch1.txt")
		
			ch1=int(commands.getoutput("cat ch1.txt"))
			if ch1==1 :
				os.system('yum install httpd -y 2>/dev/null > /dev/null')
				os.system("Xdialog --inputbox 'Enter y to restart the service: ' 15 50 2>yn.txt")
				yn=commands.getoutput("cat ch1.txt")
				if yn=="y" :
					os.system("service xinetd restart > /dev/null")		
	
				os.system("Xdialog --infobox 'Server Configured. Place your files at /var/www/html' 15 50")
				u=raw_input()
				os.system("clear")
			if ch1==2 :
				os.system("Xdialog --infobox 'Client Side' 15 50")
				u=raw_input()
				os.system("clear")
			if ch1==3 :
				break
		if ch==3 :
			os.system("Xdialog --menubox NIS 15 50 40 1 Server 2 Update 3 Exit 2>ch1.txt")
			ch1=int(commands.getoutput("cat ch1.txt"))
			if ch1==1 :
				os.system('yum install ypserv -y 2>/dev/null > /dev/null')
				os.system("Xdialog --inputbox 'Enter y to restart the service: ' 15 50 2>yn.txt")
				yn=commands.getoutput("cat ch1.txt")
				if yn=="y" :
					os.system("service ypserv restart > /dev/null")	

				os.system("yplocationname COMMON")	
				os.chdir("/var/yp")
				os.system("make > /dev/null")
				os.system("Xdialog --infobox 'Server Configured' 15 50")
				u=raw_input()
				os.system("clear")
			if ch1==2 :
				os.chdir("/var/yp/COMMON")
				os.system("make")
				os.system("Xdialog --infobox 'Users Updated' 15 50")
				os.system("clear")
			if ch1==3 :
				break
		elif ch==4 :
			exit()
	
