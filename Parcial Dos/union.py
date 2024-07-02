from claseEmpleado import *
from claseVehiculo import *
from classReparacion import*
import os
import json
from utils import *
import re
import csv
from datetime import datetime


def get_empleado():
    try:
        if os.path.exists(path_empleados):
            with open(path_empleados, 'r') as mi_archivo:
                next(mi_archivo)           #aca salteo el encabezado para que no se borre
                aux_list_empleados = []
                for linea in mi_archivo:                 
                    aux = linea.strip().split(';')    #por cada linea le saco los espacios en blanco y separo por un ;
                    id_empleado = int(aux[0])                         #pocision 0...
                    apellido_nombre = aux[1]            
                    salario = float(aux[2])
                    dni = int(aux[3])
                    telefono = aux[4].strip()  
                    # Crear objeto Empleado y agregar a la lista
                    empleado = Empleado(apellido_nombre, salario, dni, telefono)  #le asigno cada posicion a un empleado instanciandola
                    empleado.id = id_empleado
                    aux_list_empleados.append(empleado)         #agrego mi empleado a la lista aux de empleados
                print(f"[Aviso CSV] Carga exitosa de archivo {path_empleados}")      
                input('Continuar... ')
                return aux_list_empleados
        else:
            print(f"[Aviso CSV] No se encontro el archivo {path_empleados}")
            input('Continuar... ')
            return []
    except Exception as e:
        print(f"[ERROR CSV]: {e}")
        input()
        return False

def guardar_empleado(lista_nueva:list[Empleado]):
    try:
        
            with open(path_empleados, mode="w", newline="") as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(['id', 'apellido_nombre', 'salario', 'dni', 'telefono'])  # escribo encabezados
                for empleado in lista_nueva:
                    writer.writerow([empleado.id, empleado.apellido_nombre, empleado.salario, empleado.dni, empleado.telefono])
            return True
    except Exception as e:
        print(f"[ERROR CSV]: {e}")
        input()
        return False

def get_vehiculo():
    try:
        if os.path.exists(path_vehiculos):
            with open(path_vehiculos, 'r') as file:
                data = json.load(file)
                lista_vehiculos = []
                for item in data:
                    vehiculo = Vehiculo(
                        item['Marca'],
                        item['Modelo'],
                        item['Anio'],
                        item['Color'],
                        item['Patente'],
                        item['Propietario']
                    )
                    vehiculo.ID = item['ID']
                    lista_vehiculos.append(vehiculo)
                print(f"[Aviso JSON] Carga exitosa de archivo {path_vehiculos}")
                input('Continuar... ')
                
                return lista_vehiculos
        else:
            print(f"[Aviso JSON] No se encontro el archivo {path_vehiculos}")
            input('Continuar... ')
            return []
        
    except Exception as e:
        print(f"[ERROR JSON]: {e}")
        input()
        return False

def guardar_vehiculo(lista_vehiculos:list[Vehiculo]):
    try:
        with open(path_vehiculos, 'w') as mi_archivo:
            json.dump([vehiculo.parse_json() for vehiculo in lista_vehiculos], mi_archivo, indent=4)
        return True
    except Exception as e:
        print(f"[ERROR JSON]: {e}")
        return False

def get_reparaciones():
    try:
        if os.path.exists(path_reparaciones):
            with open(path_reparaciones, 'r') as mi_archivo:
                next(mi_archivo)           #aca salteo el encabezado para que no se borre
                aux_list_reparaciones = []
                for linea in mi_archivo:                 
                    aux = linea.strip().split('/')    #por cada linea le saco los espacios en blanco y separo por un ;
                    id_reparacion = int(aux[0])                         #pocision 0...
                    descripcion = aux[1]            
                    coste = float(aux[2].strip())
                    # Crear objeto Reparacion y agregar a la lista
                    reparacion = Reparacion(descripcion,coste)  #le asigno cada posicion a un empleado instanciandola
                    reparacion.id = id_reparacion
                    aux_list_reparaciones.append(reparacion)         #agrego mi empleado a la lista aux de las reparaciones
                print(f"[Aviso CSV] Carga exitosa de archivo {path_reparaciones}")      
                input('Continuar... ')
                return aux_list_reparaciones
        else:
            print(f"[Aviso CSV] No se encontro el archivo {path_reparaciones}")
            input('Continuar... ')
            return []
    except Exception as e:
        print(f"[ERROR CSV]: {e}")
        input()
        return False

