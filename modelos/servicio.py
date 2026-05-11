# Importamos herramientas abstractas
from abc import ABC, abstractmethod
# Importamos entidad
from modelos.entidad import Entidad
# Clase abstracta Servicio
class Servicio(Entidad, ABC):
# Constructor
    def __init__(self, nombre, tarifa):
        self.nombre = nombre
        self.tarifa = tarifa
# Metodo abstracto
    @abstractmethod
    def calcular_costo(self, horas):
        pass
# Metodo abstracto
    @abstractmethod
    def descripcion(self):
        pass