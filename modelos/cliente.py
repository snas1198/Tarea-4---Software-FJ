# Importamos clase abstracta
from modelos.entidad import Entidad
# Importamos excepcion personalizada
from excepciones.excepciones import ClienteError
# Clase Cliente
class Cliente(Entidad):
# Constructor
    def __init__(self, nombre, correo, telefono):
        self.set_nombre(nombre)
        self.set_correo(correo)
        self.set_telefono(telefono)
# Setter nombre
    def set_nombre(self, nombre):
# Validamos que no este vacio
        if not nombre.strip():
            raise ClienteError(
                "El nombre no puede estar vacio"
            )
        self.__nombre = nombre
# Getter nombre
    def get_nombre(self):
        return self.__nombre
    # Setter correo
    def set_correo(self, correo):
# Validamos correo
        if "@" not in correo:

            raise ClienteError(
                "Correo invalido"
            )

        self.__correo = correo
# Getter correo
    def get_correo(self):
        return self.__correo
# Setter telefono
    def set_telefono(self, telefono):
# Validamos que sean numeros
        if not telefono.isdigit():
            raise ClienteError(
                "Telefono invalido"
            )
        self.__telefono = telefono
# Getter telefono
    def get_telefono(self):
        return self.__telefono
# Metodo sobrescrito
    def mostrar_informacion(self):
        return f"""
Cliente: {self.__nombre}
Correo: {self.__correo}
Telefono: {self.__telefono}
"""