#!/usr/bin/python2

from os import system
import os
import commands

system("tput setaf 1")
system("Xdialog --msgbox 'Welcome to partition management'  0  0")
system("tput setaf 0")

while True:
	
	system("Xdialog --menubox 'Select your choice' 17 35 6 1 'Create new partition' 2 'LVM' 3 'Format a partition' 4 'Mount a partition' 5 'List all partitions' 6 'List of mounted partitions' 2> .temp")

	try:
		choice = int(commands.getoutput("cat .temp"))

	except :
		system("rm -f .temp")
		exit()


	if choice == 1:		# Partition Creation starts here
		commands.getoutput("parted /dev/sda unit MiB print free | grep 'Free Space'| gawk '{print $3,\"\t\",$4}' > .temp")
		system("Xdialog --textbox .temp 10 50")
		system("Xdialog --inputbox 'Enter size of partition in MiB' 10 40 2> .temp")
		
		try:	
			sizetr = int(commands.getoutput("cat .temp"))
			size = commands.getoutput("cat .temp")

		except (NameError,ValueError):
			system("Xdialog --msgbox 'Invalid size' 0 0")
			continue
		sizeofnewpart = "+"+size+"M"	
	

		try:
			system("echo -e 'n\n\n"+sizeofnewpart+"\np\nw\n' | fdisk -cu /dev/sda > /dev/null")
			system("partx -a /dev/sda 2> /dev/null")
			newpa=commands.getoutput("fdisk -l /dev/sda|tail -1|cut -d' ' -f1 ")
			system("Xdialog --msgbox 'New partition "+newpa+" is created' 0 0")

		except OSError:
			system("Xdialog --msgbox 'Invalid input size' 7 20")


	elif choice == 2:       # LVM -_-   L  V   M    ---      L   v    M
		system("Xdialog --menubox 'Select your choice' 15 30 4 1 'Create LVM' 2 'Reduce LV' 3 'Extend VG' 4 'Extend LV' 2> .temp")

		try:
			choicelv = int(commands.getoutput("cat .temp"))

		except :
			continue
		
		if choicelv == 1:		# Create LVM
			system("Xdialog --inputbox 'Enter no of partitions for pvcreate' 15 40 2> .temp")

			try:
				parts=int(commands.getoutput("cat .temp"))
		
			except :
				system("Xdialog --msgbox 'Enter correct no of partitions' 13 45")
				continue
			# Create a PV here. Absolutely free XD
			for i in range(0,parts):
				try:
					system("Xdialog --fselect /dev -1 -1 2> .temp")
					a=commands.getoutput("cat .temp")
					print a
					system("umount "+a)
					system("pvcreate "+a)
				except :
					system("Xdialog --msgbox 'Select partitions properly' 20 20")
					break
			# VG creation starts here
			try:
				system("Xdialog --inputbox 'Enter name of VG' 20 40 2> .temp")
				nameofvg=commands.getoutput("cat .temp")
				system("Xdialog --inputbox 'Enter no of pv you want in VG' 20 40 2> .temp")
				parts=int(commands.getoutput("cat .temp"))
		
			except :
				system("Xdialog --msgbox 'Enter correct no of partitions' 13 45")
				continue
			vglist=[]
			for i in range(0,parts):
				try:
					system("Xdialog --fselect /dev -1 -1 2> .tempvg")
					a=commands.getoutput("cat .tempvg")
					vglist.append(a)
				except :
					system("Xdialog --msgbox 'Select partitions properly' 20 20")
					break


			l=len(vglist)
			f=''
			for i in range(0,l):
				f=f+vglist[i]+" "
			print f
			system("vgcreate "+nameofvg+" "+f)
			system("rm -f .tempvg")
			system("rm -f .temp")
			
			# LV creation starts here
			try:
				commands.getoutput("vgdisplay | grep 'VG Size' > .temp")  # Display VG size
				system("Xdialog --textbox .temp 10 40 ")
			
				system("Xdialog --inputbox 'Enter lv size in MB Use M as suffix' 20 40 2> .temp")
				lvsize=commands.getoutput("cat .temp")
				system("lvcreate --size "+lvsize+" --name "+nameofvg+" "+nameofvg)
				system("Xdialog --msgbox 'LV created successully' 20 40")
			except:
				system("Xdialog --msgbox 'Something went wrong' 20 40")

		elif choicelv == 2:      # Reduce LV
			try:
				system("Xdialog --msgbox 'Select LV to reduce' 20 40 2> .temp")
				system("Xdialog --fselect /dev -1 -1 2> .temp")
				lvname=commands.getoutput("cat .temp")
				commands.getoutput("lvdisplay | grep 'LV Size' > .temp")
				system("Xdialog --textbox .temp 10 40 ")
				system("Xdialog --inputbox 'Enter new size for LV in MB with M suffix' 20 50 2> .temp")
				newsize=commands.getoutput("cat .temp")
				system("umount "+lvname+" > /dev/null")
				system("e2fsck -f "+lvname+" > /dev/null")
				system("resize2fs "+lvname+" "+newsize+" > /dev/null")
				system("echo -e 'y\n' | lvreduce --size "+newsize+" "+lvname)
				system("Xdialog --msgbox 'LV reduced successfully' 20 40 ")
			except :
				system("Xdialog --msgbox 'Something went wrong' 20 40 ")
				continue

		elif choicelv == 3:      # Extend VG
			try:			
				system("Xdialog --inputbox 'Enter name of VG to extend' 10 40 2> .temp")
				vgname=commands.getoutput("cat .temp")
			
				commands.getoutput("vgdisplay | grep 'VG Size' > .temp")
				system("Xdialog --textbox .temp 10 40 ")

				system("Xdialog --msgbox 'Select PV to add in VG' 20 40 2> .temp")
				system("Xdialog --fselect /dev -1 -1 2> .temp")
				pvname=commands.getoutput("cat .temp")
	
				system("vgextend "+vgname+" "+pvname)
				system("Xdialog --msgbox 'VG extended successfully' 20 40 ")
			except :
				system("Xdialog --msgbox 'Something went wrong' 20 40 ")
				continue


		elif choicelv == 4:      #Extend LV
			try:
				system("Xdialog --msgbox 'Select LV to extend' 20 40 2> .temp")
				system("Xdialog --fselect /dev -1 -1 2> .temp")
				lvname=commands.getoutput("cat .temp")

				commands.getoutput("lvdisplay | grep 'LV Size' > .temp")
				system("Xdialog --textbox .temp 10 40 ")
			
				system("Xdialog --msgbox 'Select VG to see its size' 20 40 2> .temp")
				system("Xdialog --dselect /dev -1 -1 2> .temp")
				vgname=commands.getoutput("cat .temp")
				system("Xdialog --textbox .temp 50 50")

				system("Xdialog --inputbox 'Enter new size for LV in MB with M as suffix.' 20 50 2> .temp")
				newsize=commands.getoutput("cat .temp")
				system("lvextend --size "+newsize+" "+lvname)
				system("umount "+lvname)
				system("e2fsck -f "+lvname)
				system("resize2fs "+lvname)
				system("Xdialog --msgbox 'LV extended successfully' 20 40 2> .temp")
			except :
				system("Xdialog --msgbox 'Something went wrong' 20 40 ")
				continue
			#LV NAME
			#CURRENT SIZE
			#VG SIZE
			#NEW LV SIZE

		else:
			pass



	elif choice == 3:      # Formats a partition
		try:		
			system("Xdialog --msgbox 'Enter name of partition you want to format' 0 0")
			system("Xdialog --fselect /dev -1 -1 2> .temp")
			nameofformpart = commands.getoutput("cat .temp")
			system("Xdialog --menubox 'Confirm format ?' 10 35 2 1 Yes 2 No 2> .temp")
			temp_ch = int(commands.getoutput("cat .temp"))

		except:
			system("Xdialog --msgbox 'Something went wrong' 20 40 ")
			continue
		if temp_ch == 1:
			system("umount "+nameofformpart)
			system("mkfs "+nameofformpart+" > /dev/null")			
			system("Xdialog --msgbox "+nameofformpart+"'has been formatted' 0 0")

		else:
			continue


	elif choice == 4:		# Mount a partition
				
		system("Xdialog --fselect /dev 0 0 2> .temp")
		try:		
			nameofdevice = commands.getoutput("cat .temp")

		except :
			system("Xdialog --msgbox 'Invalid device' 7 12")
			continue	


		try:
			system("Xdialog --dselect / 0 0 2> .temp")
			nameofmountpoint = commands.getoutput("cat .temp")

		except :
			system("Xdialog --msgbox 'Invalid mount point' 7 12")
			continue


		temp_var = system("mount -f "+nameofdevice+" "+nameofmountpoint)
		

		if temp_var == 0:
			system("Xdialog --msgbox "+nameofdevice+"'has been mounted' 10 50")

		else:
			system("Xdialog --msgbox 'Oops! Something went wrong' 10 40")
			

	elif choice == 5:    # List all partitions		
		commands.getoutput("gawk  '{ print $4 }' /proc/partitions > .temp")
		system("Xdialog --textbox .temp 18 25")


	elif choice == 6:   # List mounted partitions
		commands.getoutput("df -T | gawk  '{ print $1,\"\t\",$7 }' > .temp")
		system("Xdialog --textbox .temp 15 40")


	else:			# It does nothing
		system("Xdialog --msgbox 'Invalid Choice' 8 15")
		system("sleep 5")
		exit()
	