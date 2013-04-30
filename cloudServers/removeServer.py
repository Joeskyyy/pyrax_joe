#!/usr/bin/env python

import os
import sys
import time

import pyrax

credsFile = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(credsFile)
cs = pyrax.cloudservers

print "Here is a list of your current servers:"
for server in cs.servers.list():
        print "Name:",server.name
        print "\tID:",server.id
nameServ = raw_input("What is the name of the server you would like to delete?: ")
serv = cs.servers.find(name=nameServ)
answer = raw_input("NOTE!!!! This will result in complete data loss, please backup any data before doing this action...\nEnter in [y/n] to continue: ")
if answer != "y":
	sys.exit()
print "Deleting  server...",
serv.delete()
print "Server now in deletion...."
