#!/usr/bin/env python

import os
import sys
import time
import pyrax

creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cs = pyrax.cloudservers

print "Here is a list of your current servers:"
for server in cs.servers.list():
        print "Name:",server.name
        print "\tID:",server.id
nameServ = raw_input("What is the name of the server you need to check the status of?: ")
serv = cs.servers.find(name=nameServ)
print "%s is currently in the state %s" % (nameServ, serv.status)
