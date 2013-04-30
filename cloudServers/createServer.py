#!/usr/bin/env python

# Will create a server with name, image, and flavour of choice
# NOTE: This will spin up in DFW as of current version

import os
import pyrax

# Credentials
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cs = pyrax.cloudservers

# Name the server
servName = raw_input("What would you like to name your server?: ")
print

# List available images then prompt for image
imgs = cs.images.list()
for img in imgs:
    print img.name, "  -- ID:", img.id
print
servImg = raw_input("Enter in the ID of the image you would like to spin up: ")

# Print available flavours then prompt for flavour
flvs = cs.flavors.list()
for flv in flvs:
    print "Name:", flv.name
    print "  ID:", flv.id
    print "  RAM:", flv.ram
    print "  Disk:", flv.disk
    print "  VCPUs:", flv.vcpus
print
servFlav = raw_input("Enter in the flavour of your choice (choose the ID): ")
print

print "Now creating server..."
print

# Create server
server = cs.servers.create(servName, servImg, servFlav)

# Print out server info
print "Name:", server.name
print "ID:", server.id
print "Status:", server.status
print "Admin Password:", server.adminPass
print "Networks:",server.networks
