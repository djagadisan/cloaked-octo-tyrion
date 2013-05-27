from util import GetConfig



class GetVar(object):
    
    def __init__(self):
        
        
        
        
        helper = GetConfig()
        cells_available = ['melbourne-np','melbourne-qh2','qld','monash']
        
        self.username = helper.process_config('zone','user')
        self.passwd = helper.process_config('zone','passwd')
        self.name = helper.process_config('zone','name')
        self.url = helper.process_config('zone','url')
        self.image_id = helper.process_config('zone','image_id')
        self.image_username = helper.process_config('zone','user_name')
        self.flavour_name = helper.process_config('zone','flavour_type')
        
        
        self.work_directory = helper.process_config('config','directory')
        self.ssh_key_name = helper.process_config('config','ssh_key_name') 
        self.timeout = helper.process_config('timeout','period')
        self.cp_file = helper.process_config('file_check','local_file')
        self.tmp_dir = helper.process_config('file_check','tmp_dir')
        
        self.ssh_key = self.work_directory+self.ssh_key_name
        self.log_file = helper.process_config('log_file','file')
        self.csv_file = helper.process_config('csv_file','file')
        
        if helper.process_config('zone','cell') in cells_available:
            self.cell = helper.process_config('zone','cell')
            self.scheduler={'cell':self.cell}
        else:
            print "Cells specified not valid, available cells %r" % cells_available
            raise SystemExit
