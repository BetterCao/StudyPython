from Pages.MainPage import *

def checknum(driver):
    mp = mainpage(driver)
    check = mp.getDraftBox().text
    num = check[-2]
    if num.isdigit() is not True:
        num = 0
    return int(num)