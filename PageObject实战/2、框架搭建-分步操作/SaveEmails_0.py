from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "https://mail.qq.com/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

#登录页面
time.sleep(2)
driver.switch_to.frame("login_frame")
loginByInput = driver.find_element_by_id("switcher_plogin")
loginByInput.click()
username = driver.find_element_by_id("u")
username.send_keys("694188260@qq.com")
password = driver.find_element_by_id("p")
password.send_keys("5489,3602L65g!")
submit = driver.find_element_by_id("login_button")
submit.click()
time.sleep(5)

#主页面
check_A = driver.find_element_by_id("folder_4").text
before = check_A[-2]
if before.isdigit() is False:
    before = 0

WriteEmail = driver.find_element_by_id("composebtn")
WriteEmail.click()
time.sleep(2)

#写信页面
driver.switch_to.frame("mainFrame")
to = driver.find_element_by_xpath("//*[@id='toAreaCtrl']/div[2]/input")
to.send_keys("caojuepeng@letshare.com.cn")
title = driver.find_element_by_id("subject")
title.send_keys("this is title")
textframe = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(textframe)
text =  driver.find_element_by_tag_name("body")
text.send_keys("this is textbody")
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame("mainFrame")
save = driver.find_element_by_name("savebtn")
save.click()
time.sleep(2)

#主页面
driver.switch_to.default_content()
check_B = driver.find_element_by_id("folder_4").text
after = check_B[-2]
if after.isdigit() is False:
    after = 0

#格式 ： assert+空格+要判断语句+双引号“报错语句”
#不出错时没有输出值
assert int(after)==int(before)+1,"保存失败"

driver.quit()