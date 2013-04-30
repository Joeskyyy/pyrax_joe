#!/usr/bin/env python

import os

import pyrax
import pyrax.exceptions as exc
import pyrax.utils as utils

creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cf = pyrax.cloudfiles

print "Your current containers are: ", cf.get_all_containers()

contName = raw_input("What container would you like to upload to?: ")
cont = cf.get_container(contName)

fileName = raw_input("What is to be the name of this file?: ")

testContent = "This is a shit file...\n"*100
obj = cf.store_object(cont, fileName, testContent)
print "Stored object:",obj
