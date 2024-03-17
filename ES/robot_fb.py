from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time 
# alternativa para el módulo time: 'from time import sleep' y luego usar solo 'sleep()' o solo 'localtime()'

# DRIVER MANAGER https://github.com/SergeyPirogov/webdriver_manager?tab=readme-ov-file#use-with-chrome 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# MODULOS PROPIOS
from locators import LocatorsClass as loc
from pop_ups import PopUpsClass as pop_up


### CREDENCIALES:
# def ask_user_email(user_email=None):
#     try:
#         # Si el usuario ha introducido el user_email, devuelvelo. Si no, preguntale.
#         if user_email:
#             return user_email
#         else:
#             user_email = input('Introduce tu email de Facebook: ')
#             ask_if_secure_email = input('¿Estas seguro de que está correctamente escrito? (s/n): ')
#             if ask_if_secure_email.lower() not in ['y', 'yes', 's', 'si']:
#                 ask_user_email()
#             else:
#                 return user_email
#     except Exception as err:
#         print(f'Error de tipo "{type(err).__name__}" al intentar obtener el email de Facebook del usuario mediante preguntas --> {err}')

# def ask_user_password(user_password=None):
#     try:
#         # Si el usuario ha introducido el user_password, devuelvelo. Si no, preguntale.
#         if user_password:
#             return user_password
#         else:
#             user_password = input('Ahora introduce tu contraseña de Facebook: ')
#             ask_if_secure_pass = input('¿La contraseña también está correctamente escrita? (s/n): ')
#             if ask_if_secure_pass.lower() not in ['y', 'yes', 's', 'si']:
#                 ask_user_password()
#             else:
#                 return user_password
#     except Exception as err:
#         print(f'Error de tipo "{type(err).__name__}" al intentar obtener la contraseña de Facebook del usuario mediante preguntas --> {err}')

def ask_credentials(user_email=None, user_password=None):
    try:
        if user_email and user_password:
            return user_email, user_password
        else:
            # Ventana emergente para que el cliente introduzca los credenciales
            info_to_user_message = "Por favor, introduzca los credenciales para que el BOT pueda operar y ver sus grupos"
            info_to_user_div = pop_up.CREDENTIALS(info_to_user_message)
            driver.execute_script(info_to_user_div)

            html_oculto_credenciales_introducidos = driver.find_element(By.ID, "credenciales_introducidos")
            while html_oculto_credenciales_introducidos.get_attribute("innerHTML") != 'True':
                time.sleep(1)
                print('Esperando para obtener las credenciales...')

            html_input_user_email = driver.find_element(By.ID, "credentials_name_input")
            html_input_user_password = driver.find_element(By.ID, "credentials_password_input")
            user_email = html_input_user_email.get_attribute("value")
            user_password = html_input_user_password.get_attribute("value")
            return user_email, user_password
    except Exception as err:
        print(f'Error de tipo "{type(err).__name__}" al intentar obtener el email y la contraseña de Facebook del usuario mediante preguntas --> {err}')


### DRIVER CONFIG:
# Configurar las opciones del navegador para desactivar las notificaciones de forma predeterminada
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
# se crea una instancia del webdrive chrome
# driver_path = './chromedriver-win64/chromedriver.exe'
# driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

def open_url_after_driver_config():
    # abrimos la url y se espera a que esté completamente cargada con el metodo get de driver
    driver.get("https://www.facebook.com/")

### VERIFICACION TITULO PAGINA:
def verify_page_title():
    try:
        # tiempo manual preventivo para que no lance el error assert cuando aún no ha cargado la página ni el title
        time.sleep(1)
        # verificamos si el titulo de la página del driver es Facebook. Si no es, lanza error.
        assert "Facebook" in driver.title
    except AssertionError as err:
        print(f'Error de tipo AssertionError. El título de la página no coincide con la página cargada --> {err}\n\nCerrando en 5 segundos')
        time.sleep(5)
        driver.close()

