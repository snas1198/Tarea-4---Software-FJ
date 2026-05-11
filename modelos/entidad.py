from abc import ABC, abstractmethod # Importamos herramientas para crear clases abstractas
class Entidad(ABC): # Clase abstracta principal

#Método abstracto obligatorio
    @abstractmethod
    def mostrar_informacion(self):
        pass