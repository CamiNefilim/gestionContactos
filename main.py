# Importa modulo de tiempo
import time

#Importa clases
from clases import Agenda, Contacto

#Importa modulos
from modulos import agregar_contacto, buscar_contacto, eliminar_contacto, importar_contactos
from modulos import exportar_contactos, importar_contactos

agenda = Agenda()

#Inicia menú agenda
while True:
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Importar contactos desde CSV")
    print("5. Exportar contactos a CSV")
    print("6. Salir")
    opcion = input("Seleccione opción: ")
    
    # Evalúa las opciones
    match opcion:
        case "1":
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el teléfono del contacto: ")
            email = input("Ingrese el email del contacto: ")
            nuevo_contacto = Contacto(nombre, telefono, email)
            agregar_contacto(agenda, nuevo_contacto)
            print(f"Contacto '{nombre}' agregado correctamente.")     
        case "2":
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            eliminar_contacto(agenda, nombre)
            print(f"Contacto '{nombre}' eliminado correctamente.")
        case "3":
            busqueda = input("Ingrese el nombre, teléfono o email del contacto: ")
            resultados = buscar_contacto(agenda, busqueda)
            if resultados:
                for contacto in resultados:
                    print(contacto)
            else:
                print("No se encontraron contactos.") 
        case "4":
            archivo = input("Ingrese el nombre del archivo CSV para importar: ")
            contactos = importar_contactos(archivo)
            if len(contactos):
                agenda.contactos.extend(contactos)
                print("Contactos importados correctamente.")
        case "5":
            archivo = input("Ingrese el nombre del archivo CSV para exportar: ")
            exportar_contactos(agenda.contactos, archivo)
            print("Contactos exportados correctamente.")
        case "6":
            print("Muchas gracias por usar mi sistema de gestión de contactos.")
            break
        case _:
            print("No existe la opción ingresada")
    
    # Espera unos segundos para desplegar el menú
    time.sleep(2)    
