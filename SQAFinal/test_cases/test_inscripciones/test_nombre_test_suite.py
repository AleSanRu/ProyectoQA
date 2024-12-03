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
    def test_verify_Inscripcion(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Ingresar Correo Electrónico']").send_keys("alejandro@gmail.com")
        time.sleep(1)  
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Ingresar Contraseña']").send_keys("123456Q@")
        time.sleep(1) 
        self.driver.find_element(By.XPATH, "//button[text() = 'INGRESAR']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[contains(@class, 'mdi-fullscreen') and contains(@class, 'text-2xl') and contains(@class, 'text-gray-500')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@href='/enrollments']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Nuevo')]").click()
        time.sleep(3)
        self.date_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Selecciona una fecha']")
        self.date_input.send_keys("2024-12-01")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[contains(text(),'Buscar estudiante...')]//ancestor::div[@class='css-hlgwow']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='react-select-3-input']").send_keys("Ale")
        time.sleep(8)
        self.driver.find_element(By.XPATH, "//input[@id='react-select-3-input']").send_keys(Keys.ENTER)
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//input[@id='react-select-5-input']").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//input[@id='react-select-5-input']").send_keys("Excel")
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//input[@id='react-select-5-input']").send_keys(Keys.ENTER)
        self.driver.execute_script("window.scrollBy(0, 750);")
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//input[@id='react-select-7-input']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='react-select-7-input']").send_keys("Navidad")
        self.driver.execute_script("window.scrollBy(0, 750);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='react-select-7-input']").send_keys(Keys.ENTER)
        upload_button = self.driver.find_element(By.XPATH, "//input[@type='file' and @name='document1']")
        image_path = r"C:\Users\Usuario\Downloads\images (2).jpg"
        upload_button.send_keys(image_path)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, 750);")
        upload_button = self.driver.find_element(By.XPATH, "//input[@type='file' and @name='document2']")
        image_path = r"C:\Users\Usuario\Downloads\images (2).jpg"
        upload_button.send_keys(image_path)
        self.driver.find_element(By.XPATH, "//button[text()='Guardar']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[text()='Anular']").click()
        Mensaje_Eliminar = self.driver.find_element(By.XPATH, "//h3[contains(text(), 'seguro de que quieres eliminar')]").text
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[text()='Confirmar']").click()
        elemento = element = self.driver.find_element(By.XPATH, "//span[@class='text-md tracking-tight']").text
        esperado = "AleSanRu"
        assert elemento == esperado, f"Inicio de sesion {elemento}fallido - EL TEST :{esperado}"
    def test_verify_View_student(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Ingresar Correo Electrónico']").send_keys("alejandro@gmail.com")
        time.sleep(1)  
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Ingresar Contraseña']").send_keys("123456Q@")
        time.sleep(1) 
        self.driver.find_element(By.XPATH, "//button[text() = 'INGRESAR']").click()
        time.sleep(7)
        self.driver.find_element(By.XPATH, "//a[@href='/students']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//input[@type = 'search']").send_keys('12345678')
        time.sleep(8)
        self.driver.find_element(By.XPATH,"//button[text() = 'Ver Perfil']").click()
        time.sleep(8)
        self.driver.find_element(By.XPATH,"//button[text() = 'Volver']").click()
        time.sleep(7)
        elemento = element = self.driver.find_element(By.XPATH, "//span[@class='text-md tracking-tight']").text
        esperado = "AleSanRu"
        assert elemento == esperado, f"Inicio de sesion {elemento}fallido - EL TEST :{esperado}"