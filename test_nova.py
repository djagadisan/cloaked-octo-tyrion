import os
import sys
import random
import string
import unicodedata
import time
from process_ini import GetConfig
from novaclient.v1_1 import client 

class TESTNOVA():
    
    def createConnection(self,_user,_key,_project_id,_auth_url):
        try:
            conn = client.Client(username=_user,api_key=_key,project_id=_project_id,auth_url=_auth_url)
            
        except Exception,e:
            return "Error %s" % e 
    
        return conn

        



__init__='main'



infra='deven'
ssh_file = open(".key_rc","w")
username=GetConfig().process_config(infra,'user')
passwd=GetConfig().process_config(infra,'passwd')
name=GetConfig().process_config(infra,'name')
url=GetConfig().process_config(infra,'url')
image_name=GetConfig().process_config('image','image_name')
image_id=GetConfig().process_config('image','image_id')
client = TESTNOVA().createConnection(username,passwd,name,url)

#for x in nt.keypairs.list():
#    print getattr(x,'name')

#create a random string for keypair

char_set = string.ascii_uppercase + string.digits
keypair_name=''.join(random.sample(char_set*6,6))
pub_key=None 
#create a keypair and save in a file    
keypair=client.keypairs.create(keypair_name,pub_key)
private_key = keypair.private_key
ssh_file.write(private_key)
os.chmod(os.getcwd()+'/.key_rc', 0600)
ssh_file.close()       

#list security groups
#sg = client.security_groups.list()
#for s in sg:
#    print s.rules

#create a security group
new_sg = client.security_groups.create(keypair_name,"ssh-port")


#add a rule to security group
proto='tcp'
port_to='22'
port_frm='22'
new_rule=client.security_group_rules.create(new_sg.id,proto,port_to,port_frm)
sg_run=new_sg.name.split(',')

#check if a image exits
_image_id=client.images.list()
_g_image_id = unicode(image_id)
for i in _image_id:
    if i.id == _g_image_id:
        print i.name,i.id
        
flavour_list = client.flavors.list()
for x in flavour_list:
    print x.id,x.name


flavor='0'
#next launch the vm
name='test'
time.sleep(30)
launch_vm = client.servers.create(name,image_id,flavor,key_name=keypair.name,security_groups=sg_run)
print launch_vm.id ,launch_vm.status,launch_vm.networks

time.sleep(60)




vm_infog = client.servers.list()
for i in vm_infog:
    if i.id==unicode(launch_vm.id):
        print i.name + "\n"+i.status
        for network_label,address_list in i.networks.items():
            print "".join(address_list)
        

    
#    for network_label,address_list in i.networks.items():
#        print "".join(address_list)











