# Definir la clase Persona sin el uso de property-decorator
class Persona:
    def __init__(self, nombre, edad, genero):
        self._nombre = nombre
        self._edad = edad
        self._genero = genero

    # Método para obtener el nombre
    def get_nombre(self):
        return self._nombre

    # Método para obtener la edad
    def get_edad(self):
        return self._edad

    # Método para obtener el género
    def get_genero(self):
        return self._genero

    # Método para saludar
    def saludar(self):
        print(f"Hola, soy {self._nombre} y tengo {self._edad} años.")

# Demostración de uso
# Crear una instancia de la clase Persona
persona1 = Persona("Daniel", 19, "Masculino")

# Acceder a los métodos para obtener los atributos
print(f"Nombre: {persona1.get_nombre()}")
print(f"Edad: {persona1.get_edad()}")
print(f"Género: {persona1.get_genero()}")

# Llamar al método saludar
persona1.saludar()
persona1.saludar()
