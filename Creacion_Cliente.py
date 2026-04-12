
from json import load, dumps

# ============================== FUNCIONES_CLIENTES =========================

def creacion_cliente(nombre_estudiante, dpi, tipo_vehiculo, horario, hora):

# =========== Solicitar al usuario que ingrese su información personal y de vehículo ===========

    nombre_estudiante= str(input("\nIngrese el nombre: ")).capitalize()
    apellido_estudiante = str(input("Ingrese el apellido: ")).capitalize()
    nombre_estudiante = f"{nombre_estudiante} {apellido_estudiante}"
    dpi = int(input("Ingrese documento de identificacion: "))
    tipo_vehiculo = str(input("Desea aprender Carro o Moto?: ")).capitalize()
    if tipo_vehiculo != "Carro" and tipo_vehiculo != "Moto":
            print("Tipo de vehiculo no valido.")
            return
    horario = str(input("Desea horario (AM/PM): ")).upper()
    if horario == "PM":
         hora = input("A que hora desea la clase? (12-5): ")
    elif horario == "AM":
            hora = int(input("A que hora desea la clase? (8-11): "))
    else:
        print("Horario no valido.")
        return

# ========== Creacion del diccionario con la informacion del cliente ===========

    clientes = { dpi: {
        "Nombre": nombre_estudiante,
        "DPI": dpi,
        "Tipo de Vehiculo": tipo_vehiculo,
        "Horario": horario,
        "Hora": hora
        }
    }

# ========================= Guardar la informacion del instructor en el archivo JSON =========================

    with open ("Clientes.json", "r") as file:
        data = load(file)
        data.append(clientes)
        for i in range(len(data)-1):
            if str(dpi) in data[i]:
                    print("\n ========= Ya hay un cliente con ese DPI registrado! Revise la informacion ingresada ==========\n")
                    return
    with open ("Clientes.json", "w") as file:
        file.write(dumps(data, indent=4))
        
    print("\n========= Cliente creado exitosamente =========\n")
        
# =============================== FIN DE LA FUNCION =========================

  