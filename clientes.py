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

def buscar_usuario(ID_var, id_usu, id_entry, nombre_entry, apellidoP_entry, apellidoM_entry, telefono_entry):
    usuario_encontrado = False
    print(ID_var.get())
    # Lee el archivo de texto (puedes cambiar el nombre y formato según tu necesidad)
    with open('clientes.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if data[0] == ID_var.get():
                # Rellena los campos con la información encontrada
                id_entry.config(state='normal')
                id_entry.delete(0, tk.END)
                id_entry.insert(0, data[0])
                id_entry.config(state='disabled')

                id_usu.config(state='normal')
                id_usu.delete(0, tk.END)
                id_usu.insert(0, data[1])
                id_usu.config(state='disabled')

                nombre_entry.config(state='normal')
                nombre_entry.delete(0, tk.END)
                nombre_entry.insert(0, data[2])
                nombre_entry.config(state='disabled')

                apellidoP_entry.config(state='normal')
                apellidoP_entry.delete(0, tk.END)
                apellidoP_entry.insert(0, data[3])
                apellidoP_entry.config(state='disabled')

                apellidoM_entry.config(state='normal')
                apellidoM_entry.delete(0, tk.END)
                apellidoM_entry.insert(0, data[4])
                apellidoM_entry.config(state='disabled')

                telefono_entry.config(state='normal')
                telefono_entry.delete(0, tk.END)
                telefono_entry.insert(0, data[5])
                telefono_entry.config(state='disabled')
                
                usuario_encontrado = True
                break

        if not usuario_encontrado:
                messagebox.showinfo("Alerta", "Cliente no encontrado")

def habilitar_edicion(id_entry, id_usu, nombre_entry, apellidoP_entry, apellidoM_entry, telefono_entry):
    id_usu.config(state='normal')
    id_entry.config(state='normal')
    nombre_entry.config(state='normal')
    apellidoP_entry.config(state='normal')
    apellidoM_entry.config(state='normal')
    telefono_entry.config(state='normal')

def guardar_cambios(ID_var, id_usu, id_entry, nombre_entry, apellidoP_entry, apellidoM_entry,telefono_entry):
    # Leer el archivo de usuarios
    with open('clientes.txt', 'r') as file:
        lines = file.readlines()

    # Buscar la línea correspondiente al ID_var
    for i, line in enumerate(lines):
        data = line.strip().split(',')
        if data[0] == ID_var.get():
            # Modificar los campos con los valores actuales
            data[1] = id_usu.get()
            data[2] = nombre_entry.get()
            data[3] = apellidoP_entry.get()
            data[4] = apellidoM_entry.get()
            data[5] = telefono_entry.get()
            lines[i] = ','.join(data) + '\n'
            break

    # Escribir las líneas modificadas de vuelta al archivo
    with open('usuarios.txt', 'w') as file:
        file.writelines(lines)

    # Deshabilitar la edición después de guardar los cambios
    id_usu.config(state='disabled')
    id_entry.config(state='disabled')
    nombre_entry.config(state='disabled')
    apellidoP_entry.config(state='disabled')
    apellidoM_entry.config(state='disabled')
    telefono_entry.config(state='disabled')

    # Escribir las líneas modificadas de vuelta al archivo
    with open('clientes.txt', 'w') as file:
        file.writelines(lines)

    # Deshabilitar la edición después de guardar los cambios
    id_usu.config(state='disabled')
    id_entry.config(state='disabled')
    nombre_entry.config(state='disabled')
    apellidoP_entry.config(state='disabled')
    apellidoM_entry.config(state='disabled')
    telefono_entry.config(state='disabled')

    messagebox.showinfo("Éxito", "Usuario editado correctamente")
