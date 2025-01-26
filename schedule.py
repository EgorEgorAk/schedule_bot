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


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_message(message):
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

    reply_button_schedule = types.KeyboardButton("Расписание")
    reply_button_next_week = types.KeyboardButton("Следующая неделя")
    reply_button_previous_week = types.KeyboardButton("Предыдущая неделя")
    reply_keyboard.add(reply_button_schedule, reply_button_next_week, reply_button_previous_week)

    bot.send_message(
        message.chat.id,
        "Привет! Напиши мне 'Расписание' или отправь дату в формате 'ГГГГ-ММ-ДД', чтобы получить расписание.",
        reply_markup=reply_keyboard
    )

def parsing_schedule(message):
    driver = webdriver.Chrome()
    width = 1360
    height = 1250  # Округлённое значение высоты
    driver.set_window_size(width, height)
    
    # Загрузка страницы
    driver.get(f'https://www.sut.ru/studentu/raspisanie/raspisanie-zanyatiy-studentov-ochnoy-i-vecherney-form-obucheniya?group=56043&date')
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
def handle_schedule_request(message):
    bot.send_message(message.chat.id, "Загружаю расписание на текущую дату")
    screenshot_path1 = parsing_schedule(message)
    with open(screenshot_path1, mode="rb") as screenshot_descriptor:
        bot.send_photo(message.chat.id, screenshot_descriptor)


@bot.message_handler(func=lambda message: message.text == "Расписание")
def handle_reply_button(message):
    screenshot_path = parsing_schedule(message)
    with open(screenshot_path, mode="rb") as screenshot_descriptor:
        bot.send_photo(message.chat.id, screenshot_descriptor)


@bot.message_handler(func=lambda message: True)
def handle_date_message(message):
    date = message.text.strip()

    # Проверяем, является ли сообщение датой в формате ГГГГ-ММ-ДД
    try:
        time.strptime(date, "%Y-%m-%d")  # Проверка формата даты
        bot.send_message(message.chat.id, f"Загружаю расписание на дату: {date}...")
        
        # Формируем ссылку и запускаем парсинг
        url = f"https://www.sut.ru/studentu/raspisanie/raspisanie-zanyatiy-studentov-ochnoy-i-vecherney-form-obucheniya?group=56043&date={date}"
        screenshot_path = parse_schedule(url)
        
        # Отправляем скриншот пользователю
        with open(screenshot_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите дату в формате 'ГГГГ-ММ-ДД'.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")


def parse_schedule(url):
    try:
        # Настройки Selenium
        driver = webdriver.Chrome()
        width = 1360
        height = 1250
        driver.set_window_size(width, height)

        # Загрузка страницы
        driver.get(url)
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

        # Обрезка скриншота
        cropped_screenshot_path = "screenshots/centered_screenshot.png"
        with Image.open(screenshot_path) as img:
            img_width, img_height = img.size
            left = (img_width - width) // 2
            top = (img_height - height) // 2
            right = left + width
            bottom = top + height
            cropped_image = img.crop((left, top, right, bottom))
            cropped_image.save(cropped_screenshot_path)

        driver.quit()
        return cropped_screenshot_path
    except Exception as e:
        if driver:
            driver.quit()
        raise Exception(f"Ошибка при парсинге: {e}")


@bot.message_handler(func=lambda message: message.text == "Следующая неделя")
def handle_next_week(message):
    bot.send_message(message.chat.id, "Расписание на следующую неделю (функция пока не реализована).")


@bot.message_handler(func=lambda message: message.text == "Предыдущая неделя")
def handle_previous_week(message):
    bot.send_message(message.chat.id, "Расписание на предыдущую неделю (функция пока не реализована).")


@bot.message_handler(func=lambda message: True)
def handle_unknown_message(message):
    bot.send_message(message.chat.id, "ОШИБКА: неизвестная команда или сообщение.")


bot.polling(none_stop=True)