import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Variable global para el ID
global_id = 1

def cargar_ids_usuarios(perfil_combobox):
    try:
        with open('usuarios.txt', 'r') as file:
            lines = file.readlines()
            ids_usuarios = [line.split(',')[0] for line in lines]
            perfiles = ["--Selecciona ID de usuario--"] + ids_usuarios
            perfil_combobox['values'] = perfiles
            perfil_combobox.current(0)  # Establece el valor por defecto
            return perfiles  # Devuelve la lista de perfiles
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo usuarios.txt")

def crear_ventana_registro(ventana):
    # Función para manejar el botón Sign Up y abrir una nueva ventana de registro
    ventana_registro = tk.Toplevel(ventana)
    ventana_registro.title("Registro de cliente")

    # Variables para almacenar la información del nuevo usuario
    ID_usu_var = tk.StringVar()
    nombre_var = tk.StringVar()
    ap_paterno_var = tk.StringVar()
    ap_materno_var = tk.StringVar()
    telefono_var = tk.StringVar()
    
    # Función para guardar la información en un archivo de texto
    def guardar_usuario():
        global global_id  # Indica que estamos utilizando la variable global_id definida fuera de esta función
        # Obtener los valores de las variables
        id_usuario = ID_usu_var.get()
        nombre = nombre_var.get()
        ap_paterno = ap_paterno_var.get()
        ap_materno = ap_materno_var.get()
        telefono = telefono_var.get()

        # Validar que se hayan ingresado todos los datos
        if not id_usuario or not nombre or not ap_paterno or not ap_materno or not telefono:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return
        
        with open("clientes.txt", "a") as archivo:
            archivo.write(f"{global_id},")
            archivo.write(f"{ID_usu_var.get()},")
            archivo.write(f"{nombre_var.get()},")
            archivo.write(f"{ap_paterno_var.get()},")
            archivo.write(f"{ap_materno_var.get()},")
            archivo.write(f"{telefono_var.get()}\n")
            
        global_id += 1
        ventana_registro.destroy()
        messagebox.showinfo("Éxito", "Cliente guardado correctamente.")

    # Interfaz de la ventana de registro

    # Etiqueta y combobox para el perfil
    ttk.Label(ventana_registro, text="ID usuario").grid(row=0, column=0, padx=10, pady=10)

    perfil_combobox = ttk.Combobox(ventana_registro, textvariable=ID_usu_var, state="readonly")
    perfil_combobox.grid(row=0, column=1, padx=10, pady=10)

    perfiles = cargar_ids_usuarios(perfil_combobox)

    ttk.Label(ventana_registro, text="Nombre:").grid(row=1, column=0, padx=10, pady=10)
    ttk.Entry(ventana_registro, textvariable=nombre_var).grid(row=1, column=1, padx=10, pady=10)

    ttk.Label(ventana_registro, text="Apellido Paterno:").grid(row=2, column=0, padx=10, pady=10)
    ttk.Entry(ventana_registro, textvariable=ap_paterno_var).grid(row=2, column=1, padx=10, pady=10)

    ttk.Label(ventana_registro, text="Apellido Materno:").grid(row=3, column=0, padx=10, pady=10)
    ttk.Entry(ventana_registro, textvariable=ap_materno_var).grid(row=3, column=1, padx=10, pady=10)

    ttk.Label(ventana_registro, text="Teléfono:").grid(row=4, column=0, padx=10, pady=10)
    ttk.Entry(ventana_registro, textvariable=telefono_var).grid(row=4, column=1, padx=10, pady=10)


    ttk.Button(ventana_registro, text="Guardar", command=guardar_usuario).grid(row=5, column=0, columnspan=4, pady=10)