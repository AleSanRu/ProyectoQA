""" Incluir acá los test cases para el módulo específico. """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestDescuentos:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:5173')
        time.sleep(5)
    def teardown_method(self):
        self.driver.quit()
        print("Prueba terminada")

    def test_descuentos(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@type = 'email']").send_keys('admin@test.com')
        self.driver.find_element(By.XPATH,"//input[@type = 'password']").send_keys('qwerty123')
        self.driver.find_element(By.XPATH,"//button[@type = 'submit']").click()
        time.sleep(3)

        # Descuentos
        self.driver.find_element(By.XPATH,"//span[text() = 'Descuentos']").click()
        time.sleep(7)

        # Registrar Nuevo Descuento
        self.driver.find_element(By.XPATH,"//button[contains(@class, 'inline-flex items-center justify-center text-sm px-5 py-2.5 mb-4 font-medium')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name = 'name']").send_keys('DESCUENTO DE NAVIDAD')
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'percentage']").send_keys('25')
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[text() = 'Guardar']").click()
        time.sleep(2)

        self.driver.find_element(By.XPATH,"//input[@type = 'search']").send_keys('DESCUENTO DE NAVIDAD')
        time.sleep(5)

        # Editar Descuento
        self.driver.find_element(By.XPATH,"//button[text() = 'Editar']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'name']").clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'name']").send_keys('DESCUENTO DE AÑO NUEVO')
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'percentage']").clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'percentage']").send_keys('15')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[text() = 'Actualizar']").click()
        time.sleep(7)

        # Eliminar Descuento
        self.driver.find_element(By.XPATH,"//input[@type = 'search']").send_keys('DESCUENTO DE AÑO NUEVO')
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[text() = 'Eliminar']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[text() = 'Confirmar']").click()
        time.sleep(2)

    


