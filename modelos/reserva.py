# Importamos excepcion personalizada
from excepciones.excepciones import ReservaError
# Clase Reserva
class Reserva:
# Constructor
    def __init__(self, cliente, servicio, horas):
# Validamos duracion
        if horas <= 0:
            raise ReservaError(
                "La duracion debe ser mayor a cero"
            )
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"
# Confirmar reserva
    def confirmar(self):

        self.estado = "Confirmada"
# Cancelar reserva
    def cancelar(self):
        self.estado = "Cancelada"
# Procesar reserva
    def procesar_reserva(self):
        try:
# Calculamos costo
            costo = self.servicio.calcular_costo(
                self.horas
            )
        except Exception as error:
# Encadenamiento excepcion
            raise ReservaError(
                "Error al procesar reserva"
            ) from error
        else:
# Confirmamos reserva
            self.confirmar()
            return costo
        finally:
            print(
                "Proceso finalizado"
            )
# Mostrar informacion
    def mostrar_reserva(self):
        return f"""
Cliente: {self.cliente.get_nombre()}
Servicio: {self.servicio.nombre}
Horas: {self.horas}
Estado: {self.estado}
"""