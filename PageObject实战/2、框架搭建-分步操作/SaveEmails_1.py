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
lp.login()

#主页面
mp = mainpage(driver)
before = mp.findDraftBox()
print(before)
mp.toWritePage()

#写信页面
wp = writepage(driver)
wp.writeNewEmail()
wp.saveEmail()

#主页面
after = mp.findDraftBox()
print(after)

assert int(after)==int(before)+1,"保存失败"

driver.quit()