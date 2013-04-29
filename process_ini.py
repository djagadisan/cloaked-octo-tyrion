import os
import sys
import argparse
from ConfigParser import SafeConfigParser



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


