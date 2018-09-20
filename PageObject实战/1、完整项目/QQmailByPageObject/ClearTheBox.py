from Actions.Login import *
from selenium import webdriver
from Utils.ExcelUtils import *
from Actions.CheckDraftBoxNum import *
from Actions.ClearDraftBox import *

driver = webdriver.Chrome()
url = "https://mail.qq.com/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)


re = ExcelUtils(test_data_excel_path)
# ==================== 登录 ====================
re.set_sheet_by_name("登录账号")
username = re.get_cell_content(2,2)
password = re.get_cell_content(2,3)
login(driver,username,password)

# ==================== 清空草稿箱 ====================
before = checknum(driver)
if before == 0:
    print("草稿箱已经是空的了，不必清空")
    after = 0
else:
    clearbox(driver)
    after = checknum(driver)

assert after == 0,"清空失败"
driver.quit()