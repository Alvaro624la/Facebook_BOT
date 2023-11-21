from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time 
# alternativa para el módulo time: 'from time import sleep' y luego usar solo 'sleep()' o solo 'localtime()'

### CREDENCIALES:
try:
    user_email = ''
    user_password = ''

    def ask_user_email():
        # Indicamos que va a trabajar sobre la variable global y evitar crear una local en esta función
        global user_email

        ################################################################################################################################
        ########################################## OMITIR INTRODUZCION MANUAL DE CREDENCIALES ##########################################
        ############################################ Introduce aquí de forma fija tu email  ############################################

        # user_email = ''

        ################################ Si no quieres omitir, descomenta la siguiente parte de código ################################

        user_email = input('Introduce tu email de Facebook: ')
        ask_if_secure_email = input('¿Estas seguro de que está correctamente escrito? (s/n): ')
        if ask_if_secure_email.lower() not in ['y', 'yes', 's', 'si'] : ask_user_email()

        ################################################################################################################################


    def ask_user_password():
        # Indicamos que va a trabajar sobre la variable global y evitar crear una local en esta función
        global user_password

        ################################################################################################################################
        ########################################## OMITIR INTRODUZCION MANUAL DE CREDENCIALES ##########################################
        ########################################## Introduce aquí de forma fija tu contraseña ##########################################

        # user_password = ''

        ################################ Si no quieres omitir, descomenta la siguiente parte de código  ################################

        user_password = input('Ahora introduce tu contraseña de Facebook: ')
        ask_if_secure_pass = input('¿La contraseña también está correctamente escrita? (s/n): ')
        if ask_if_secure_pass.lower() not in ['y', 'yes', 's', 'si'] : ask_user_password()

        ################################################################################################################################

    ask_user_email()
    ask_user_password()
    
except Exception as err:
    print(f'Error de tipo "{type(err).__name__}" al intentar obtener el email y contraseña de Facebook del usuario mediante preguntas --> {err}')

### DRIVER CONFIG:
# Configurar las opciones del navegador para desactivar las notificaciones de forma predeterminada
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

driver_path = './chromedriver-win64/chromedriver.exe'

# se crea una instancia del webdrive chrome
driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

# abrimos la url y se espera a que esté completamente cargada con el metodo get de driver
driver.get("https://www.facebook.com/")

### VERIFICACION TITULO PAGINA:
try:
    # verificamos si el titulo de la página del driver es Facebook. Si no es, lanza error.
    assert "Facebook" in driver.title
except AssertionError as err:
    print(f'Error de tipo AssertionError. El título de la página no coincide con la página cargada --> {err}\n\nCerrando en 5 segundos')
    time.sleep(5)
    driver.close()

### COOKIES:
# Apaño temporal para que cargue bien la ventana de cookies y no ejecute el btn_cookies antes de tiempo causando un error ----------------------------------------------
time.sleep(1) #---------------------------------------------------------------------------------------------------------------------------------------------------------
# detectamos si existe un boton de cookies, y las rechazamos. Si este no existe, seguimos
btn_cookies = driver.find_element(By.XPATH, '//button[@title="Rechazar cookies opcionales"]')
if btn_cookies:
    print('Rechazando cookies opcionales')
    btn_cookies.click()
else:
    print('Configuración de cookies ya definida. Continuando...')

