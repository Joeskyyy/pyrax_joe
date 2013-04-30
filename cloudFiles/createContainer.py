#!/usr/bin/env python

# This will create a cloud files container, it will give the user the option to enable CDN, as well as set the TTL
import os
import pyrax

# Credentials
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cf = pyrax.cloudfiles

# Prompts for container name
cont_name = raw_input("Please enter in the container name you would like to create: ")

# Prompts for CDN, if user chooses yes, TTL is set
isCDN = raw_input("Would you like to enable public CDN on this folder? [y/n]: ")
if isCDN == "y":
	TTL = raw_input("What is the ttl (in seconds) that you would like for this container? [1-1576800000]: ")
print

# Create the container
print "Creating container with name:", cont_name
cont = cf.create_container(cont_name)

# Prints out container information
print "New container added successfully!"
print "Name:", cont.name
# Prints out CDN information is CDN was chosen
if isCDN == "y":
	cont.make_public(ttl = TTL)
	print "CDN Enabled:",cont.cdn_enabled
	print "CDN TTL in days:",cont.cdn_ttl
	print "Public URI:", cont.cdn_uri
	print "SSL URI:", cont.cdn_ssl_uri
	print "Streaming URI:", cont.cdn_streaming_uri
	print "iOS URI:", cont.cdn_ios_uri
print

