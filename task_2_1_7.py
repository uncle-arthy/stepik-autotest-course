import math
import time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_css_selector('#treasure')
    x = int(x_element.get_attribute("valuex"))
    y = calc(x)

    answer_field = browser.find_element_by_css_selector('#answer')
    answer_field.send_keys(y)

    robot_checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    robot_checkbox.click()

    robot_radio = browser.find_element_by_css_selector('#robotsRule')
    robot_radio.click()   

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()