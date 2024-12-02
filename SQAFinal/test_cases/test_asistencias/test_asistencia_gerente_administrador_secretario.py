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
        
        # asisencia
        self.driver.find_element(By.XPATH,"//span[text() = 'Asistencias']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//select[contains(@class , 'border-gray-300 text-sm tracking-normal dark:border-gray-700')]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[contains(@class , 'border-gray-300 text-sm tracking-normal dark:border-gray-700')]//option[@value = '1']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//h1[text() = 'Registro de Asistencias']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"(//input[@name = 'attendance-642']//parent::label)[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[text() = 'Guardar']").click()
        time.sleep(5)
