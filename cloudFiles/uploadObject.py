#!/usr/bin/env python

# This file right now will upload a file named by the user, to the container
# The contents will contain 100 lines with the same message

import os
import pyrax
import pyrax.exceptions as exc
import pyrax.utils as utils

# Credentials
pyrax.set_setting("identity_type", "rackspace")
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cf = pyrax.cloudfiles

# List current Containers
print "Your current containers are: ", cf.get_all_containers()
contName = raw_input("What container would you like to upload to?: ")
cont = cf.get_container(contName)
print

# Lets user choose name of file
fileName = raw_input("What is to be the name of this file?: ")

#Create contents of file
testContent = "This is a test file...\n"*100

#Store the file
obj = cf.store_object(cont, fileName, testContent)
print "Stored object:",obj
