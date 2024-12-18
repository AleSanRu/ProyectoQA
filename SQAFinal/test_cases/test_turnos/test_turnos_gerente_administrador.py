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
        self.driver.get('http://localhost:5173')
        time.sleep(5)
    def teardown_method(self):
        self.driver.quit()
        print("Prueba terminada")

    def test_turnos(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@type = 'email']").send_keys('admin@test.com')
        self.driver.find_element(By.XPATH,"//input[@type = 'password']").send_keys('qwerty123')
        self.driver.find_element(By.XPATH,"//button[@type = 'submit']").click()
        time.sleep(3)

        # Turnos
        self.driver.find_element(By.XPATH,"//span[text() = 'Turnos']").click()
        time.sleep(5)

        # Registrar Nuevo Turno
        self.driver.find_element(By.XPATH,"//button[contains(@class, 'inline-flex items-center justify-center text-sm px-5 py-2.5 mb-4 font-medium')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'name']").send_keys('MAÑANA')
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@id = 'react-select-3-input']").send_keys('AULA 1')
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@id = 'react-select-3-input']").send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'start_time']").send_keys('07:15')
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'end_time']").send_keys('09:15')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[text() = 'Guardar']").click()
        time.sleep(7)
        
        self.driver.find_element(By.XPATH,"//input[@type = 'search']").send_keys('MAÑANA')
        time.sleep(10)

        # Editar Turno
        self.driver.find_element(By.XPATH,"//button[text() = 'Editar']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name = 'name']").clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'name']").send_keys('NOCHE')
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'start_time']").clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'start_time']").send_keys('19:15')
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'end_time']").clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'end_time']").send_keys('21:15')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[text() = 'Actualizar']").click()
        time.sleep(7)

        # Eliminar Turno
        self.driver.find_element(By.XPATH,"//input[@type = 'search']").send_keys('NOCHE')
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[text() = 'Eliminar']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[text() = 'Confirmar']").click()
        time.sleep(2)

    


