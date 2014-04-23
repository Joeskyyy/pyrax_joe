#!/usr/bin/env python

# Lists all flavours available

import os
import pyrax

# Credentials
pyrax.set_setting("identity_type", "rackspace")
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cs = pyrax.cloudservers

# Gets flavours
flvs = cs.flavors.list()

# Prints out each flavour
for flv in flvs:
	print "Name:", flv.name
	print " ID:", flv.id
	print " RAM:", flv.ram
	print " Disk:", flv.disk
	print " VCPUs:", flv.vcpus
	print
