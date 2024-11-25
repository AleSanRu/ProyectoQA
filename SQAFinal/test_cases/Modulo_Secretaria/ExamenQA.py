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
        elemento=self.driver.find_element(By.XPATH,"//span[text()='AleSanRu']")
        assert elemento is not None, "Inicio de sesion fallido - EL TEST FALLO"
        print("Inicio de sesion exitoso")
    def test_verify_Register_student(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Ingresar Correo Electrónico']").send_keys("alejandro@gmail.com")
        time.sleep(1)  
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Ingresar Contraseña']").send_keys("123456Q@")
        time.sleep(1) 
        self.driver.find_element(By.XPATH, "//button[text() = 'INGRESAR']").click()
        time.sleep(7)
        self.driver.find_element(By.XPATH, "//a[@href='/students']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Nuevo')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Nombres']").send_keys("Ale Ale")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Apellido Paterno']").send_keys("Apaza")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Apellido Materno']").send_keys("Apaza")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Cédula de Identidad']").send_keys("12345678")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Ingresar fecha']").send_keys("01/01/2000")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//select[@name='placeofbirth']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//select[@name='placeofbirth']/option[@value='LA PAZ']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Teléfono']").send_keys("78945612")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//select[@name='gender']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//select[@name='gender']/option[@value='MASCULINO']").click()
        time.sleep(1)
        upload_button = self.driver.find_element(By.XPATH, "//input[@id = 'image-upload']")
        image_path = r"C:\Users\Usuario\Downloads\images (2).jpg"
        upload_button.send_keys(image_path)
        time.sleep(2)
        ##self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Guardar')]").click()
        time.sleep(4)
        elemento=self.driver.find_element(By.XPATH,"//span[text()='AleSanRu']")
        assert elemento is not None, "Inicio de sesion fallido - EL TEST FALLO"
        print("Inicio de sesion exitoso")
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
        self.driver.find_element(By.XPATH, "//input[@id='react-select-3-input']").send_keys("Alejandro")
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
        elemento = self.driver.find_element(By.XPATH, "//td[text()='Ale Ale']").text
        self.driver.find_element(By.XPATH, "//button[text()='Anular']").click()
        Mensaje_Eliminar = self.driver.find_element(By.XPATH, "//h3[contains(text(), 'seguro de que quieres eliminar')]").text
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[text()='Confirmar']").click()
        esperado = "ALE ALE"
        assert elemento == esperado, f"Inicio de sesion {elemento}fallido - EL TEST :{esperado}"
        Eliminar_esperado="¿Estás seguro de que quieres eliminar esta inscripción?"
        assert Eliminar_esperado == Mensaje_Eliminar, f"Inicio de sesion {elemento}fallido - EL TEST :{esperado}"