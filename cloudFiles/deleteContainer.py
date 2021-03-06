#!/usr/bin/env python

# This will delete a container
# NOTE: The container will need to be empty BEFORE attempting to delete

import os
import pyrax

# Credentials
pyrax.set_setting("identity_type", "rackspace")
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cf = pyrax.cloudfiles

# List containers and then prompt for container to delete
print "Your current containers are:\n", cf.get_all_containers()
cont_name = raw_input("Enter in the name of the container you would like to delete: ")
cont = cf.get_container(cont_name)
print

# Delete the container
print "Now deleting container:",cont_name
cont.delete()
print "Containter successfully deleted!"
