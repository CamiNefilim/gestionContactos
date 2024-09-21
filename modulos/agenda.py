from .csv_handler import importar_contactos

def agregar_contacto(agenda, contacto):
    agenda.contactos.append(contacto)

def eliminar_contacto(agenda, nombre):
    agenda.contactos = [c for c in agenda.contactos if c.nombre != nombre]

def buscar_contacto(agenda, busqueda):
    return [c for c in agenda.contactos if (busqueda.lower() in c.nombre.lower() or
                                            busqueda in c.telefono or
                                            busqueda.lower() in c.email.lower())]

def importar_contactos(agenda, archivo):    
    agenda.contactos = importar_contactos(archivo)