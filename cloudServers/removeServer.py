#!/usr/bin/env python

# Deletes a server in either ORD or DFW

import os
import sys
import time
import pyrax

pyrax.set_setting("identity_type", "rackspace")
credsFile = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(credsFile)

print "Here is a list of your current servers:"
# Prints out all your current servers
# Note: lists for DFW and ord
csDfw = pyrax.connect_to_cloudservers(region="DFW")
csOrd = pyrax.connect_to_cloudservers(region="ORD")
for dfwServer in csDfw.servers.list():
        print "Name:",dfwServer.name
        print "   ID:",dfwServer.id
        print "   Region: DFW"
for ordServer in csOrd.servers.list():
        print "Name:",ordServer.name
        print "   ID:",ordServer.id
        print "   Region: ORD"
print

# Select the region of the server
isRegion = raw_input("What is the region your server is in? (DFW or ORD): ")
# Select the name of the server you would like to delete
nameServ = raw_input("What is the name of the server you would like to delete?: ")

# Determines if server was in DFW or ORD
if isRegion == "DFW":
	serv = csDfw.servers.find(name=nameServ)
if isRegion == "ORD":
	serv = csOrd.servers.find(name=nameServ)

# Warning notice (:
answer = raw_input("NOTE!!!! This will result in complete data loss, please backup any data before doing this action...\nEnter in [y/n] to continue: ")
if answer != "y":
	sys.exit()

# Delete the server
print "Deleting server now..."
print
serv.delete()
print "Server now in deletion...."
