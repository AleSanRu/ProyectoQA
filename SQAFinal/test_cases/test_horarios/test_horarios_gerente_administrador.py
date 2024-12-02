""" Incluir acá los test cases para el módulo específico. """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestHorarios:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:5173')
        time.sleep(5)
    def teardown_method(self):
        self.driver.quit()
        print("Prueba terminada")

    def test_horarios(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@type = 'email']").send_keys('admin@test.com')
        self.driver.find_element(By.XPATH,"//input[@type = 'password']").send_keys('qwerty123')
        self.driver.find_element(By.XPATH,"//button[@type = 'submit']").click()
        time.sleep(3)

        # Horarios
        self.driver.find_element(By.XPATH,"//span[text() = 'Horarios']").click()
        time.sleep(7)
        self.driver.find_element(By.XPATH,"//button[contains(@class, 'inline-flex items-center justify-center text-sm px-5 py-2.5 mb-4 font-medium')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@id = 'react-select-3-input']").send_keys('OFIMÁTICA - A')
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@id = 'react-select-3-input']").send_keys(Keys.ENTER)
        time.sleep(2)

        # Lunes
        self.driver.find_element(By.XPATH,"//input[@id = 'react-select-5-input']").send_keys('TARDE (15:15 - 17:15)')
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@id = 'react-select-5-input']").send_keys(Keys.ENTER)
        time.sleep(2)

        # Miercoles
        self.driver.find_element(By.XPATH,"//input[@id = 'react-select-9-input']").send_keys('TARDE (15:15 - 17:15)')
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@id = 'react-select-9-input']").send_keys(Keys.ENTER)
        time.sleep(2)

        # Viernes
        self.driver.find_element(By.XPATH,"//input[@id = 'react-select-13-input']").send_keys('TARDE (17:30 - 19:30)')
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@id = 'react-select-13-input").send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[text() = 'Guardar']").click()
        time.sleep(7)

    


