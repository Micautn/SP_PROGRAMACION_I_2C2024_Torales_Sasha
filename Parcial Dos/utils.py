def my_filter(lista: list, func):
    aux = lista.copy()
    lista_aux = []
    for elemento in aux:
        if func(elemento) == True:
            lista_aux.append(elemento)
    return lista_aux

def my_reduce(lista: list, func):
    aux = lista.copy()
    variable = aux[0]
    for i in range(1,len(lista)):
        variable = func(variable, aux[i])
    return variable

def burbujeo2(lista, funcion):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if funcion(lista[j], lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def mymap(lista:list, funcion):
    # Creamos una lista vacía para almacenar los resultados
    aux = lista.copy()
    resultado = []
    
    # Iteramos sobre cada elemento en la lista original
    for elemento in aux:
        # Aplicamos la función al elemento actual y añadimos el resultado a la lista de resultados
        resultado.append(funcion(elemento))
    
    # Devolvemos la lista de resultados
    return resultado

def leer_txt(path, modo='r'):
    try:
        with open(path, modo) as file:
            contenido = file.read()
        return contenido
    except Exception as e:
        print(f"Error al leer el archivo TXT: {e}")
        return None

def escribir_txt(path, modo='w', data=''):                       #path: La ruta del archivo en el que se desea escribir.
#modo: El modo en el que se abrirá el archivo ( es 'w', que significa escribir)  #data: Los datos que se escribirán en el archivo.       #try-except: Maneja cualquier excepción que pueda ocurrir al intentar escribir en el archivo.
    try:
        with open(path, modo) as file:
            file.write(data)
    except Exception as e:
        print(f"Error al escribir en el archivo TXT: {e}")

def leer_json(path, modo='r'):
    try:
        with open(path, modo) as file:
            contenido = json.load(file)
        return contenido
    except Exception as e:
        print(f"Error al leer el archivo JSON: {e}")
        return None
def escribir_json(path, modo='w', data=None):
    try:
        with open(path, modo) as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error al escribir en el archivo JSON: {e}")
def ingreso_float_rango(mensaje, msj_error, min, max, reintentos)->float|None:
    intentos = 0
    while intentos < reintentos:
        try:
            valor = float(input(mensaje))
            if min <= valor <= max:
                return valor
            else:
                print(msj_error)
        except ValueError:
            print(msj_error)
        intentos += 1
    print("Número máximo de reintentos excedido.")
    return None
VALOR_OK = 0
CAD_NO_VALIDA = -1
CAD_FUERA_DE_RANGO = -2

def get_int(msj:str, msj_error: str, min: int, max:int, reintentos: int | None = None) -> int | None:
    
    while reintentos is None or reintentos > 0 or reintentos == -1:
        try:
            aux_str = input(msj)
            if aux_str == '':
                print(msj_error)
                if reintentos is not None and reintentos != -1:
                    reintentos -= 1
                continue

            aux = int(aux_str)
            if min <= aux <= max:
                return aux
            else:
                print(msj_error)
                if reintentos is not None and reintentos != -1:
                    reintentos -= 1
        except ValueError:
            print(msj_error)
            if reintentos is not None and reintentos != -1:
                reintentos -= 1

    return None

def get_solo_string_rango2(mensaje: str, mensaje_error: str, min_len: int, max_len: int, max_espacios: int, max_intentos: int | None = None):
    intentos = max_intentos
    while intentos is None or intentos > 0:
        entrada = input(mensaje)
        palabras = entrada.split()
        if min_len <= len(entrada) <= max_len and len(palabras) <= max_espacios + 1:
            if all(len(palabra) > 0 for palabra in palabras):
                return entrada
        print(mensaje_error)
        if intentos is not None:
            intentos -= 1
    return False
def get_solo_string_rango(msj: str, msj_error :str,min: int, max: int, reintentos:int) -> str | int:
    
    while reintentos > 0:
        aux = input(msj)
        res = validar_solo_alfabeticos(aux, min, max)

        if res == VALOR_OK:
            return aux
        else:
            reintentos -= 1
            print(msj_error)
            if reintentos > 0:
                print(f"Intentos Restantes: {reintentos}")

    return None
def validar_solo_alfabeticos(cad: str, min: int, max: int) -> int:
    rtn = CAD_NO_VALIDA
    if cad.isalpha() == True:
        if len(cad) >= min and len(cad) < max:
            rtn = VALOR_OK
        else:
            rtn = CAD_FUERA_DE_RANGO
        
    return rtn
    
def desea_continuar(msj):
    opcion = input(msj)
    return True if (opcion == 'S' or opcion == 's') else False

def encontrar_max_num(num_uno: int, num_dos:int , num_tres:int)->int:
    if num_uno > num_dos and num_uno > num_tres:
        max_num = num_uno
    elif num_dos > num_tres:
        max_num = num_dos
    else:
        max_num = num_uno 
    return max_num
def get_str_rango_alfanumericos(msj, msjerror, minimo, maximo, reintentos)->str | None:
    """
    Solicita una cadena alfanumérica dentro de un rango especificado de longitud, 
    con un número limitado de reintentos en caso de error.
    
    Parámetros:
    msj (str): Mensaje que se muestra al usuario solicitando la entrada.
    msjerror (str): Mensaje que se muestra al usuario en caso de error.
    minimo (int): Longitud mínima de la cadena alfanumérica.
    maximo (int): Longitud máxima de la cadena alfanumérica.
    reintentos (int): Número de reintentos permitidos en caso de error.
    
    Retorna:
    str: Cadena alfanumérica válida ingresada por el usuario.
    """
    intentos = 0
    
    while intentos < reintentos:
        cadena = input(msj)
        
        if cadena.isalnum() and minimo <= len(cadena) <= maximo:
            return cadena
        else:
            print(msjerror)
            intentos += 1
    
    print("Número máximo de reintentos alcanzado. Entrada no válida.")
    return None

#pide un nro y lo devuelve en el print

def get_int_rango(mensaje:str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    
    while reintentos > 0:
        try:
            numero_ingresado = int(input(mensaje))
            
            if minimo <= numero_ingresado <= maximo:
                return numero_ingresado
            else:
                print(mensaje_error)
        except ValueError:
            print(mensaje_error)
        
        reintentos -= 1
        print(f"Intentos Restantes: {reintentos}")
    
    return None

def resta(numero_uno:int, numero_dos:int)->int:
    resultado = numero_uno - numero_dos
    return resultado

def suma(numero_uno:int, numero_dos:int)->int:
    resultado = numero_uno + numero_dos
        
    return resultado
def menu(opciones:list,mensaje:str):
    while True:
        print(mensaje)
        for i, opcion in enumerate(opciones, start=1):
            print(f'[{i}] {opcion}')
        print('[X] Para salir')
        opcion = input('[OPCION]: ').strip().upper()
        if opcion == 'X':
            return -1  # Indicar salida del menú
        elif opcion.isdigit():
            num_opcion = int(opcion)
            if 1 <= num_opcion <= len(opciones):
                return num_opcion
            else:
                print('ERROR - Ingresar una opción válida.')
        else:
            print('ERROR - Ingresar una opción numérica.')
def meniu(opc: list, msj:str)-> int:
    i = 0
    print(msj)
    while i < len(opc):
        print (f'[{i+1}] {opc[i]}')
        i +=1
    
    print('\n[X] Para salir')
    opcion = input('[OPCION]:')
    while True:
        if opcion.isdigit() == False or opcion == 'X' or opcion == 'x':
            opcion = input('ERROR - Ingresar una opción numerica: ').upper()
        else:
            a = int(opcion)
            if a <= len(opc):
                return a
            else:
                a = input('Ingresar opción numérica válida!!!!: ')

def busqueda_lineal(lista:list, elemento_a_buscar:int,)->int:
    for i in range(len(lista)):
        if lista[i] == elemento_a_buscar:
            return i
    return None


def busqueda_binaria(lista:list, elemento_a_buscar)->int:
    indice_minimo = 0
    indice_maximo = len(lista) -1

    while indice_minimo <= indice_maximo:
      medio = (indice_maximo + indice_minimo) //2

    if lista[medio] == elemento_a_buscar:
        return lista
    else:
        if lista[medio] < elemento_a_buscar:
            indice_minimo = medio +1
        else:
            indice_maximo = medio -1
    return None

def burbujeo(lista: list, funcion):
    lista_aux = lista.copy()
    aux = ''
    for i in range(len(lista_aux) - 1):
        for j in range(i + 1, len(lista_aux)):
            if funcion(lista_aux[i] > lista_aux[j]) == True:        #me compara entre dos objetos
                aux = lista_aux[j]
                lista_aux[j] = lista_aux[i]
                lista_aux[i] = aux
    return lista_aux

def burbujeoo(lista: list, key):
    lista_aux = lista.copy()
    for i in range(len(lista_aux) - 1):
        for j in range(i + 1, len(lista_aux)):                   #me compara porla key, el atributo
            if key(lista_aux[i]) > key(lista_aux[j]):
                lista_aux[i], lista_aux[j] = lista_aux[j], lista_aux[i]
    return lista_aux
def selection_sort_menor(lista:list)->int:
    for i in range(len(lista)-1): #para mantener elementos ordenados
        indice_minimo = i
    for j in range(i+1, len(lista)): #para buscar elemento mas chico
            if lista [indice_minimo] > lista[j]:
                indice_minimo = j
    aux = lista [indice_minimo]
    lista [i] = lista[indice_minimo]
    lista[indice_minimo] = aux

def selection_sort_mayor(lista:list)->int:
    for i in range(len(lista)+1): #para mantener elementos ordenados
        indice_maximo = i
    for j in range(i-1, len(lista)): #para buscar elemento mas grande
        if lista [indice_maximo] < lista[j]:
            indice_maximo = j
    aux = lista [indice_maximo]
    lista [i] = lista[indice_maximo]
    lista[indice_maximo] = aux

#quicksort divide lista en varias partes (agarro un nro de la lista y divide la lista a la mitad, 
    #un lado pone los mas chicos q el nro seleccionado y el otro los mas grandes(es recursivo osea q con esas listas creadas hace lo mismo))
def quick_sort(lista:list)->int: 
    if len(lista) <= 1:
        return lista
    pivote = lista.pop() #pivote es nro seleccionado

    elementos_mas_chicos = list()       #creo listas vacias para almacenar los elementos
    elementos_mas_grandes = list()

    for elemento in lista:
        if elemento > pivote:
            elementos_mas_grandes.append(elemento)    #agrego a las listas los elementos
        else:
            elementos_mas_chicos.append(elemento)

    return quick_sort(elementos_mas_chicos) + [pivote] + quick_sort (elementos_mas_grandes) #ordeno lo elementos

#listas multidimensionales en vez deener numeros sueltos, va a tener adentro otras listas(matrices)

#filtrar una lista

def filtrar_nros_positivos(lista:list):
    lista_filtrada = list()

    for elemento in lista:
        if lista[elemento] >0:
            lista_filtrada.append(elemento)

    return lista_filtrada
import json
ROJO = '\033[91m'
VERDE = '\033[92m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'

def _print(status: int, msj: str):
    match status:
        case -1:
            print(f'{ROJO}{msj}{RESET}')
        case 0:
            print(f'{AMARILLO}{msj}{RESET}')
        case 1:
            print(f'{VERDE}{msj}{RESET}')

def _validate_range(min: float, max: float, data: float) -> bool:
    data = float(data) 
    return min <= data <= max

def menuu(tittle: str, opc: list) -> int:
    i = 0
    print(f'{AMARILLO}[{tittle}]{RESET}\n')
    while i < len(opc):
        print(f'\t{MAGENTA}[{i+1:02d}]{CIAN} {opc[i]}{RESET}')
        i += 1
    print(f'\n{AZUL}[0] SALIR{RESET}')

    return get_int('\n\t[OPCION]: ', '[ERROR, Opcion no valida]', 0, len(opc), -1)

def get_int2(msj:str, msj_error: str, min: int, max: int, retries: int | None = None) -> int | None:
    
    while retries is None or retries > 0 or retries == -1:
        aux = int(input(msj))
        if _validate_range(min, max, aux):
            return aux
        else:
            match(retries):
                case None:
                    break
                case -1:
                    print(msj_error)
                case _:
                    print(msj_error)
                    retries -= 1
    return None


def get_string(msj: str, msj_error: str) -> str:
    while True:
        user_input = input(msj)
        if user_input.isalpha():
            return user_input
        else:
            _print(0, msj_error)

def get_string_range(msj: str, msj_error: str, min_len: int, max_len: int) -> str:
    while True:
        user_input = get_string(msj, msj_error)
        if len(user_input) < min_len or len(user_input) > max_len:
            _print(0, f'[FUERA DE RANGO] MIN de {min_len} - MAX de {max_len} caracteres.')
        else:
            return user_input
            
def get_date_ddmmyy(msj_dd: str, msj_mm: str, msj_yyyy: str, min_yyyy: int, max_yyyy: int) -> str:

    dd = get_int(msj_dd, '[ERROR] El dia debe estar entre 1 y 31.', 1, 31, -1)
    mm = get_int(msj_mm, '[ERROR] El mes debe estar entre 1 y 12.', 1, 12, -1)
    yyyy = get_int(msj_yyyy, f'[ERROR] El año debe estar entre {min_yyyy} y {max_yyyy}.', min_yyyy, max_yyyy, -1)

    return f"{dd:02d}/{mm:02d}/{yyyy:04d}"

def save_txt(path: str, data: str, append: bool = False) -> bool:
    try:
        with open(path, 'a' if append else 'w') as file:
            file.write(data)
        return True
    except Exception:
        return False

def save_json(path: str, data: list) -> bool:
    try:
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
        return True
    except Exception:
        return False

def load_txt(path: str) -> str | bool:
    try:
        with open(path, 'r') as file:
            return file.read()
    except Exception:
        return False

def load_json(path: str) -> bool:
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except Exception:
        return False    
def mi_reduce(func, data: list, initializer=None):
    if len(data) == 0: return None

    value = data[0] if initializer is None else initializer

    for element in data:
        value = func(value, element)

    return value

