from selenium import webdriver
import time
import os

try: 
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(cur_dir, 'empty.txt')
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    name_field = browser.find_element_by_name('firstname')
    name_field.send_keys('Жугдэрдэмидийн')

    surname_field = browser.find_element_by_name('lastname')
    surname_field.send_keys('Гуррагча')

    email_field = browser.find_element_by_name('email')
    email_field.send_keys('mongol@cosmonaut.mn')

    send_file_element = browser.find_element_by_css_selector('#file')
    send_file_element.send_keys(filepath)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
