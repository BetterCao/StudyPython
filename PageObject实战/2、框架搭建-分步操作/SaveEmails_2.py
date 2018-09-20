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
loginframe = lp.getFrame("id","login_frame")
driver.switch_to.frame(loginframe)
lp.getLoginTypeBtn("id","switcher_plogin").click()
lp.getUserName("id","u").send_keys("694188260@qq.com")
lp.getPassword("id","p").send_keys("5489,3602L65g!")
lp.getLoginBtn("id","login_button").click()

#主页面
mp = mainpage(driver)
before = mp.getDraftBox("id","folder_4")
print(before)
mp.getWriteBtn("id","composebtn").click()

#写信页面
wp = writepage(driver)
mainframe = wp.getFrame("id","mainFrame")
driver.switch_to.frame(mainframe)
wp.getToUser("xpath","//*[@id='toAreaCtrl']/div[2]/input").send_keys("2112710849@qq.com")
wp.getTitle("id","subject").send_keys("this is title")
bodyframe = wp.getFrame("tag name","iframe")
driver.switch_to.frame(bodyframe)
wp.getTextBody("tag name","body").send_keys("this is body")
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame(mainframe)
wp.getSaveBtn("name","savebtn").click()
time.sleep(2)

#主页面
driver.switch_to.default_content()
after = mp.getDraftBox("id","folder_4")
print(after)

assert int(after)==int(before)+1,"保存失败"

driver.quit()