### COOKIES:
def cookies():
    # detectamos si existe un boton de cookies, y las rechazamos. Si este no existe, seguimos
    # Usar *loc.COOKIES permite desempaquetar la tupla
    # if(driver.find_element(*loc.COOKIES_ES)):
    #     btn_cookies = driver.find_element(*loc.COOKIES_ES)
    # if(driver.find_element(*loc.COOKIES_CA)):
    #     btn_cookies = driver.find_element(*loc.COOKIES_CA)
    # if(driver.find_element(*loc.COOKIES_EN)):
    #     btn_cookies = driver.find_element(*loc.COOKIES_EN)
    try:
        btn_cookies = WebDriverWait(driver, 1).until(EC.presence_of_element_located((loc.COOKIES_ES)))
        btn_cookies.click()
        print('Rechazando cookies opcionales')
    except Exception:
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
        usuario_inicio_sesion = driver.find_element(*loc.LOGIN_EMAIL)
        usuario_inicio_sesion.clear()
        usuario_inicio_sesion.send_keys(user_email)
        contraseña_inicio_sesion = driver.find_element(*loc.LOGIN_PASS)
        contraseña_inicio_sesion.clear()
        contraseña_inicio_sesion.send_keys(user_password)
        btn_inicio_sesion = driver.find_element(*loc.LOGIN_BTN)
        btn_inicio_sesion.click()
        print('Iniciando sesión...')
        intentos_inicio_sesion += 1
    except:
        # Sesion ya iniciada, porque no encuentra los campos de inicio de sesion email, pass y login
        print('Iniciando sesión...')

    # Comprobación del correcto iniciado sesión (usando try except de manera inversa)
    # try:            
        # try:
            # Localizamos y clicamos en btn: ¿Has olvidado la contraseña?
            # btn_olvidado_contraseña = WebDriverWait(driver, 5).until(EC.presence_of_element_located(loc.LOGIN_FORGOTTEN_PASS_LINK))
            # btn_olvidado_contraseña.click()
            # ask_user_password()
            # driver.find_element(By.ID, "pass").clear()
            # driver.find_element(By.ID, "pass").send_keys(user_password)
            # driver.find_element(By.XPATH, "//button[@name='login']").click()
        # except:
        # Detectar algún mensaje de error en el inicio de sesión
        
        # try:
        #     WebDriverWait(driver, 0).until(EC.presence_of_element_located(loc.LOGIN_ERR_MSG_1))
            
        #     # html_input_user_email = driver.find_element(By.ID, "credentials_name_input")
        #     # html_input_user_password = driver.find_element(By.ID, "credentials_password_input")
        #     # html_input_user_email.clear()
        #     # html_input_user_password.clear()
        #     # driver.execute_script("arguments[0].value = ''", html_input_user_email)
        #     # driver.execute_script("arguments[0].value = ''", html_input_user_password)
        #     driver.execute_script('document.getElementById("credentials_name_input").value = "";')
        #     driver.execute_script('document.getElementById("credentials_password_input").value = "";')
            
        #     info_to_user_message = "Error al iniciar sesión. Introduzca correctamente los credenciales de nuevo."
        #     info_to_user_div = pop_up.QUICK_MESSAGE(info_to_user_message)
        #     driver.execute_script(info_to_user_div)

        #     driver.get("https://www.facebook.com/")
        #     ask_credentials()
        #     facebook_login()
        # except:
        #     WebDriverWait(driver, 0).until(EC.presence_of_element_located(loc.LOGIN_ERR_MSG_2))

        #     # html_input_user_email = driver.find_element(By.ID, "credentials_name_input")
        #     # html_input_user_password = driver.find_element(By.ID, "credentials_password_input")
        #     # html_input_user_email.clear()
        #     # html_input_user_password.clear()
        #     # driver.execute_script("arguments[0].value = ''", html_input_user_email)
        #     # driver.execute_script("arguments[0].value = ''", html_input_user_password)
        #     driver.execute_script('document.getElementById("credentials_name_input").value = "";')
        #     driver.execute_script('document.getElementById("credentials_password_input").value = "";')
            
        #     info_to_user_message = "Error al iniciar sesión. Introduzca correctamente los credenciales de nuevo."
        #     info_to_user_div = pop_up.QUICK_MESSAGE(info_to_user_message)
        #     driver.execute_script(info_to_user_div)

        #     driver.get("https://www.facebook.com/")
        #     ask_credentials()
        #     facebook_login()
    # except:
    # Localizar el boton de grupos de Facebook. Significa que hemos iniciado sesión con éxito.
    # info_to_user_message = "Siga los pasos para iniciar sesión por completo"
    info_to_user_message = "Error al iniciar sesión. Siga los pasos que Facebook le marca, para iniciar sesión por completo"
    info_to_user_div = pop_up.QUICK_MESSAGE(info_to_user_message)
    driver.execute_script(info_to_user_div)
    # pongo 999 de espera por si la cuenta tiene verificacion en dos pasos con el movil para dar tiempo a completarla y entrar en facebook, y seguir el proceso
    WebDriverWait(driver, 999).until(EC.presence_of_element_located(loc.GROUPS_BTN))


