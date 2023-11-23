import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Variable global para el ID
global_id = 1

def cargar_ids_clientes(perfil_combobox):
    try:
        with open('clientes.txt', 'r') as file:
            lines = file.readlines()
            ids_clientes = [line.split(',')[0] for line in lines]
            perfiles = ["--Selecciona ID de cliente--"] + ids_clientes
            perfil_combobox['values'] = perfiles
            perfil_combobox.current(0)  # Establece el valor por defecto
            return perfiles  # Devuelve la lista de perfiles
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo clientes.txt")

def crear_ventana_registro_vehiculo(ventana):
    # Función para manejar el botón Sign Up y abrir una nueva ventana de registro
    ventana_registro = tk.Toplevel(ventana)
    ventana_registro.title("Registro de vehículo")

    # Variables para almacenar la información del nuevo usuario
    ID_cli_var = tk.StringVar()
    matricula_var = tk.StringVar()
    fecha_var = tk.StringVar()
    marca_var = tk.StringVar()
    modelo_var = tk.StringVar()
    
    # Función para guardar la información en un archivo de texto
    def guardar_usuario():
        global global_id  # Indica que estamos utilizando la variable global_id definida fuera de esta función
        # Obtener los valores de las variables
        id_usuario = ID_cli_var.get()
        nombre = matricula_var.get()
        fecha = fecha_var.get()
        marca = marca_var.get()
        modelo = modelo_var.get()

        # Validar que se hayan ingresado todos los datos
        if not id_usuario or not nombre or not fecha or not marca or not modelo:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return
        
        with open("vehiculos.txt", "a") as archivo:
            archivo.write(f"{global_id},")
            archivo.write(f"{ID_cli_var.get()},")
            archivo.write(f"{matricula_var.get()},")
            archivo.write(f"{fecha_var.get()},")
            archivo.write(f"{marca_var.get()},")
            archivo.write(f"{modelo_var.get()}\n")
            
        global_id += 1
        ventana_registro.destroy()
        messagebox.showinfo("Éxito", "Vehículo guardado correctamente.")

    # Interfaz de la ventana de registro

    # Etiqueta y combobox para el perfil
    ttk.Label(ventana_registro, text="ID cliente").grid(row=0, column=0, padx=10, pady=10)

    perfil_combobox = ttk.Combobox(ventana_registro, textvariable=ID_cli_var, state="readonly")
    perfil_combobox.grid(row=0, column=1, padx=10, pady=10)

    perfiles = cargar_ids_clientes(perfil_combobox)

    ttk.Label(ventana_registro, text="Matricula:").grid(row=1, column=0, padx=10, pady=10)
    ttk.Entry(ventana_registro, textvariable=matricula_var).grid(row=1, column=1, padx=10, pady=10)

    ttk.Label(ventana_registro, text="Fecha DD/MM/AAAA:").grid(row=2, column=0, padx=10, pady=10)
    ttk.Entry(ventana_registro, textvariable=fecha_var).grid(row=2, column=1, padx=10, pady=10)

    ttk.Label(ventana_registro, text="Marca:").grid(row=3, column=0, padx=10, pady=10)
    ttk.Entry(ventana_registro, textvariable=marca_var).grid(row=3, column=1, padx=10, pady=10)

    ttk.Label(ventana_registro, text="Modelo:").grid(row=4, column=0, padx=10, pady=10)
    ttk.Entry(ventana_registro, textvariable=modelo_var).grid(row=4, column=1, padx=10, pady=10)


    ttk.Button(ventana_registro, text="Guardar", command=guardar_usuario).grid(row=5, column=0, columnspan=4, pady=10)

