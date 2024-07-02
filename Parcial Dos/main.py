import utils as u
import union as p
import os

def menu(consigna,lista_empleados,lista_vehiculos,lista_reparaciones):
    opcion =  u.menu(consigna,'Menú')
    match opcion:
        case 'X' | 'x':
            print('Ha salido del programa.')
            exit
            menu(consigna,lista_empleados,lista_vehiculos,lista_reparaciones)
        case 1:
            lista_vehiculos = p.ver_vehiculos(lista_vehiculos)
            p.listar_vehiculos(lista_vehiculos)
            menu(consigna,lista_empleados,lista_vehiculos,lista_reparaciones)
        case 2:
            lista_empleados = p.ver_empleados(lista_empleados)
            p.listar_empleados(lista_empleados)
            menu(consigna,lista_empleados,lista_vehiculos,lista_reparaciones)
        case 3:
            if p.alta_empleado(lista_empleados):
                print('Ha dado de alta correctamente.')
            else:
                print('[ERROR] No ha podido dar de alta al empleado.')
            menu(consigna,lista_empleados,lista_vehiculos,lista_reparaciones)
        case 4:
            if p.baja_empleado(lista_empleados):
                print('Se ha dado de baja correctamente')
            else:
                print('ERROR AL DAR DE BAJA')
            menu(consigna,lista_empleados,lista_vehiculos,lista_reparaciones)
        case 5:
            if p.empleado_modificacion(lista_empleados):
                print('Se ha modificado correctamente.')
            else:
                print('ERROR, Falla en modificación')
            menu(consigna,lista_empleados,lista_vehiculos,lista_reparaciones)
        case 6:
            if p.guardar_empleado(lista_empleados):
                print('Se ha guardado correctamente el archivo.')
            else:
                print('[ERROR] EN GUARDADO DE ARCHIVO CSV')
            menu(consigna,lista_empleados,lista_vehiculos,lista_reparaciones)
        case 7:
            if p.alta_vehiculo(lista_vehiculos):
                print('Se ha dado de alta correctamente')
            else:
                print('Error en dar de alta.')
            menu(consigna,lista_empleados,lista_vehiculos,lista_reparaciones)
        case 8:
            if p.vehiculo_baja(lista_vehiculos):
                print('Se ha dado de baja el vehiculo correctamente.')
            else:
                print('[ERROR] En baja de vehiculo.')
            menu(consigna,lista_empleados,lista_vehiculos,lista_reparaciones)
        case 9:
            if p.vehiculo_modificacion(lista_vehiculos):
                print('Se han modificado correctamente los datos')
            else:
                print('ERROR en modificación de datos.')
            menu(consigna,lista_empleados,lista_vehiculos,lista_reparaciones)
        case 10:
            if p.guardar_vehiculo(lista_vehiculos):
                print('Se han guardado los cambios en el archivo JSON')
                input('')
            else:
                print("[ERROR] En guardar los datos en el archivo JSON")
                input('')
            menu(consigna,lista_empleados,lista_vehiculos,lista_reparaciones)
        case 11:
            if p.reparar(lista_empleados,lista_vehiculos,lista_reparaciones):
                print('')
            else:
                print('ERROR, en reparación')
            menu(consigna,lista_empleados,lista_vehiculos,lista_reparaciones)
        case 12:
            p.ver_reparaciones(lista_vehiculos,lista_empleados,lista_reparaciones)
            menu(consigna,lista_empleados,lista_vehiculos,lista_reparaciones)
        case 13:
            p.calcular_ingresos(lista_reparaciones)
            menu(consigna,lista_empleados,lista_vehiculos,lista_reparaciones)
        case 14:
            p.buscar_reparacion(lista_reparaciones)
            menu(consigna,lista_empleados,lista_vehiculos,lista_reparaciones)
        case 15:
            p.buscar_patente(lista_vehiculos)
            menu(consigna,lista_empleados,lista_vehiculos,lista_reparaciones)
        case 16:
            p.filtrar_colores(lista_vehiculos)
            menu(consigna,lista_empleados,lista_vehiculos,lista_reparaciones)
        case 17:
            p.filtrar_propietarios(lista_vehiculos)
            menu(consigna,lista_empleados,lista_vehiculos,lista_reparaciones)
        case 18:
            p.ordenar_fechas(lista_vehiculos,lista_empleados,lista_reparaciones)
            menu(consigna,lista_empleados,lista_vehiculos,lista_reparaciones)

def main():
    os.system('cls')
    consigna = ['VER VEHICULOS', 'VER EMPLEADOS', 'EMPLEADO ALTA', 'EMPLEADO BAJA', 'EMPLEADO MODIFICACION','GUARDAR EMPLEADOS.csv'
                ,'VEHICULO ALTA','VEHICULO BAJA','VEHICULO MODIFICACIÓN','GUARDAR VEHICULOS.json','TALLER REPARAR', 'VER REPARACIONES', 
                'CALCULAR INGRESOS TOTALES POR TIPO DE REPARACIÓN','MOSTRAR REPARACION CON MAS REPARACIONES', 'BUSCAR POR PATENTE',
                'FILTRO VEHICULOS POR COLOR', 'FILTRO VEHICULOS POR PROPIETARIOS','ORDENAR FECHAS DE REPARACIONES']
    lista_empleados = p.get_empleado()
    lista_vehiculos = p.get_vehiculo()
    lista_reparaciones = p.get_reparaciones()
    menu(consigna,lista_empleados,lista_vehiculos, lista_reparaciones)
main()