def guardar_reparacion(lista_reparaciones : list[Reparacion]):
    try:
            with open(path_reparaciones, mode="w", newline="") as file:
                writer = csv.writer(file, delimiter='/')
                writer.writerow(['id', 'descripcion', 'coste'])  # escribo encabezados
                for reparacion in lista_reparaciones:
                    writer.writerow([reparacion.id, reparacion.descripcion, reparacion.coste])
            return True
    except Exception as e:
        print(f"[ERROR CSV]: {e}")
        input()
        return False

def ordenamiento_anio(lista_vehiculos:list[Vehiculo]):
    lista_aux = burbujeoo(lista_vehiculos, criterio_anio)
    return lista_aux

def ordenamiento_marca(lista_vehiculos:list[Vehiculo]):
    lista_aux = burbujeoo(lista_vehiculos, criterio_marca)
    return lista_aux

def ordenamiento_propietario(lista_vehiculos:list[Vehiculo]):
    lista_aux = burbujeoo(lista_vehiculos, criterio_propietario)
    return lista_aux

def criterio_propietario(vehiculo:Vehiculo):
    return vehiculo.Propietario

def criterio_marca(vehiculo:Vehiculo):
    return vehiculo.Marca

def criterio_anio(vehiculo:Vehiculo):
    return vehiculo.Anio

def ordenamiento_salario(lista_empleados:list[Empleado]):
    lista_aux = burbujeoo(lista_empleados, criterio_salario)
    return lista_aux

def criterio_salario(empleado:Empleado):
    return empleado.salario

def ordenamiento_nombre(lista_empleados:list[Empleado]):
    lista_aux = burbujeoo(lista_empleados, lambda a:a.apellido_nombre)
    return lista_aux

def listar_empleados(lista_empleados:list[Empleado]):
    os.system('cls')
    if lista_empleados != None and lista_empleados != False:
        for empleado in lista_empleados:
            print(empleado)
        input('')
    return

def listar_vehiculos(lista_vehiculos:list[Vehiculo]):
    os.system('cls')
    if lista_vehiculos != None and lista_vehiculos != False:
        for v in lista_vehiculos:
            print(v)
        input('')
    return

def validar_telefono(telefono):
    # Expresión regular para el formato "11-NNNN-NNNN"
    patron = r'^11-\d{4}-\d{4}$'
    
    # Validar el número de teléfono con el patrón
    if re.match(patron, telefono):
        return True
    else:
        return False

def validar_nombre_apellido(apellido_nombre):
    patron = re.compile(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\' -]+$')
    if patron.match(apellido_nombre):
        return True
    else:
        return False

def alta_empleado(lista_empleados:list[Empleado])->Empleado:
    os.system('cls')
    """
    Permite dar de alta a un nuevo empleado.

    Args:

        lista_empleados (list[Empleado]): La lista de empleados actuales.
    Returns:

        Empleado: El empleado recién agregado.
    """
    apellido_nombre = input("Deme su apellido y nombre: ").title()
    while validar_nombre_apellido(apellido_nombre) == False:
        apellido_nombre = input('[error]Ingrese apellido y nombre valido: ').title()
    dni= get_int_rango("Deme su D.N.I:", '[ERROR]Deme un D.N.I correcto', 13000000, 55000000, 6)
    salario = ingreso_float_rango("Deme su salario: ","Error ingrese salario valido",5000,1000000,5)
    telefono = input('FORMATO[11-NNNN-NNNN]\n Ingrese número su de telefono: ')
    while validar_telefono(telefono) == False:
        telefono = input('[ERROR]FORMATO[11-NNNN-NNNN]\n Ingrese número su de telefono: ')
    nuevo_empleado = Empleado(apellido_nombre,salario,dni,telefono)
    empleado_existente = False
    for i in range(len(lista_empleados)):
        if lista_empleados[i].dni == nuevo_empleado.dni:
            empleado_existente== True
            print("usuario ya existente")
            return False
    if empleado_existente == False:
        lista_empleados.append(nuevo_empleado)
        guardar_empleado(lista_empleados)
        input('')
    return True

