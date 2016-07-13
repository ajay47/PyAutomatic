#!/usr/bin/python2

from os import system
import os
import commands
import subprocess

while True:
	try:
		system("Xdialog --menubox MENU 20 50 7 1 'Create a file' 2 'Create a Directory' 3 'Delete a file' 4 'Delete a directory' 5 'Rename a file' 6 'List all the files' 7 'Back' 2>/root/Desktop/ch1.txt")


		ch=int(commands.getoutput("cat /root/Desktop/ch1.txt"))

		if ch==1 :
			os.system("Xdialog --inputbox 'Enter the LOCATION: ' 15 50 2>/root/Desktop/loc.txt")
			location=commands.getoutput("cat /root/Desktop/loc.txt")
			xyz=0
			try:
				os.chdir(location)
			except:
				os.system("Xdialog --infobox 'Invalid Location' 15 50")
				u=raw_input()
				xyz=1
			if xyz==1 :
				system('clear')
			elif xyz==0 :
				tempvar=commands.getoutput('find . -maxdepth 1 -type f -print | cut -d "/" -f2')
				filelist=tempvar.split()	
				os.system("Xdialog --inputbox 'Enter the name of the file you want to create: ' 15 50 2>/root/Desktop/nam.txt")
				name=commands.getoutput("cat /root/Desktop/nam.txt")
				abcd=0
				if name=="" :
					os.system("Xdialog --infobox 'You have not entered anything!' 15 50")
					u=raw_input()
					system("clear")
				else :
					for x in filelist :
						if name==x :
							abcd=1
					if abcd==1 :
						os.system("Xdialog --infobox 'File already Exists!' 15 50")
						u=raw_input()
						break
						system('clear')		
					elif abcd==0 :		
						system('touch -- ' + name)
						os.system("Xdialog --infobox 'Your file has been created at "+location+"' 15 50")
						u=raw_input()
						system('clear')
		elif ch==2 :
			os.system("Xdialog --inputbox 'Enter the LOCATION: ' 15 50 2>/root/Desktop/loc.txt")
			location=commands.getoutput("cat /root/Desktop/loc.txt")
			xyz=0
			try :
				os.chdir(location)
			except:
				os.system("Xdialog --infobox 'Invalid Location' 15 50")
				u=raw_input()
				xyz=1
			if xyz==1 :
				system('clear')
			elif xyz==0 :
				tempvar=commands.getoutput('find . -maxdepth 1 -type d -print | grep / | cut -d "/" -f2')
				filelist=tempvar.split()
				os.system("Xdialog --inputbox 'Enter the name of the directory you want to create: ' 15 50 2>/root/Desktop/nam1.txt")
				dirname=commands.getoutput("cat /root/Desktop/nam1.txt")
				abcd=0
				if dirname=="" :
					os.system("Xdialog --infobox 'You have not entered anything!' 15 50")
					u=raw_input()
					system("clear")
				else :
					for x in filelist :
						if dirname==x :
							abcd=1
					if abcd==1 :
						os.system("Xdialog --infobox 'Directory already Exists!' 15 50")
						u=raw_input()
						system('clear')
					elif abcd==0 :
						system('mkdir ' + dirname)
						os.system("Xdialog --infobox 'Your directory has been created at "+location+"' 15 50")
						u=raw_input()
						system('clear')
		elif ch==3 :
			os.system("Xdialog --inputbox 'Enter the LOCATION: ' 15 50 2>/root/Desktop/loc.txt")
			location=commands.getoutput("cat /root/Desktop/loc.txt")
			xyz=0
			try:
				os.chdir(location)
			except:
				os.system("Xdialog --infobox 'Invalid Location' 15 50")
				u=raw_input()
				xyz=1
			if xyz==1 :
				system('clear')
			elif xyz==0 :
				os.system("Xdialog --fselect " + location + "/ 0 0 2>/root/Desktop/fsel.txt")
				tempvar=commands.getoutput('find . -maxdepth 1 -type f -print | cut -d "/" -f2')	
				filelist=tempvar.split()
				os.system("Xdialog --inputbox 'Enter the name of the file you want to delete: ' 15 50 2>/root/Desktop/nam.txt")
				name=commands.getoutput("cat /root/Desktop/nam.txt")
				abcd=0
				for x in filelist :
					if name==x :
						abcd=1
				if abcd==1 :
					system('rm ' + name)
					os.system("Xdialog --infobox 'Your file has been sucessfully deleted' 15 50")
					u=raw_input()
					system('clear')
				elif abcd==0 :
					os.system("Xdialog --infobox 'No such File Exists!' 50 50")
					u=raw_input()
					system('clear')
		elif ch==4 :
			os.system("Xdialog --inputbox 'Enter the LOCATION: ' 15 50 2>/root/Desktop/loc.txt")
			location=commands.getoutput("cat /root/Desktop/loc.txt")
			xyz=0
			try:
				os.chdir(location)
			except:
				os.system("Xdialog --infobox 'Invalid Location' 15 50")
				u=raw_input()
				xyz=1
			if xyz==1 :
				system('clear')
			elif xyz==0 :
				os.system("Xdialog --fselect " + location + "/ 0 0 2>/root/Desktop/fsel.txt")
				tempvar=commands.getoutput('find . -maxdepth 1 -type d -print | grep / | cut -d "/" -f2')
				filelist=tempvar.split()
				os.system("Xdialog --inputbox 'Enter the name of the directory you want to delete: ' 15 50 2>/root/Desktop/nam.txt")
				dirname=commands.getoutput("cat /root/Desktop/nam.txt")
				abcd=0
				for x in filelist :
					if dirname==x :
						abcd=1
				if abcd==1 :
					system("rmdir " + dirname)
					os.system("Xdialog --infobox 'Your directory has been sucessfully deleted' 15 50")
					u=raw_input()
					system("clear")
				elif abcd==0 :
					os.system("Xdialog --infobox 'No such Directory Exists!' 15 50")
					u=raw_input()
					system('clear')
		elif ch==5 :
			os.system("Xdialog --inputbox 'Enter the LOCATION: ' 15 50 2>/root/Desktop/loc.txt")
			location=commands.getoutput("cat /root/Desktop/loc.txt")
			xyz=0
			try:
				os.chdir(location)
			except:
				os.system("Xdialog --infobox 'Invalid Location' 15 50")
				u=raw_input()
				xyz=1
			if xyz==1 :
				system('clear')
			elif xyz==0 :
				os.system("Xdialog --fselect " + location + "/ 0 0 2>/root/Desktop/fsel.txt")
				tempvar=commands.getoutput(' find . -maxdepth 1 -print | cut -d "/" -f2')
				filelist=tempvar.split()	
				os.system("Xdialog --inputbox 'Enter the name of the file/directory you want to rename: ' 50 50 2>/root/Desktop/nam.txt")
				name1=commands.getoutput("cat /root/Desktop/nam.txt")
				abcd=0
				if name1=="" :
					os.system("Xdialog --infobox 'You have not entered anything!' 15 50")
					u=raw_input()
					system("clear")
				else :
					for x in filelist :
						if name1==x :
							abcd=1
					if abcd==0 :
						os.system("Xdialog --infobox 'File doesnot Exist!' 15 50")
						u=raw_input()
						system('clear')		
					elif abcd==1 :		
						os.system("Xdialog --inputbox 'Enter the name you want: ' 15 50 2>/root/Desktop/nam.txt")
						name2=commands.getoutput("cat /root/Desktop/nam.txt")
						abcd=0
						if name1=="" :
							os.system("Xdialog --infobox 'You have not entered anything!' 15 50")
							u=raw_input()
							system("clear")
						else :
							for y in filelist :
								if name2==y :
									abcd=1
							if abcd==1 :
								os.system("Xdialog --infobox 'File/Directory with that name already Exist!' 15 50")
								u=raw_input()
								system('clear')		
							elif abcd==0 :		
								system('mv ' + name1 + ' ' + name2)
								os.system("Xdialog --infobox 'Your file/directory has been renamed as "+ name2 +"' 15 50")
								u=raw_input()
								system('clear')
		elif ch==6 :
			os.system("Xdialog --inputbox 'Enter the LOCATION: ' 15 50 2>/root/Desktop/loc.txt")
			location=commands.getoutput("cat /root/Desktop/loc.txt")
			xyz=0
			try:
				os.chdir(location)
			except:
				os.system("Xdialog --infobox 'Invalid Location' 15 50")
				u=raw_input()
				xyz=1
			if xyz==1 :
				system('clear')
			elif xyz==0 :
				os.system("Xdialog --fselect " + location + "/ 0 0 2>/root/Desktop/fsel.txt")
				system("clear")

		elif ch==7 :
			exit()
		else :
			os.system("Xdialog --infobox 'Invalid Option' 15 50")
			u=raw_input()
			system("clear")
	except:
		break
