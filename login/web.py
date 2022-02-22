# from selenium import webdriver
from selenium.webdriver.common.by import By
# import time
# driver = webdriver.Edge()
# driver.implicitly_wait(10)
# driver.get("https://www.zhihu.com/signin?next=%2F")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//div[text()='密码登录']").click()
# driver.find_element(By.XPATH,"//input[@name='username']").send_keys("13970560162")
# driver.find_element(By.XPATH,"//input[@name='password']").send_keys("wq19990910")
# time.sleep(1)
# driver.find_element(By.XPATH,"//button[text()='注册/登录']").click()

def open_url(url,driver):
    driver.get(url)
    driver.maximize_window()
def login_page(username,password,driver):
    driver.find_element(By.XPATH, "//div[text()='密码登录']").click()
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='注册/登录']").click()
def go(url,driver,username,password):
    open_url(url, driver)
    login_page(username, password, driver)
