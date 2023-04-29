from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver1 = webdriver.Chrome(r"C:/Users/swaraj.s/OneDrive - kpisoft Inc/Desktop/chromedriver.exe")
driver1.get('https://www.timesjobs.com/')
driver1.maximize_window()
print("opening website ")
time.sleep(1)
driver1.find_element(By.XPATH, '//*[@id="site"]/div[6]/div/div[2]/button').click()
print("close cookie")
time.sleep(1)
driver1.find_element(By.XPATH, '//*[@id="site"]/section/div[1]/section/ul/li[1]/a').click()
print('IT link clicked')
time.sleep(10)
try:
    driver1.find_element(By.XPATH, '//*[@id="closeSpanId"]').click()
except Exception as ex:
    print(ex)

driver1.implicitly_wait(20)

links = []
url = driver1.find_elements(By.XPATH, '//*[@class="clearfix"]//h2//a')
while (True):
    try:
        for urls in url[:3]:
            temp1 = urls.get_attribute("href")
            time.sleep(1)
            links.append(temp1)
            time.sleep(1)
            print(links)
            print(len(links))
            time.sleep(1)
        next = driver1.find_element(By.XPATH, '//*[@class="nxtC"]')
        # driver1.execute_script("arguments[0].click();", next)
        if len(links>3):
            driver1.execute_script("arguments[0].click();", next)
        else:
            break
            

    except Exception as ex:
        print(ex)
        # continue
        break

