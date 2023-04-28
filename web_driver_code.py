import time

from selenium import webdriver
from selenium.webdriver.common.by import  By
driver1=webdriver.Chrome("C:/Users/erswa/PycharmProjects/pythonProject/chromedriver_win32/chromedriver.exe")
driver1.get("https://www.google.com/")
time.sleep(10)
box=driver1.find_element(By.XPATH,'//*[@id="APjFqb"]')
query='DBIT'
for i in query:
    box.send_keys(i)
    time.sleep(2)
driver1.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys('\ue007')
print('entered')
time.sleep(10)