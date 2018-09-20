from configparser import ConfigParser
from Config.BaseInfo import *

class ReadIni(object):
    def __init__(self):
        self.cf = ConfigParser()    #生成解析器
        self.cf.read(elements_path)

    def getItemSection(self,sectionName):
        return dict(self.cf.items(sectionName))

    def getOptionValue(self,sectionName,optionName):
        return self.cf.get(sectionName,optionName)