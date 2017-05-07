# coding=utf-8
from selenium import webdriver


def login(driver, name, passwd):
    driver.find_element_by_name("login_name").send_keys(name)
    driver.find_element_by_name("login_password").send_keys(passwd)
    driver.find_element_by_xpath("//button[@type='button']").click()


if __name__=='__main__':
    driver = webdriver.Firefox()
    base_url = "http://10.17.2.129:8083/system/login.htm"
    driver.get(base_url)
    login(driver, 'admin','123456')