### IR A TUS GRUPOS
def ir_a_grupos():
    print('Sesión iniciada con éxito')
    try:
        # busco el enlace a grupos y le doy click
        btn_grupos = WebDriverWait(driver, 10).until(EC.presence_of_element_located(loc.GROUPS_BTN))
        print('Dirigiendome a grupos')
        btn_grupos.click()
    except Exception as err:
        # print(f'Error de tipo "{type(err).__name__}" al buscar el enlace a grupos --> {err}')
        print('Yendo a grupos través de URL específica .../groups/feed/')
        driver.get("https://www.facebook.com/groups/feed/")

#########################################################################################
################################ OBTENER LINKS DE GRUPOS ################################

def obtener_obj_grupos():
    #########################################################################################
    ############# EN CASO DE NO ENTRAR EN BOTON GRUPOS > TUS GRUPOS: ########################

    # Encontrar todos los enlaces de grupos en la url actual, que no tengan el panel principal role"main" como elemento padre (para no obtener links de grupos sugeridos)
    # all_a_tags = driver.find_elements(By.XPATH, '//a[not(ancestor::div[@role="main"])]')

    #########################################################################################
    #################### ENTRAR EN BOTON GRUPOS > TUS GRUPOS: ###############################
    driver.get("https://www.facebook.com/groups/joins/?nav_source=tab&ordering=viewer_added")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@role="main"]')))

    arr_obj_grupos_obtenidos = []
    
    # bajar pagina hasta abajo para cargar todos los grupos 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Esperar un momento para que la página cargue completamente
    time.sleep(3)
    # bajar página de nuevo por si acaso
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # dentro de --> 
    panel_central = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@role="main" and @aria-label="Preview of a group"]')))
    print('panel central: ')
    print(panel_central)
    # de cada padre --> role="listitem": 
    list_item = panel_central.find_elements(By.XPATH, '//div[@role="listitem"]') # por si sirve, también tiene --> style="max-width: 600px; min-width: 320px;"
    print('COMP0: list_item length: ')
    print(len(list_item))
    array_existe_link = []
    grupo_index = -1
    for grupo in list_item:
        try:
            # el tag --> 
            a_tag = WebDriverWait(grupo, 0).until(EC.presence_of_element_located((By.TAG_NAME, 'a')))
            # el link dentro del tag-->
            link_regex = re.search(r"https://www.facebook.com/groups/\d+", a_tag.get_attribute("href"))
            link = link_regex.group()

            if link not in array_existe_link:
                # añadelo para la siguiente comprobación
                array_existe_link.append(link)

                grupo_index += 1
                # la img --> 
                img_tag = WebDriverWait(grupo, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'image')))
                img_url = img_tag.get_attribute("xlink:href")

                # el titulo --> 
                title_tag = WebDriverWait(grupo, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'svg')))
                title = title_tag.get_attribute("aria-label")

                # crea un nuevo obj
                new_obj = {
                    'index': 0,
                    'link': '',
                    'img_url': '',
                    'title': ''
                }
                # asigna valores al obj
                new_obj['index'] = grupo_index
                new_obj['link'] = link
                new_obj['img_url'] = img_url
                new_obj['title'] = title
                arr_obj_grupos_obtenidos.append(new_obj)

                # print('arr_obj_grupos_obtenidos-------------------------------------------------------------------------------------')
                # print(len(arr_obj_grupos_obtenidos))
                print('Obtención de links: grupo obtenido')
        except Exception as err:
            print('Obtención de links: procesando...')

            # print('a_tag: ')
            # print(err)
        print('Obtención de links: link ya existente')
    return arr_obj_grupos_obtenidos

