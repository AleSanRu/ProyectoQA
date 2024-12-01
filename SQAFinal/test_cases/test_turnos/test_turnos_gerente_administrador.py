""" Incluir acá los test cases para el módulo específico. """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestTurnos:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:5173/shifts')
        time.sleep(2)
    def teardown_method(self):
        self.driver.quit()
        print("Prueba terminada")

    def test_turnos(self):
        # Registrar Turno
        self.driver.find_element(By.XPATH,"//button[contains(@class, 'inline-flex items-center justify-center text-sm px-5 py-2.5 mb-4 font-medium')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'name']").send_keys('MAÑANA')

    


