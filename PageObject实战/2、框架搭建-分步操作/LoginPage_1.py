import time

class loginpage(object):
    def __init__(self,driver):
        self.driver = driver

    def login(self):
        time.sleep(2)
        self.driver.switch_to.frame("login_frame")
        loginByInput = self.driver.find_element_by_id("switcher_plogin")
        loginByInput.click()
        username = self.driver.find_element_by_id("u")
        username.send_keys("694188260@qq.com")
        password = self.driver.find_element_by_id("p")
        password.send_keys("5489,3602L65g!")
        submit = self.driver.find_element_by_id("login_button")
        submit.click()
        time.sleep(5)