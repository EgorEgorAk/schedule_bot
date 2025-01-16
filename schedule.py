import telebot
from telebot import types
from token_1 import TOKEN

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['help', 'start'])
def send_message(message):
    
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    reply_button_pn = types.KeyboardButton("Понедельник")
    reply_button_vt = types.KeyboardButton("Вторник")
    reply_button_sr = types.KeyboardButton("Среда")
    reply_button_cht = types.KeyboardButton("Четверг")
    reply_button_pt = types.KeyboardButton("Пятница")
    reply_button_sb = types.KeyboardButton("Суббота")
    reply_keyboard.add(reply_button_pn)
    reply_keyboard.add(reply_button_vt)
    reply_keyboard.add(reply_button_sr)
    reply_keyboard.add(reply_button_cht)
    reply_keyboard.add(reply_button_pt)
    reply_keyboard.add(reply_button_sb)
    
    bot.send_message(message.chat.id,"Привет,выбери день недели.",reply_markup=reply_keyboard)


def parsing_pn ():
    driver = webdriver.Chrome()
    driver.get("https://www.sut.ru/")

    time.sleep(1)
    student = driver.find_element(By.LINK_TEXT, "Студенту")
    student.click()
    schedule = driver.find_element(By.LINK_TEXT, "Расписание")
    schedule.click()

    schedule_details = driver.find_element(By.LINK_TEXT, "Расписание занятий студентов очной и вечерней форм обучения")
    schedule_details.click()

    time.sleep(3) 
    ikpi = driver.find_element(By.LINK_TEXT, "ИКПИ-11")
    ikpi.click()

    time.sleep(3)  
    pn = driver.find_element(By.LINK_TEXT, "понедельник")
    pn.click()

    screenshot_path = "screenshots/monday_screenshot.png"
    driver.save_screenshot(screenshot_path)
    driver.quit()

    return screenshot_path


def parsing_vt():
    driver = webdriver.Chrome()
    driver.get("https://www.sut.ru/")

    student = driver.find_element(By.LINK_TEXT, "Студенту")
    student.click()
    schedule = driver.find_element(By.LINK_TEXT, "Расписание")
    schedule.click()
    schedule_details = driver.find_element(By.LINK_TEXT, "Расписание занятий студентов очной и вечерней форм обучения")
    schedule_details.click()

    time.sleep(3) 
    ikpi = driver.find_element(By.LINK_TEXT, "ИКПИ-11")
    ikpi.click()

    time.sleep(3)  
    vt = driver.find_element(By.LINK_TEXT, "вторник")
    vt.click()

    screenshot_path = "screenshots/tuesday_screenshot.png"
    driver.save_screenshot(screenshot_path)
    driver.quit()

    return screenshot_path


def parsing_sr():
    driver = webdriver.Chrome()
    driver.get("https://www.sut.ru/")

    student = driver.find_element(By.LINK_TEXT, "Студенту")
    student.click()
    schedule = driver.find_element(By.LINK_TEXT, "Расписание")
    schedule.click()
    schedule_details = driver.find_element(By.LINK_TEXT, "Расписание занятий студентов очной и вечерней форм обучения")
    schedule_details.click()

    time.sleep(3) 
    ikpi = driver.find_element(By.LINK_TEXT, "ИКПИ-11")
    ikpi.click()

    time.sleep(3)  
    cr = driver.find_element(By.LINK_TEXT, "среда")
    cr.click()

    screenshot_path = "screenshots/wednesday_screenshot.png"
    driver.save_screenshot(screenshot_path)
    driver.quit()

    return screenshot_path


def parsing_cht():
    driver = webdriver.Chrome()
    driver.get("https://www.sut.ru/")

    student = driver.find_element(By.LINK_TEXT, "Студенту")
    student.click()
    schedule = driver.find_element(By.LINK_TEXT, "Расписание")
    schedule.click()
    schedule_details = driver.find_element(By.LINK_TEXT, "Расписание занятий студентов очной и вечерней форм обучения")
    schedule_details.click()

    time.sleep(3) 
    ikpi = driver.find_element(By.LINK_TEXT, "ИКПИ-11")
    ikpi.click()

    time.sleep(3)  
    cht = driver.find_element(By.LINK_TEXT, "четверг")
    cht.click()

    screenshot_path = "screenshots/thursday_screenshot.png"
    driver.save_screenshot(screenshot_path)
    driver.quit()

    return screenshot_path


def parsing_pt():
    driver = webdriver.Chrome()
    driver.get("https://www.sut.ru/")

    student = driver.find_element(By.LINK_TEXT, "Студенту")
    student.click()
    schedule = driver.find_element(By.LINK_TEXT, "Расписание")
    schedule.click()
    schedule_details = driver.find_element(By.LINK_TEXT, "Расписание занятий студентов очной и вечерней форм обучения")
    schedule_details.click()

    time.sleep(3) 
    ikpi = driver.find_element(By.LINK_TEXT, "ИКПИ-11")
    ikpi.click()

    time.sleep(3)  
    pt = driver.find_element(By.LINK_TEXT, "пятница")
    pt.click()

    screenshot_path = "screenshots/friday_screenshot.png"
    driver.save_screenshot(screenshot_path)
    driver.quit()

    return screenshot_path

def parsing_sb():
    driver = webdriver.Chrome()
    driver.get("https://www.sut.ru/")

    student = driver.find_element(By.LINK_TEXT, "Студенту")
    student.click()
    schedule = driver.find_element(By.LINK_TEXT, "Расписание")
    schedule.click()
    schedule_details = driver.find_element(By.LINK_TEXT, "Расписание занятий студентов очной и вечерней форм обучения")
    schedule_details.click()

    time.sleep(3) 
    ikpi = driver.find_element(By.LINK_TEXT, "ИКПИ-11")
    ikpi.click()

    time.sleep(3)  
    sb = driver.find_element(By.LINK_TEXT, "суббота")
    sb.click()

    screenshot_path = "screenshots/saturday_screenshot.png"
    driver.save_screenshot(screenshot_path)
    driver.quit()

    return screenshot_path

@bot.message_handler(commands=['schedule'])
def send_schedule(message):
    bot.send_message(message.chat.id, "Подождите, загружаю расписание...")
    try:
        screenshot_path = parsing_sb()  
        with open(screenshot_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)  
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")



@bot.message_handler(func=lambda message: message.text == "Понедельник")
def handle_reply_button(message):
    parsing_pn(message)

@bot.message_handler(func=lambda message: message.text == "Вторник")
def handle_reply_button(message):
    parsing_vt(message)

@bot.message_handler(func=lambda message: message.text == "Среда")
def handle_reply_button(message):
    parsing_sr(message)

@bot.message_handler(func=lambda message: message.text == "Четверг")
def handle_reply_button(message):
    parsing_cht(message)

@bot.message_handler(func=lambda message: message.text == "Пятница")
def handle_reply_button(message):
    parsing_pt(message)

@bot.message_handler(func=lambda message: message.text == "Суббота")
def handle_reply_button(message):
    parsing_sb(message)

@bot.message_handler(func=lambda message: True)  
def handle_unknown_message(message):
    bot.send_message(message.chat.id, "ОШИБКА: неизвестная команда или сообщение.")




    bot.polling(none_stop=True)