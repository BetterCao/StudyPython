from selenium import webdriver
from Pages.LoginPage import *
from Pages.MainPage import *
from Pages.WritePage import *

driver = webdriver.Chrome()
url = "https://mail.qq.com/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

#登录页面
lp = loginpage(driver)
loginframe = lp.getFrame()
driver.switch_to.frame(loginframe)
lp.getLoginTypeBtn().click()
lp.getUserName().send_keys("694188260@qq.com")
lp.getPassword().send_keys("5489,3602L65g!")
lp.getLoginBtn().click()

#主页面
mp = mainpage(driver)
check = mp.getDraftBox().text
before = check[-2]
if before.isdigit() is not True:
    before = 0
print(before)
mp.getWriteBtn().click()

#写信页面
wp = writepage(driver)
mainframe = wp.getFrame("id","mainFrame")
driver.switch_to.frame(mainframe)
wp.getToUser().send_keys("2112710849@qq.com")
wp.getTitle().send_keys("this is title")
bodyframe = wp.getFrame("tag name","iframe")
driver.switch_to.frame(bodyframe)
wp.getTextBody().send_keys("this is body")
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame(mainframe)
wp.getSaveBtn().click()
time.sleep(2)

#主页面
driver.switch_to.default_content()
check = mp.getDraftBox().text
after = check[-2]
if after.isdigit() is not True:
    after = 0
print(after)

assert int(after)==int(before)+1,"保存失败"

driver.quit()