def validar_patente(patente):
    patron = r'^[A-Z]{3}-\d{3}$'
    if re.match(patron, patente):
        return True
    else:
        return False

def alta_vehiculo(lista_vehiculos:list[Vehiculo])-> Vehiculo:
    '''
Permite dar de alta a un nuevo vehículo.

    Args:
        lista_vehiculos (list[Vehiculo]): La lista de vehículos actuales.

    Returns:
        Vehiculo: El vehículo recién agregado si no existía previamente en la lista, de lo contrario False.
    '''
    os.system('cls')
    marca = get_solo_string_rango('Ingrese marca del vehiculo: ','[ERROR] Ingrese marca de su vehículo válida:', 1,20,10).capitalize()
    modelo = get_solo_string_rango('Ingrese modelo del vehiculo: ', 'ERROR, Ingrese modelo del vehiculo válido: ', 1,20,4).capitalize()
    anio = get_int_rango('Ingrese el año de su vehiculo: ', 'ERROR, Ingrese año válido: ', 1800,2024,4)
    color =  get_solo_string_rango('Ingrese color del vehículo: ', '[ERROR] Ingrese color válido: ', 1,20,5).capitalize()
    patente =  input('FORMATO [XXX-NNN]\nIngrese patente del vehiculo: ').upper()
    while validar_patente(patente) == False:
        patente =  input('FORMATO [XXX-NNN]\nIngrese patente del vehiculo: ').upper()
    propietario = input("Deme nombre y apellido del propietario: ").title()
    while validar_nombre_apellido(propietario) == False:
        propietario = input("Deme nombre y apellido del propietario: ").title()
    nuevo_vehiculo = Vehiculo(marca,modelo,anio,color,patente, propietario)
    empleado_existente = False
    for i in range(len(lista_vehiculos)):
        if lista_vehiculos[i].Patente == nuevo_vehiculo.Patente:
            empleado_existente== True
            print("usuario ya existente")
            input('')
            return False
    if empleado_existente == False:
        lista_vehiculos.append(nuevo_vehiculo)
        guardar_vehiculo(lista_vehiculos)
    return True

def ver_vehiculos(lista_vehiculos:list[Vehiculo]):
    os.system('cls')
    opcion = menu(['ORDENAR POR MARCA', 'ORDENAR POR AÑO', 'ORDENAR POR PROPIETARIO'], 'Indique por que criterio desea ordenar la lista de vehiculos:')
    match opcion:
        case 0:
            return False
        case 1:
            print('Lista vehiculos ordenados por marca:')
            lista_vehiculos = ordenamiento_marca(lista_vehiculos)
            return lista_vehiculos
        case 2:
            print('Lista vehiculos ordenados por año:')
            lista_vehiculos = ordenamiento_anio(lista_vehiculos)
            return lista_vehiculos
        case 3:
            print('Lista vehiculos ordenados por propietario:')
            lista_vehiculos = ordenamiento_propietario(lista_vehiculos)
            return lista_vehiculos

def ver_empleados(lista_empleados:list[Empleado]):
    os.system('cls')
    opcion = menu(['ORDENAR POR NOMBRE', 'ORDENAR POR SALARIO'], 'Indique por que criterio desea ordenar la lista de EMPLEADOS:')
    match opcion:
        case 'X' | 'x':
            return False
        case 1:
            print('Lista empleados ordenado por nombre:')
            lista_empleados = ordenamiento_nombre(lista_empleados)
            return lista_empleados
        case 2:
            print('Lista empleados ordenada por salario:')
            lista_empleados = ordenamiento_salario(lista_empleados)
            return lista_empleados

