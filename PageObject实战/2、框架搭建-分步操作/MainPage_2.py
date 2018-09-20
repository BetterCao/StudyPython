import time

class mainpage(object):
    def __init__(self,driver):
        self.driver = driver

    def getDraftBox(self,locateType,location):
        check = self.driver.find_element(by=locateType,value=location).text
        num = check[-2]
        if num.isdigit() is False:
            num = 0
        return num

    def getWriteBtn(self,locateType,location):
        writebtn = self.driver.find_element(by=locateType,value=location)
        return writebtn