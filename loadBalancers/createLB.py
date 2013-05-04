#!/usr/bin/env python

# Will create a cloud LB, with user selected options

import os
import pyrax

# Creds
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)


# Get region and name
isRegion = raw_input("What region would you like to create this load balancer in? (DFW/ORD): ")
print

# Set the region for your LB object
if isRegion == "DFW":
        lb = pyrax.connect_to_cloud_loadbalancers(region="DFW")
if isRegion == "ORD":
        lb = pyrax.connecto_to_cloud_loadbalancers(region="ORD")
lbName = raw_input("What would you like to name the load balancer?: ")
print

#Set the region for your CS object
if isRegion == "DFW":
	cs = pyrax.connect_to_cloudservers(region="DFW")
if isRegion == "ORD":
	cs = pyrax.connecto_to_cloudservers(region="ORD")
for srv in cs.servers.list():
	print "Name:",srv.name
	print "   ID:",srv.id
print

# Get the initial node
nodeID = raw_input("Which server would you like to add as the first node? (Enter in the ID): ")
node1 = cs.servers.get(nodeID)
# Retrieve the ServiceNet IP
nodeIP = node1.networks["private"][0]
print

# List out all available protocols
print lb.protocols
print

# Set the protocol
lbprot = raw_input("What protocol would you like to use? (i.e. HTTP, HTTPS, TCP): ")
print

# Set the port
lbport = raw_input("What port would you like to use? (i.e. 80, 443): ")
print

# Sets public or private LB
lbtype = raw_input("Is this a PUBLIC or PRIVATE loadbalancer?: ")
vip = lb.VirtualIP(type=lbtype)
print

# Create the node object
node = lb.Node(address=nodeIP, port = lbport, condition = "ENABLED")

# Create the LB
print "Creating load balancer now!"
loadbalancer = lb.create(lbName, port=lbport, protocol=lbprot, nodes=[node], virtual_ips=[vip])
print

# List out LB info
print "Created successfully! Here's the loabalancer information:\n"
print "Name", loadbalancer.name
print "Virtual IP:", loadbalancer.virtual_ips
print "Protocol:", loadbalancer.protocol

