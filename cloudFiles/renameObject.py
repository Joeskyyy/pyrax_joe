#!/usr/bin/env python

# This will "Rename" and object by utilizing the move object function
# It moves the object within a container to the same container, only with a new name

import os
import pyrax
import pyrax.exceptions as exc
import pyrax.utils as utils

# Credentials
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cf = pyrax.cloudfiles

# List out your current containers
print "Your current containers are:\n", cf.get_all_containers()
print

# Select container for object
contName = raw_input("Which container is the file in?: ")
cont = cf.get_container(contName)

# List out objects
print "That container has the following objects:\n", cont.get_objects()
print

# Prompt for file to rename
file = raw_input("Which file would you like to rename?: ")
print

# Prompt for new name
newName = raw_input("What would you like to rename the file to?: ")

# "Move" the file to the same container, only with a new name
cf.move_object(cont,file,cont,newName)
print

print "Renamed file successfully!"
print

