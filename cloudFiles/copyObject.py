#!/usr/bin/env python

# This will copy a container from one container to another
# NOTE: This will keep the file name the same!

import os
import pyrax
import pyrax.exceptions as exc
import pyrax.utils as utils

# Credentials
pyrax.set_setting("identity_type", "rackspace")
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cf = pyrax.cloudfiles

# List all containers
print "Your current containers are:\n", cf.get_all_containers()
print

# prompt for name of container and select that container
contName = raw_input("Which container is the file in?: ")
cont = cf.get_container(contName)

# list that containers objects
print "That container has the following objects:\n", cont.get_objects()
print

# Prompt for name of file to copy
file = raw_input("Which file would you like to copy?: ")
print

# List containers again for usability
print "Your current containers are:\n", cf.get_all_containers()

# Prompt for destination container
dest = raw_input("What container would you like to copy your file to?: ")

# Copy the file over without deleting original
cf.copy_object(cont,file,dest)

print
print "Copied file successfully!"
print

