import time
from Utils.IniUtils import *

class mainpage(object):
    def __init__(self,driver):
        self.driver = driver
        self.readini = ReadIni()
        self.mainpage_items = self.readini.getItemSection("PO-MainPage")

    def getDraftBox(self):
        self.driver.switch_to.default_content()
        locateType, location = self.mainpage_items['draftbox'].split('>')
        check = self.driver.find_element(by=locateType,value=location)
        return check

    def getWriteBtn(self):
        self.driver.switch_to.default_content()
        locateType, location = self.mainpage_items['writebtn'].split('>')
        writebtn = self.driver.find_element(by=locateType,value=location)
        return writebtn