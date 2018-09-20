from selenium import webdriver
from Actions.Login import *
from Actions.CheckDraftBoxNum import *
from Actions.Write import *
from Pages.MainPage import *
from Pages.WritePage import *

driver = webdriver.Chrome()
url = "https://mail.qq.com/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

login(driver,'694188260@qq.com','5489,3602L65g!')
before = checknum(driver)
print(before)
write(driver,'2112710849@qq.com')
time.sleep(2)
after = checknum(driver)
print(after)

assert after==before+1,"保存失败"

driver.quit()