def eleccion_emp(lista_empleados:list[Empleado],msj):
    lista_e = []
    for e in lista_empleados:
        lista_e.append(f' [{e.id}]  - Apellido y nombre: {e.apellido_nombre}'   )
    eleccion = menu(lista_e, msj)
    if eleccion == 'x' or eleccion == 'X':
        return 
    else:
        return eleccion - 1

def baja_empleado(lista_empleados:list[Empleado]):
    index = eleccion_emp(lista_empleados, 'Empleados registrados\nElija el número del empleado que desee dar de baja: ')
    if index == False:
        return False
    lista_empleados.pop(index)
    guardar_empleado(lista_empleados)
    return True

def empleado_modificacion(lista_empleados:list[Empleado]):
    index= eleccion_emp(lista_empleados, 'Empleados registrados\nElija el número del empleado que desee modificar: ')
    if index == None or index == False:
        return False
    opcion = menu(['MODIFICAR APELLIDO Y NOMBRE', 'MODIFICAR SALARIO', 'MODIFICAR TELEFONO', 'MODIFICAR D.N.I' ], 'Indique el número de lo que desea modificar')
    match opcion:
        case 1:
            apellido_nombre_nuevo = input("Deme su apellido y nombre: ").title()
            while validar_nombre_apellido(apellido_nombre_nuevo) == False:
                apellido_nombre_nuevo = input('[error]Ingrese apellido y nombre valido: ').title()
            lista_empleados[index].apellido_nombre = apellido_nombre_nuevo
            return apellido_nombre_nuevo
        case 2:
            salario_nuevo = ingreso_float_rango("Deme su salario: ","Error ingrese salario valido",5000,1000000,5)
            if salario_nuevo:
                lista_empleados[index].salario = salario_nuevo
            else:
                return False
        case 3:
            telefono_nuevo = input('FORMATO[11-NNNN-NNNN]\n Ingrese número su de telefono: ')
            while validar_telefono(telefono_nuevo) == False:
                telefono_nuevo = input('[ERROR]FORMATO[11-NNNN-NNNN]\n Ingrese número su de telefono: ')
            lista_empleados[index].telefono = telefono_nuevo
            return telefono_nuevo
        case 4:
            dni_nuevo = get_int_rango("Deme su D.N.I:", '[ERROR]Deme un D.N.I correcto', 13000000, 55000000, 6)
            if dni_nuevo:
                lista_empleados[index].dni == dni_nuevo
                return dni_nuevo
            else:
                return False

def elegir_vehiculo(lista_vehiculos:list[Vehiculo],msj):
    lista_v = []
    for v in lista_vehiculos:
        lista_v.append(f' [{v.Patente}]  - Propietario: {v.Propietario} - Marca: {v.Marca}/{v.Modelo}'   )
    eleccion = menu(lista_v, f"{msj}")
    if eleccion == 'x' or eleccion == 'X':
        return 
    else:
        return eleccion - 1

def vehiculo_baja(lista_vehiculos:list[Vehiculo]):
    index = elegir_vehiculo(lista_vehiculos, 'Indique el número del vehiculo a dar de baja: ')
    if index == False:
        return False
    lista_vehiculos.pop(index)
    guardar_vehiculo(lista_vehiculos)
    return True

