"""Incluir acá los test cases para el módulo específico."""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestInicio:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:5173')
        time.sleep(2)
    def teardown_method(self):
        self.driver.quit()
        print("Prueba terminada")

    def test_inicio(self):

        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@type = 'email']").send_keys('admin@test.com')
        self.driver.find_element(By.XPATH,"//input[@type = 'password']").send_keys('qwerty123')
        self.driver.find_element(By.XPATH,"//button[@type = 'submit']").click()
        time.sleep(8)
        
        # Inicio
        self.driver.find_element(By.XPATH,"//span[@class = 'mdi mdi-bell-outline text-2xl text-gray-500 cursor-pointer']").click()
        time.sleep(7)
        self.driver.find_element(By.XPATH,"//span[text() = 'Inicio']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//span[@class= 'mdi mdi-fullscreen text-2xl text-gray-500']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//span[@class= 'mdi mdi-fullscreen text-2xl text-gray-500']").click()
        time.sleep(1)