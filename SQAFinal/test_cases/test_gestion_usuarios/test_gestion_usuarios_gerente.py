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

        #GESTION DE USUARIOS
        #USUARIOS
        self.driver.find_element(By.XPATH,"//span[text() = 'Gestión de Usuarios']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//span[text() = 'Usuarios']").click()
        time.sleep(8)
        self.driver.find_element(By.XPATH,"//select[contains(@class, 'block appearance-none w-full text-sm font-bold bg-white border')]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@type = 'search']").send_keys('Miguel')
        time.sleep(6)
        self.driver.find_element(By.XPATH,"//button[text() = 'Ver']").click()
        time.sleep(8)
        self.driver.find_element(By.XPATH,"//button[text() = 'Volver']").click()
        time.sleep(7)
        self.driver.find_element(By.XPATH,"(//button[text() = 'Roles y Permisos']//parent::button)[2]").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH,"//select[contains(@class, 'border-gray-300 text-sm tracking-normal dark:border-gray-700')]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//option[@value = 'Gerente']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div[@class = 'hidden sm:ml-10 sm:flex p-5']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//input[@type = 'checkbox']//parent::div)[1]").click()
        time.sleep(0.1)
        self.driver.find_element(By.XPATH,"(//input[@type = 'checkbox']//parent::div)[2]").click()
        time.sleep(0.1)
        self.driver.find_element(By.XPATH,"(//input[@type = 'checkbox']//parent::div)[3]").click()
        time.sleep(0.1)
        self.driver.find_element(By.XPATH,"(//input[@type = 'checkbox']//parent::div)[4]").click()
        time.sleep(0.1)
        self.driver.find_element(By.XPATH,"(//input[@type = 'checkbox']//parent::div)[5]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[contains(@class, 'text-white bg-gradient-to-r from-green-400')]").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,"//button[contains(@class, 'text-white bg-gradient-to-r from-gray-400 via-gray-500')]").click()
        time.sleep(5)

        #Reportes
        self.driver.find_element(By.XPATH,"//span[text() = 'Reportes']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"(//select[contains(@class, 'border-gray-300 text-sm tracking-normal')]//parent::select)[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//option[@value = 'enrollment']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div[@class = 'p-2 sm:ml-64']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//select[contains(@class, 'border-gray-300 text-sm tracking-normal')]//parent::select)[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//option[@value = '1']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"(//select[contains(@class, 'border-gray-300 text-sm tracking-normal')]//parent::select)[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[contains(@class , 'text-white text-md bg-gradient-to-r')]").click()
        time.sleep(5)