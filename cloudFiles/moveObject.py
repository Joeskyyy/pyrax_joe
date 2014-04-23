#!/usr/bin/env python

# This will move an object from one container to another
# NOTE: This will delete the old file, the file name will not change

import os
import pyrax
import pyrax.exceptions as exc
import pyrax.utils as utils

# Credentials
pyrax.set_setting("identity_type", "rackspace")
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cf = pyrax.cloudfiles

# List Containers
print "Your current containers are:\n", cf.get_all_containers()
print
# Prompt for container
contName = raw_input("Which container is the file in?: ")
cont = cf.get_container(contName)
print

# List current objects in containers
print "That container has the following objects:\n", cont.get_objects()
print

# Prompt for file to move
file = raw_input("Which file would you like to move?: ")
print

# Re-list containers for usability
print "Your current containers are:\n", cf.get_all_containers()
dest = raw_input("What container would you like to move your file to?: ")

# Move files from one container to the other with the same name in tact
cf.move_object(cont,file,dest)

print
print "Moved file successfully!"
print

