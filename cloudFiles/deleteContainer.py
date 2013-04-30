#!/usr/bin/env python

import os
import pyrax

creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cf = pyrax.cloudfiles


print "Your current containers are:\n", cf.get_all_containers()
cont_name = raw_input("Enter in the name of the container you would like to delete: ")

cont = cf.get_container(cont_name)
print "Now deleting container:",cont_name
cont.delete()
print "Containter successfully deleted!"
