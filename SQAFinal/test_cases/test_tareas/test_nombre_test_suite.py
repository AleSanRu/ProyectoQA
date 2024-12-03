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
    def teardown_method(self):
        self.driver.quit()
        print("Prueba de interfaz finalizada")
        #Inicio de sesion 
    def test_verify_Tareas(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Ingresar Correo Electrónico']").send_keys("alejandro@gmail.com")
        time.sleep(1)  
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Ingresar Contraseña']").send_keys("123456Q@")
        time.sleep(1) 
        self.driver.find_element(By.XPATH, "//button[text() = 'INGRESAR']").click()
        time.sleep(7)
        self.driver.find_element(By.XPATH, "//a[@href='/tasks']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//div[@class='mb-6']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//option[@value ='2']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Ver Notas']").click()
        time.sleep(2)
        Estudent=self.driver.find_elements(By.XPATH, "//input[@type='number']")
        CheckEstudent=self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        assert len(Estudent) == len(CheckEstudent), "La cantidad de inputs y checkboxes no coincide."
        for i in range(len(Estudent)):
            Estudent[i].clear()
            Estudent[i].send_keys("70")
            time.sleep(2)
            CheckEstudent[i].click()
            time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Guardar']").click()
        time.sleep(2)
        DatosEst=self.driver.find_element(By.XPATH, "//span[text()='Vito']").text
        DatoPedido="Vito Abad Pujol"
        assert DatosEst==DatoPedido,f"El dato {DatosEst} no es igual a {DatoPedido}"
        Guardado=self.driver.find_element(By.XPATH, "//div[text()='Notas guardadas con éxito']").text
        GuardarEsperado="Notas guardadas con éxito"
        assert Guardado==GuardarEsperado,f"el valor {Guardado} no es igual al valor {GuardarEsperado}"
        self.driver.find_element(By.XPATH, "//button[text()='Ocultar Notas']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Nueva Actividad']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Título de la Actividad']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Título de la Actividad']").send_keys("Prueba1")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@role='textbox']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys("Prueba1")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type='date']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type='date']").send_keys("05052025")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Registrar Actividad']").click()
        time.sleep(2)
        Guardado=self.driver.find_element(By.XPATH, "//div[text()='Actividad creada con éxito']").text
        GuardarEsperado="Actividad creada con éxito"
        assert Guardado==GuardarEsperado,f"el valor {Guardado} no es igual al valor {GuardarEsperado}"