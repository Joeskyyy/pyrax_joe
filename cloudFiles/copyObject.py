#!/usr/bin/env python

import os

import pyrax
import pyrax.exceptions as exc
import pyrax.utils as utils

creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cf = pyrax.cloudfiles

print "Your current containers are:\n", cf.get_all_containers()
print
contName = raw_input("Which container is the file in?: ")
cont = cf.get_container(contName)
print "That container has the following objects:\n", cont.get_objects()

print
file = raw_input("Which file would you like to copy?: ")
print
print "Your current containers are:\n", cf.get_all_containers()
dest = raw_input("What container would you like to copy your file to?: ")

#MOVE FILE FROM CURRENT CONTAINER TO DEST CONTAINER WITHOUR RENAMING
cf.copy_object(cont,file,dest)

print
print "Copied file successfully!"
print

