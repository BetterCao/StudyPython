from Pages.DraftBoxPage import *
from Pages.MainPage import *

def clearbox(driver):
    dbp = draftboxPage(driver)
    mp = mainpage(driver)
    mp.getDraftBox().click()
    driver.switch_to_frame(dbp.getframe())
    time.sleep(1)
    dbp.getAll().click()
    dbp.getDelete().click()
    time.sleep(1)
    driver.switch_to.default_content()
    dbp.getOK().click()
    time.sleep(1)