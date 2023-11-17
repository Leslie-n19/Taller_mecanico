import tkinter as tk
from tkinter import ttk
from login import crear_ventana_registro, iniciar_sesion


def crear_pestana(ventana, nombre):
    pestaña = ttk.Frame(ventana)
    pestaña.pack(expand=True, fill='both')

    if nombre == "Log In":
        ttk.Label(pestaña, text="Usuario:").grid(row=0, column=0, padx=10, pady=10)
        ttk.Entry(pestaña, textvariable=usuario_var).grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(pestaña, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10)
        ttk.Entry(pestaña, textvariable=contraseña_var, show="*").grid(row=1, column=1, padx=10, pady=10)

        ttk.Button(pestaña, text="Log In", command=lambda: iniciar_sesion(usuario_var, contraseña_var)).grid(row=2, column=0, columnspan=2, pady=10)
        ttk.Button(pestaña, text="Sign Up", command=lambda: crear_ventana_registro(ventana)).grid(row=3, column=0, columnspan=2, pady=10)
    elif nombre == "Usuarios":
        ttk.Label(pestaña, text="Buscar por ID:").grid(row=0, column=0, padx=10, pady=10)
        ttk.Entry(pestaña, textvariable=ID_var, state='normal').grid(row=0, column=1, padx=10, pady=10)
        ttk.Button(pestaña, text="Buscar", command=lambda: buscar_usuario(id_entry, nombre_entry, apellidoP_entry, apellidoM_entry,
                                                                          perfil_entry, telefono_entry, direccion_entry, usuario_entry, 
                                                                          contraseña_entry)).grid(row=0, column=2, pady=10)


        ttk.Label(pestaña, text="ID:").grid(row=1, column=0, padx=10, pady=10)
        id_entry = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        id_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(pestaña, text="Nombre:").grid(row=2, column=0, padx=10, pady=10)
        nombre_entry = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        nombre_entry.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(pestaña, text="Apellido Paterno:").grid(row=3, column=0, padx=10, pady=10)
        apellidoP_entry = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        apellidoP_entry.grid(row=3, column=1, padx=10, pady=10)

        ttk.Label(pestaña, text="Apellido Materno:").grid(row=4, column=0, padx=10, pady=10)
        apellidoM_entry = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        apellidoM_entry.grid(row=4, column=1, padx=10, pady=10)

        ttk.Label(pestaña, text="Perfil:").grid(row=5, column=0, padx=10, pady=10)
        perfil_entry = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        perfil_entry.grid(row=5, column=1, padx=10, pady=10)

        ttk.Label(pestaña, text="Teléfono:").grid(row=6, column=0, padx=10, pady=10)
        telefono_entry = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        telefono_entry.grid(row=6, column=1, padx=10, pady=10)

        ttk.Label(pestaña, text="Dirección:").grid(row=7, column=0, padx=10, pady=10)
        direccion_entry = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        direccion_entry.grid(row=7, column=1, padx=10, pady=10)

        ttk.Label(pestaña, text="Usuario:").grid(row=8, column=0, padx=10, pady=10)
        usuario_entry = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        usuario_entry.grid(row=8, column=1, padx=10, pady=10)

        ttk.Label(pestaña, text="Contraseña:").grid(row=9, column=0, padx=10, pady=10)
        contraseña_entry = ttk.Entry(pestaña, state='disabled', show="*", textvariable=tk.StringVar())
        contraseña_entry.grid(row=9, column=1, padx=10, pady=10)


        ttk.Button(pestaña, text="Editar", command=lambda: print("Botón editar presionado")).grid(row=10, column=0, pady=10)
        ttk.Button(pestaña, text="Eliminar", command=lambda: print("Botón Eliminar presionado")).grid(row=10, column=1, pady=10)
        ttk.Button(pestaña, text="Guardar", command=lambda: print("Botón guardar presionado")).grid(row=10, column=2, pady=10)

            # Agrega más etiquetas, entradas y botones según tus necesidades

    controlador.add(pestaña, text=nombre)

def buscar_usuario(id_entry, nombre_entry, apellidoP_entry, apellidoM_entry, perfil_entry, telefono_entry, direccion_entry, usuario_entry, contraseña_entry):
    # Lee el archivo de texto (puedes cambiar el nombre y formato según tu necesidad)
    with open('usuarios.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if data[0] == ID_var.get():
                # Rellena los campos con la información encontrada
                id_entry.config(state='normal')
                id_entry.delete(0, tk.END)
                id_entry.insert(0, data[0])
                id_entry.config(state='disabled')

                nombre_entry.config(state='normal')
                nombre_entry.delete(0, tk.END)
                nombre_entry.insert(0, data[1])
                nombre_entry.config(state='disabled')

                apellidoP_entry.config(state='normal')
                apellidoP_entry.delete(0, tk.END)
                apellidoP_entry.insert(0, data[2])
                apellidoP_entry.config(state='disabled')

                apellidoM_entry.config(state='normal')
                apellidoM_entry.delete(0, tk.END)
                apellidoM_entry.insert(0, data[3])
                apellidoM_entry.config(state='disabled')

                perfil_entry.config(state='normal')
                perfil_entry.delete(0, tk.END)
                perfil_entry.insert(0, data[4])
                perfil_entry.config(state='disabled')

                telefono_entry.config(state='normal')
                telefono_entry.delete(0, tk.END)
                telefono_entry.insert(0, data[5])
                telefono_entry.config(state='disabled')

                direccion_entry.config(state='normal')
                direccion_entry.delete(0, tk.END)
                direccion_entry.insert(0, data[6])
                direccion_entry.config(state='disabled')

                usuario_entry.config(state='normal')
                usuario_entry.delete(0, tk.END)
                usuario_entry.insert(0, data[7])
                usuario_entry.config(state='disabled')

                contraseña_entry.config(state='normal')
                contraseña_entry.delete(0, tk.END)
                contraseña_entry.insert(0, data[8])
                contraseña_entry.config(state='disabled')
                
                break 

# Crea la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación con Pestañas")

# Crea el controlador de pestañas
controlador = ttk.Notebook(ventana)

# Variables para almacenar la información
ID_var = tk.StringVar()
nombre_var = tk.StringVar()
apellidoP_var = tk.StringVar()
apellidoM_var = tk.StringVar()
perfil_var = tk.StringVar()
telefono_var = tk.StringVar()
direccion_var = tk.StringVar()
usuario_var = tk.StringVar()
contraseña_var = tk.StringVar()

# Crea las dos pestañas
crear_pestana(ventana, "Log In")
crear_pestana(ventana, "Usuarios")
crear_pestana(ventana, "Clientes")
crear_pestana(ventana, "Vehículos")
crear_pestana(ventana, "Reparaciones")
crear_pestana(ventana, "Piezas")

# Empaqueta el controlador de pestañas en la ventana principal
controlador.pack(expand=1, fill="both")

# Inicia el bucle principal de la aplicación
ventana.mainloop()
