from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestGestionCursos:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:5173/modalities')
        time.sleep(2)
    def teardown_method(self):
        self.driver.quit()
        print("Prueba terminada")

    def test_gestion_cursos(self):
        # Gestión de Cursos
        # Modalidades
        # Registrar Modalidad
        self.driver.find_element(By.XPATH,"//button[contains(@class, 'inline-flex items-center justify-center text-sm px-5 py-2.5 mb-4 font-medium')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'name']").send_keys('Diseño Grafico')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'duration_in_months']").send_keys('12')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[text() = 'Guardar']").click()
        time.sleep(12)

        # Editar Modalidad
        self.driver.find_element(By.XPATH,"//input[@type = 'search']").send_keys('Diseño Grafico')
        time.sleep(13)
        self.driver.find_element(By.XPATH,"//button[text() = 'Editar']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//input[@name = 'name']").clear()
        time.sleep(4)
        self.driver.find_element(By.XPATH,"//input[@name = 'name']").send_keys('Renderizado Grafico')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'duration_in_months']").clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name = 'duration_in_months']").send_keys('6')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[text() = 'Actualizar']").click()
        time.sleep(6)

        # Eliminar Modalidad
        self.driver.find_element(By.XPATH,"//input[@type = 'search']").send_keys('Renderizado Grafico')
        time.sleep(10)
        self.driver.find_element(By.XPATH,"//button[text() = 'Eliminar']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[text() = 'Confirmar']").click()
        time.sleep(5)

        # Cursos
        # Registrar Curso
        self.driver.find_element(By.XPATH,"//button[contains(@class, 'inline-flex items-center justify-center text-sm px-5 py-2.5 mb-4 font-medium')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'name']").send_keys('Renderizad lo que sea')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[@name = 'parallel']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[@name = 'parallel']//option[@value = 'A']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'description']").send_keys('aqui hay clases equisde')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@placeholder= 'Seleccionar fecha de inicio']").send_keys('04/02/2025')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//div[text() = '4']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@placeholder= 'Seleccionar fecha de finalización']").send_keys('04/07/2025')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//div[text() = '4']").click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@id = 'react-select-3-input']").send_keys('AGUSTÍ PLANAS ELOY - 87384491')
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@id = 'react-select-3-input']").send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@id = 'react-select-5-input']").send_keys('Diplomado en Psicología')
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@id = 'react-select-5-input']").send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name = 'cost']").send_keys('1000')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[text() = 'Guardar']").click()
        time.sleep(10)

        # Editar Curso
        self.driver.find_element(By.XPATH,"(//button[text() = 'Ver Detalles']//parent::button)[4]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[text() = 'Editar']").click()
        time.sleep(7)
        self.driver.find_element(By.XPATH,"//input[@name = 'name']").clear()
        time.sleep(4)
        self.driver.find_element(By.XPATH,"//input[@name = 'name']").send_keys('Renderizad lo que sea')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[@name = 'parallel']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[@name = 'parallel']//option[@value = 'B']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//h2[text() = 'Actualizar datos del Curso']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name = 'description']").clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name = 'description']").send_keys('aqui hay clases equisde asd asd')
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'cost']").clear()
        time.sleep(4)
        self.driver.find_element(By.XPATH,"//input[@name = 'cost']").send_keys('1500')
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[text() = 'Actualizar']").click()
        time.sleep(7)

        # Eliminar Curso
        self.driver.find_element(By.XPATH,"(//button[text() = 'Ver Detalles']//parent::button)[4]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[text() = 'Eliminar']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[text() = 'Confirmar']").click()
        time.sleep(5)
    


