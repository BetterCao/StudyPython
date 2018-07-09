# 指向 python 的路径，windows下可以不写
#!/usr/bin/python3
# 指定编码：utf-8
# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep

desired_caps = {}

#手机设置
desired_caps['deviceName'] = '127.0.0.1:7555'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.4'
#app设置
desired_caps['appPackage'] = 'com.ibox.calculators'
desired_caps['appActivity'] = 'com.ibox.calculators.SplashActivity'
#appium设置
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'
desired_caps['noReset'] = 'True'
desired_caps['automationName'] = 'Appium'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

sleep(10)
driver.find_element_by_xpath("//android.widget.Button[@text='1']").click()
driver.find_element_by_xpath("//android.widget.Button[@text='+']").click()
driver.find_element_by_xpath("//android.widget.Button[@text='8']").click()
driver.find_element_by_xpath("//android.widget.Button[@text='=']").click()
driver.quit()


