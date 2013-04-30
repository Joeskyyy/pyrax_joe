#!/usr/bin/env python
import os
import pyrax

creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cs = pyrax.cloudservers

for server in cs.servers.list():
	print "Name:",server.name
	print "\tID:",server.id
servID = raw_input("Which server would you like to delete? (Enter in the Server ID): ")

delServer = cs.servers.get(servID)

imgName = raw_input("What would you like to name this image?: ")
print "Creating image now..."

delServer.create_image(imgName)

print "Image in creation!"