### INICIAR SESION
intentos_inicio_sesion = 0
def facebook_login():
    global intentos_inicio_sesion
    if intentos_inicio_sesion >= 3:
        print(f'Has intentado iniciar sesion {intentos_inicio_sesion} veces.\nExiste algún problema externo a este BOT de Facebook que impide iniciar sesion correctamente.\nCompruebe el error que le muestra la página de Facebook e intente arreglarlo para volver a intentar entrar. Cerrando en 15 segundos')
        time.sleep(15)
        driver.close()
    try:
        usuario_inicio_sesion = driver.find_element(By.ID, "email")
        usuario_inicio_sesion.clear()
        usuario_inicio_sesion.send_keys(user_email)
        contraseña_inicio_sesion = driver.find_element(By.ID, "pass")
        contraseña_inicio_sesion.clear()
        contraseña_inicio_sesion.send_keys(user_password)
        btn_inicio_sesion = driver.find_element(By.XPATH, "//button[@name='login']")
        btn_inicio_sesion.click()
        print('Iniciando sesión...')
        intentos_inicio_sesion += 1
    except:
        # Sesion ya iniciada, porque no encuentra los campos de inicio de sesion email, pass y login
        print('Iniciando sesión...')

    # Comprobación del correcto iniciado sesión (usando try except de manera inversa)
    try:            
        try:
            # Localizamos y clicamos en btn: ¿Has olvidado la contraseña?
            btn_olvidado_contraseña = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, '_97w4')))
            btn_olvidado_contraseña.click()
            ask_user_password()
            driver.find_element(By.ID, "pass").clear()
            driver.find_element(By.ID, "pass").send_keys(user_password)
            driver.find_element(By.XPATH, "//button[@name='login']").click()
        except:
            # Detectar algún mensaje de error en el inicio de sesión
            WebDriverWait(driver, 0).until(EC.presence_of_element_located((By.CLASS_NAME, '_9ay7')))
            print('Error al iniciar sesión. Introduzca los credenciales de nuevo.')
            ask_user_email()
            ask_user_password()
            facebook_login()
    except:
        # Localizar el boton de grupos de Facebook. Significa que hemos iniciado sesión con éxito.
        WebDriverWait(driver, 0).until(EC.presence_of_element_located((By.XPATH, '//a[@aria-label="Grupos" or @aria-label="Groups" or @href="https://www.facebook.com/groups/?ref=bookmarks"]')))

facebook_login()
print('Sesión iniciada con éxito')

### IR A TUS GRUPOS
try:
    # busco el enlace a grupos y le doy click
    btn_grupos = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@aria-label="Grupos" or @aria-label="Groups" or @href="https://www.facebook.com/groups/?ref=bookmarks"]')))
    print('Dirigiendome a grupos')
    btn_grupos.click()
except Exception as err:
    print(f'Error de tipo "{type(err).__name__}" al buscar el enlace a grupos --> {err}')
    print('Yendo a grupos través de URL específica .../groups/feed/')
    driver.get("https://www.facebook.com/groups/feed/")

#########################################################################################
################################ OBTENER LINKS DE GRUPOS ################################

# Encontrar todos los enlaces de grupos en la url actual
all_links = driver.find_elements(By.XPATH, '//a')
# Declaramos la variable donde definiremos el array de tipo set que usaremos para almacenar todos los links que sean de grupos
arr_links_grupos_obtenidos = set([])

print('Buscando grupos')
for i in range(len(all_links)):
    link = all_links[i]
    link_regex = re.search(r"https://www.facebook.com/groups/\d+", link.get_attribute("href"))
    try:
        if link_regex : arr_links_grupos_obtenidos.add(link_regex.group())
    except Exception as err:
        print(f'Ha habido un error de tipo "{type(err).__name__}" obteniendo los links de los grupos --> {err}')

print(f'{"-"*30}\nEnlaces obtenidos: {len(arr_links_grupos_obtenidos)} enlaces de grupo')
print(arr_links_grupos_obtenidos)

################################ OBTENER LINKS DE GRUPOS ################################
#########################################################################################

# Variables de fecha. Siempre pueden ser útiles.
actual_year = time.localtime().tm_year
actual_month = time.localtime().tm_mon
actual_day = time.localtime().tm_mday
actual_hour = time.localtime().tm_hour
actual_min = time.localtime().tm_min
actual_sec = time.localtime().tm_sec

# Porcentaje de completado del script entero. Regla de tres calculando todos los links como el 100%.
porcentaje_completado = 0
porcentaje_unico_link = (1 * 100) / len(arr_links_grupos_obtenidos)
def informe_porcenataje_completado():
    # /3 porque son 3 los procesos para publicar: abrir cuadro/escribir/btn publicar, y quiero que en cada uno informe del porcentaje
    global porcentaje_completado 
    porcentaje_completado += porcentaje_unico_link/3
    print(f'{int(round(porcentaje_completado, 0))}% completado')

######################################################################################################
################################# EL USUARIO ESCRIBE EL POST DESEADO #################################

# Avisar al usuario de escribir el post por consola
info_to_user_message = "Por favor, escribe el post en la consola/terminal abierta del principio"
info_to_user_div = f"var mensaje = document.createElement('div'); mensaje.textContent = '{info_to_user_message}'; mensaje.style.cssText = 'font-size: 1.2em; position: fixed; top: 15px; left: 15px; padding: 20px; background-color: yellow; border-radius: 5px; z-index: 9999'; document.body.appendChild(mensaje);"
driver.execute_script(info_to_user_div)

