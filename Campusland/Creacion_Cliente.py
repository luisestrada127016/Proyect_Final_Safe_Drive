
from json import load, dumps

# ============================== FUNCIONES_CLIENTES =========================

def creacion_cliente(nombre_estudiante, dpi, tipo_vehiculo, horario, hora):

# =========== Solicitar al usuario que ingrese su información personal y de vehículo ===========

    nombre_estudiante= (input("\nIngrese el nombre: ")).capitalize()
    apellido_estudiante = (input("Ingrese el apellido: ")).capitalize()
    if not nombre_estudiante.isalpha() or not apellido_estudiante.isalpha():
        print("\n--- El nombre y apellido deben contener solo letras ---\n")
    
    nombre_estudiante = f"{nombre_estudiante} {apellido_estudiante}"

    dpi = input("Ingrese documento de identificacion: ")
    if not dpi.isdigit():
        print("\n--- El DPI no debe contener letras ni caracteres especiales ---\n")
        
    tipo_vehiculo = (input("Desea aprender Carro o Moto?: ")).capitalize()
    if tipo_vehiculo != "Carro" and tipo_vehiculo != "Moto":
            print("Tipo de vehiculo no valido.")
            
    horario = (input("Desea horario (AM/PM): ")).upper()
    if horario == "PM":
        hora = input("A que hora desea la clase? (12-5): ")
    elif horario == "AM":
            hora = (input("A que hora desea la clase? (8-11): "))
    else:
        print("Horario no valido.")



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
        with open("Clientes.json", "r") as file:
            data = load(file)
        if dpi in data:
            print("Ya existe un cliente con ese DPI")
            return
    data[dpi] = clientes[dpi]
    with open ("Clientes.json", "w") as file:
        file.write(dumps(data, indent=4))
        
    print("\n========= Cliente creado exitosamente =========\n")
        
# =============================== FIN DE LA FUNCION =========================
