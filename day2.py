# 使用占位符，输出变量
# name = input("请输入姓名:")
# age = input("请输入年龄:")
# hobby = input("请输入爱好:")
# print('''
# name:{}
# age:{}
# hobby:{}
# '''.format(name,age,hobby))

# str1 = 'python hello aaa 123123aabb'
# # 打印字符串中的python
# print(str1[0:6])
# # 判断是否在字符串中
# print('o a' in str1)
# print('he' in str1)
# print('ab' in str1)
# # lemon替换python
# str1 = str1.replace('python','lemon')
# # 输出aaa的起始位置
# print(str1.find('aaa'))




# a = [1,2,'6','summer']
# print('i' in a)
#
# dict_1={"class_id":45,"num":20}
# a = dict_1["num"]
# if a > 500:
#     print(a)
# else:
#     print('hhhh')


# list3 = ['菠萝','球球','Lewis','瓜瓜','兔兔','不停']
#import selenium 工具所有内容导入
import time

from selenium import webdriver #selenium工具导入webdriver库
from selenium.webdriver.common.by import By
driver = webdriver.Edge() #选择Edge浏览器，初始化
#1.打开一个网址
driver.get("http://127.0.0.1/Home/user/login.html")
#2.窗口最大化
driver.maximize_window()

# # #3.打开新页面
# # time.sleep(3) #等待，默认单位为秒
# # driver.get("https://www.baidu.com/")
# # #4.向前，退后，刷新
# # time.sleep(2)
# # driver.back()#退回上一个页面
# # time.sleep(2)
# driver.forward()#前进下一个页面
# time.sleep(2)
# driver.refresh()#刷新页面
# #5.退出
# driver.quit()#关闭驱动,session关闭
# driver.close()#关闭当前窗口，不会退出会话
# #6 以上是浏览器常规操作，非常规怎么实现？


