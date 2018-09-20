import time

class loginpage(object):
    def __init__(self,driver):
        self.driver = driver

    def getFrame(self,locateType,location):
        time.sleep(2)
        frame = self.driver.find_element(by=locateType,value=location)
        return frame

    def getLoginTypeBtn(self,locateTyep,location):
        loginType = self.driver.find_element(by=locateTyep,value=location)
        return loginType

    def getUserName(self,locateType,location):
        username = self.driver.find_element(by=locateType,value=location)
        return username

    def getPassword(self,locateType,location):
        password = self.driver.find_element(by=locateType,value=location)
        return password

    def getLoginBtn(self,locateType,location):
        submit = self.driver.find_element(by=locateType,value=location)
        return submit
