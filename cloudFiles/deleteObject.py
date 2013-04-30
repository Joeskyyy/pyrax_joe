#!/usr/bin/env python

# Deletes an object from a selected container, will loop for usability purposes

import os
import pyrax
import pyrax.exceptions as exc
import pyrax.utils as utils

creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cf = pyrax.cloudfiles

ans = "y"
# While the user still wants to delete files
while ans == "y":
	# Print out the current containers
	print "Your current containers are:\n", cf.get_all_containers()
	print
	# Prompt for container name
	contName = raw_input("Which container is the file in?: ")
	cont = cf.get_container(contName)
	print
	
	# List container contents
	print "That container has the following objects:\n", cont.get_objects()
	print
	# Prompt for object to delete
	file = raw_input("Which file would you like to delete?: ")

	# Delete object
	cont.delete_object(file)
	
	print
	print "Deleted file successfully!"
	print
	# Prompt to delete another file
	ans = raw_input("Would you like to delete another file? [y/n]: ")
