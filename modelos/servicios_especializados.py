# Importamos servicio
from modelos.servicio import Servicio
# Importamos excepciones
from excepciones.excepciones import ServicioError
# CLASE RESERVA DE SALAS
class ReservaSala(Servicio):
# Metodo polimorfico
    def calcular_costo(self, horas):

        if horas <= 0:

            raise ServicioError(
                "Horas invalidas"
            )
        return self.tarifa * horas
# Metodo sobrescrito
    def descripcion(self):
        return "Servicio de reserva de salas"
    # Metodo heredado
    def mostrar_informacion(self):
        return f"""
Servicio: {self.nombre}
Tarifa: {self.tarifa}
"""
# CLASE ALQUILER EQUIPO
class AlquilerEquipo(Servicio):
# Metodo sobrescrito
    def calcular_costo(self, horas):
        if horas <= 0:
            raise ServicioError(
                "Horas invalidas"
            )
        seguro = 20
        return (self.tarifa * horas) + seguro
    def descripcion(self):
        return "Servicio de alquiler de equipos"
    def mostrar_informacion(self):
        return f"""
Servicio: {self.nombre}
Tarifa: {self.tarifa}
"""
# CLASE ASESORIA
class AsesoriaEspecializada(Servicio):
# Metodo sobrescrito
    def calcular_costo(self, horas):
        if horas <= 0:
            raise ServicioError(
                "Horas invalidas"
            )
        iva = 0.19
        return (self.tarifa * horas) * (1 + iva)
    def descripcion(self):
        return "Servicio de asesoria especializada"
    def mostrar_informacion(self):
        return f"""
Servicio: {self.nombre}
Tarifa: {self.tarifa}
"""