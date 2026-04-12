import json
from Consultas import consultar_cliente, consultar_disponibles_por_disponibilidad

def creacion_cita():

    print("\n========= Creacion de cita =========\n")
    # Se mostrara la informacion del cliente <<<

    print("Primero, ingrese la informacion del cliente...\n")
    consultar_cliente(dpi=0)

    # Se colocara de forma manual la informacion de cliente <<<

    dpi_cliente = int(input("Ingrese el DPI del cliente: "))
    tipo_vehiculo_cliente = input("Ingrese el tipo de vehiculo del cliente (Carro o Moto): ").capitalize()
    horario = input("Ingrese el horario (AM/PM): ")
    hora = input("Ingrese la hora deaseada: ")

    consultar_disponibles_por_disponibilidad()

    dpi_instructor = int(input("Ingrese el DPI del instructor: "))
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


