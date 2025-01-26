from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
from selenium.webdriver.chrome.options import Options   

from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
width = 1360
height = 1250  
driver.set_window_size(width, height)
    
# Загрузка страницы
driver.get(f'https://www.sut.ru/studentu/raspisanie/raspisanie-zanyatiy-studentov-ochnoy-i-vecherney-form-obucheniya?group=56043&date')
time.sleep(3)
    
driver.execute_script("document.body.style.zoom='50%'")
time.sleep(2)

dateInput = driver.find_element(By.XPATH, "//*[@id='rasp-date']")
date = "19122024"
dateInput.send_keys(date)

time.sleep(15)