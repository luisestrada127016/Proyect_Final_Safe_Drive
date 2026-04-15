import json
from Consultas import consultar_cliente, consultar_disponibles_por_disponibilidad

def creacion_cita():

    print("\n========= Creacion de cita =========\n")
    # Se mostrara la informacion del cliente <<<

    print("Primero, ingrese la informacion del cliente...\n")
    consultar_cliente(dpi=0)

    # Se colocara de forma manual la informacion de cliente <<<

    dpi_cliente = (input("Ingrese el DPI del cliente: "))
    tipo_vehiculo_cliente = input("Ingrese el tipo de vehiculo del cliente (Carro o Moto): ").capitalize()
    horario = input("Ingrese el horario (AM/PM): ")
    hora = input("Ingrese la hora deaseada: ")

    consultar_disponibles_por_disponibilidad()

    dpi_instructor = (input("Ingrese el DPI del instructor: "))
    placa = input("Ingrese la placa del vehiculo: ")
    fecha = input("Ingrese la fecha de la cita (Mes/Dia): ")

    cita = { dpi_cliente: {
        "DPI": dpi_cliente,
        "dpi de instructor": dpi_instructor,
        "Tipo de vehiculo": tipo_vehiculo_cliente,
        "Placa": placa,
        "Fecha": fecha,
        "Hora": hora,
        "Horario": horario
    }
    }

    with open ("Citas.json", "r") as file:
            data = json.load(file)
            data.append(cita)
            if len(data) > 1:
                for i in range(len(data)-1):
                    if dpi_cliente in data[i]:
                        print("\n========= El cliente ya tiene una cita ==========\n")
                        return
    with open ("Citas.json", "w") as file:
        file.write(json.dumps(data, indent=4))

    print("\n========= Cita creado exitosamente =========\n") 


def cerrar_cita():
    dpi = input("\nIngrese el DPI del cliente: ").strip()

    # ================== BUSCAR CITA ==================
    with open("Citas.json", "r") as file:
        citas = json.load(file)

    if dpi not in citas:
        print("Cita no encontrada")
        return

    info = citas[dpi]
    print("\nCita encontrada:")
    print(info)

    asistio = input("\n¿El cliente asistió? (SI/NO): ").upper()

    if asistio == "NO":
        calif = 0

    elif asistio == "SI":
        try:
            calif = int(input("Ingrese la nota del estudiante (0-100): "))
            if not (0 <= calif <= 100):
                print("--- Solo ingrese un número entre 0 - 100 ---")
                return
        except ValueError:
            print("--- Solo ingrese números ---")
            return
    else:
        print("Respuesta inválida, escriba SI o NO")
        return

    # Guardar calificación
    citas[dpi]["calificacion"] = calif
    with open("Citas.json", "w") as file:
        json.dump(citas, file, indent=4)

    # ================== LIBERAR INSTRUCTOR ==================
    with open("Instructores.json", "r") as file:
        instructores = json.load(file)

    for inst in instructores:
        if str(info["dpi de instructor"]) in inst:
            inst[str(info["dpi de instructor"])]["disponibilidad"] = True

    with open("Instructores.json", "w") as file:
        json.dump(instructores, file, indent=4)

    # ================== LIBERAR VEHICULO ==================
    with open("Vehiculos.json", "r") as file:
        vehiculos = json.load(file)

    for veh in vehiculos:
        if info["Placa"].upper() in veh:
            veh[info["Placa"].upper()]["Disponibilidad"] = True

    with open("Vehiculos.json", "w") as file:
        json.dump(vehiculos, file, indent=4)

    print("\nInstructor y vehículo liberados")
    print("\n=== Cita completada ===")

