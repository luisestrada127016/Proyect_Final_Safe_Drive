import json
from Consultas import consultar_cita
def registro_evaluaciones():
    consultar_cita()
    
    




def menu_evaluaciones ():
    print("\n=== SISTEMA DE EVALUACIONES DRIVESAFE ===\n")
    opcion = print("""Seleccione una opcion:
          1. Registrar nueva evaluacion
          2. Consultar evaluaciones por estudiante
          3. Calcular promedio general
          4. Salir
          opcion: """)
    # if opcion == 1:
