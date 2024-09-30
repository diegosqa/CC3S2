# Programación Orientada a Objetos (POO) en Python - Conceptos Básicos y Avanzados

# -------------------------------
# Concepto Básico: Clase y Objeto
# -------------------------------
class Persona:
    # Constructor de la clase (Método especial __init__)
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # Método de instancia
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Crear un objeto de la clase Persona
persona1 = Persona("Carlos", 30)
persona1.saludar()  # Output: Hola, soy Carlos y tengo 30 años.


# ---------------------------------------
# Concepto Avanzado: Atributos y Métodos
# ---------------------------------------
class Perro:
    especie = "Canino"  # Atributo de clase (compartido por todas las instancias)

    def __init__(self, nombre, raza):
        self.nombre = nombre  # Atributo de instancia
        self.raza = raza      # Atributo de instancia

    # Método de instancia
    def describir(self):
        print(f"Soy un {self.raza} llamado {self.nombre}.")

perro1 = Perro("Max", "Labrador")
perro1.describir()  # Output: Soy un Labrador llamado Max.
print(Perro.especie)  # Output: Canino


# --------------------------------
# Concepto Avanzado: Encapsulamiento
# --------------------------------
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca       # Público
        self.__modelo = modelo   # Privado (encapsulado)

    # Método para acceder al atributo privado
    def obtener_modelo(self):
        return self.__modelo

coche1 = Coche("Toyota", "Corolla")
print(coche1.marca)                # Output: Toyota
print(coche1.obtener_modelo())     # Output: Corolla


# -------------------------------
# Concepto Avanzado: Herencia
# -------------------------------
class Estudiante(Persona):  # Hereda de la clase Persona
    def __init__(self, nombre, edad, universidad):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase padre
        self.universidad = universidad

    def mostrar_universidad(self):
        print(f"Estudio en {self.universidad}.")

estudiante1 = Estudiante("Ana", 22, "PUCP")
estudiante1.saludar()               # Hereda el método de Persona
estudiante1.mostrar_universidad()   # Output: Estudio en PUCP


# -----------------------------------------
# Concepto Avanzado: Polimorfismo
# -----------------------------------------
class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado en la subclase")

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

perro = Perro()
gato = Gato()

print(perro.hacer_sonido())  # Output: Guau
print(gato.hacer_sonido())   # Output: Miau


# -----------------------------------------
# Concepto Avanzado: Sobrecarga de Operadores
# -----------------------------------------
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Sobrecarga del operador +
    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

    # Método especial para representación en cadena
    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Punto(2, 3)
p2 = Punto(4, 5)
resultado = p1 + p2
print(resultado)  # Output: (6, 8)


# -------------------------------------------
# Concepto Avanzado: Métodos Estáticos y de Clase
# -------------------------------------------
class Matematica:
    @staticmethod
    def sumar(a, b):
        return a + b

    @classmethod
    def mostrar_clase(cls):
        print(f"Esta es la clase {cls.__name__}")

# Llamar método estático
print(Matematica.sumar(5, 10))  # Output: 15

# Llamar método de clase
Matematica.mostrar_clase()  # Output: Esta es la clase Matematica


# -------------------------------------------
# Concepto Avanzado: Herencia Múltiple
# -------------------------------------------
class Trabajador:
    def __init__(self, trabajo):
        self.trabajo = trabajo

    def mostrar_trabajo(self):
        print(f"Trabajo como {self.trabajo}.")

class EstudianteTrabajador(Persona, Trabajador):
    def __init__(self, nombre, edad, trabajo, universidad):
        Persona.__init__(self, nombre, edad)
        Trabajador.__init__(self, trabajo)
        self.universidad = universidad

    def mostrar_info(self):
        print(f"Soy {self.nombre}, estudio en {self.universidad} y trabajo como {self.trabajo}.")

persona1 = EstudianteTrabajador("Ana", 22, "Ingeniera", "PUCP")
persona1.mostrar_info()  # Output: Soy Ana, estudio en PUCP y trabajo como Ingeniera.


# -------------------------------------------
# Concepto Avanzado: Clases Abstractas
# -------------------------------------------
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def moverse(self):
        pass

class Coche(Vehiculo):
    def moverse(self):
        print("El coche está avanzando.")

coche = Coche()
coche.moverse()  # Output: El coche está avanzando.


# -------------------------------------------
# Concepto Avanzado: Excepciones Personalizadas
# -------------------------------------------
class ErrorPersonalizado(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def dividir(a, b):
    if b == 0:
        raise ErrorPersonalizado("No se puede dividir entre cero.")
    return a / b

try:
    resultado = dividir(10, 0)
except ErrorPersonalizado as e:
    print(f"Error: {e}")  # Output: Error: No se puede dividir entre cero.
