from time import sleep
from selenium import webdriver
#from selenium.webdriver.support.ui import Select

LINK_ENTEL_FORM = "https://www.entel.cl/validaform/?id=rev_fact_home"
PATH = "C:\chromedriver.exe"
DEPTOS_POR_PISO = 4
DEPTO_INICIAL = 21
DEPTO_FINAL = 164

driver = webdriver.Chrome(PATH)
driver.get(LINK_ENTEL_FORM)

COMUNA = "LAS CONDES"
CALLE = "ESTRELLA DEL NORTE"
NMO = "980"
input_depto_gral = [i for i in range(DEPTO_INICIAL, DEPTO_FINAL)]

input_depto = []
for dep in input_depto_gral:
    if 0 < dep%10 <= DEPTOS_POR_PISO:
        input_depto.append(dep)


print("\n")
print("".center(100, "*"))
print(f"  DEPARTAMENTOS DE {CALLE} {NMO} SOLICITANDO ENTEL  ".center(100, "*"))
print("".center(100, "*"))
print("\n")
print("\n")
for dep in input_depto:
    sleep(3)
    comuna_input = driver.find_element_by_xpath('//*[@id="inputSelCom"]')
    calle_input = driver.find_element_by_xpath('//*[@id="selDir"]')
    numero_input = driver.find_element_by_xpath('//*[@id="selNum"]')
    depto_input = driver.find_element_by_xpath('//*[@id="depaCasa"]')
    boton_continuar = driver.find_element_by_xpath('//*[@id="buttonDireccion"]')
    try:
        comuna_input.send_keys(COMUNA)
        calle_input.click()
        sleep(1.5)
        calle_input.send_keys(CALLE)
        numero_input.click()
        sleep(1.5)
        numero_input.send_keys(NMO)
        depto_input.click()
        sleep(3)
        depto_input.send_keys(dep)
        boton_continuar.click()
        sleep(5)
        print(f"DEPARTAMENTO {dep}:  SOLICITADO")
        boton_volver = driver.find_element_by_xpath('//*[@id="volverFacti"]')
        boton_volver.click()

    except:
        print(f"Hubo un error con el depto {dep}")

driver.quit()