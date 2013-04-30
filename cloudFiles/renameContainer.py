#!/usr/bin/env python

# This will "Rename" a container by utilizing the move object function
# It moves the objects within a container to a new container
# Will carry over CDN and TTL if enabled and spit out new URIs

import os
import pyrax
import pyrax.exceptions as exc
import pyrax.utils as utils

# Credentials
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cf = pyrax.cloudfiles

# List out your current containers
print "Your current containers are:\n", cf.get_all_containers()
print

# Select container to rename
contName = raw_input("Which container would you like to rename?: ")
cont = cf.get_container(contName)
print

# Prompt for rename then create new container
newName = raw_input("What would you like to rename the container to?: ")
print

newCont = cf.create_container(newName)

# Check for CDN and TTL, if old container was CDN, enable CDN and set TTL
isCDN = cont.cdn_enabled
if isCDN == True:
	newCont.make_public(ttl = cont.cdn_ttl)

# Move the files to the new container
for obj in cont.get_objects():
	cf.move_object(cont,obj,newCont)
print

print "Renamed folder successfully!"
print

# Delete old container
cont.delete

# If CDN was enabled, provide new URIs
if isCDN == True:
	print "Here's your updated CDN URIs:"
	print "Public URI:",newCont.cdn_uri
	print "SSL URI:",newCont.cdn_ssl_uri
	print "Streaming URI:", newCont.cdn_streaming_uri
	print "iOS URI:",newCont.cdn_ios_uri
print
