import telebot
from telebot import types
from token_1 import TOKEN

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from PIL import Image


bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['help', 'start'])
def send_message(message):
    
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

    reply_button_scheldule = types.KeyboardButton("Расписание")
    reply_button_next_week = types.KeyboardButton("Следующая неделя")
    reply_button_previous_week = types.KeyboardButton("Предыдущая неделя")
    reply_keyboard.add(reply_button_scheldule)
    reply_keyboard.add(reply_button_next_week)
    reply_keyboard.add(reply_button_previous_week)
    bot.send_message(message.chat.id,"Привет,выбери день недели.",reply_markup=reply_keyboard)

@bot.message_handler(commands=['schedule'])
def send_schedule(message):
    bot.send_message(message.chat.id, "Подождите, загружаю расписание...")
    try:
        screenshot_path = parsing_schlude(message)  
        with open(screenshot_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)  
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")



    




def parsing_schlude(message):
    driver = webdriver.Chrome()
    width = 1360
    height = 1250  # Округлённое значение высоты
    driver.set_window_size(width, height)
    
    # Загрузка страницы
    driver.get(f'https://www.sut.ru/studentu/raspisanie/raspisanie-zanyatiy-studentov-ochnoy-i-vecherney-form-obucheniya?group=56043&date=2024-12-01')
    time.sleep(3)
    
    # Уменьшение масштаба страницы
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)

    # Прокрутка до нужного элемента
    element = driver.find_element(By.CLASS_NAME, "vt232")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # Сохранение полного скриншота
    screenshot_path = "screenshots/full_screenshot.png"
    driver.save_screenshot(screenshot_path)

    # Обрезка скриншота по центру
    cropped_screenshot_path = "screenshots/centered_screenshot.png"
    with Image.open(screenshot_path) as img:
        img_width, img_height = img.size

        # Рассчитываем координаты центральной области
        left = (img_width - width) // 2
        top = (img_height - height) // 2
        right = left + width
        bottom = top + height
        cropped_image = img.crop((left, top, right, bottom))
        cropped_image.save(cropped_screenshot_path)
        print(f"Обрезанный по центру скриншот сохранён: {cropped_screenshot_path}")

    driver.quit()
    return cropped_screenshot_path


@bot.message_handler(func=lambda message: message.text == "Расписание")
def handle_reply_button(message):
    screenshot_path1 = parsing_schlude(message)
    with open(screenshot_path1, mode="rb") as screenshot_descriptor:
        bot.send_photo(message.chat.id, screenshot_descriptor)

@bot.message_handler(func=lambda message: message.text == "Следующая неделя")
def handle_reply_button(message):
    bot.send_message(message.chat.id,"Рсаписание на следующую неделю")

@bot.message_handler(func=lambda message: message.text == "Предыдущая неделя")
def handle_reply_button(message):
    bot.send_message(message.chat.id,"Рсаписание на пердыдущую неделю")

        

@bot.message_handler(func=lambda message: True)  
def handle_unknown_message(message):
    bot.send_message(message.chat.id, "ОШИБКА: неизвестная команда или сообщение.")


bot.polling(none_stop=True)