def vehiculo_modificacion(lista_vehiculos:list[Vehiculo]):
    index= elegir_vehiculo(lista_vehiculos, 'Autos registrados:\nElija el número del vehiculo que desee modificar: ')
    opcion = menu(['MODIFICAR MARCA', 'MODIFICAR MODELO', 'MODIFICAR AÑO', 'MODIFICAR PATENTE', 'MODIFICAR COLOR', 'MODIFICAR NOMBRE DE PROPIETARIO' ], 'Indique el número de lo que desea modificar')
    match opcion:
        case 0:
            return False
        case 1:
            marca_nueva = get_solo_string_rango('Ingrese marca del vehiculo: ','[ERROR] Ingrese marca de su vehículo válida:', 1,20,10).capitalize()
            if marca_nueva:
                lista_vehiculos[index].Marca = marca_nueva
            return marca_nueva
        case 2:
            modelo_nuevo = get_solo_string_rango('Ingrese modelo del vehiculo: ', 'ERROR, Ingrese modelo del vehiculo válido: ', 1,20,4).capitalize()
            if modelo_nuevo:
                lista_vehiculos[index].Modelo = modelo_nuevo
            else:
                return False
        case 3:
            anio_nuevo = get_int_rango('Ingrese el año de su vehiculo: ', 'ERROR, Ingrese año válido: ', 1800,2024,4)
            if anio_nuevo:
                lista_vehiculos[index].Anio = anio_nuevo
                return anio_nuevo
            else: 
                return False
        case 4:
            patente_nueva =  input('FORMATO [XXX-NNN]\nIngrese patente del vehiculo: ')
            while validar_patente(patente_nueva) == False:
                patente_nueva =  input('FORMATO [XXX-NNN]\nIngrese patente del vehiculo: ')
            lista_vehiculos[index].Patente = patente_nueva
            return patente_nueva
        case 5:
            color_nuevo =  get_solo_string_rango('Ingrese color del vehículo: ', '[ERROR] Ingrese color válido: ', 1,20,5).capitalize()
            if color_nuevo:
                lista_vehiculos[index].Color == color_nuevo
                return color_nuevo
            else:
                return False
        case 6:
            propietario_nuevo = input("Deme nombre y apellido del propietario: ").title()
            while validar_nombre_apellido(propietario_nuevo) == False:
                propietario_nuevo = input("Deme nombre y apellido del propietario: ").title()
            lista_vehiculos[index].Propietario = propietario_nuevo
            return propietario_nuevo

def agregar_servicio(lista_reparaciones:list[Reparacion]):
    descripcion = get_solo_string_rango2('Nombre de servicio nuevo: ', 'ERROR, Ingrese servicio válido: ', 4,50,20,5).title()
    if descripcion == False or descripcion ==None:
        return False
    coste = get_int_rango('Ingrese coste del servicio: ', 'ERROR, Ingrese costo válido: ', 100,10000000,5)
    if coste == None:
        return False
    nuevo_servicio = Reparacion(descripcion, coste)
    lista_reparaciones.append(nuevo_servicio)
    guardar_reparacion(lista_reparaciones)
    return True

def eleccion_servicio(lista_reparaciones:list[Reparacion], msj):
    lista_r = []
    for r in lista_reparaciones:
        lista_r.append(f' [{r.id}]  - Descripcion: {r.descripcion} - Coste: {r.coste}'   )
    eleccion = menu(lista_r, f"{msj}")
    if eleccion == 'x' or eleccion == 'X':
        return 
    else:
        return eleccion - 1

def baja_servicio(lista_reparaciones:list[Reparacion]):
    index = eleccion_servicio(lista_reparaciones, 'Ingrese el número del servicio a dar de baja:')
    if index == None or index == False:
        return False
    lista_reparaciones.pop(index)
    guardar_reparacion(lista_reparaciones)
    return True

