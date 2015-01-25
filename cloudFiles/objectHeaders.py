# This will set object headers for each file in a container
# Threaded for large containers
# No error trapping yet... caution
# Written by: Joe Engel

import os
import pyrax
import threading
import time

CONCURRENCY = 1000

# Credentials
pyrax.set_setting("identity_type", "rackspace")
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cf = pyrax.connect_to_cloudfiles(region="ORD")

# List containers and then prompt for container to delete
cont_name = ""
cont = cf.get_container(cont_name)
metadata = {""}

def header_obj(cfobj):
        print "Setting header for obj: %s" % cfobj.name
        cf.set_object_metadata(cont, cfobj)

print
for obj in cont.get_objects(full_listing=True):
    while threading.activeCount() > CONCURRENCY:
            time.sleep(0.1)
    threading.Thread(target=header_obj, args=(obj,)).start()

# Delete the container

print "DONE!"
