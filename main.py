# Importamos tkinter
import tkinter as tk
# Importamos ventanas emergentes
from tkinter import messagebox
# IMPORTAMOS CLASES DEL PROYECTO
from modelos.cliente import Cliente
from modelos.servicios_especializados import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from modelos.reserva import Reserva
from utilidades.logger import registrar_log
# LISTAS INTERNAS
# Lista para almacenar clientes
clientes = []
# Lista para almacenar reservas
reservas = []
# Funcion para registrar clientes
def registrar_cliente():
    # Manejo de errores
    try:
        # Capturamos nombre
        nombre = entry_nombre.get()
        # Capturamos correo
        correo = entry_correo.get()
        # Capturamos telefono
        telefono = entry_telefono.get()
        # Creamos objeto cliente
        cliente = Cliente(
            nombre,
            correo,
            telefono
        )
        # Guardamos cliente
        clientes.append(cliente)
        # Registramos evento
        registrar_log(
            f"Cliente registrado: {nombre}"
        )
        # Mostramos mensaje exitoso
        messagebox.showinfo(
            "Exito",
            "Cliente registrado correctamente"
        )
    # Capturamos excepciones
    except Exception as e:
        # Registramos error
        registrar_log(
            f"ERROR cliente: {e}"
        )
        # Mostramos mensaje error
        messagebox.showerror(
            "Error",
            str(e)
        )
# Funcion para crear reservas
def crear_reserva():
    # Manejo de errores
    try:
        # Validamos clientes
        if len(clientes) == 0:
            raise Exception(
                "Debe registrar un cliente primero"
            )
        # Capturamos horas
        horas = int(
            entry_horas.get()
        )
        # Capturamos opcion
        opcion = servicio_var.get()
        # Validamos servicio sala
        if opcion == "Sala":
            servicio = ReservaSala(
                "Sala VIP",
                100
            )
        # Validamos servicio equipo
        elif opcion == "Equipo":
            servicio = AlquilerEquipo(
                "Laptop Gamer",
                80
            )
        # Servicio asesoria
        else:
            servicio = AsesoriaEspecializada(
                "Consultoria TI",
                150
            )
        # Creamos reserva
        reserva = Reserva(
            clientes[-1],
            servicio,
            horas
        )
        # Procesamos reserva
        total = reserva.procesar_reserva()
        # Guardamos reserva
        reservas.append(
            reserva
        )
        # Registramos log
        registrar_log(
            f"Reserva creada correctamente Total: {total}"
        )
        # Mostramos informacion
        texto_resultado.insert(
            tk.END,
            reserva.mostrar_reserva()
        )
        # Mostramos total
        texto_resultado.insert(
            tk.END,
            f"Costo Total: {total}\n"
        )
        # Mostramos separador
        texto_resultado.insert(
            tk.END,
            "========================\n"
        )
        # Mostramos mensaje
        messagebox.showinfo(
            "Reserva",
            "Reserva procesada correctamente"
        )
    # Capturamos excepciones
    except Exception as e:
        # Registramos error
        registrar_log(
            f"ERROR reserva: {e}"
        )
        # Mostramos error
        messagebox.showerror(
            "Error",
            str(e)
        )
# Creamos ventana
ventana = tk.Tk()
# Titulo ventana
ventana.title(
    "Software FJ - Gestion de Reservas"
)
# Tamaño ventana
ventana.geometry(
    "700x600"
)
# Creamos titulo
label_titulo = tk.Label(
    ventana,
    text="Sistema Integral Software FJ",
    font=("Arial", 18, "bold")
)
# Mostramos titulo
label_titulo.pack(
    pady=10
)
# FORMULARIO CLIENTE
# Etiqueta nombre
label_nombre = tk.Label(
    ventana,
    text="Nombre"
)
label_nombre.pack()
# Caja texto nombre
entry_nombre = tk.Entry(
    ventana,
    width=40
)
entry_nombre.pack()
# Etiqueta correo
label_correo = tk.Label(
    ventana,
    text="Correo"
)
label_correo.pack()
# Caja texto correo
entry_correo = tk.Entry(
    ventana,
    width=40
)
entry_correo.pack()
# Etiqueta telefono
label_telefono = tk.Label(
    ventana,
    text="Telefono"
)
label_telefono.pack()
# Caja texto telefono
entry_telefono = tk.Entry(
    ventana,
    width=40
)
entry_telefono.pack()
# Boton registrar cliente
boton_cliente = tk.Button(
    ventana,
    text="Registrar Cliente",
    command=registrar_cliente,
    bg="green",
    fg="white"
)
# Mostramos boton
boton_cliente.pack(
    pady=10
)
# SERVICIOS
# Etiqueta servicio
label_servicio = tk.Label(
    ventana,
    text="Seleccione Servicio"
)
label_servicio.pack()
# Variable servicios
servicio_var = tk.StringVar()
# Valor inicial
servicio_var.set(
    "Sala"
)
# Menu desplegable
menu_servicios = tk.OptionMenu(
    ventana,
    servicio_var,
    "Sala",
    "Equipo",
    "Asesoria"
)
# Mostramos menu
menu_servicios.pack()
# HORAS
# Etiqueta horas
label_horas = tk.Label(
    ventana,
    text="Horas"
)
label_horas.pack()
# Caja texto horas
entry_horas = tk.Entry(
    ventana,
    width=20
)
entry_horas.pack()
# Boton reserva
boton_reserva = tk.Button(
    ventana,
    text="Procesar Reserva",
    command=crear_reserva,
    bg="blue",
    fg="white"
)
# Mostramos boton
boton_reserva.pack(
    pady=10
)
# AREA RESULTADOS
# Area de texto
texto_resultado = tk.Text(
    ventana,
    width=80,
    height=15
)
# Mostramos area
texto_resultado.pack(
    pady=20
)
# Ejecutamos ventana
ventana.mainloop()