def modificar_reparacion(lista_reparaciones:list[Reparacion]):
    index= eleccion_emp(lista_reparaciones, 'Servicios del taller:\nElija el número del servicio que desee modificar ')
    opcion = menu(['MODIFICAR DESCRIPCION', 'MODIFICAR COSTE' ], 'Indique el número de lo que desea modificar')
    match opcion:
        case 0:
            return
        case 1:
            descripcion_nueva = get_solo_string_rango2('Nombre de servicio nuevo: ', 'ERROR, Ingrese servicio válido: ', 4,50,5,5).capitalize()
            if descripcion_nueva == False:
                return False
            lista_reparaciones[index].descripcion = descripcion_nueva
            return descripcion_nueva
        case 2:
            coste_nuevo = ingreso_float_rango("Deme costo nuevo del servicio: ","Error ingrese costo valido",500,1000000,5)
            if coste_nuevo == None or coste_nuevo == False:
                return False
            lista_reparaciones[index].coste = coste_nuevo
            return coste_nuevo

def reparar(lista_empleados:list[Empleado], lista_vehiculos:list[Vehiculo], lista_reparaciones:list[Reparacion]):
    os.system('cls')
    empleado_index = eleccion_emp(lista_empleados, 'Ingrese número que corresponda del empleado a realizar el trabajo:')
    if empleado_index == False or empleado_index == None:
        return False
    input('')
    vehiculo_index = elegir_vehiculo(lista_vehiculos, 'Ingrese el número que corresponda del vehículo a reparar:' )
    if vehiculo_index == False or vehiculo_index == None:
        return False
    input('')
    servicio_index = eleccion_servicio(lista_reparaciones, 'Ingrese número de servicio a realizar')
    if servicio_index == False or servicio_index == None:
        return False
    input('')
    fecha_hora_actual = datetime.now()
    #formato = fecha_hora_actual.strftime("%d/%m/%Y %H:%M")
    _log= f'{lista_empleados[empleado_index].id} / {lista_vehiculos[vehiculo_index].ID} / {lista_reparaciones[servicio_index].id} / {fecha_hora_actual} \n'
    print(_log)                                        #ej: 23/05/2024 15:30 
    with open('Reparaciones.txt','a') as mi_archivo:
        mi_archivo.write(_log)

def get_txt():
    lista_aux = []
    with open('Reparaciones.txt', 'r') as mi_archivo:
        for linea in mi_archivo:
            aux = linea.strip().split('/')
            id_empleado = aux[0]
            id_vehiculo = aux[1]
            id_reparacion = aux[2]
            fecha_hora = aux[3]

            lista_aux.append({'id_empleado':id_empleado,'id_vehiculo':id_vehiculo,'id_reparacion':id_reparacion,'fecha_hora':fecha_hora})
    return lista_aux

def ver_reparaciones(lista_vehiculos:list[Vehiculo], lista_empleados:list[Empleado], lista_reparaciones:list[Reparacion]):
    lista_txt = get_txt()
    os.system('cls')
    for a in lista_txt:
        hora = a['fecha_hora']
        for i in range(len(lista_empleados)):
            if lista_empleados[i].id == int(a['id_empleado']):
                nombre_empleado = lista_empleados[i].apellido_nombre
                break
        for i in range(len(lista_vehiculos)):
            if lista_vehiculos[i].ID == int(a['id_vehiculo']):
                propietario = lista_vehiculos[i].Propietario
                marca = lista_vehiculos[i].Marca
                modelo = lista_vehiculos[i].Modelo
                patente = lista_vehiculos[i].Patente
                break
        for i in range(len(lista_reparaciones)):
            if lista_reparaciones[i].id == int(a['id_reparacion']):
                descripcion = lista_reparaciones[i].descripcion
                break
        print(f'[REPARACIÓN {hora}]\n'
            f'Empleado: {nombre_empleado}\n'
            f'Propietario: {propietario}\n'
            f'Reparación: {descripcion}\n'
            f'Vehículo: [{marca}], [{modelo}], [{patente}]\n')
    input('')
