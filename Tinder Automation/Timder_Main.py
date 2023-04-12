from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

fb_email="mamun2021to2022may@gmail.com"
passd="testing@464"

Chrome_Dev_path= "E:\Python Udemy\Day 48\Chrome Dev Tools\chromedriver.exe"
driver=Service(Chrome_Dev_path)
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
browser=webdriver.Chrome(service=driver,options=option)

url="https://tinder.com/"
browser.get(url)

# sleep(5)
login=browser.find_element(By.XPATH,"//*[text()='Log in']")
login.click()

sleep(5)
google_login=browser.find_element(By.XPATH,'//*[@id="q2069402257"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div/div')
google_login.click()

print(browser.title)
base_window = browser.window_handles[0]
fb_login_window = browser.window_handles[1]
browser.switch_to.window(fb_login_window)
print(browser.title)

set_fb_mail=browser.find_element(By.ID, "email")
set_fb_mail.send_keys(fb_email)

set_fb_pass=browser.find_element(By.ID, "pass")
set_fb_pass.send_keys(passd)
set_fb_pass.send_keys(Keys.ENTER)

browser.switch_to.window(base_window)
print(browser.title)

sleep(180)
location=browser.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
location.click()
#
sleep(10)
notifi=browser.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
notifi.click()
#
sleep(10)
cokiee=browser.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
cokiee.click()
#sv809

sleep(10)
love=browser.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[4]/button/span/span')
love.click()