def buscar_vehiculo (ID_var_vehiculo, id_cli, id_vehiculo, matricula, fecha, marca, modelo):
    usuario_encontrado = False
    print(ID_var_vehiculo.get())
    # Lee el archivo de texto (puedes cambiar el nombre y formato según tu necesidad)
    with open('vehiculos.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if data[0] == ID_var_vehiculo.get():
                # Rellena los campos con la información encontrada
                id_vehiculo.config(state='normal')
                id_vehiculo.delete(0, tk.END)
                id_vehiculo.insert(0, data[0])
                id_vehiculo.config(state='disabled')

                id_cli.config(state='normal')
                id_cli.delete(0, tk.END)
                id_cli.insert(0, data[1])
                id_cli.config(state='disabled')

                matricula.config(state='normal')
                matricula.delete(0, tk.END)
                matricula.insert(0, data[2])
                matricula.config(state='disabled')

                fecha.config(state='normal')
                fecha.delete(0, tk.END)
                fecha.insert(0, data[3])
                fecha.config(state='disabled')

                marca.config(state='normal')
                marca.delete(0, tk.END)
                marca.insert(0, data[4])
                marca.config(state='disabled')

                modelo.config(state='normal')
                modelo.delete(0, tk.END)
                modelo.insert(0, data[5])
                modelo.config(state='disabled')
                
                usuario_encontrado = True
                break

        if not usuario_encontrado:
                messagebox.showinfo("Alerta", "Vehículo no encontrado")

def habilitar_edicion_vehiculo(id_cli, id_vehiculo, matricula, fecha, marca, modelo):
    id_cli.config(state='normal')
    id_vehiculo.config(state='normal')
    matricula.config(state='normal')
    fecha.config(state='normal')
    marca.config(state='normal')
    modelo.config(state='normal')

def guardar_cambios_vehiculo(ID_var_vehiculo, id_cli, id_vehiculo, matricula, fecha, marca, modelo):
    # Leer el archivo de usuarios
    with open('vehiculos.txt', 'r') as file:
        lines = file.readlines()

    # Buscar la línea correspondiente al ID_var
    for i, line in enumerate(lines):
        data = line.strip().split(',')
        if data[0] == ID_var_vehiculo.get():
            # Modificar los campos con los valores actuales
            data[1] = id_cli.get()
            data[2] = matricula.get()
            data[3] = fecha.get()
            data[4] = marca.get()
            data[5] = modelo.get()
            lines[i] = ','.join(data) + '\n'
            break

    # Escribir las líneas modificadas de vuelta al archivo
    with open('vehiculos.txt', 'w') as file:
        file.writelines(lines)

    # Deshabilitar la edición después de guardar los cambios
    id_cli.config(state='disabled')
    id_vehiculo.config(state='disabled')
    matricula.config(state='disabled')
    fecha.config(state='disabled')
    marca.config(state='disabled')
    modelo.config(state='disabled')

    # Escribir las líneas modificadas de vuelta al archivo
    with open('vehiculos.txt', 'w') as file:
        file.writelines(lines)

    # Deshabilitar la edición después de guardar los cambios
    id_cli.config(state='disabled')
    id_vehiculo.config(state='disabled')
    matricula.config(state='disabled')
    fecha.config(state='disabled')
    marca.config(state='disabled')
    modelo.config(state='disabled')

    messagebox.showinfo("Éxito", "Vehículo editado correctamente")

def eliminar_vehiculo(ID_var_vehiculo, id_cli, id_vehiculo, matricula, fecha, marca, modelo):
    # Leer el archivo de usuarios
    with open('vehiculos.txt', 'r') as file:
        lines = file.readlines()

    # Buscar la línea correspondiente al ID_var
    for i, line in enumerate(lines):
        data = line.strip().split(',')
        if data[0] == ID_var_vehiculo.get():
            # Eliminar el usuario
            del lines[i]
            break
    else:
        # Si el bucle no se rompió, el usuario no se encontró
        messagebox.showerror("Error", "No se pudo encontrar el vehículo para eliminar")
        return

    # Escribir las líneas modificadas de vuelta al archivo
    with open('vehiculos.txt', 'w') as file:
        file.writelines(lines)

    habilitar_edicion_vehiculo(id_cli, id_vehiculo, matricula, fecha, marca, modelo)

    # Limpiar y deshabilitar los campos después de eliminar el usuario
    id_cli.delete(0, tk.END)
    id_vehiculo.delete(0, tk.END)
    matricula.delete(0, tk.END)
    fecha.delete(0, tk.END)
    marca.delete(0, tk.END)
    modelo.delete(0, tk.END)
    
    id_cli.config(state='disabled')
    id_vehiculo.config(state='disabled')
    matricula.config(state='disabled')
    fecha.config(state='disabled')
    marca.config(state='disabled')
    modelo.config(state='disabled')
    
    # Mostrar ventana de alerta
    messagebox.showinfo("Éxito", "Vehículo eliminado correctamente")