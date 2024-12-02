from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:5173')
        time.sleep(5)

    def teardown_method(self):
        self.driver.quit()
        print('Test Finalizado')
    
    def test_meraki(self):
        #Iniciar Sesión como Administrador Absoluto
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@type = 'email']").send_keys('admin@test.com')
        self.driver.find_element(By.XPATH,"//input[@type = 'password']").send_keys('qwerty123')
        self.driver.find_element(By.XPATH,"//button[@type = 'submit']").click()
        time.sleep(8)
