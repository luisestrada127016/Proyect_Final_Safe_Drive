import json

def consultar_cliente (dpi):
    dpi = int(input("\nIngrese el dpi del cliente: "))
    with open("Clientes.json", "r") as file:
        data = json.load(file)
        for cliente in data:
            if str(dpi) in cliente:
                print("\n========= Informacion del cliente =========\n")
                print(f"Nombre: {cliente[str(dpi)]['Nombre']}")
                print(f"DPI: {cliente[str(dpi)]['DPI']}")
                print(f"Tipo de Vehiculo: {cliente[str(dpi)]['Tipo de Vehiculo']}")
                print(f"Horario: {cliente[str(dpi)]['Horario']}")
                print(f"Hora: {cliente[str(dpi)]['Hora']}")
                print("\n==========================================\n")
                return
            else:
                return print("Cliente no encontrado")

# consultar_cliente(dpi=0)

# ================================================================================================================

def consultar_instructor (dpi):
    dpi = int(input("\nIngrese el dpi del instructor: "))
    with open("Instructores.json", "r") as file:
        data = json.load(file)
        for instructor in data:
            if str(dpi) in instructor:
                print("\n========= Informacion del instructor =========\n")
                print(f"Nombre: {instructor[str(dpi)]['Nombre']}")
                print(f"DPI: {instructor[str(dpi)]['DPI']}")
                print(f"Tipo de Vehiculo: {instructor[str(dpi)]['Tipo de Vehiculo']}")
                print(f"Horario: {instructor[str(dpi)]['Horario']}")
                print(f"Disponibilidad: {instructor[str(dpi)]['disponibilidad']}")
                print("\n==========================================\n")
                return
            else:
                return print("Instructor no encontrado")

# consultar_instructor(dpi=0)

# ================================================================================================================

def consultar_vehiculo (placa):
    placa = (input("\nIngrese la placa del vehiculo: ")).upper()
    with open("Vehiculos.json", "r") as file:
        data = json.load(file)
        for vehiculo in data:
            if (placa) in vehiculo:
                print("\n========= Informacion del vehiculo =========\n")
                print(f"Placa: {vehiculo[str(placa)]['Placa']}")
                print(f"Tipo de Vehiculo: {vehiculo[str(placa)]['Tipo de Vehiculo']}")
                print(f"Año: {vehiculo[str(placa)]['Year']}")
                print(f"Modelo: {vehiculo[str(placa)]['Modelo']}")
                print(f"Marca: {vehiculo[str(placa)]['Marca']}")
                print(f"Disponibilidad: {vehiculo[str(placa)]['Disponibilidad']}")
                print("\n==========================================\n")
                return
            else:
                return print("Vehiculo no encontrado")

# consultar_vehiculo(placa="")

# ================================================================================================================

def consultar_disponibles_por_disponibilidad():
    horario = input("Ingrese el horario buscado (AM/PM): ").strip().upper()
    if horario not in ("AM", "PM"):
        print("Horario no válido. Use AM o PM.")
        return

    print("\n========= Instructores disponibles =========")
    with open("Instructores.json", "r") as file:
        data = json.load(file)
        encontrados = False
        for instructor in data:
            for dpi, info in instructor.items():
                if info.get("Horario", "").upper() == horario and info.get("disponibilidad") is True:
                    encontrados = True
                    print(f"Nombre: {info.get('Nombre')}")
                    print(f"DPI: {info.get('DPI')}")
                    print(f"Tipo de Vehículo: {info.get('Tipo de Vehiculo')}")
                    print(f"Horario: {info.get('Horario')}")
                    print(f"Disponibilidad: {info.get('disponibilidad')}")
                    print("-" * 40)
        if not encontrados:
            print("No hay instructores disponibles en ese horario.")

    print("\n========= Vehículos disponibles =========")
    with open("Vehiculos.json", "r") as file:
        data = json.load(file)
        encontrados = False
        for vehiculo in data:
            for placa, info in vehiculo.items():
                veh_horario = info.get("Horario")
                if info.get("Disponibilidad") is True and (veh_horario is None or veh_horario.upper() == horario):
                    encontrados = True
                    print(f"Placa: {info.get('Placa')}")
                    print(f"Tipo de Vehículo: {info.get('Tipo de Vehiculo')}")
                    print(f"Año: {info.get('Year')}")
                    print(f"Modelo: {info.get('Modelo')}")
                    print(f"Marca: {info.get('Marca')}")
                    if veh_horario is not None:
                        print(f"Horario: {veh_horario}")
                    print(f"Disponibilidad: {info.get('Disponibilidad')}")
                    print("-" * 40)
        if not encontrados:
            print("No hay vehículos disponibles en ese horario.")

# consultar_disponibles_por_disponibilidad()
def consultar_cita():
    dpi = input("\nIngrese el dpi del cliente para ver su cita: ").strip()
    with open("Citas.json", "r") as file:
        data = json.load(file)

    for cita in data:
        if isinstance(cita, dict) and dpi in cita:
            info = cita[dpi]
            print("\n========= Informacion del cliente =========\n")
            print(f"DPI cliente: {info.get('DPI')}")
            print(f"DPI instructor: {info.get('dpi de instructor')}")
            print(f"Tipo de Vehiculo: {info.get('Tipo de Vehiculo')}")
            print(f"Horario: {info.get('Horario')}")
            print(f"Hora: {info.get('Hora')}")
            print(f"Fecha: {info.get('Fecha')}")
            print("\n==========================================\n")
            return
        else:    
            print("Cita no encontrada")






