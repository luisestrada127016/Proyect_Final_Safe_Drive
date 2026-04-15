import json

def consultar_cliente (dpi):
    dpi = (input("\nIngrese el dpi del cliente: "))
    with open("Clientes.json", "r") as file:
        data = json.load(file)
        for cliente in data:
            if (dpi) in cliente:
                print("\n========= Informacion del cliente =========\n")
                print(f"Nombre: {cliente[(dpi)]['Nombre']}")
                print(f"DPI: {cliente[(dpi)]['DPI']}")
                print(f"Tipo de Vehiculo: {cliente[(dpi)]['Tipo de Vehiculo']}")
                print(f"Horario: {cliente[(dpi)]['Horario']}")
                print(f"Hora: {cliente[(dpi)]['Hora']}")
                print("\n==========================================\n")
        print("Cliente no encontrado")

# consultar_cliente(dpi=0)

# ================================================================================================================

def consultar_instructor (dpi):
    dpi = (input("\nIngrese el dpi del instructor: "))
    with open("Instructores.json", "r") as file:
        data = json.load(file)
        for instructor in data:
            if (dpi) in instructor:
                print("\n========= Informacion del instructor =========\n")
                print(f"Nombre: {instructor[(dpi)]['Nombre']}")
                print(f"DPI: {instructor[(dpi)]['DPI']}")
                print(f"Tipo de Vehiculo: {instructor[(dpi)]['Tipo de Vehiculo']}")
                print(f"Horario: {instructor[(dpi)]['Horario']}")
                print(f"Disponibilidad: {instructor[(dpi)]['disponibilidad']}")
                print("\n==========================================\n")
        print("Instructor no encontrado")

# consultar_instructor(dpi=0)

# ================================================================================================================

def consultar_vehiculo (placa):
    placa = (input("\nIngrese la placa del vehiculo: ")).upper()
    with open("Vehiculos.json", "r") as file:
        data = json.load(file)
        for vehiculo in data:
            if (placa) in vehiculo:
                print("\n========= Informacion del vehiculo =========\n")
                print(f"Placa: {vehiculo[(placa)]['Placa']}")
                print(f"Tipo de Vehiculo: {vehiculo[(placa)]['Tipo de Vehiculo']}")
                print(f"Año: {vehiculo[(placa)]['Year']}")
                print(f"Modelo: {vehiculo[(placa)]['Modelo']}")
                print(f"Marca: {vehiculo[(placa)]['Marca']}")
                print(f"Disponibilidad: {vehiculo[(placa)]['Disponibilidad']}")
                print("\n==========================================\n")                 
        print("Vehiculo no encontrado")
     

# consultar_vehiculo(placa="")

# ================================================================================================================

import json

def consultar_disponibles_por_disponibilidad():
    horario = input("Ingrese el horario buscado (AM/PM): ").strip().upper()
    if horario not in ("AM", "PM"):
        print("Horario no válido. Use AM o PM.")
        return

    print("\n========= Instructores disponibles =========")
    with open("Instructores.json", "r") as file:
        data = json.load(file)
        encontrados_instructores = False
        for instructor in data:
            for dpi, info in instructor.items():
                if info.get("Horario", "").upper() == horario and str(info.get("disponibilidad")).lower() == "true":
                    encontrados_instructores = True
                    print(f"Nombre: {info.get('Nombre')}")
                    print(f"DPI: {info.get('DPI')}")
                    print(f"Tipo de Vehículo: {info.get('Tipo de Vehiculo')}")
                    print(f"Horario: {info.get('Horario')}")
                    print(f"Disponibilidad: {info.get('disponibilidad')}")
                    print("-" * 40)
        if not encontrados_instructores:
            print("No hay instructores disponibles en ese horario.")

    print("\n========= Vehículos disponibles =========")
    with open("Vehiculos.json", "r") as file:
        data = json.load(file)
        encontrados_vehiculos = False
        for vehiculo in data:
            for placa, info in vehiculo.items():
                veh_horario = info.get("Horario")
                if str(info.get("Disponibilidad")).lower() == "true" and (veh_horario is None or veh_horario.upper() == horario):
                    encontrados_vehiculos = True
                    print(f"Placa: {info.get('Placa')}")
                    print(f"Tipo de Vehículo: {info.get('Tipo de Vehiculo')}")
                    print(f"Año: {info.get('Year')}")
                    print(f"Modelo: {info.get('Modelo')}")
                    print(f"Marca: {info.get('Marca')}")
                    if veh_horario is not None:
                        print(f"Horario: {veh_horario}")
                    print(f"Disponibilidad: {info.get('Disponibilidad')}")
                    print("-" * 40)
        if not encontrados_vehiculos:
            print("No hay vehículos disponibles en ese horario.")


def consultar_cita():
    dpi = input("\nIngrese el dpi del cliente para ver su cita: ").strip()
    if not dpi.isdigit():
        print("\n--- El DPI no debe contener letras ni caracteres especiales ---\n")
        return

    with open("Citas.json", "r") as file:
        data = json.load(file)

    encontrada = False
    for cita in data:
        if isinstance(cita, dict) and dpi in cita:
            encontrada = True
            info = cita[dpi]
            print("\n========= Información del cliente =========\n")
            print(f"DPI cliente: {info.get('DPI')}")
            print(f"DPI instructor: {info.get('dpi de instructor')}")
            print(f"Tipo de Vehículo: {info.get('Tipo de Vehiculo')}")
            print(f"Horario: {info.get('Horario')}")
            print(f"Hora: {info.get('Hora')}")
            print(f"Fecha: {info.get('Fecha')}")
            print("\n==========================================\n")
            break  # salimos del loop al encontrar la cita

    if not encontrada:
        print("Cita no encontrada")
        