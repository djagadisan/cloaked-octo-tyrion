import getpass
import sys
import socket
host='115.146.85.177'
port=21
timeout=5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(timeout)
try :
        s.connect((host, int(port)))
except :
        print 'Unable to connect'
        sys.exit()
     
print 'Connected to remote host'
s.close()