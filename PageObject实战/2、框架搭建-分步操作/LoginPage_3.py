import time
from Utils.IniUtils import *

class loginpage(object):
    def __init__(self,driver):
        self.driver = driver
        self.readini = ReadIni()
        self.loginpage_items = self.readini.getItemSection("PO-LoginPage")

    def getFrame(self):
        time.sleep(2)
        locateType,location = self.loginpage_items["loginframe"].split('>')
        frame = self.driver.find_element(by=locateType,value=location)
        return frame

    def getLoginTypeBtn(self):
        locateType, location = self.loginpage_items["logintypebtn"].split('>')
        loginType = self.driver.find_element(by=locateType,value=location)
        return loginType

    def getUserName(self):
        locateType, location = self.loginpage_items["username"].split('>')
        username = self.driver.find_element(by=locateType,value=location)
        return username

    def getPassword(self):
        locateType, location = self.loginpage_items["password"].split('>')
        password = self.driver.find_element(by=locateType,value=location)
        return password

    def getLoginBtn(self):
        locateType, location = self.loginpage_items["loginbtn"].split('>')
        submit = self.driver.find_element(by=locateType,value=location)
        return submit
