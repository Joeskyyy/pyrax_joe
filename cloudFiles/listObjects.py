#!/usr/bin/env python

# Just lists the objects in a selected container

import os
import pyrax

# Credentials
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cf = pyrax.cloudfiles

# Lists containers
print "Your current cloud files containers are:"
print cf.get_all_containers()

# Select the container to list out
contName = raw_input("Which container would you like to list the contents of?: ")
cont = cf.get_container(contName)

# List out objects
print "The current objects in that container are:\n", cont.get_objects()

