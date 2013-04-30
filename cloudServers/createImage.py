#!/usr/bin/env python

# This is a simple image creation program, nothin fancy

import os
import pyrax

# Credentials
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)

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

# Get Region
isRegion = raw_input("What region is the server in? (DFW or ORD [case sensitive!]): ")
# Get server ID
servID = raw_input("Which server would you like to make an image of (Enter in the Server ID): ")
print

# Which region?
if isRegion == "DFW":
	imgServer = csDfw.servers.get(servID)
if isRegion == "ORD":
	imgServer = csOrd.servers.get(servID)

imgName = raw_input("What would you like to name this image?: ")
print "Creating image now..."

imgServer.create_image(imgName)

print "Image in creation!"
