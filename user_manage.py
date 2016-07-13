#!/usr/bin/python2

import os
import commands as c

while True:
	os.system("clear")
	


	 
	try:
		os.system("Xdialog --title 'User Management' --cancel-label 'Back' --center --menubox 'chose from menu' 20 40 8 1 'Existing User' 2 'Add User' 3 'Delete User' 4 'change password' 5 'Rename User' 6 'add group' 7 'delete group' 8 'Rename Group' 2>.temp")
		ch=int(c.getoutput("cat .temp|tail -1"))
	except:
		
		os.system("rm -f .temp")
		exit()

	if ch==1:
		os.system("Xdialog --title 'existing user' --menubox '' 15 40 2 1 'system user' 2 'local user' 2>.temp2")
		ch=int(c.getoutput("cat .temp2|tail -1"))
		if ch==1:
			os.system("cat /etc/passwd |awk -F: '{if($3<500 || $3>60000){print $1}}' >.temp2")
			os.system("Xdialog --title 'system User' --textbox .temp2 20 40 ")
		elif ch==2:
			os.system("cat /etc/passwd |awk -F: '{if($3>=500 && $3<=60000){print $1}}' >.temp2")
			os.system("Xdialog --title 'local User' --textbox .temp2 20 40 ")
 		os.system("rm -f .temp2")
	elif ch==2:
		os.system("Xdialog --title 'Add User' --inputbox 'User Name' 15 40 2>.temp")
		u_name=c.getoutput("cat .temp")

		ex=os.system("useradd "+u_name+" 2> .temp")
		err=c.getoutput("cat .temp")
		if ex==0:
			pass
		elif ex==2304:
			os.system("Xdialog --title 'Add user' --infobox 'user allready exist' 15 40")
			continue
		else:
			os.system("Xdialog --title 'Add user' --msgbox '"+err+"' 15 50")
			continue
	#password for user
		os.system("Xdialog  --title 'Add user' --password --inputbox 'password' 15 40 2>.temp")
		u_pass=c.getoutput("cat .temp|tail -1")
		ex=os.system("echo "+u_pass+"|passwd --stdin "+u_name+" 1> /dev/null")
		if ex==0:
			os.system("Xdialog  --title 'Add user' --infobox 'user successfully created' 15 40")
		else:
			pass
	
	
	elif ch==3:
		os.system("Xdialog --title 'Delete User ' --inputbox 'User Name' 15 40 2>.temp")
		u_name=c.getoutput("cat .temp|tail -1")
		ex=os.system("userdel -r "+u_name+" 2>/dev/null")
		if ex==0:
			os.system("Xdialog --title 'Delete User ' --infobox 'user "+u_name+" successfully deleted' 15 40")
		else:
			os.system("Xdialog --title 'Delete User ' --infobox 'user "+u_name+" does not exist' 15 40")
	elif ch==4:
		os.system("Xdialog --title 'change password' --inputbox 'User Name' 15 40 2>.temp")
		u_name=c.getoutput("cat .temp|tail -1")

		os.system("Xdialog  --title 'change password' --password --inputbox 'password' 15 40 2>.temp")
		u_pass=c.getoutput("cat .temp|tail -1")
		ex=os.system("echo "+u_pass+"|passwd --stdin "+u_name+" 1> /dev/null")
		if ex==0:
			os.system("Xdialog  --title 'change password' --infobox 'password successfully changes' 15 40")
		else:
			pass
	elif ch==5:
		os.system("Xdialog --title 'Rename User' --inputbox 'User Name' 15 40 2>.temp")
		u_name=c.getoutput("cat .temp|tail -1")
		os.system("Xdialog --title 'Rename User' --inputbox 'New User Name' 15 40 2>.temp")
		newu_name=c.getoutput("cat .temp|tail -1")
		os.system("usermod -l "+newu_name+" "+u_name)
		os.system("Xdialog --title 'Rename User' --msgbox 'successfully Renamed' 15 40")
		
	elif ch==6:
		os.system("Xdialog --title 'Add group' --inputbox 'Group Name' 15 40 2>.temp")
		g_name=c.getoutput("cat .temp|tail -1")
		os.system("groupadd "+g_name)
		while True:
			os.system("Xdialog --title 'Add group member' --inputbox 'group members' 15 40 2>.temp")
			m_name=c.getoutput("cat .temp|tail -1")
			os.system("gpasswd -a "+m_name+" "+g_name)
			ex=os.system("Xdialog --title 'Add group member' --yesno 'add more member' 15 40 2>.temp")
			if ex==0:
				pass
			else:
				break
		
	elif ch==7:
		os.system("Xdialog --title 'Delete group' --inputbox 'Group Name' 15 40 2>.temp")
		g_name=c.getoutput("cat .temp|tail -1")
		os.system("groupdel "+g_name)
		os.system("Xdialog --title 'Delete group' --msgbox 'group "+g_name+" successfully deleted' 15 40")

	elif ch==8:
		os.system("Xdialog --title 'change group name' --inputbox 'Group Name' 15 40 2>.temp")
		g_name=c.getoutput("cat .temp|tail -1")
		os.system("Xdialog --title 'change group name' --inputbox 'New Group Name' 15 40 2>.temp")
		newg_name=c.getoutput("cat .temp|tail -1")
		os.system("groupmod -n "+newg_name+" "+g_name)
		os.system("Xdialog --title 'change group name' --msgbox 'group "+g_name+" successfully Renamed to "+newg_name+"' 15 50")
		



	



