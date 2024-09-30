class Agenda:
    #Definimos nuestro constructor
    def __init__(self):
        self.contactos = {} 

    def agregar_contacto(self,nombre,telefono,email):
        #Almacenar contactos
        self.contactos[nombre]={"telefono": telefono, "email": email}
        print(f"Contacto {nombre} agregado con éxtio")

    def eliminar_contacto(self,nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
        else:
            print(f"La persona {nombre} no esta en la lista")
    def mostrar_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda")
        else:
            for nombre,info in self.contactos.items():
                print(f"Nombre: {nombre}, Teléfono: {info['telefono']}, Email: {info['email']}")

    def buscar_contacto(self,nombre):
        if nombre in self.contactos:
            info = self.contactos[nombre]
            print(f"Nombre: {nombre}, Teléfono: {info['telefono']}, Email: {info['email']}")
        else:
            print(f"El contacto {nombre} no fue encontrado")

mi_agenda = Agenda()

mi_agenda.agregar_contacto("Carlos", "123456789", "carlos@example.com")
mi_agenda.agregar_contacto("Ana", "987654321", "ana@example.com")

# Mostrar todos los contactos
mi_agenda.mostrar_contactos()

# Buscar un contacto
mi_agenda.buscar_contacto("Ana")

# Eliminar un contacto
mi_agenda.eliminar_contacto("Carlos")

# Mostrar contactos después de eliminar
mi_agenda.mostrar_contactos()