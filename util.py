import os
import sys
import getpass
import socket
import paramiko
from ConfigParser import SafeConfigParser
from paramiko import SSHClient, SSHConfig


class Alarm():
    pass

    def handler(self,signum,frame):
        raise Alarm()



class GetConfig():
    parser = SafeConfigParser()
    config_file = os.getcwd() +"/config.ini"
    parser.read(config_file)
    
    def process_config(self,section,option):
        for section_name in self.parser.sections():
            try:
                if section_name == section:
                    list_items = self.parser.get(section_name,option)
            except:
                list_items=None
                return list_items

        return list_items
    
    def port_test(self,host,timeout,port):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
            s.connect((host, int(port)))
        except IOError,e:
            return e
        return 0
        
    def connectSSH(self,hostname,user,key_rc):
        config = SSHConfig()
        #config.parse(open(ssh_config))
        #o = config.lookup(hostname)
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname, username=user, key_filename=key_rc)
        
        return ssh_client
    
    def runCommand(self,ssh_session,_type=None,cmd=None,local_file=None):
        if _type==1:
            stdin, stdout, stderr = ssh_session.exec_command(cmd)
            
            return 0
        elif _type==2:
            stdin, stdout, stderr = ssh_session.exec_command(cmd)
            _close = stdout.read()
            return _close
            
        elif _type==3:
            _scp=ssh_session.open_sftp()
            print local_file
            _scp.put(local_file,'test012')
            _scp.close()
            return 0
        else:
            ssh_session.close()
            
            
        
        
        
    
    
        
        
                    
            
            
            
        
    