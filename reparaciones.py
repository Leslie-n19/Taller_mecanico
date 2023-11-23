import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Variable global para el ID
global_id = 1

def cargar_ids_vehiculos(perfil_combobox):
    try:
        with open('vehiculos.txt', 'r') as file:
            lines = file.readlines()
            ids_vehiculos = [line.split(',')[0] for line in lines]
            perfiles = ["--Selecciona ID del vehículo--"] + ids_vehiculos
            perfil_combobox['values'] = perfiles
            perfil_combobox.current(0)  # Establece el valor por defecto
            return perfiles  # Devuelve la lista de perfiles
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo vehiculos.txt")

def cargar_ids_piezas(perfil_combobox):
    try:
        with open('piezas.txt', 'r') as file:
            lines = file.readlines()
            ids_piezas = [line.split(',')[0] for line in lines]
            perfiles = ["--Selecciona ID del vehículo--"] + ids_piezas
            perfil_combobox['values'] = perfiles
            perfil_combobox.current(0)  # Establece el valor por defecto
            return perfiles  # Devuelve la lista de perfiles
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo piezas.txt")

def crear_ventana_registro_reparacion(ventana):
    # Función para manejar el botón Sign Up y abrir una nueva ventana de registro
    ventana_registro = tk.Toplevel(ventana)
    ventana_registro.title("Registro de reparación")

    # Variables para almacenar la información del nuevo usuario
    ID_veh_var = tk.StringVar() #ID externos
    ID_pieza_var = tk.StringVar() #ID externo
    fechaEn_var = tk.StringVar()
    fechaSal_var = tk.StringVar()
    falla_var = tk.StringVar()
    cantidad_var = tk.StringVar()
    
    # Función para guardar la información en un archivo de texto
    def guardar_usuario():
        global global_id  # Indica que estamos utilizando la variable global_id definida fuera de esta función
        # Obtener los valores de las variables
        id_veh = ID_veh_var.get()
        id_pieza = ID_pieza_var.get()
        fechaEn = fechaEn_var.get()
        fechaSal = fechaSal_var.get()
        falla = falla_var.get()
        cantidad = cantidad_var.get()

        # Validar que se hayan ingresado todos los datos
        if not id_veh or not id_pieza or not fechaEn or not fechaSal or not falla or not cantidad:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return
        
        with open("reparaciones.txt", "a") as archivo:
            archivo.write(f"{global_id},")
            archivo.write(f"{ID_veh_var.get()},")
            archivo.write(f"{ID_pieza_var.get()},")
            archivo.write(f"{fechaEn_var.get()},")
            archivo.write(f"{fechaSal_var.get()},")
            archivo.write(f"{falla_var.get()},")
            archivo.write(f"{cantidad_var.get()}\n")
            
        global_id += 1
        ventana_registro.destroy()
        messagebox.showinfo("Éxito", "Reparación guardado correctamente.")

    # Interfaz de la ventana de registro

    # Etiqueta y combobox para vehículos
    ttk.Label(ventana_registro, text="ID Vehículo").grid(row=0, column=0, padx=10, pady=10)

    perfil_combobox = ttk.Combobox(ventana_registro, textvariable=ID_veh_var, state="readonly")
    perfil_combobox.grid(row=0, column=1, padx=10, pady=10)

    perfiles = cargar_ids_vehiculos(perfil_combobox)

    # Etiqueta y combobox para piezas
    ttk.Label(ventana_registro, text="ID pieza").grid(row=1, column=0, padx=10, pady=10)

    perfil_combobox = ttk.Combobox(ventana_registro, textvariable=ID_pieza_var, state="readonly")
    perfil_combobox.grid(row=1, column=1, padx=10, pady=10)

    perfiles = cargar_ids_piezas(perfil_combobox)

    ttk.Label(ventana_registro, text="Fecha entrada DD/MM/AAAA:").grid(row=2, column=0, padx=10, pady=10)
    ttk.Entry(ventana_registro, textvariable=fechaEn_var).grid(row=2, column=1, padx=10, pady=10)

    ttk.Label(ventana_registro, text="Fecha Salida DD/MM/AAAA:").grid(row=3, column=0, padx=10, pady=10)
    ttk.Entry(ventana_registro, textvariable=fechaSal_var).grid(row=3, column=1, padx=10, pady=10)

    ttk.Label(ventana_registro, text="Falla:").grid(row=4, column=0, padx=10, pady=10)
    ttk.Entry(ventana_registro, textvariable=falla_var).grid(row=4, column=1, padx=10, pady=10)

    ttk.Label(ventana_registro, text="Cantidad de piezas:").grid(row=5, column=0, padx=10, pady=10)
    ttk.Entry(ventana_registro, textvariable=cantidad_var).grid(row=5, column=1, padx=10, pady=10)


    ttk.Button(ventana_registro, text="Guardar", command=guardar_usuario).grid(row=6, column=0, columnspan=4, pady=10)

