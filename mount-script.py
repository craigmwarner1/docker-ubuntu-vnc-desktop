#!/usr/bin/python

import subprocess
from types import *

class SessionUser:
	"""Class containing the mountpoint destination for the google-drive FUSE directory and an id."""	
	def _init_(self):
		self._uid = ""
		self._mountpoint = ""
		
	def getUID(self):
		return self._uid

	def getMount(self):
		return self._mountpoint

	def _setUID(self, userName):
		assert type(userName) is StringType, "invalid username, not a string"
		self._uid = userName
#		if type(userName) == type(str):
#			self._uid = userName
#			return False
#		else:
#			print "Invalid type for username. Username is of type " + str(type(userName)) + " instead of type" + type(str) +"."
#			return True 	

	def _setMount(self, mountLoc):
		assert type(mountLoc) is StringType, "invalid mountpoint, not a string"
		self._mountpoint = mountLoc
#                 if type(mountLoc) == type(str):
#                         self._mountpoint  = mountLoc
# 			return False
#                 else:
#                         print "Invalid type for mountpoint. Mountpoint is of type " + type(mountLoc) + " instead of type" + type(str) +"."
# 			return True


def mountFolder(user):
	mountDestination = str(user.getUID()) + "-gdrive" 
	newMount = user._setMount(mountDestination)
	if newMount:
		print "Please enter a valid mountpoint."
	else:
		pass

def setUser(user):
	userTag = raw_input("Enter your username. ")
	newUser = user._setUID(userTag)
	if newUser:
		print "Please enter a valid username."
	else:
		pass

def main():
	
	#Initializes FUSE, creates necessary directory, authenticates in browser.
	subprocess.call("google-drive-ocamlfuse")	
	
	thisUser = SessionUser() 
	setUser(thisUser)
	mountFolder(thisUser)
	
	mountpoint = str(thisUser.getUID())	
	subprocess.call(["mkdir", mountpoint])
	subprocess.call(["google-drive-ocamlfuse", mountpoint])


main()
