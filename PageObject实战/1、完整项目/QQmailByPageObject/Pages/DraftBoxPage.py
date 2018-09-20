from Utils.IniUtils import *
from time import *

class draftboxPage(object):
    def __init__(self,driver):
        self.driver = driver
        self.readini = ReadIni()
        self.draftboxPage_items = self.readini.getItemSection("PO-DraftBoxPage")

    def getframe(self):
        locateType,location = self.draftboxPage_items["mainframe"].split('>')
        frame = self.driver.find_element(by=locateType,value=location)
        return frame

    def getAll(self):
        locateType, location = self.draftboxPage_items['selectall'].split('>')
        all = self.driver.find_element(by=locateType,value=location)
        return all

    def getDelete(self):
        locateType,location = self.draftboxPage_items['delete'].split('>')
        delete = self.driver.find_element(by=locateType,value=location)
        return delete

    def getOK(self):
        locateType, location = self.draftboxPage_items['okok'].split('>')
        delete = self.driver.find_element(by=locateType, value=location)
        return delete