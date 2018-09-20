import time

class writepage(object):
    def __init__(self,driver):
        self.driver = driver

    def writeNewEmail(self):
        self.driver.switch_to.frame("mainFrame")
        to = self.driver.find_element_by_xpath("//*[@id='toAreaCtrl']/div[2]/input")
        to.send_keys("caojuepeng@letshare.com.cn")
        title = self.driver.find_element_by_id("subject")
        title.send_keys("this is title")
        textframe = self.driver.find_element_by_tag_name("iframe")
        self.driver.switch_to.frame(textframe)
        text = self.driver.find_element_by_tag_name("body")
        text.send_keys("this is textbody")
        time.sleep(2)

    def saveEmail(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        save = self.driver.find_element_by_name("savebtn")
        save.click()
        time.sleep(2)