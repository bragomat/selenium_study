from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://music.yandex.ru/")
#login_button = driver.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[2]/a")
#login_button.click()
#time.sleep(5)
#login = driver.find_element_by_id('passp-field-login')
#login.clear()
#login.send_keys('*****')
#driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[2]/div/div/div[1]/form/div[3]/button[1]').click()
#time.sleep(2)
#password = driver.find_element_by_name('passwd')
#password.send_keys('*******')
#driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[2]/div/div/form/div[2]/button[1]').click()
#time.sleep(2)
#searchbox = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div[1]/div[1]/div/div[1]/input')
searchbox = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div[1]/div[1]/div/div[1]/input')
searchbox.send_keys('simon says')
searchbox.send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[2]/div/div/div[2]/div/div[3]/div[1]/div[3]/span/button').click()
