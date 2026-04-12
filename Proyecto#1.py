
# from Programcion_de_Citas import creacion_cita

from Creacion_Instructor import creacion_instructor
from Creacion_Cliente import creacion_cliente
from Creacion_Vehiculos import creacion_vehiculo

from Consultas import consultar_cliente, consultar_instructor, consultar_vehiculo, consultar_cita

from Programcion_de_Citas import creacion_cita

        
# =========================== INICIO DEL PROGRAMA ===========================


def menu_principal():
    while True:
        print("""
================== WELCOME TO CAMPUSLAND DRIVING SCHOOL ===================

██████╗ ██████╗ ██╗██╗   ██╗███████╗   ███████╗ █████╗ ███████╗███████╗
██╔══██╗██╔══██╗██║██║   ██║██╔════╝   ██╔════╝██╔══██╗██╔════╝██╔════╝
██║  ██║██████╔╝██║██║   ██║█████╗     ███████╗███████║███████╗█████╗  
██║  ██║██╔══██╗██║╚██╗ ██╔╝██╔══╝     ╚════██║██╔══██║██╔════╝██╔══╝  
██████╔╝██║  ██║██║ ╚████╔╝ ███████╗   ███████║██║  ██║██║     ███████╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝
===========================================================================
#By Henry Morales
 \n""")
        opcion = int(input(
            "\nSeleccione una opcion: "
            "\n1. Agregar Info + "
            "\n2. Consultar Info "
            "\n3. Salir "
            "\nOpcion: "
        ))

        if opcion == 1:
            menu_agregar()

        elif opcion == 2:
            menu_consultar()

        elif opcion == 3:
            print("Cerrando programa...")
            break
        else:
            print("Opcion no valida. Intente de nuevo...")

def menu_agregar():
    while True:
        opcion = int(input(
            "\nSeleccione una opcion: "
            "\n1. Agregar Cliente "
            "\n2. Agregar Vehiculo "
            "\n3. Agregar Instructor "
            "\n4. Crear cita "
            "\n5. Volver al menú principal "
            "\nOpcion: "
        ))

        if opcion == 1:
            creacion_cliente(nombre_estudiante="", dpi=0, tipo_vehiculo="", horario="", hora="")
        elif opcion == 2:
            creacion_vehiculo(tipo_vehiculo="", placa="", año=0, modelo="", marca="", disponibilidad=True)
        elif opcion == 3:
            creacion_instructor(nombre_instructor="", dpi=0, tipo_vehiculo="", horario="")
        elif opcion == 4:
            creacion_cita()
        elif opcion == 5:
            break
        else:
            print("Opcion no valida. Intente de nuevo...")

def menu_consultar():
    while True:
        opcion = int(input(
            "\nSeleccione una opcion: "
            "\n1. Consultar Clientes "
            "\n2. Consultar Instructores "
            "\n3. Consultar Vehiculos "
            "\n4. Consultar Citas "
            "\n5. Volver al menú principal "
            "\nOpcion: "
        ))

        if opcion == 1:
            consultar_cliente(dpi=0)
        elif opcion == 2:
            consultar_instructor(dpi=0)
        elif opcion == 3:
            consultar_vehiculo(placa="")
        elif opcion == 4:
            consultar_cita()
        elif opcion == 5:
            break
        else:
            print("Opcion no valida. Intente de nuevo...")

# Ejecutar el programa
menu_principal()    
