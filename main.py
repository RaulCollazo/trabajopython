<<<<<<< HEAD
import os
from datetime import datetime


# variables globales
mascotasRegistradas = {}   # {id: [nombre, especie, edad, peso, condicionReproductiva, estadoVacunacion, intolerancias, historialClinico, motivoConsulta, fechaIngreso]}
propietarios = {}          # {dni: [nombreCompleto, numeroCelular, direccion, [idMascota1, idMascota2, ...]]}
turnos = {}                # {idTurno: [idMascota, fecha, hora, estado]}
atenciones = {}            # {idMascota: [[fecha, servicio, diagnostico, tratamiento], ...]}
ingresosServicios = {      # [Cantidad, Total Recaudado]
    "Consulta General": [0, 0.0],
    "Vacunacion": [0, 0.0],
    "Cirugia": [0, 0.0]
}

PRECIOS = {
    "Consulta General": 1500.0,
    "Vacunacion": 2500.0,
    "Cirugia": 8000.0
}

id = 0
idTurno = 0


# funciones de validacion
def validar_no_vacio(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: El campo no puede estar vacio.")

def validar_entero_positivo(mensaje):
    while True:
        valor = input(mensaje).strip()
        try:
            num = int(valor)
            if num > 0:
                return num
            print("Error: Debe ingresar un numero entero positivo.")
        except ValueError:
            print("Error: Debe ingresar un numero entero valido.")

def validar_numerico_positivo(mensaje):
    while True:
        valor = input(mensaje).strip()
        try:
            num = float(valor)
            if num > 0:
                return num
            print("Error: Debe ingresar un numero positivo.")
        except ValueError:
            print("Error: Debe ingresar un valor numerico valido.")

def validar_dni(mensaje):
    while True:
        dni = input(mensaje).strip()
        if dni.isdigit() and 7 <= len(dni) <= 8:
            return dni
        print("Error: El DNI debe contener entre 7 y 8 digitos numericos.")

def validar_telefono(mensaje):
    while True:
        tel = input(mensaje).strip()
        if tel.isdigit() and len(tel) >= 8:
            return tel
        print("Error: El telefono debe contener al menos 8 digitos numericos.")

def validar_fecha(mensaje):
    while True:
        fecha = input(mensaje).strip()
        try:
            datetime.strptime(fecha, "%d/%m/%Y")
            return fecha
        except ValueError:
            print("Error: La fecha debe tener el formato DD/MM/AAAA.")

def validar_hora(mensaje):
    while True:
        hora = input(mensaje).strip()
        try:
            datetime.strptime(hora, "%H:%M")
            return hora
        except ValueError:
            print("Error: La hora debe tener el formato HH:MM.")


# funciones de utilidad
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


# menus
def mostrarMenu():
    print("Bienvenido al sistema de atencion veterinaria")
    print("------------------------------------------------------------------")
    print("""
    Por favor seleccione una opcion:
1- Registro de animales
2- Agendar un turno
3- Consultar Atencion Medica
4- Control de servicios Realizados
5- Estadisticas
0- Salir""")


# sub-funciones de registro de animales
def registrar_mascota():
    limpiar_pantalla()
    print("Registro de animal")
    print("-----------------------------------------------")

    dni = validar_dni("Ingrese el DNI del propietario: ")
    if dni in propietarios:
        print(f"Hemos encontrado al propietario {propietarios[dni][0]}")
        nombreCompleto = propietarios[dni][0]
        usuarioRegistrado = True
    else:
        nombreCompleto = validar_no_vacio("Ingrese el nombre completo del propietario. Ej: (Juan Perez): ")
        numeroCelular = validar_telefono("Ingrese el numero de telefono: ")
        direccion = validar_no_vacio("Ingrese la direccion del propietario: ")
        usuarioRegistrado = False

    global id
    id += 1
    idMascota = id

    nombre_mascota = validar_no_vacio("Ingrese el nombre de la mascota: ")
    especie = validar_no_vacio("Especie: ")
    edad = validar_entero_positivo("Edad (en años): ")
    pesoActual = validar_numerico_positivo("Peso (en kg): ")
    condicionReproductiva = validar_no_vacio("Condicion reproductiva (castrado/sin castrar): ")
    estadoDeVacunacion = validar_no_vacio("Estado de vacunacion: ")
    intoleranciasMedicas = validar_no_vacio("Intolerancias medicas: ")
    historialClinico = validar_no_vacio("Historial clinico: ")
    motivoConsulta = validar_no_vacio("Motivo de la consulta: ")
    fechaIngreso = datetime.now().strftime("%d/%m/%Y")

    mascota = [nombre_mascota, especie, edad, pesoActual, condicionReproductiva,
               estadoDeVacunacion, intoleranciasMedicas, historialClinico, motivoConsulta, fechaIngreso]
    mascotasRegistradas[idMascota] = mascota

    if usuarioRegistrado:
        propietarios[dni][3].append(idMascota)
    else:
        propietarios[dni] = [nombreCompleto, numeroCelular, direccion, [idMascota]]

    print(f"Mascota {nombre_mascota} registrada con el ID {idMascota} al propietario {nombreCompleto}")
    input("Presione Enter para continuar...")

def eliminar_mascota():
    limpiar_pantalla()
    print("Eliminar animal")
    print("------------------------------")
    id_eliminar = validar_entero_positivo("Ingrese el ID del animal a eliminar: ")
    if id_eliminar in mascotasRegistradas:
        mascotasRegistradas.pop(id_eliminar)
        print(f"Animal con ID {id_eliminar} eliminado.")
    else:
        print("Error al eliminar, animal no encontrado.")
    input("Presione Enter para continuar...")

def mostrar_mascotas():
    limpiar_pantalla()
    print("Listado de animales registrados:")
    print("-------------------------------------------------")
    if not mascotasRegistradas:
        print("No hay animales registrados.")
    else:
        for id_animal, datos in mascotasRegistradas.items():
            print(f"ID: {id_animal} | Nombre: {datos[0]} | Motivo: {datos[8]} | Ingreso: {datos[9]}")
            print("-------------------------------------------------")
    input("Presione Enter para continuar...")

def registroDeAnimales():
    limpiar_pantalla()
    print("Registro de animales")
    print("-----------------------------------------------")
    print("""
1- Registrar
2- Eliminar
3- Mostrar
""")
    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        opcion = -1
    if opcion == 1:
        registrar_mascota()
    elif opcion == 2:
        eliminar_mascota()
    elif opcion == 3:
        mostrar_mascotas()
    else:
        print("Opcion invalida.")
        input("Presione Enter para continuar...")


def agendarTurno():
    global idTurno
    limpiar_pantalla()
    print("Agendar un Turno")
    print("-----------------------------------------------")
    id_m = validar_entero_positivo("Ingrese el ID de la mascota para el turno: ")
    if id_m in mascotasRegistradas:
        fecha = validar_fecha("Ingrese la fecha del turno (DD/MM/AAAA): ")
        hora = validar_hora("Ingrese la hora del turno (HH:MM): ")
        idTurno += 1
        turnos[idTurno] = [id_m, fecha, hora, "Pendiente"]
        nombre_m = mascotasRegistradas[id_m][0]
        print(f"Turno N° {idTurno} agendado para {nombre_m} el {fecha} a las {hora} hs.")
    else:
        print("Ese ID de mascota no existe en el sistema.")
    input("Presione Enter para continuar...")


def consultarAtencionMedica():
    limpiar_pantalla()
    print("Consultar Atencion Medica")
    print("-----------------------------------------------")
    id_m = validar_entero_positivo("Ingrese el ID de la mascota a consultar: ")
    if id_m in mascotasRegistradas:
        nombre_m = mascotasRegistradas[id_m][0]
        print(f"\nHistorial de: {nombre_m} (ID: {id_m})")
        print(f"Especie: {mascotasRegistradas[id_m][1]} | Ultimo Peso: {mascotasRegistradas[id_m][3]} kg")
        print(f"Motivo de ingreso inicial: {mascotasRegistradas[id_m][8]}")
        print("-----------------------------------------------")
        if id_m in atenciones and atenciones[id_m]:
            print("Consultas y Atenciones registradas:")
            for idx, atencion in enumerate(atenciones[id_m], 1):
                print(f"{idx}. Fecha: {atencion[0]} | Servicio: {atencion[1]}")
                print(f"   Diagnostico: {atencion[2]}")
                print(f"   Tratamiento: {atencion[3]}")
                print("-" * 30)
        else:
            print("Esta mascota aun no registra atenciones medicas en el sistema.")
    else:
        print("Ese ID de mascota no existe.")
    input("Presione Enter para continuar...")


def controlDeServicios():
    limpiar_pantalla()
    print("Control de Servicios Realizados")
    print("-----------------------------------------------")
    pendientes = [(t_id, datos) for t_id, datos in turnos.items() if datos[3] == "Pendiente"]
    if not pendientes:
        print("No hay turnos pendientes para procesar.")
        input("Presione Enter para continuar...")
        return
    for t_id, datos in pendientes:
        nom_m = mascotasRegistradas[datos[0]][0]
        print(f"Turno N° {t_id} -> Mascota: {nom_m} (ID: {datos[0]}) | Fecha: {datos[1]} a las {datos[2]}")
    print("-----------------------------------------------")
    t_atender = validar_entero_positivo("Ingrese el Numero de Turno a atender: ")
    if t_atender in turnos and turnos[t_atender][3] == "Pendiente":
        id_m = turnos[t_atender][0]
        print("\nSeleccione el servicio realizado:")
        print("1- Consulta General ($1500)")
        print("2- Vacunacion ($2500)")
        print("3- Cirugia ($8000)")
        op = input("Opcion: ")
        if op == "1":
            serv = "Consulta General"
        elif op == "2":
            serv = "Vacunacion"
        elif op == "3":
            serv = "Cirugia"
        else:
            print("Opcion invalida. Cancelando atencion.")
            input()
            return
        costo = PRECIOS[serv]
        diag = validar_no_vacio("Ingrese el diagnostico medico: ")
        trat = validar_no_vacio("Ingrese el tratamiento recetado: ")
        fecha_hoy = datetime.now().strftime("%d/%m/%Y")
        if id_m not in atenciones:
            atenciones[id_m] = []
        atenciones[id_m].append([fecha_hoy, serv, diag, trat])
        ingresosServicios[serv][0] += 1
        ingresosServicios[serv][1] += costo
        turnos[t_atender][3] = "Atendido"
        print(f"\n¡Atencion guardada con exito para {mascotasRegistradas[id_m][0]}!")
    else:
        print("El numero de turno no es valido o ya fue atendido.")
    input("Presione Enter para continuar...")


def estadisticas():
    limpiar_pantalla()
    print("Estadisticas del Sistema")
    print("-----------------------------------------------")
    total_general = 0.0
    max_cant = -1
    servicio_frecuente = "Ninguno"
    for serv, datos in ingresosServicios.items():
        cant = datos[0]
        monto = datos[1]
        total_general += monto
        print(f"- {serv}: {cant} veces realizadas | Recaudado: ${monto:.2f}")
        if cant > max_cant and cant > 0:
            max_cant = cant
            servicio_frecuente = serv
    print("-----------------------------------------------")
    print(f"Servicio mas solicitado: {servicio_frecuente}")
    print(f"Total Recaudado en Caja: ${total_general:.2f}")
    input("\nPresione Enter para continuar...")


def main():
    seguir = True
    while seguir:
        limpiar_pantalla()
        mostrarMenu()
        print("-----------------------------------------------")
        try:
            opcion = int(input())
            if opcion > 5 or opcion < 0:
                opcion = -1
        except ValueError:
            opcion = -1
        if opcion == 0:
            seguir = False
        elif opcion == 1:
            registroDeAnimales()
        elif opcion == 2:
            agendarTurno()
        elif opcion == 3:
            consultarAtencionMedica()
        elif opcion == 4:
            controlDeServicios()
        elif opcion == 5:
            estadisticas()
        elif opcion == -1:
            limpiar_pantalla()
            print("Opcion Invalida")
            print("Por favor, ingrese una opcion valida entre 0 y 5.")
            input("Presione Enter para continuar...")


if __name__ == "__main__":
    main()
=======
import os
from datetime import datetime
from pyfiglet import Figlet


# variables globales
mascotasRegistradas = {}
propietarios = {}
turnos = {}             # Estructura: {idTurno: [idMascota, fecha, hora, estado]}
atenciones = {}         # Estructura: {idMascota: [[fecha, motivo, diagnostico, tratamiento]]}
ingresosServicios = {   # Para control de servicios y estadísticas
    "Consulta General": [0, 0.0],  # [Cantidad, Total Recaudado]
    "Vacunación": [0, 0.0],
    "Cirugía": [0, 0.0]
}

id = 0
idTurno = 0

# Menus
def mostrarMenu():
    print('Bienvenido al sistema de atención veterinaria')
    print("------------------------------------------------------------------")
    print("""
    Por favor seleccione una opción:
1- Registro de animales 
2- Agendar un turno 
3- Consultar Atención Médica 
4- Control de servicios Realizados 
5- Estadísticas
0- Salir""")

def registroDeAnimales():
    usuarioRegistrado = False
    if os.name== 'nt' :
        os.system('cls')
    else:
        os.system('clear')
          
    print("""Registro de animales""")
    print("""-----------------------------------------------""")
    print("""
1- Registrar
2- Eliminar
3- Mostrar 
          """)
    try:
        opcion= int(input('Ingrese una opción '))
    except:
        opcion=-1
    
    if opcion == 1:
        if os.name== 'nt' :
            os.system('cls')
        else:
            os.system('clear')
            
    # solicitamos los datos del propietario
        print("Datos del propietario")
        dni = input("Ingrese el D.N.I del propietario: ")
        if propietarios.get(dni, {}):
            print(f"Hemos encontrado al propietario {propietarios[dni][0]}")
            nombreCompleto = propietarios[dni][0]
            usuarioRegistrado = True
        else:
            nombreCompleto = input("Ingrese el nombre completo del propietario. Ej:(Juan Perez): ")
            numeroCelular = input("Ingrese el número de teléfono: ") 
            direccion = input("Ingrese la dirección del propietario: ")

        # definimos un id unico
        global id
        id += 1
        idMascota = id
    
        # solicitamos datos del animal
        nombre_mascota = input("Ingrese el nombre de la mascota: ")
        especie = input("Especie? ")
        edad = input("Edad? ")
        pesoActual = input("Peso? ")
        condicionReproductiva = input("Ingrese la condición reproductiva. (castrado/sin castrar): ")
        estadoDeVacunacion = input("Ingrese el estado de vacunación: ")
        intoleranciasMedicas = input("Ingrese las intolerancias médicas: ")
        historialClinico = input("Ingrese el historial clínico: ")
        motivoConsulta = input("Ingrese el motivo de la consulta: ")
        fechaIngreso = datetime.now().strftime("%d/%m/%Y")
    
        if usuarioRegistrado:
            mascotasRegistradas.update({id: [nombre_mascota, especie, edad, pesoActual, condicionReproductiva,  estadoDeVacunacion, intoleranciasMedicas, historialClinico, motivoConsulta, fechaIngreso]})
            propietarios[dni][3].append(idMascota)
        else:
            propietarios.update({dni: [nombreCompleto, numeroCelular, direccion, [idMascota]]})
            mascotasRegistradas.update({id: [nombre_mascota, especie, edad, pesoActual, condicionReproductiva,  estadoDeVacunacion, intoleranciasMedicas, historialClinico, motivoConsulta, fechaIngreso]})
        
        print(f'Mascota {nombre_mascota} registrada con el ID {idMascota} al propietario {nombreCompleto}')
        input('Presione Enter para continuar...')
    elif opcion  == 2:
        if os.name== 'nt' :
            os.system('cls')
        else:
            os.system('clear')
        
        print('Eliminar')
        print("------------------------------")
        try:
            id_eliminar = int(input("ingresa el id del animal a eliminar: "))
        except:
            id_eliminar=-1
        if id_eliminar != -1:
            if mascotasRegistradas.pop(id_eliminar,False):
                print(f'Animal con id {id_eliminar} eliminado')
            else:
                print('Error al eliminar, animal no encontrado')
        
        else:
            print('opción invalida')
            
        input('Presione Enter para continuar...')
    elif opcion==3:
        if os.name== 'nt' :
            os.system('cls')
        else:
            os.system('clear')
            
        print('Listado de animales registrados:')
        print('-------------------------------------------------')
        
        for animal in mascotasRegistradas.items():
            print(f"ID: {animal[0]}: Nombre: {animal[1][0]} motivo de la consulta: {animal[1][8]} fecha de ingreso: {animal[1][9]} ")
            print('-------------------------------------------------')
        input('Presione Enter para continuar...')
            
            
        

def agendarTurno():
    global idTurno
    if os.name== 'nt' :
        os.system('cls')
    else:
        os.system('clear')
          
    print("""Agendar un Turno""")
    print("""-----------------------------------------------""")
    try:
        id_m = int(input("Ingrese el ID de la mascota para el turno: "))
    except:
        id_m=-1
    
    if id_m in mascotasRegistradas:
        fecha = input("Ingrese la fecha del turno (DD/MM/AAAA): ")
        hora = input("Ingrese la hora del turno (HH:MM): ")
        
        idTurno += 1
        turnos.update({idTurno: [id_m, fecha, hora, "Pendiente"]})
        
        nombre_m = mascotasRegistradas[id_m][0]
        print(f"Turno N° {idTurno} agendado para {nombre_m} el {fecha} a las {hora} hs.")
    else:
        print("Ese ID de mascota no existe en el sistema.")
    input('Presione Enter para continuar...')

def consultarAtencionMedica():
    if os.name== 'nt' :
        os.system('cls')
    else:
        os.system('clear')
          
    print("""Consultar Atención Médica""")
    print("""-----------------------------------------------""")
    
    id_m = int(input("Ingrese el ID de la mascota a consultar: "))
    
    if id_m in mascotasRegistradas:
        nombre_m = mascotasRegistradas[id_m][0]
        print(f"\nHistorial de: {nombre_m} (ID: {id_m})")
        print(f"Especie: {mascotasRegistradas[id_m][1]} | Último Peso: {mascotasRegistradas[id_m][3]}")
        print(f"Motivo de ingreso inicial: {mascotasRegistradas[id_m][8]}")
        print("-----------------------------------------------")
        
        if id_m in atenciones and len(atenciones[id_m]) > 0:
            print("Consultas y Atenciones registradas:")
            for idx, f in enumerate(atenciones[id_m], 1):
                print(f"{idx}. Fecha: {f[0]} | Servicio: {f[1]}")
                print(f"   Diagnóstico: {f[2]}")
                print(f"   Tratamiento: {f[3]}")
                print("-" * 30)
        else:
            print("Esta mascota aún no registra atenciones médicas en el sistema.")
    else:
        print("Ese ID de mascota no existe.")
    input('Presione Enter para continuar...')

def controlDeServicios():
    if os.name== 'nt' :
        os.system('cls')
    else:
        os.system('clear')
          
    print("""Control de Servicios Realizados""")
    print("""-----------------------------------------------""")
    
    hay_pendientes = False
    for t_id, datos in turnos.items():
        if datos[3] == "Pendiente":
            hay_pendientes = True
            nom_m = mascotasRegistradas[datos[0]][0]
            print(f"Turno N° {t_id} -> Mascota: {nom_m} (ID: {datos[0]}) | Fecha: {datos[1]} a las {datos[2]}")
            
    if not hay_pendientes:
        print("No hay turnos pendientes para procesar.")
        input('Presione Enter para continuar...')
        return

    print("-----------------------------------------------")
    t_atender = int(input("Ingrese el Número de Turno a atender: "))
    
    if t_atender in turnos and turnos[t_atender][3] == "Pendiente":
        id_m = turnos[t_atender][0]
        
        print("\nSeleccione el servicio realizado:")
        print("1- Consulta General ($1500)\n2- Vacunación ($2500)\n3- Cirugía ($8000)")
        op = input("Opción: ")
        
        if op == "1":
            serv = "Consulta General"
            costo = 25000.0
        elif op == "2":
            serv = "Vacunación"
            costo = 15500.0
        elif op == "3":
            serv = "Cirugía"
            costo = 83400.0
        else:
            print("Opción inválida. Cancelando atención.")
            input()
            return
            
        diag = input("Ingrese el diagnóstico médico: ")
        trat = input("Ingrese el tratamiento recetado: ")
        fecha_hoy = datetime.now().strftime("%d/%m/%Y")
        
        # Registrar en atenciones
        if id_m not in atenciones:
            atenciones[id_m] = []
        atenciones[id_m].append([fecha_hoy, serv, diag, trat])
        
        # Actualizar acumuladores y contadores de estadística
        ingresosServicios[serv][0] += 1
        ingresosServicios[serv][1] += costo
        
        # Cambiar estado del turno
        turnos[t_atender][3] = "Atendido"
        print(f"\n¡Atención guardada con éxito para {mascotasRegistradas[id_m][0]}!")
    else:
        print("El número de turno no es válido o ya fue atendido.")
    input('Presione Enter para continuar...')

def estadisticas():
    if os.name== 'nt' :
        os.system('cls')
    else:
        os.system('clear')
          
    print("""Estadísticas del Sistema""")
    print("""-----------------------------------------------""")
    
    total_general = 0.0
    max_cant = -1
    servicio_frecuente = "Ninguno"
    
    for serv, datos in ingresosServicios.items():
        cant = datos[0]
        monto = datos[1]
        total_general += monto
        print(f"• {serv}: {cant} veces realizadas | Recaudado: ${monto}")
        
        if cant > max_cant and cant > 0:
            max_cant = cant
            servicio_frecuente = serv
            
    print("-----------------------------------------------")
    print(f"Servicio más solicitado: {servicio_frecuente}")
    print(f"Total Recaudado en Caja: ${total_general}")
    input('\nPresione Enter para continuar...')

def main():
    seguir = True
    while seguir:
        if os.name== 'nt' :
                os.system('cls')
        else:
            os.system('clear')
                
        mostrarMenu()        
        print("""-----------------------------------------------""")
        try:
            opcion = int(input())
            if opcion > 5 or opcion < 0:
                opcion = -1
        except:
            opcion = -1
            
        if opcion == 0:
            seguir = False
        elif opcion == 1:
            registroDeAnimales()
        elif opcion == 2:
            agendarTurno()
        elif opcion == 3:
            consultarAtencionMedica()
        elif opcion == 4:
            controlDeServicios()
        elif opcion == 5:
            estadisticas()
        elif opcion == -1:
            if os.name== 'nt' :
                os.system('cls')
            else:
                os.system('clear')
                
            print("Opcion Inválida")
            print(f"Ante la flagrante torpeza del usuario, el sistema desestima el frío laconismo interviene mediante una vehemente reprensión vernácula. Este deliberado artificio retórico corrige la insubordinación apelando al rigor de la vergüenza jocosa y al habla popular de su expresión")
            input('Presione cualquier tecla para continuar')

if __name__ == "__main__":
    main()
>>>>>>> 215c3462eb1840f2cda1c55f1cc744634be4ca8d
