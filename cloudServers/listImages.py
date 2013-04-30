#!/usr/bin/env python

import os
import pyrax

creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cs = pyrax.cloudservers

imgs = cs.images.list()

for img in imgs:
	print "Name: %s\n	ID: %s" % (img.name, img.id)
