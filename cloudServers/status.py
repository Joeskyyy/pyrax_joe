#!/usr/bin/env python

import os
import sys
import time
import pyrax

pyrax.set_setting("identity_type", "rackspace")
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)

# Prints out all your current servers and their statuses
# Note: lists for DFW and ord
print "Here is a list of your current servers and their status"
csDfw = pyrax.connect_to_cloudservers(region="DFW")
csOrd = pyrax.connect_to_cloudservers(region="ORD")
for dfwServer in csDfw.servers.list():
        print "Name:",dfwServer.name
        print "   ID:",dfwServer.id
        print "   Region: DFW"
	print "   Status:",dfwServer.status
for ordServer in csOrd.servers.list():
        print "Name:",ordServer.name
        print "   ID:",ordServer.id
        print "   Region: ORD"
	print "   Status:", ordServer.status
print

