from selenium import webdriver
from login import web
from text import text
from selenium.webdriver.common.by import By
import time
driver = webdriver.Edge()
driver.implicitly_wait(10)
url = text.url["url"]
username = text.login["username"]
password = text.login["password"]
web.go(url=url,driver=driver,username=username,password=password)