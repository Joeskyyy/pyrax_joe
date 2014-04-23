#!/usr/bin/env python

# Lists all available images

import os
import pyrax

# Credentials
pyrax.set_setting("identity_type", "rackspace")
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cs = pyrax.cloudservers

# Retrieve available images
imgs = cs.images.list()

# Print Images
for img in imgs:
	print "Name: %s\n	ID: %s" % (img.name, img.id)