def js_function():
    # Elegir grupos donde publicar (internamente: agregar o quitar links de los grupos del array --> arr_links_grupos_obtenidos y agregarlos al arr final de links --> arr_links_grupos_seleccionados)
    # arr_obj_prueba = ['https://www.facebook.com/groups/740970037910764', 'https://www.facebook.com/groups/867005741560869']
    # arr_obj_grupos_obtenidos_ej = [{'index': 0, 'link': 'https://www.facebook.com/groups/1113068039716987', 'img_url': 'https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/429679221_2579686565547152_5684308905641758804_n.jpg?stp=cp0_dst-jpg_s110x80&_nc_cat=103&ccb=1-7&_nc_sid=aae68a&_nc_ohc=mgnzalFHSQkAX9lcfZY&_nc_ht=scontent-mad1-1.xx&oh=00_AfDGcA6adJsCdZYMLOWO1fj5DIH7wZhnJA0_6woVj8y7nw&oe=65E94F31', 'title': 'pruebas alvaro 2'}, {'index': 1, 'link': 'https://www.facebook.com/groups/1478094899435458', 'img_url': 'https://scontent-mad2-1.xx.fbcdn.net/v/t1.30497-1/116687302_959241714549285_318408173653384421_n.jpg?stp=cp0_dst-jpg_p80x80&_nc_cat=1&ccb=1-7&_nc_sid=b81613&_nc_ohc=2ZA3jlLB-iYAX_gXh1Q&_nc_oc=AQmPss0Bj9qLPTXOEf_xlBU06Lan9G2pSsnktKESv4wmTc1i7Yp8GrR7t96c5AEs_hg&_nc_ht=scontent-mad2-1.xx&oh=00_AfAlpVSjfQIW1VPlGtYTNG2SlvMsMGGHUlrKFr0bF2EQpg&oe=6602DC03', 'title': 'Pruebas alvaro'}, {'index': 2, 'link': 'https://www.facebook.com/groups/867005741560869', 'img_url': 'https://scontent-mad2-1.xx.fbcdn.net/v/t1.30497-1/116687302_959241714549285_318408173653384421_n.jpg?stp=cp0_dst-jpg_p80x80&_nc_cat=1&ccb=1-7&_nc_sid=b81613&_nc_ohc=2ZA3jlLB-iYAX_gXh1Q&_nc_oc=AQmPss0Bj9qLPTXOEf_xlBU06Lan9G2pSsnktKESv4wmTc1i7Yp8GrR7t96c5AEs_hg&_nc_ht=scontent-mad2-1.xx&oh=00_AfAlpVSjfQIW1VPlGtYTNG2SlvMsMGGHUlrKFr0bF2EQpg&oe=6602DC03', 'title': 'pruebas 2'}, {'index': 3, 'link': 'https://www.facebook.com/groups/740970037910764', 'img_url': 'https://scontent-mad2-1.xx.fbcdn.net/v/t1.30497-1/116687302_959241714549285_318408173653384421_n.jpg?stp=cp0_dst-jpg_p80x80&_nc_cat=1&ccb=1-7&_nc_sid=b81613&_nc_ohc=2ZA3jlLB-iYAX_gXh1Q&_nc_oc=AQmPss0Bj9qLPTXOEf_xlBU06Lan9G2pSsnktKESv4wmTc1i7Yp8GrR7t96c5AEs_hg&_nc_ht=scontent-mad2-1.xx&oh=00_AfAlpVSjfQIW1VPlGtYTNG2SlvMsMGGHUlrKFr0bF2EQpg&oe=6602DC03', 'title': 'pruebas 1'}]
    info_to_user_message = "Por favor, selecciona los grupos donde deseas compartir"
    info_to_user_div = pop_up.GROUP_SELECTION(info_to_user_message, arr_obj_grupos_obtenidos)
    driver.execute_script(info_to_user_div)

