from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

class Test_ITC_LOGIN:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:5173/login')
        time.sleep(1)
    def teardown_method(self):
        self.driver.quit()
        print("Prueba de Login")
    def test_verify_frgt_password_Iniciar(self):
        actual = self.driver.find_element(By.XPATH, "//h2[text()='Iniciar Sesión']").text
        esperado = "Iniciar Sesión"
        print(actual)
        time.sleep(1)
        assert actual == esperado, f"FALLO: actual: {actual}, esperado: {esperado}"
    def test_verify_frgt_password_Correo(self):
        actual = self.driver.find_element(By.XPATH, "//label[text()='Correo Electrónico']").text
        esperado = "Correo Electrónico"
        print(actual)
        time.sleep(1)
        assert actual == esperado, f"FALLO: actual: {actual}, esperado: {esperado}"
    def test_verify_frgt_password_Contraseña(self):
        actual = self.driver.find_element(By.XPATH, "//label[text()='Contraseña']").text
        esperado = "Contraseña"
        print(actual)
        time.sleep(1)
        assert actual == esperado, f"FALLO: actual: {actual}, esperado: {esperado}"
    def test_verify_frgt_password_Olvidaste(self):
        actual = self.driver.find_element(By.XPATH, "//a[text()='¿Olvidaste tu contraseña?']").text
        esperado = "¿Olvidaste tu contraseña?"
        print(actual)
        time.sleep(1)
        assert actual == esperado, f"FALLO: actual: {actual}, esperado: {esperado}"
    def test_verify_frgt_password_ingresar(self):
        actual = self.driver.find_element(By.XPATH, "//a[@class='font-medium text-primary-600 hover:underline']").click()
        time.sleep(2)
    ############################################################################################################################
class Test_ITC_regristro:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:5173/register')
        time.sleep(1)
    def teardown_method(self):
        self.driver.quit()
        print("Prueba de Login")
    def test_verify_frgt_password_Registrarse(self):
        actual = self.driver.find_element(By.XPATH, "//h2[text()='Registrarse']").text
        esperado = "Registrarse"
        print(actual)
        time.sleep(1)
        assert actual == esperado, f"FALLO: actual: {actual}, esperado: {esperado}"
    def test_verify_frgt_password_Usuario(self):
        actual = self.driver.find_element(By.XPATH, "//label[text()='Usuario']").text
        esperado = "Usuario"
        print(actual)
        time.sleep(1)
        assert actual == esperado, f"FALLO: actual: {actual}, esperado: {esperado}"
    def test_verify_frgt_password_Correo(self):
        actual = self.driver.find_element(By.XPATH, "//label[text()='Correo Electrónico']").text
        esperado = "Correo Electrónico"
        print(actual)
        time.sleep(1)
        assert actual == esperado, f"FALLO: actual: {actual}, esperado: {esperado}"
    def test_verify_frgt_password_Contra(self):
        actual = self.driver.find_element(By.XPATH, "//label[text()='Contraseña']").text
        esperado = "Correo Electrónico"
        print(actual)
        time.sleep(1)
        assert actual != esperado, f"FALLO: actual: {actual}, esperado: {esperado}"
    def test_verify_frgt_password_Anuncio(self):
        actual = self.driver.find_element(By.XPATH, "//p[@class='tracking-tighter font-light text-sm']").text
        esperado = "La contraseña debe tener al menos 8 carácteres, debe empezar por mayúscula y tener 1 carácter especial."
        print(actual)
        time.sleep(1)
        assert actual == esperado, f"FALLO: actual: {actual}, esperado: {esperado}"

class Test_ITC_Llenado:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:5173/register')
        time.sleep(1)
    def teardown_method(self):
        self.driver.quit()
        print("Prueba de Login")
    def test_verify_lenado(self):
       
        actual = self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Mauricio Torres")
        actual = self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys("torres@gmail.com")
        actual = self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Bayonett@2024")
        
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)   
        
        print(f"Texto encontrado: {actual}")
        time.sleep(3)

class Test_ITC_messenger:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://mailtrap.io/inboxes/3223560/messages')
        time.sleep(1)
    def teardown_method(self):
        self.driver.quit()
        print("Prueba de Login")
    def test_verify_llenado(self):
       
        actual = self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Mauricio Torres")
        actual = self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys("torres@gmail.com")
        actual = self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Bayonett@2024")
        
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)   
        
        print(f"Texto encontrado: {actual}")
        time.sleep(3)

class Test_Verificaion:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://mailtrap.io/signin')
        time.sleep(1)
    def teardown_method(self):
        self.driver.quit()
        print("Prueba de Login")
    
    def test_click_first_verification_link(self):
        
        
        self.driver.find_element(By.XPATH, "//input[@autofocus='autofocus']").send_keys("chatnoircatmua2024@gmail.com")
        time.sleep(1)
       
        self.driver.find_element(By.XPATH, "//a[@class='login_next_button button button--medium button--block']").click()
        time.sleep(1)
       
        actual = self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("mer4ki2024")
        
        self.driver.find_element(By.XPATH, "//input[@value='Log In']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[text()='Deny']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[text()='My Inbox']").click()
        time.sleep(5)
        actual = self.driver.find_element(By.XPATH, "(//a[contains(@class, 'i18m0o91') and contains(@class, 'i16w2k3p')])[1]").click()
        time.sleep(3)
        #self.driver.find_element(By.XPATH, "//a[contains(@href, 'api/email/verify')]").click()
        
        time.sleep(5)
        #self.driver.find_element(By.XPATH, "//a[contains(@href, 'api/email/verify')]").click()
        
        
        
    
    
         

   
        
class Test_Entrar:
     def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:5173/login')
        time.sleep(1)
     def teardown_method(self):
        self.driver.quit()
        print("Prueba de Login")
     def test_verify_llenado(self):
       
        
        actual = self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys("torres@gmail.com")
        actual = self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Bayonett@2024")
        
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)   
        
        print(f"Texto encontrado: {actual}")
        time.sleep(3)


        
        
    
