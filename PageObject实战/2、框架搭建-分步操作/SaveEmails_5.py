from selenium import webdriver
from Actions.Login import *
from Actions.CheckDraftBoxNum import *
from Actions.Write import *
from Pages.WritePage import *
from Utils.ExcelUtils import *

driver = webdriver.Chrome()
url = "https://mail.qq.com/"
driver.maximize_window()
driver.implicitly_wait(5)

#先去Config.BathInfo里加入test_data_excel_path
re = ExcelUtils(test_data_excel_path)
re.set_sheet_by_name("登录账号")
rows = re.get_all_rows()[1:]

for id,row in enumerate(rows):
    driver.get(url)
    #==========登录==========
    if row[3].value == 'y':
        username = row[1].value
        password = row[2].value
        try:
            login(driver,username,password)
            assert "邮箱首页" in driver.page_source,'不对'
            re.write_cell_content(id+2,5,'pass')
        except:
            re.set_sheet_by_name("登录账号")
            re.write_cell_content(id+2,5,'fail')
        # ==========写信==========
        re.set_sheet_by_name("写信")
        rows1 = re.get_all_rows()[1:]
        for id1,row1 in enumerate(rows1):
            if row1[4].value == 'y':
                before = checknum(driver)
                print(before)
                toWho = row1[1].value
                title = row1[2].value
                text = row1[3].value
                write(driver,toWho,text,title)
                time.sleep(2)
                after = checknum(driver)
                print(after)
                try:
                    assert after == before+1,"保存失败"
                    re.write_cell_content(id1+2,6,'pass')
                except:
                    re.set_sheet_by_name('写信')
                    re.write_cell_content(id1+2,6,'fail')
            else:
                re.set_sheet_by_name("写信")
                re.write_cell_content(id1+2,6,'忽略')
    else:
        re.set_sheet_by_name('登录账号')
        re.write_cell_content(id+2,5,'忽略')

driver.quit()