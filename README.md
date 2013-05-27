cloaked-octo-tyrion
===================
RC test utility performs 2 types for runs

1. Run Instances


  a. Create keypair and write ssh key to a file

  b. Create a security group and ssh rule

  c. Launch an instances

  d. Runs a dd command to create a 50MB size file and get md5sum check remotely

  e. Downloads the file locally and compares the md5sum

  f. Uploads a 2MB random file

  g. Reboots the instances

  h. Cleanup, remove keypair,security group and terminate instances
  


2. Run Instances and Snapshot

  a. Create keypair and write ssh key to a file

  b. Create a security group and ssh rule

  c. Launch an instances

  d. Runs a dd command to create a 50MB size file and get md5sum check remotely

  e. Downloads the file locally and compares the md5sum

  f. Uploads a 2MB random file

  g. Reboots the instances

  h. Creates a snapshot from the running VM

  i. Cleanup once the snapshot is active

------------------------------------------------------------------------------------------------------------------------

Required package

python-paramiko

python-novaclient

------------------------------------------------------------------------------------------------------------------------


Configuration File

Copy the test_config.ini to /tmp/ directory


[zone]

cell=melbourne-np

user=rc_user_name(e.g. xx@unimelb.edu.au)

passwd=rc_user_passwd(!=dashboard)

name=tenant_name

url=https://keystone.com:35357/v2.0/

image_id=662be806-845b-4610-9895-803e0827386b (image id)

user_name=ec2-user (image user name e.g. ubuntu)

flavour_type=m1.small

[config]

directory=/tmp/

ssh_key_name=.key_rc

[timeout]

period=10

[file_check]

local_file=/tmp/data.file

tmp_dir=/tmp/

[log_file]

file=/tmp/nova.log

[csv_file]

file=/tmp/csv_data.csv


-----------------------------------------------------------------------------------------------------------------------

The test will log run time information to /tmp/nova.log

Result of test is saved in /tmp/csv_data.csv

"TestId","DATETIME","CELL","VMRUN","RUN_STAT","SNAPRUN","SNAP_STAT","OVERALL","OVERA_STAT"

"2G04DD-270513142326","270513142326","melbourne-np","201.9579348564148","0","98.77477788925171","0","336.86215710639954","0"


"Z9L8WM-270513143313","270513143313","melbourne-np","135.35868287086487","0","NA","NA","159.4681658744812","0"




---------------------------------------------------------------------------------------------------------------------

Running the test

/nectar-test --h

usage: nectar-test [-h] (--all | --instances)

Run VM Test on NeCTAR

optional arguments:

-h, --help   show this help message and exit

--all        Run VM and Snapshot Test

--instances  Run VM Test only
