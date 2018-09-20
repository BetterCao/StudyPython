import time

class mainpage(object):
    def __init__(self,driver):
        self.driver = driver

    def findDraftBox(self):
        self.driver.switch_to.default_content()
        check = self.driver.find_element_by_id("folder_4").text
        num = check[-2]
        if num.isdigit() is False:
            num = 0
        return num

    def toWritePage(self):
        self.driver.switch_to.default_content()
        WriteEmail = self.driver.find_element_by_id("composebtn")
        WriteEmail.click()
        time.sleep(2)