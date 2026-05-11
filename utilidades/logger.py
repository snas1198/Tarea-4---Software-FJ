# Importamos fecha y hora
from datetime import datetime
# Funcion para registrar eventos y errores
def registrar_log(mensaje):
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(
            f"{datetime.now()} - {mensaje}\n"
        )