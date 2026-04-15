from json import load,dumps

# ========================= FUNCIONES_INSTRUCTORES ===========================

def creacion_instructor(nombre_instructor, dpi, tipo_vehiculo, horario):

# ============== Solicitar al instructor que ingrese su información personal y de vehículo ==================

    nombre_instructor = str(input("\nIngrese el nombre: ")).capitalize()
    apellido_instructor = str(input("Ingrese el apellido: ")).capitalize()
    if not nombre_instructor.isalpha() or not apellido_instructor.isalpha():
        print("\n--- El nombre y apellido deben contener solo letras ---\n")
    nombre_instructor = f"{nombre_instructor} {apellido_instructor}"
    
    dpi = input("Ingrese documento de identificacion: ")
    if dpi.isdigit():
        pass
    else:
        print("\n--- El dpi no debe contener letras ni caracteres especiales ---\n")
    
    tipo_vehiculo = str(input("Da leciones de Carro o Moto?: ")).capitalize()
    if tipo_vehiculo != "Carro" and tipo_vehiculo != "Moto":
            print("Tipo de vehiculo no valido.")
            return
    horario= str(input("Que horario tiene disponible para sus clases (AM/PM): ")).upper()
    if horario != "AM" and horario != "PM":
        print ("\n--- Solo se ingresa AM o PM ---")
        return
    disponibilidad = True

# ================== Creacion del diccionario con la informacion del instructor ==================

    Instructores = { dpi: {
        "Nombre": nombre_instructor,
        "DPI": dpi,
        "Tipo de Vehiculo": tipo_vehiculo,
        "Horario": horario,
        "disponibilidad": disponibilidad
        }
    }
# ========================= Guardar la informacion del instructor en el archivo JSON =========================

    with open ("Instructores.json", "r") as file:
        with open("Instructores.json", "r") as file:
            data = load(file)
        if dpi in data:
            print("Ya existe un cliente con ese DPI")
            return
    data[dpi] = Instructores[dpi]
    with open ("Instructores.json", "w") as file:
        file.write(dumps(data, indent=4))

    print("\n========= Instructor creado exitosamente =========\n")

# =============================== FIN DE LA FUNCION =========================
