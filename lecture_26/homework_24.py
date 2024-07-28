from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Инициализация драйвера
driver = webdriver.Chrome()
driver.maximize_window()

# Открываем главную страницу
driver.get('http://localhost:8000/dz.html')

# Взаимодействие с первым фреймом
driver.switch_to.frame('frame1')
input1 = driver.find_element(By.ID, 'input1')
input1.send_keys('Frame1_Secret')
driver.find_element(By.XPATH, '//button[text()="Перевірити"]').click()

# Проверяем алерт
alert = Alert(driver)
time.sleep(1)
alert_text = alert.text
if alert_text == 'Верифікація пройшла успішно!':
    print('Frame 1 verification successful!')
alert.accept()

# Возврашаемся к первоначальному состоянию
driver.switch_to.default_content()

# Взаимодействие со вторым фреймом
driver.switch_to.frame('frame2')
input2 = driver.find_element(By.ID, 'input2')
input2.send_keys('Frame2_Secret')
driver.find_element(By.XPATH, '//button[text()="Перевірити"]').click()

# Проверяем алерт
alert = Alert(driver)
time.sleep(1)
alert_text = alert.text
if alert_text == 'Верифікація пройшла успішно!':
    print('Frame 2 verification successful!')
alert.accept()

# Закрываем браузер
driver.quit()
