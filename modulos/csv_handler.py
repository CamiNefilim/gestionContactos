import csv
from clases import Contacto

def exportar_contactos(contactos, archivo):
    try:
        
        with open(archivo, 'w', newline='',encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Nombre', 'Teléfono', 'Email'])  # Encabezados
            for contacto in contactos:
                writer.writerow([contacto.nombre, contacto.telefono, contacto.email])
    except Exception:
        print("Ocurrió un error inesperado al intentar exportar contactos.")
        
def importar_contactos(archivo):
    contactos = []
    try:
        with open(archivo, 'r',encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacto = Contacto(row['Nombre'], row['Teléfono'], row['Email'])
                contactos.append(contacto)
    except Exception:
        print("Ocurrió un error inesperado al intentar exportar contactos.")
    return contactos
