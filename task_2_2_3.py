import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

try:
    link = 'http://suninjuly.github.io/selects2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    num1_elm = browser.find_element_by_css_selector('#num1')
    num1 = int(num1_elm.text)

    num2_elm = browser.find_element_by_css_selector('#num2')
    num2 = int(num2_elm.text)

    total = num1 + num2


    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_visible_text(str(total))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(3)	

finally:
    time.sleep(5)
    browser.quit()
    