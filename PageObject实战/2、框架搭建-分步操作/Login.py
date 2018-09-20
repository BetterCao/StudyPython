from Pages.LoginPage import *

def login(driver,username,password):
    lp = loginpage(driver)
    driver.switch_to.frame(lp.getFrame())
    time.sleep(3)
    lp.getLoginTypeBtn().click()
    lp.getUserName().send_keys(username)
    lp.getPassword().send_keys(password)
    lp.getLoginBtn().click()
    time.sleep(2)