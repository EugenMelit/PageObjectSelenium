from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
options = webdriver.ChromeOptions()
driver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service, options=options)
driver.get(url="http://tutorialsninja.com/demo/index.php?route=account/register")

first_name = driver.find_element(By.CSS_SELECTOR,"#input-firstname")
first_name.send_keys("eugenn")
time.sleep(3)
last_name = driver.find_element(By.CSS_SELECTOR, "#input-lastname")
last_name.send_keys("surganan")
time.sleep(3)
email = driver.find_element(By.CSS_SELECTOR,"#input-email")
email.send_keys("myemailll@ukr.net")
time.sleep(3)
telefone = driver.find_element(By.CSS_SELECTOR, "#input-telephone")
telefone.send_keys("1231231239")
time.sleep(3)
password = driver.find_element(By.CSS_SELECTOR,"#input-password")
password.send_keys("yourstorss")
time.sleep(3)
password_confirm = driver.find_element(By.CSS_SELECTOR,"#input-confirm")
password_confirm.send_keys("yourstorss")
time.sleep(3)
priv_policy = driver.find_element(By.CSS_SELECTOR, "#content > form > div > div > input[type=checkbox]:nth-child(2)").click()
button_continue = driver.find_element(By.CSS_SELECTOR, "#content > form > div > div > input.btn.btn-primary").click()
time.sleep(5)
proverka = driver.find_element(By.CSS_SELECTOR, "#content > h1").text
print(proverka)
proverka1 = "Your Account Has Been Created!"
if proverka == proverka1:
    print("Тест прошел успешно")
else:
    print("Тест проверку не прошел")




if __name__ == '__main__':
    print("main")