#.strftime("%d/%m/%Y %H:%M")}]
def calcular_ingresos(lista_reparaciones:list[Reparacion]):
    os.system('cls')
    acum1 = 0
    acum2 = 0
    acum3 = 0
    acum4 = 0
    acum5 = 0
    
    lista_txt = get_txt()

    for a in lista_txt:
        for reparacion in lista_reparaciones:
            if reparacion.id == int(a['id_reparacion']):
                if reparacion == lista_reparaciones[0]:
                    acum1 += 1
                elif reparacion == lista_reparaciones[1]:
                    acum2 += 1
                elif reparacion == lista_reparaciones[2]:
                    acum3 += 1
                elif reparacion == lista_reparaciones[3]:
                    acum4 += 1
                elif reparacion == lista_reparaciones[4]:
                    acum5 += 1
    acum1 = acum1* lista_reparaciones[0].coste
    acum2 = acum2* lista_reparaciones[1].coste
    acum3 = acum3* lista_reparaciones[2].coste
    acum4 = acum4* lista_reparaciones[3].coste
    acum5 = acum5* lista_reparaciones[4].coste
    print(f'INGRESOS TOTALES POR TIPO DE REPARACIÓN:\n{lista_reparaciones[0].descripcion}: ${acum1}\n{lista_reparaciones[1].descripcion}: ${acum2}\n{lista_reparaciones[2].descripcion}: ${acum3}\n{lista_reparaciones[3].descripcion}: ${acum4}\n{lista_reparaciones[4].descripcion}: ${acum5} ')

def buscar_reparacion(lista_reparaciones:list[Reparacion]):
    os.system('cls')
    acum1 = 0
    acum2 = 0
    acum3 = 0
    acum4 = 0
    acum5 = 0
    
    lista_txt = get_txt()
    
    for a in lista_txt:
        for reparacion in lista_reparaciones:
            if reparacion.id == int(a['id_reparacion']):
                descripcion = reparacion.descripcion
                if reparacion == lista_reparaciones[0]:
                    acum1 += 1
                elif reparacion == lista_reparaciones[1]:
                    acum2 += 1
                elif reparacion == lista_reparaciones[2]:
                    acum3 += 1
                elif reparacion == lista_reparaciones[3]:
                    acum4 += 1
                elif reparacion == lista_reparaciones[4]:
                    acum5 += 1
    if acum1 > acum2 or acum1> acum3 or acum1>acum4:
        mas_reparaciones = acum1
    else:
        acum2 > acum3 or acum1>acum3 or acum1 >acum4
        mas_reparaciones = acum2
        if acum3 > acum4:
            mas_reparaciones = acum3
        else: 
            if acum4> acum5:
                mas_reparaciones = acum4
            else:
                mas_reparaciones = acum5
    print(f'La reparación con más ventas es: {descripcion} - con {mas_reparaciones} reparaciones')
    input('')

def buscar_patente(lista_vehiculos:list[Vehiculo]):
    os.system('cls')
    patente =  input('FORMATO [XXX-NNN]\nIngrese patente del vehiculo a buscar: ').upper()
    while validar_patente(patente) == False:
        patente =  input('FORMATO [XXX-NNN]\nIngrese patente del vehiculo: ').upper()
    encontrado = False
    for vehiculo in lista_vehiculos:
        if vehiculo.Patente == patente:
            print(f'Vehículo con patente {patente}')
            print(f'Vehículo: [{vehiculo.Marca}, {vehiculo.Modelo}]\n'
                f'Propietario: {vehiculo.Propietario}')
            input('')
            encontrado = True
            break  

    if encontrado == False:
        print('No existe esa patente en nuestra base de datos.')
        input('')

    return encontrado

def setear_colores(lista_vehiculos:list[Vehiculo]):
    aux= []
    for v in lista_vehiculos:
        aux.append(v.Color)
    lista = set(aux)
    return list(lista)

def seleccionar_color(lista_vehiculos:list[Vehiculo]):
    aux = setear_colores(lista_vehiculos)
    opc = menu(aux,'Elija el color de los vehículos que desea filtrar: ')
    if opc != -1:
        color_seleccionado = aux[opc - 1]
        return color_seleccionado