def crear_post():
    print("Escribe aquí tu post línea por línea (presiona Enter dos veces para terminar):\n")
    lineas = []
    while True:
        linea = input()
        # Si en linea hay contenido, es True. Si es "", es False y termina el bucle
        if linea:
            lineas.append(linea)
        else:
            break
    post = "\n".join(lineas)
    
    # El usuario revisa su post y confirma para proceder a compartir, si no, vuelve a escribir el post de nuevo
    print("\nTu post será el siguiente:")
    print(post)
    ask_if_secure_post = input('Estas seguro de querer publicarlo en todos los grupos (s/n): ')
    if ask_if_secure_post.lower() not in ['y', 'yes', 's', 'si'] : crear_post()

    return post

contenido_publicacion = crear_post()


################################# EL USUARIO ESCRIBE EL POST DESEADO #################################
######################################################################################################

##########################################################################################
################################# ABRIR LINKS Y PUBLICAR #################################

# Manejo la alerta que a veces aparece inesperadamente durante la ejecución del script y está fuera de nuestro control.
def dismiss_alert():
    try:
        alert = driver.switch_to.alert
        alert.dismiss()  # O bien alert.accept() para rechazarla
        print("Alerta manejada")
    except:
        print("No se encontró ninguna alerta. Continuando...")

# Recorremos el array con todos los links de grupos y publicamos en cada uno
for link in arr_links_grupos_obtenidos:
    
    dismiss_alert()
    try:
        driver.get(link)
        # Espera a que cargue el escribe algo box y localizamos el elemento para clicarlo posteriormente
        # (Creamos una tupla para que el webdriverwait espere a que el elemento se localize (max 10s). * la tupla hace de unico argumento para el EC)
        escribe_algo_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Escribe algo")]')))
        escribe_algo_box.click()
        # Informar del porcentage completado del script total
        informe_porcenataje_completado()
    except Exception as err:
        print(f'Error 1 de tipo {type(err).__name__} - Encontrar cuadro de dialogo para escribir --> {err}')
    
    dismiss_alert()
    try:
        # (Creamos una tupla para que el webdriverwait espere a que el elemento se localize (max 10s). * la tupla hace de unico argumento para el EC)
        crea_una_publicacion_publica = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "_1mf") and contains(@class, "_1mj")]')))
        crea_una_publicacion_publica.send_keys(contenido_publicacion)
        try:
            # Si sale un cuadro de texto sobre "Información adicional sobre este contenido" le damos a "Compartir de todas formas"
            popup_adicional_al_pegar_link = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Compartir de todas formas"]')))
            popup_adicional_al_pegar_link.click()
        except:
            print('No ha aparecido ningún problema con agregar el link en la publicación. Continuando...')
        # Tiempo de espera para que la miniatura del posible link de la publicación se cargue correctamente (tiempo de espera estimado, a ojimetro)
        time.sleep(2)
        # Informar del porcentage completado del script total
        informe_porcenataje_completado()
    except Exception as err:
        print(f'Error 2 de tipo {type(err).__name__} - Escribir en el recuadro --> {err}')

    dismiss_alert()
    try:
        # (Creamos una tupla para que el webdriverwait espere a que el elemento se localize (max 10s). * la tupla hace de unico argumento para el EC)
        btn_publicar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Publicar"]')))
        btn_publicar.click()
        # Informar del porcentage completado del script total
        informe_porcenataje_completado()
    except Exception as err:
        print(f'Error 3 de tipo {type(err).__name__} - Click en el boton Publicar --> {err}')
        
    # Esperar a que el boton de Publicar desaparezca
    btn_publicar = WebDriverWait(driver, 10).until_not(EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Publicar"]')))
    
    #Se vuelve a ejecutar el bucle for, hasta que no queden mas links en el arr 

################################# ABRIR LINKS Y PUBLICAR #################################
##########################################################################################

print('Contenido publicado en todos los grupos')

print(f'Cerrando en 10 segundos.\n{"-"*30}\nAlvaro624la te agradece haber utilizado su herramienta y espera que te haya sido útil ;D')
print("                       _            ")
print("                      (_)           ")
print("   __ _ _ __ __ _  ___ _  __ _ ___  ")
print("  / _` | '__/ _` |/ __| |/ _` / __| ")
print(" | (_| | | | (_| | (__| | (_| \__ \ ")
print("  \__, |_|  \__,_|\___|_|\__,_|___/ ")
print("   __/ |                            ")
print("  |___/   ")
time.sleep(10)
driver.close()