from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestAtt:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:5173/login')
        time.sleep(2)
    def teardown_method(self):
        self.driver.quit()
        print("Prueba terminada")

    def test_meraki(self):
        #INICIO de sesion
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@type = 'email']").send_keys('admin@test.com')
        self.driver.find_element(By.XPATH,"//input[@type = 'password']").send_keys('qwerty123')
        self.driver.find_element(By.XPATH,"//button[@type = 'submit']").click()
        time.sleep(8)

        #inicio
        self.driver.find_element(By.XPATH,"//span[@class = 'mdi mdi-bell-outline text-2xl text-gray-500 cursor-pointer']").click()
        time.sleep(7)
        self.driver.find_element(By.XPATH,"//span[text() = 'Inicio']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//span[@class= 'mdi mdi-fullscreen text-2xl text-gray-500']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//span[@class= 'mdi mdi-fullscreen text-2xl text-gray-500']").click()
        time.sleep(1)

        #PERFIL
        self.driver.find_element(By.XPATH,"//span[@class = 'text-md tracking-tight']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//a[@class = 'block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//button[contains(@class, 'text-white bg-gradient-to-br from-green-400')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[contains(@class, 'text-white bg-gradient-to-r from-gray-400 via-gray-500 to-gray-600')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//span[text() = 'Inicio']").click()
        time.sleep(4)

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

        #Estudaintes
        self.driver.find_element(By.XPATH,"//span[text()= 'Estudiantes']").click()
        time.sleep(9)

        #CREAR
        self.driver.find_element(By.XPATH,"//div[@class = 'flex justify-between items-center mb-4']//button[contains(@class, 'inline-flex items-center justify-center')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'name']").send_keys('Michael Bryan')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'last_name']").send_keys('Paz')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'second_last_name']").send_keys('Rodriguez')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'ci']").send_keys('6894308')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@placeholder = 'Ingresar fecha']").send_keys('06/03/2002')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//div[text() = '6']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[@name = 'placeofbirth']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[@name = 'placeofbirth']//option[@value = 'LA PAZ']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'phone']").send_keys('68062423')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[@name = 'gender']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[@name = 'gender']//option[@value = 'MASCULINO']").click()
        time.sleep(1)
        upload_button = self.driver.find_element(By.XPATH, "//input[@id = 'image-upload']")
        image_path = r"D:\Users\Sr.Michael\Downloads\est1.png"
        upload_button.send_keys(image_path)
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[contains(@class, 'text-white bg-gradient-to-r from-green-400')]").click()
        time.sleep(9)

        #VER PERFIL
        self.driver.find_element(By.XPATH,"//input[@type = 'search']").send_keys('6894308')
        time.sleep(10)
        self.driver.find_element(By.XPATH,"//div[contains(@class, 'relative w-11 h-6 bg-gray-200 peer-focus:outline-none')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[text() = 'Confirmar']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//div[contains(@class, 'relative w-11 h-6 bg-gray-200 peer-focus:outline-none')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[text() = 'Confirmar']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[text() = 'Ver Perfil']").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH,"//button[text() = 'Volver']").click()
        time.sleep(7)

        #Editar
        self.driver.find_element(By.XPATH,"//input[@type = 'search']").send_keys('6894308')
        time.sleep(10)
        self.driver.find_element(By.XPATH,"//button[text() = 'Editar']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//input[@name = 'name']").clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name = 'name']").send_keys('Miguel Perez')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'last_name']").clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name = 'last_name']").send_keys('Apaza')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'second_last_name']").clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name = 'second_last_name']").send_keys('Figueroa')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'ci']").clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name = 'ci']").send_keys('2033166')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@placeholder = 'Ingresar fecha']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//select[@class = 'react-datepicker__year-select']//option[@value = '2000']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div[text() = '6']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[@name = 'placeofbirth']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[@name = 'placeofbirth']//option[@value = 'COCHABAMBA']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'phone']").clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name = 'phone']").send_keys('73044815')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[@name = 'gender']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[@name = 'gender']//option[@value = 'MASCULINO']").click()
        time.sleep(1)
        upload_button = self.driver.find_element(By.XPATH, "//input[@type = 'file']")
        image_path = r"D:\Users\Sr.Michael\Downloads\est2.jpg"
        upload_button.send_keys(image_path)
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[contains(@class, 'text-white bg-gradient-to-r from-green-400')]").click()
        time.sleep(9)

        #ELIMINAR
        self.driver.find_element(By.XPATH,"//input[@type = 'search']").send_keys('2033166')
        time.sleep(10)
        self.driver.find_element(By.XPATH,"//button[text() = 'Eliminar']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[text() = 'Confirmar']").click()
        time.sleep(5)

        #DOCENTES
        self.driver.find_element(By.XPATH,"//span[text() = 'Docentes']").click()
        time.sleep(9)

        #CREAR
        
        self.driver.find_element(By.XPATH,"//button[contains(@class, 'inline-flex items-center justify-center text-sm px-5 py-2.5 mb-4 font-medium')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'name']").send_keys('Michael Bryan')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'last_name']").send_keys('Paz')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'second_last_name']").send_keys('Rodriguez')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'ci']").send_keys('6894308')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'phone']").send_keys('68062423')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[@name = 'placeofbirth']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[@name = 'placeofbirth']//option[@value = 'LA PAZ']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@placeholder = 'Ingresar fecha']").send_keys('06/03/2002')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//div[text() = '6']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'specialty']").send_keys('Contador')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[@name = 'gender']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[@name = 'gender']//option[@value = 'MASCULINO']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[contains(@class, 'text-white bg-gradient-to-r from-green-400')]").click()
        time.sleep(9)

        #EDITAR

        self.driver.find_element(By.XPATH,"//input[@type = 'search']").send_keys('6894308')
        time.sleep(8)
        self.driver.find_element(By.XPATH,"//button[text() = 'Editar']").click()
        time.sleep(7)
        self.driver.find_element(By.XPATH,"//input[@name = 'name']").clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name = 'name']").send_keys('Miguel Perez')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'last_name']").clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name = 'last_name']").send_keys('Apaza')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'second_last_name']").clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name = 'second_last_name']").send_keys('Figueroa')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'ci']").clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name = 'ci']").send_keys('2033166')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@placeholder = 'Ingresar fecha']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//select[@class = 'react-datepicker__year-select']//option[@value = '2000']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div[text() = '6']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[@name = 'placeofbirth']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[@name = 'placeofbirth']//option[@value = 'COCHABAMBA']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'phone']").clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name = 'phone']").send_keys('73044815')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[@name = 'gender']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//select[@name = 'gender']//option[@value = 'MASCULINO']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'specialty']").clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name = 'specialty']").send_keys('Diseñador')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[text() = 'Actualizar']").click()
        time.sleep(7)

        #ELIMINAR

        self.driver.find_element(By.XPATH,"//input[@type = 'search']").send_keys('2033166')
        time.sleep(8)
        self.driver.find_element(By.XPATH,"//button[text() = 'Eliminar']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[text() = 'Confirmar']").click()
        time.sleep(6)

        #GESTION DE CURSOS
        #MODALIDADES
        self.driver.find_element(By.XPATH,"//span[text() = 'Gestión de Cursos']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//span[text() = 'Modalidades']").click()
        time.sleep(5)

        #CREAR

        self.driver.find_element(By.XPATH,"//button[contains(@class, 'inline-flex items-center justify-center text-sm px-5 py-2.5 mb-4 font-medium')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@name = 'name']").send_keys('Diseño Grafico')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name = 'duration_in_months']").send_keys('12')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[text() = 'Guardar']").click()
        time.sleep(12)

        #EDITAR

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

        #ELIMINAR
        self.driver.find_element(By.XPATH,"//input[@type = 'search']").send_keys('Renderizado Grafico')
        time.sleep(10)
        self.driver.find_element(By.XPATH,"//button[text() = 'Eliminar']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[text() = 'Confirmar']").click()
        time.sleep(5)

        #CURSOS

        self.driver.find_element(By.XPATH,"//span[text() = 'Cursos']").click()
        time.sleep(7)

        #CREAR
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

        #Editar
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

        #Eliminar
        self.driver.find_element(By.XPATH,"(//button[text() = 'Ver Detalles']//parent::button)[4]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[text() = 'Eliminar']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[text() = 'Confirmar']").click()
        time.sleep(5)

















        



















        
        
        
        

        







        














        