def filtrar_colores(lista_vehiculos:list[Vehiculo]):
    os.system('cls')
    color_seleccionado = seleccionar_color(lista_vehiculos)
    vehiculos_filtrados = my_filter(lista_vehiculos, lambda vehiculo: vehiculo.Color == color_seleccionado)
    if vehiculos_filtrados:
        print(f'Vehículos encontrados con color "{color_seleccionado}":')
        for vehiculo in vehiculos_filtrados:
            print(f'[PROPIETARIO: {vehiculo.Propietario}]\n'
                f'[{vehiculo.Marca}] [{vehiculo.Modelo}] - {vehiculo.Patente}')
            input('')
    else:
        print(f'No se encontraron vehículos con color {color_seleccionado}')

def setear_propietarios(lista_vehiculos:list[Vehiculo]):
    aux = []
    for v in lista_vehiculos:
        aux.append(v.Propietario)
    lista = set(aux)
    return list(lista)

def seleccionar_propietario(lista_vehiculos:list[Vehiculo]):
    aux = setear_propietarios(lista_vehiculos)
    opc =  menu(aux,'Elija el número del propietario que desea filtrar: ')
    if opc != -1:
        propietario_seleccionado = aux[opc - 1]
        return propietario_seleccionado

def filtrar_propietarios(lista_vehiculos:list[Vehiculo]):
    os.system('cls')
    propietario_seleccionado = seleccionar_propietario(lista_vehiculos)
    prop_filtrados = my_filter(lista_vehiculos, lambda vehiculo: vehiculo.Propietario == propietario_seleccionado)
    if prop_filtrados:
        print(f'Vehículos encontrados con propietario: "{propietario_seleccionado}":')
        for vehiculo in prop_filtrados:
            print(f'[PROPIETARIO: {vehiculo.Propietario}]\n'
                f'[{vehiculo.Marca}] [{vehiculo.Modelo}] - {vehiculo.Patente}')
            input('')
    else:
        print(f'No se encontraron vehículos con Propietario llamado "{propietario_seleccionado}"')

def selec_fechas():
    lista_txt = get_txt()
    aux = []
    for a in lista_txt:
        hora= a['fecha_hora']
        aux.append(hora)
    return aux

def ordenar_fechas(lista_vehiculos:list[Vehiculo],lista_empleados:list[Empleado],lista_reparaciones:list[Reparacion]):
    os.system('cls')
    lista_txt = get_txt()
    lista_fechas = selec_fechas()
    aux = []

    match menu(['ASCENDENTE','DESCENDENTE'], 'SELECCIONE MODO DE ORDENAMIENTO DE FECHAS:'):
        case 1:
            funcion = lambda a,b : a > b
        case 2:
            funcion = lambda a,b : a < b
        case 'X' | 'x':
            return
    
    lista_ordenada = burbujeo2(lista_fechas, funcion)
    for i in range(len(lista_ordenada)):
        for j in range(len(lista_txt)):
            if lista_ordenada[i] == lista_txt[j]['fecha_hora']:
                aux.append(lista_txt[j])
    for h in aux:
        hora = h['fecha_hora']
        for i in range(len(lista_empleados)):
            if lista_empleados[i].id == int(h['id_empleado']):
                nombre_empleado = lista_empleados[i].apellido_nombre
                break
        for i in range(len(lista_vehiculos)):
            if lista_vehiculos[i].ID == int(h['id_vehiculo']):
                propietario = lista_vehiculos[i].Propietario
                marca = lista_vehiculos[i].Marca
                modelo = lista_vehiculos[i].Modelo
                patente = lista_vehiculos[i].Patente
                break
        for i in range(len(lista_reparaciones)):
            if lista_reparaciones[i].id == int(h['id_reparacion']):
                descripcion = lista_reparaciones[i].descripcion
                break
        print(f'[REPARACIÓN {hora}]\n'
            f'Empleado: {nombre_empleado}\n'
            f'Propietario: {propietario}\n'
            f'Reparación: {descripcion}\n'
            f'Vehículo: [{marca}], [{modelo}], [{patente}]\n')
    input('')