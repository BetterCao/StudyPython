import time

class writepage(object):
    def __init__(self,driver):
        self.driver = driver

    def getFrame(self,locateType,location):
        time.sleep(2)
        frame = self.driver.find_element(by=locateType,value=location)
        return frame

    def getToUser(self,locateType,location):
        to = self.driver.find_element(by=locateType,value=location)
        return to

    def getTitle(self,locatType,location):
        title = self.driver.find_element(by=locatType,value=location)
        return title

    def getTextBody(self,locateType,location):
        textbody = self.driver.find_element(by=locateType,value=location)
        return textbody

    def getSaveBtn(self,locateType,location):
        savebtn = self.driver.find_element(by=locateType,value=location)
        return savebtn