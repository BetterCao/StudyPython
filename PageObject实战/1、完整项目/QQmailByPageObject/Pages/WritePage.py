import time
from Utils.IniUtils import *

class writepage(object):
    def __init__(self,driver):
        self.driver = driver
        self.readini = ReadIni()
        self.writepage_items = self.readini.getItemSection('PO-WritePage')

    #这一页有多个frame，所以不能统一，还是需要指定
    def getFrame(self,locateType,location):
        time.sleep(2)
        frame = self.driver.find_element(by=locateType,value=location)
        return frame

    def getToUser(self):
        locateType, location = self.writepage_items['towho'].split('>')
        to = self.driver.find_element(by=locateType,value=location)
        return to

    def getTitle(self):
        locateType, location = self.writepage_items['title'].split('>')
        title = self.driver.find_element(by=locateType,value=location)
        return title

    def getTextBody(self):
        locateType, location = self.writepage_items['textbody'].split('>')
        textbody = self.driver.find_element(by=locateType,value=location)
        return textbody

    def getSaveBtn(self):
        locateType, location = self.writepage_items['savebtn'].split('>')
        savebtn = self.driver.find_element(by=locateType,value=location)
        return savebtn