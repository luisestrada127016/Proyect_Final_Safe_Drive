import json

# ========================= FUNCION PARA CREAR VEHICULOS ===========================
def creacion_vehiculo(tipo_vehiculo, placa, modelo, marca, disponibilidad, año):
    tipo_vehiculo = input("\nIngrese el tipo de vehiculo (carro o moto): ").capitalize()
    if tipo_vehiculo != "Carro" and tipo_vehiculo != "Moto":
            print("Tipo de vehiculo no valido.")
            return
    placa = input("Ingrese la placa del vehiculo: ").upper()
    año = int(input("Ingrese el año del vehiculo: "))
    modelo = input("Ingrese el modelo del vehiculo: ").capitalize()
    marca = input("Ingrese la marca del vehiculo: ").capitalize()
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
        data = json.load(file)
        data.append(vehiculo)
        if len(data) > 1:
            for i in range(len(data)-1):
                if placa in data[i]:
                    print("\n========= Ya hay un vehiculo con esa placa registrado! Revise la informacion ingresada ==========\n")
                    return
    with open ("Vehiculos.json", "w") as file:
        file.write(json.dumps(data, indent=4))

    print("\n========= Vehiculo creado exitosamente =========\n")

