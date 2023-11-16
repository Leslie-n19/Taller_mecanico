import tkinter as tk
from tkinter import ttk
from login import iniciar_sesion, crear_ventana_registro

def crear_pestana_login(ventana, nombre):
    pestaña = ttk.Frame(ventana)
    pestaña.pack(expand=True, fill='both')

    ttk.Label(pestaña, text="Usuario:").grid(row=0, column=0, padx=10, pady=10)
    ttk.Entry(pestaña, textvariable=usuario_var).grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(pestaña, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10)
    ttk.Entry(pestaña, textvariable=contraseña_var, show="*").grid(row=1, column=1, padx=10, pady=10)

    ttk.Button(pestaña, text="Log In", command=lambda: iniciar_sesion(usuario_var, contraseña_var)).grid(row=2, column=0, columnspan=2, pady=10)
    ttk.Button(pestaña, text="Sign Up", command=lambda: crear_ventana_registro(ventana)).grid(row=3, column=0, columnspan=2, pady=10)

    controlador.add(pestaña, text=nombre)

ventana = tk.Tk()
ventana.title("Aplicación con Pestañas")

controlador = ttk.Notebook(ventana)

usuario_var = tk.StringVar()
contraseña_var = tk.StringVar()

crear_pestana_login(ventana, "Log In")

controlador.pack(expand=1, fill="both")
ventana.mainloop()
