import time
from selenium import webdriver
from src.tongQuan import btn_XemChiTiet


# def webdriverConfig():
#     driver = webdriver.Chrome('C:/Users/MinhNV/OneDrive/Desktop/SeleniumTool/chromedriver.exe')
#     return driver

def login(timeout):
    driver = webdriver.Chrome('C:/Users/MinhNV/OneDrive/Desktop/SeleniumTool/chromedriver.exe')
    # driver = webdriverConfig()
    driver.get ("https://banhang.upgo.vn")
    print(driver.current_url)
    print (driver.title  )
    time.sleep(timeout)
    print("========= LOGIN=================")
    username = '0328716036'
    password = 'minh123456'
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id ("password").send_keys(password)
    driver.find_element_by_class_name("my-4").click()
    time.sleep(timeout)
    driver.get ("https://banhang.upgo.vn/#/item/list")
    time.sleep(timeout)
    try:
        res=  driver.find_elements_by_class_name("p-button-label")[0].text
        print('========================================')
        print(res)
        if(res=='Thêm'):
            print ("LOGIN THÀNH CÔNG !")
        else:
            print("LOGIN KHÔNG THÀNH CÔNG !")
    except:
        print("LOGIN KHÔNG THÀNH CÔNG !")
    return driver
        # driver.quit()