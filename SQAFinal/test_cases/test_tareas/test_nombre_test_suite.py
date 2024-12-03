from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time 

class TestColum:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:5173/login')
        time.sleep(1)
        #yield
        #self.driver.quit()
        #print("Prueba de interfaz finalizada")   
    def teardown_method(self):
        self.driver.quit()
        print("Prueba de interfaz finalizada")
        #Inicio de sesion 
        
    def test_verify_Login(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Ingresar Correo Electrónico']").send_keys("alejandro@gmail.com")
        time.sleep(1)  
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Ingresar Contraseña']").send_keys("123456Q@")
        time.sleep(1) 
        self.driver.find_element(By.XPATH, "//button[text() = 'INGRESAR']").click()
        time.sleep(7)
        #//span[text()='alejandro']
        elemento = element = self.driver.find_element(By.XPATH, "//span[@class='text-md tracking-tight']").text
        esperado = "AleSanRu"
        assert elemento == esperado, f"Inicio de sesion {elemento}fallido - EL TEST :{esperado}"
        
    def test_verify_Tareas(self):
        self.driver.find_element(By.XPATH, "//a[@href='/enrollments']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Ingresar Correo Electrónico']").send_keys("alejandro@gmail.com")
        time.sleep(1)  
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Ingresar Contraseña']").send_keys("123456Q@")
        time.sleep(1) 
        self.driver.find_element(By.XPATH, "//button[text() = 'INGRESAR']").click()
        time.sleep(7)