def esperar_hasta_cliente_selecciona_grupos():
    div_ids_oc_sel = driver.find_element(By.ID, "ids_ocultos_seleccionados")
    while div_ids_oc_sel.get_attribute("innerHTML") != 'True':
        time.sleep(1)
        print('Esperando a aceptar la selección de grupos donde compartir...')

def finds_links_with_ids_ocultos_arr():
    ids_ocultos = driver.find_element(By.ID, "ids_ocultos")
    ids_ocultos_innerHTML = ids_ocultos.get_attribute("innerHTML")
    arr_indices_ocultos_seleccionados = ids_ocultos_innerHTML.split(',')
    arr_final_links = []

    for indice_oculto in arr_indices_ocultos_seleccionados:
        try:
            # Convertimos el índice a entero para usarlo como índice en arr_obj_grupos_obtenidos
            indice_oculto = int(indice_oculto.strip())
            if arr_obj_grupos_obtenidos[indice_oculto]['link']:
                arr_final_links.append(arr_obj_grupos_obtenidos[indice_oculto]['link'])
        except Exception as err:
            print(f"Error al obtener el enlace del grupo con índice {indice_oculto}: {err}")

    print(arr_final_links)
    return arr_final_links
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
def informe_porcenataje_completado():
    porcentaje_unico_link = (1 * 100) / len(arr_links_grupos_obtenidos)
    # /3 porque son 3 los procesos para publicar: abrir cuadro/escribir/btn publicar, y quiero que en cada uno informe del porcentaje
    global porcentaje_completado 
    porcentaje_completado += porcentaje_unico_link/3
    print(f'{int(round(porcentaje_completado, 0))}% completado')

######################################################################################################
################################# EL USUARIO ESCRIBE EL POST DESEADO #################################

