
import json

# ========================= FUNCIONES_INSTRUCTORES ===========================

def creacion_instructor(nombre_instructor, dpi, tipo_vehiculo, horario):

# ============== Solicitar al instructor que ingrese su información personal y de vehículo ==================

    nombre_instructor = str(input("\nIngrese su nombre: ")).capitalize()
    apellido_instructor = str(input("Ingrese su apellido: ")).capitalize()
    nombre_instructor = f"{nombre_instructor} {apellido_instructor}"
    dpi = int(input("Ingrese documento de identificacion: "))
    tipo_vehiculo = str(input("Da leciones de Carro o Moto?: ")).capitalize()
    if tipo_vehiculo != "Carro" and tipo_vehiculo != "Moto":
            print("Tipo de vehiculo no valido.")
            return
    horario= str(input("Que horario tiene disponible para sus clases (AM/PM): ")).upper()
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
        data = json.load(file)
        data.append(Instructores)
        if len(data) > 1:
            for i in range(len(data)-1):
                if str(dpi) in data[i]:
                    print("\n========= Ya hay un instructor con ese DPI registrado! Revise la informacion ingresada ==========\n")
                    return
    with open ("Instructores.json", "w") as file:
        file.write(json.dumps(data, indent=4))

    print("\n========= Instructor creado exitosamente =========\n")

# =============================== FIN DE LA FUNCION =========================
