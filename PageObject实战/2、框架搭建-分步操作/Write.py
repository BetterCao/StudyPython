from Pages.MainPage import *
from Pages.WritePage import *

def write(driver,to,textbody=None,*title):
            #必选参数，默认参数，*可选参数
    driver.implicitly_wait(5)
    mp = mainpage(driver)
    mp.getWriteBtn().click()
    wp = writepage(driver)
    driver.switch_to.frame(wp.getFrame('id','mainFrame'))
    wp.getToUser().send_keys(to)
    wp.getTitle().send_keys(title)
    driver.switch_to.frame(wp.getFrame('tag name','iframe'))
    if textbody is None:
        textbody = []
    wp.getTextBody().send_keys(textbody)
    time.sleep(1)
    driver.switch_to.default_content()
    driver.switch_to.frame(wp.getFrame('id','mainFrame'))
    wp.getSaveBtn().click()
    time.sleep(2)
