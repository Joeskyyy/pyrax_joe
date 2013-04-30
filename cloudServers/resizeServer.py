#!/usr/bin/env python
import os
import pyrax

creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cs = pyrax.cloudservers

print "Here is a list of your current servers:"
for server in cs.servers.list():
        print "Name:",server.name
        print "\tID:",server.id
servID = raw_input("Which server would you like to resize? (Enter in the Server ID): ")
print

flvs = cs.flavors.list()
for flv in flvs:
        print "Name: %s   ID: %s" % (flv.name, flv.id)
	print "\tDisk Space: ",flv.disk
	print "\tvCPUs: ",flv.vcpus

newSize = raw_input("What size would you like to size to? (Enter in the ID): ")

print

print "Staring resize now..."
serv = cs.servers.get(servID)
serv.resize(newSize)

print "Server now in resize!"
