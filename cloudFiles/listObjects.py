#!/usr/bin/env python

import os
import pyrax

creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cf = pyrax.cloudfiles

print "Your current cloud files containers are:"
print cf.get_all_containers()
contName = raw_input("Which container would you like to list the contents of?: ")
cont = cf.get_container(contName)

print "The current objects in that container are:\n", cont.get_objects()

