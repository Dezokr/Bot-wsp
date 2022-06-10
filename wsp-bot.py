from os import read
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
import time




#driver = webdriver.Edge(executable_path='./driver/msedgedriver')
options = EdgeOptions()
options.use_chromium = True

options.add_experimental_option('excludeSwitches', ['enable-logging'])
#options.add_experimental_option("excludeSwitches" , ["enable-automation","load-extension"])
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
driver = Edge(options = options,executable_path = r'.\\driver\\msedgedriver.exe')


def selectChat(nombre: str):
    buscando = True
    while buscando:
        print("BUSCANDO CHAT")
        time.sleep(1)
        try:
            elements = driver.find_elements_by_tag_name("span")
            for element in elements:
                if element.text == nombre:
                    print("CHAT ENCONTRADO")
                    buscando = False
                    element.click()
                    break
        except:
            print("NO SE ENCONTRO EL CHAT.......")
            break
    


def enviarMensaje(mensaje: str):
    chatbox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')
    chatbox.send_keys(mensaje)
    chatbox.send_keys(Keys.ENTER)

def leerArchivo(ruta:str):
    try:
        archivo = open(ruta, mode='r', encoding='utf-8')
    except:
        print("NO SE ENCONTRO ARCHIVO")
        quit()
        #xpath del cuadro de texto
    chatbox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')
    for line in archivo:
        print("MENSAJE: ", line)
        chatbox.send_keys(line)

    archivo.close()



def validaQR():
    try:
        element = driver.find_element_by_tag_name('canvas')
    except:
        return False
    return True


def botWsp():
    driver.get("https://web.whatsapp.com/")
    time.sleep(5)

    espera = True
    while espera:
        print("ESTOY ESPERANDO")
        espera = validaQR()
        time.sleep(2)
        if espera == False:
            print("SE AUTENTICO")
            break #rompe el bucle
    
    selectChat("Fakafakafakamadafacka")
    #enviarMensaje("HOLA")
    time.sleep(2)
    leerArchivo('./resource/pruebaBot.txt')

botWsp()

