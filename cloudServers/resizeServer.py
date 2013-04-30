#!/usr/bin/env python

# Resizes a desired server in either ORD or DFW
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

# Get region
isRegion = raw_input("What region is the server in? (DFW or ORD): ")

#Get ID of server
servID = raw_input("Which server would you like to resize? (Enter in the Server ID): ")
print

# Lists available flavours
flvs = csDfw.flavors.list()
for flv in flvs:
        print "Name: %s   ID: %s" % (flv.name, flv.id)
	print "\tDisk Space: ",flv.disk
	print "\tvCPUs: ",flv.vcpus

# Retrieve desired size
newSize = raw_input("What size would you like to size to? (Enter in the ID): ")

print

print "Staring resize now..."

# Do resize, checks for region first
if isRegion == "DFW":
	serv = csDfw.servers.get(servID)
if isRegion == "ORD":
	serv = csOrd.servers.get(servID)
serv.resize(newSize)

print "Server now in resize!"
