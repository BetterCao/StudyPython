# 指向 python 的路径，windows下可以不写
#!/usr/bin/python3
# 指定编码：utf-8
# -*- coding: utf-8 -*-

from selenium import webdriver
import selenium
from time import sleep

driver = webdriver.Chrome()
driver.get("http://172.24.115.120:8001/")
driver.implicitly_wait(5)

try:
    driver.maximize_window()
    driver.find_element_by_id("userId").send_keys("caojuepeng")
    driver.find_element_by_id("passwd").send_keys("111111")
    driver.find_element_by_id("verificationCode").click()
    sleep(2)
    driver.find_element_by_id("btnSubmit").click()
    print(driver.find_element_by_css_selector("span[class='welcome-title']").text)
    driver.find_element_by_link_text("仓库").click()
    driver.find_element_by_link_text("仓库开户").click()
    sleep(2)
    driver.switch_to.frame("serviceiframe")
    driver.switch_to.frame("viewiframe")
    driver.find_element_by_id("formEdit_editor_WAREHOUSENAME").send_keys("单位名称")
    driver.find_element_by_css_selector("button[class='btn btn-primary command-pin']").click();

except AttributeError as e:
    print("对象没有这个属性，没有办法做出操作")
    print(e)
except selenium.common.exceptions.NoSuchElementException as e:
    print("元素没有定位到")
    print(e)
except Exception as e:
    print("出现其他错误")
    print(e)
finally:
    sleep(2)
    driver.quit()