from json import load, dumps

# ========================= FUNCION PARA CREAR VEHICULOS ===========================
def creacion_vehiculo(tipo_vehiculo, placa, modelo, marca, disponibilidad, año):
    tipo_vehiculo = input("\nIngrese el tipo de vehiculo (carro o moto): ").capitalize()
    if tipo_vehiculo != "Carro" and tipo_vehiculo != "Moto":
            print("Tipo de vehiculo no valido.")
    placa = input("Ingrese la placa del vehículo: ").upper()
    if not placa.isalnum():  
        print("\n--- La placa debe contener solo letras y números ---\n")
    try:
        año = int(input("Ingrese el año del vehículo: "))
    except ValueError:
        año = None
        print("\n--- El año debe ser un número entero ---\n")
    modelo = input("Ingrese el modelo del vehículo: ").capitalize()
    if not modelo.isalpha():
        print("\n--- El modelo debe contener solo letras ---\n")
    marca = input("Ingrese la marca del vehículo: ").capitalize()
    if not marca.isalpha():
        print("\n--- La marca debe contener solo letras ---\n")
    print(f"\nVehículo registrado: Placa={placa}, Año={año}, Modelo={modelo}, Marca={marca}")
    disponibilidad = True

# ================== Creacion del diccionario con la informacion del vehiculo ==================
    vehiculo = {
        placa: {
            "Tipo de Vehiculo": tipo_vehiculo,
            "Placa": placa,
            "Year": año,
            "Modelo": modelo,
            "Marca": marca,
            "Disponibilidad": disponibilidad
        }
    }

# ========================= Guardar la informacion del vehiculo en el archivo JSON =========================

    with open ("Vehiculos.json", "r") as file:
        with open("Vehiculos.json", "r") as file:
            data = load(file)
        if placa in data:
            print("Ya existe un cliente con ese DPI")
            return
    data[placa] = vehiculo[placa]
    with open ("Vehiculos.json", "w") as file:
        file.write(dumps(data, indent=4))

    print("\n========= Vehiculo creado exitosamente =========\n")

