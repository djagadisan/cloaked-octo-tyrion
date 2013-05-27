import time
import datetime
from util import GetConfig
from runtestinstances import RunInstancesTest
from runsnapshot import RunSnapshot
from logger import Logger
from cleanup import CleanUp
from write_to_csv import WriteCSV


class RunTest1():
    
   
    
    var_ = GetConfig()
    log = Logger()
    test = RunInstancesTest()
    clear = CleanUp()
    startTime = time.time()
    writer_ = WriteCSV()
    run_time = datetime.datetime.now().strftime("%d%m%y%H%M%S")
    
    def runTest1(self,config):
        
        test_name = self.var_._randomName()
        print "Running Instances and Snapshot Test:%s" % test_name
        if self.test.preTestCheck(config)!=False:
            
            msg = "Pre Check passed, running instances test"
            self.log.log_data(config.log_file,msg,"INFO")
            run_result = self.test.runTest(config,test_name)
            if run_result[0]!=False:
                msg = "Instances test completed, proceed with snapshot"
                self.log.log_data(config.log_file,msg,"INFO")
                print msg
                snap = RunSnapshot().runSnapshot(config,run_result[1],test_name)
                if snap[1]!=False:
                    msg = "Snapshot Test passed"
                    self.log.log_data(config.log_file,msg,"INFO")
                    print msg 
                    msg = "Test Successful"
                    self.log.log_data(config.log_file,msg,"INFO")
                    print msg
                
                    msg = "Running Cleaning up"
                    self.log.log_data(config.log_file,msg,"INFO")
                    print msg
                
                    msg = "Terminating Instances"
                    self.log.log_data(config.log_file,msg,"INFO")
                    print msg
                    self.clear.removeInstances(config, run_result[1])
                
                    msg = "Removing Snapshot"
                    self.log.log_data(config.log_file,msg,"INFO")
                    print msg
                    self.clear.removeSnapshot(config, snap[0])
                
                    msg = "Removing Security Groups and Keypair"
                    self.log.log_data(config.log_file,msg,"INFO")
                    misc = {'sg':test_name,'kp':test_name}
                    time.sleep(int(config.timeout))
                    if self.clear.removeMisc(config,misc,run_result[1])==True:
                        time_comp = self.var_.getrunTime('time')-self.startTime 
                        msg = "Clean Up complete, exiting test"
                        self.log.log_data(config.log_file,msg,"INFO")
                        print msg               
                        data_insert = [test_name,self.run_time,config.cell,run_result[2],'0',snap[2],'0',time_comp,'0']
                        WriteCSV().createCSVFile(config.csv_file, data_insert)
                        raise SystemExit
                    else:
                        time_comp = time.time()-self.startTime
                        msg = "Error, Unable to remove security group and key pair"
                        self.log.log_data(config.log_file,msg,"ERROR")
                        print msg
                        data_insert = [test_name,self.run_time,config.cell,run_result[2],'0',snap[2],'0',time_comp,'1']
                        WriteCSV().createCSVFile(config.csv_file, data_insert)
                        raise SystemExit
                     
                else:
                    
                    msg = "Snapshot test failed"
                    self.log.log_data(config.log_file,msg,"ERROR")
                    print msg
                    
                    msg = "Running Cleaning up"
                    self.log.log_data(config.log_file,msg,"INFO")
                    print msg
                    
                    msg = "Removing Failed Snapshot"
                    self.log.log_data(config.log_file,msg,"INFO")
                    print msg
                    self.clear.removeSnapshot(config, snap[0])
                    
                    msg = "Terminating Instances"
                    self.log.log_data(config.log_file,msg,"INFO")
                    print msg
                    self.clear.removeInstances(config, run_result[1])
                    
                    msg = "Removing Security Groups and Keypair"
                    self.log.log_data(config.log_file,msg,"INFO")
                    misc = {'sg':test_name,'kp':test_name}
                    time.sleep(int(config.timeout))
                    if self.clear.removeMisc(config,misc,run_result[1])==True:
                        time_comp = self.var_.getrunTime('time')-self.startTime 
                        msg = "Clean Up complete, exiting test"
                        self.log.log_data(config.log_file,msg,"INFO")
                        print msg               
                        data_insert = [test_name,self.run_time,config.cell,run_result[2],'0','F','1',time_comp,'1']
                        WriteCSV().createCSVFile(config.csv_file, data_insert)
                        raise SystemExit
                    else:
                        time_comp = time.time()-self.startTime
                        msg = "Error, Unable to remove security group and key pair"
                        self.log.log_data(config.log_file,msg,"ERROR")
                        print msg
                        data_insert = [test_name,self.run_time,config.cell,run_result[2],'0','F','1',time_comp,'1']
                        WriteCSV().createCSVFile(config.csv_file, data_insert)
                        raise SystemExit
                    
            else:
                msg = "Run instances test failed"
                self.log.log_data(config.log_file,msg,"ERROR")
                print msg
                
                                    
                msg = "Running Cleaning up"
                self.log.log_data(config.log_file,msg,"INFO")
                print msg
                
                msg = "Terminating Instances"
                self.log.log_data(config.log_file,msg,"INFO")
                print msg
                self.clear.removeInstances(config, run_result[1])
                msg = "Removing Security Groups and Keypair"
                self.log.log_data(config.log_file,msg,"INFO")
                misc = {'sg':test_name,'kp':test_name}
                if self.clear.removeMisc(config,misc,run_result[1])==True:
                        time_comp = self.var_.getrunTime('time')-self.startTime 
                        msg = "Clean Up complete, exiting test"
                        self.log.log_data(config.log_file,msg,"INFO")
                        print msg               
                        data_insert = [test_name,self.run_time,config.cell,'F','1','NA','NA',time_comp,'1']
                        WriteCSV().createCSVFile(config.csv_file, data_insert)
                        raise SystemExit
                else:
                        time_comp = time.time()-self.startTime
                        msg = "Error, Unable to remove security group and key pair"
                        self.log.log_data(config.log_file,msg,"ERROR")
                        print msg
                        data_insert = [test_name,self.run_time,config.cell,'F','1','NA','NA',time_comp,'1']
                        WriteCSV().createCSVFile(config.csv_file, data_insert)
                        raise SystemExit
        else:
            msg = "Pre Check failed, test halted"
            time_comp = self.var_.getrunTime('time')-self.startTime
            data_insert = [test_name,self.run_time,config.cell,'F','1','NA','NA',time_comp,'1']
            WriteCSV().createCSVFile(config.csv_file, data_insert)
            self.log.log_data(config.log_file,msg,"ERROR")
            print msg
            raise SystemExit