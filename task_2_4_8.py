import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    wait = WebDriverWait(browser, 12)

    good_price = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    book_button = browser.find_element_by_id('book')
    book_button.click()

    time.sleep(1)

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    answer_field = browser.find_element_by_css_selector('#answer')
    answer_field.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_id('solve')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()