def crear_post():
    # Avisar al usuario de escribir el post por consola
    info_to_user_message = "Por favor, escribe el post en la consola/terminal abierta del principio"
    info_to_user_div = pop_up.QUICK_MESSAGE(info_to_user_message)
    driver.execute_script(info_to_user_div)

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
    
    if post.strip() == '':
        print('Error: Sin contenido. Por favor, escribe o introduce contenido para generar el post.')
        crear_post()
    else:
        # El usuario revisa su post y confirma para proceder a compartir, si no, vuelve a escribir el post de nuevo
        print("\nTu post será el siguiente:")
        print(post)
        ask_if_secure_post = input('Estas seguro de querer publicarlo en todos los grupos (s/n): ')
        if ask_if_secure_post.lower() not in ['y', 'yes', 's', 'si'] : crear_post()

        return post


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
def publicar_en_cada_grupo():
    for link in arr_links_grupos_obtenidos:
        
        dismiss_alert()
        try:
            driver.get(link)
            # Espera a que cargue el escribe algo box y localizamos el elemento para clicarlo posteriormente
            # (Creamos una tupla para que el webdriverwait espere a que el elemento se localize (max 10s). * la tupla hace de unico argumento para el EC)
            escribe_algo_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located(loc.GROUP_WRITE_STG_LINEBOX))
            escribe_algo_box.click()
            # Informar del porcentage completado del script total
            informe_porcenataje_completado()
        except Exception as err:
            print(f'Error 1 de tipo {type(err).__name__} - Encontrar cuadro de dialogo para escribir --> {err}')
        
        dismiss_alert()
        try:
            # (Creamos una tupla para que el webdriverwait espere a que el elemento se localize (max 10s). * la tupla hace de unico argumento para el EC)
            crea_una_publicacion_publica = WebDriverWait(driver, 10).until(EC.presence_of_element_located(loc.POST_WRITE_BOX))
            crea_una_publicacion_publica.send_keys(contenido_publicacion)
            try:
                # Si sale un cuadro de texto sobre "Información adicional sobre este contenido" le damos a "Compartir de todas formas"
                popup_adicional_al_pegar_link = WebDriverWait(driver, 3).until(EC.presence_of_element_located(loc.WARNING_LINK_POPUP))
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
            btn_publicar = WebDriverWait(driver, 10).until(EC.presence_of_element_located(loc.POST_BTN))
            btn_publicar.click()
            # Informar del porcentage completado del script total
            informe_porcenataje_completado()
        except Exception as err:
            print(f'Error 3 de tipo {type(err).__name__} - Click en el boton Publicar --> {err}')
            
        # Esperar a que el boton de Publicar desaparezca
        btn_publicar = WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(loc.POST_BTN))
        
        #Se vuelve a ejecutar el bucle for, hasta que no queden mas links en el arr --> arr_links_grupos_obtenidos

################################# ABRIR LINKS Y PUBLICAR #################################
##########################################################################################

def mensage_final_cerrar_bot():
    informe_porcenataje_completado()
    print('Contenido publicado en todos los grupos')

    print(f'Cerrando en 10 segundos.\n{"-"*30}\nAlvaro624la te agradece haber utilizado su herramienta y espera que te haya sido útil ;D')
    print(r"                       _            ")
    print(r"                      (_)           ")
    print(r"   __ _ _ __ __ _  ___ _  __ _ ___  ")
    print(r"  / _` | '__/ _` |/ __| |/ _` / __| ")
    print(r" | (_| | | | (_| | (__| | (_| \__ \ ")
    print(r"  \__, |_|  \__,_|\___|_|\__,_|___/ ")
    print(r"   __/ |                            ")
    print(r"  |___/   ")
    time.sleep(7)
    print('Cerrando en 3 segundos')
    time.sleep(1)
    print('Cerrando en 2 segundos')
    time.sleep(1)
    print('Cerrando en 1 segundo')
    time.sleep(1)
    driver.close()


############################################################################
################################# FUNCIONES ################################
############################################################################
# CONFIG
open_url_after_driver_config()
verify_page_title()
cookies()
# INICIO SESIÓN
###################### Iniciar sesión automáticamente ######################
# Para iniciar sesión automáticamente, puedes añadir tus datos entre comillas (simples o dobles) separadas por una coma, así: 
# -->> user_email, user_password = ask_credentials('aquí_tu_email', 'aquí_tu_contraseña') <<--
# aquí debajo:
user_email, user_password = ask_credentials()
############################################################################
facebook_login()
# SELECCIÓN GRUPOS 
ir_a_grupos()
arr_obj_grupos_obtenidos = obtener_obj_grupos()
js_function()
esperar_hasta_cliente_selecciona_grupos()
# CREAR POST
contenido_publicacion = crear_post()
# PUBLICAR
arr_links_grupos_obtenidos = finds_links_with_ids_ocultos_arr()
publicar_en_cada_grupo()
# AGRADECIMIENTOS Y CERRAR
mensage_final_cerrar_bot()