def buscar_reparacion(ID_var_repa, id_veh, id_pie, id_reparacion, fechaEn, fechaSal, falla, cantidad):
    usuario_encontrado = False
    print(ID_var_repa.get())
    # Lee el archivo de texto (puedes cambiar el nombre y formato según tu necesidad)
    with open('reparaciones.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if data[0] == ID_var_repa.get():
                # Rellena los campos con la información encontrada
                id_reparacion.config(state='normal')
                id_reparacion.delete(0, tk.END)
                id_reparacion.insert(0, data[0])
                id_reparacion.config(state='disabled')

                id_veh.config(state='normal')
                id_veh.delete(0, tk.END)
                id_veh.insert(0, data[1])
                id_veh.config(state='disabled')

                id_pie.config(state='normal') #ID externo
                id_pie.delete(0, tk.END)
                id_pie.insert(0, data[2])
                id_pie.config(state='disabled')

                fechaEn.config(state='normal')
                fechaEn.delete(0, tk.END)
                fechaEn.insert(0, data[3])
                fechaEn.config(state='disabled')

                fechaSal.config(state='normal')
                fechaSal.delete(0, tk.END)
                fechaSal.insert(0, data[4])
                fechaSal.config(state='disabled')

                falla.config(state='normal')
                falla.delete(0, tk.END)
                falla.insert(0, data[5])
                falla.config(state='disabled')

                cantidad.config(state='normal')
                cantidad.delete(0, tk.END)
                cantidad.insert(0, data[6])
                cantidad.config(state='disabled')
                
                usuario_encontrado = True
                break

        if not usuario_encontrado:
                messagebox.showinfo("Alerta", "Reparación no encontrada")

def habilitar_edicion_reparacion(id_veh, id_pie, id_reparacion, fechaEn, fechaSal, falla, cantidad):
    id_veh.config(state='normal') #ID externo
    id_pie.config(state='normal')
    id_reparacion.config(state='normal')
    fechaEn.config(state='normal')
    fechaSal.config(state='normal')
    falla.config(state='normal')
    cantidad.config(state='normal')

def guardar_cambios_reparacion(ID_var_repa, id_veh, id_pie, id_reparacion, fechaEn, fechaSal, falla, cantidad):
    # Leer el archivo de usuarios
    with open('reparaciones.txt', 'r') as file:
        lines = file.readlines()

    # Buscar la línea correspondiente al ID_var
    for i, line in enumerate(lines):
        data = line.strip().split(',')
        if data[0] == ID_var_repa.get():
            # Modificar los campos con los valores actuales
            data[1] = id_veh.get() #ID externo
            data[2] = id_pie.get()
            data[3] = fechaEn.get()
            data[4] = fechaSal.get()
            data[5] = falla.get()
            data[6] = cantidad.get()
            lines[i] = ','.join(data) + '\n'
            break

    # Escribir las líneas modificadas de vuelta al archivo
    with open('reparaciones.txt', 'w') as file:
        file.writelines(lines)

    # Deshabilitar la edición después de guardar los cambios
    id_veh.config(state='disabled') #Id externo
    id_pie.config(state='disabled')
    id_reparacion.config(state='disabled')
    fechaEn.config(state='disabled')
    fechaSal.config(state='disabled')
    falla.config(state='disabled')
    cantidad.config(state='disabled')

    # Escribir las líneas modificadas de vuelta al archivo
    with open('reparaciones.txt', 'w') as file:
        file.writelines(lines)

    # Deshabilitar la edición después de guardar los cambios
    id_veh.config(state='disabled') #ID externo
    id_pie.config(state='disabled')
    id_reparacion.config(state='disabled')
    fechaEn.config(state='disabled')
    fechaSal.config(state='disabled')
    falla.config(state='disabled')
    cantidad.config(state='disabled')

    messagebox.showinfo("Éxito", "Vehículo editado correctamente")

def eliminar_reparacion(ID_var_repa, id_veh, id_pie, id_reparacion, fechaEn, fechaSal, falla, cantidad):
    # Leer el archivo de usuarios
    with open('reparaciones.txt', 'r') as file:
        lines = file.readlines()

    # Buscar la línea correspondiente al ID_var
    for i, line in enumerate(lines):
        data = line.strip().split(',')
        if data[0] == ID_var_repa.get():
            # Eliminar el usuario
            del lines[i]
            break
    else:
        # Si el bucle no se rompió, el usuario no se encontró
        messagebox.showerror("Error", "No se pudo encontrar la reparación para eliminar")
        return

    # Escribir las líneas modificadas de vuelta al archivo
    with open('reparaciones.txt', 'w') as file:
        file.writelines(lines)

    habilitar_edicion_reparacion(id_veh, id_pie, id_reparacion, fechaEn, fechaSal, falla, cantidad)

    # Limpiar y deshabilitar los campos después de eliminar el usuario
    id_veh.delete(0, tk.END)
    id_pie.delete(0, tk.END)
    id_reparacion.delete(0, tk.END)
    fechaEn.delete(0, tk.END)
    fechaSal.delete(0, tk.END)
    falla.delete(0, tk.END)
    cantidad.delete(0, tk.END)
    
    id_veh.config(state='disabled')
    id_pie.config(state='disabled')
    id_reparacion.config(state='disabled')
    fechaEn.config(state='disabled')
    fechaSal.config(state='disabled')
    falla.config(state='disabled')
    cantidad.config(state='disabled')
    
    # Mostrar ventana de alerta
    messagebox.showinfo("Éxito", "Reparación eliminada correctamente")