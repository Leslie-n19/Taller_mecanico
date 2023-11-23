import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Variable global para el ID
global_id = 1

def crear_ventana_registro_pieza(ventana):
    # Función para manejar el botón Sign Up y abrir una nueva ventana de registro
    ventana_registro = tk.Toplevel(ventana)
    ventana_registro.title("Registro de piezas")

    # Variables para almacenar la información del nuevo usuario
    descripcion_var = tk.StringVar() #ID externos
    stock_var = tk.StringVar() #ID externo
    
    # Función para guardar la información en un archivo de texto
    def guardar_usuario():
        global global_id  # Indica que estamos utilizando la variable global_id definida fuera de esta función
        # Obtener los valores de las variables
        descripcion = descripcion_var.get()
        stock = stock_var.get()


        # Validar que se hayan ingresado todos los datos
        if not descripcion or not stock :
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return
        
        with open("piezas.txt", "a") as archivo:
            archivo.write(f"{global_id},")
            archivo.write(f"{descripcion_var.get()},")
            archivo.write(f"{stock_var.get()}\n")
            
            global_id += 1
        ventana_registro.destroy()
        messagebox.showinfo("Éxito", "Pieza guardado correctamente.")

    # Interfaz de la ventana de registro

    ttk.Label(ventana_registro, text="Descripción:").grid(row=2, column=0, padx=10, pady=10)
    ttk.Entry(ventana_registro, textvariable=descripcion_var).grid(row=2, column=1, padx=10, pady=10)

    ttk.Label(ventana_registro, text="Stock:").grid(row=3, column=0, padx=10, pady=10)
    ttk.Entry(ventana_registro, textvariable=stock_var).grid(row=3, column=1, padx=10, pady=10)

    ttk.Button(ventana_registro, text="Guardar", command=guardar_usuario).grid(row=6, column=0, columnspan=4, pady=10)

def buscar_pieza(ID_var_pieza, id_pieza, descripcion, stock):
    usuario_encontrado = False
    print(ID_var_pieza.get())
    # Lee el archivo de texto (puedes cambiar el nombre y formato según tu necesidad)
    with open('piezas.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if data[0] == ID_var_pieza.get():
                # Rellena los campos con la información encontrada
                id_pieza.config(state='normal')
                id_pieza.delete(0, tk.END)
                id_pieza.insert(0, data[0])
                id_pieza.config(state='disabled')

                descripcion.config(state='normal')
                descripcion.delete(0, tk.END)
                descripcion.insert(0, data[1])
                descripcion.config(state='disabled')

                stock.config(state='normal') 
                stock.delete(0, tk.END)
                stock.insert(0, data[2])
                stock.config(state='disabled')
                
                usuario_encontrado = True
                break

        if not usuario_encontrado:
                messagebox.showinfo("Alerta", "Pieza no encontrada")

def habilitar_edicion_pieza(id_pieza, descripcion, stock):
    descripcion.config(state='normal') 
    stock.config(state='normal')
    id_pieza.config(state='normal')

def guardar_cambios_pieza(ID_var_pieza, id_pieza, descripcion, stock):
    # Leer el archivo de usuarios
    with open('piezas.txt', 'r') as file:
        lines = file.readlines()

    # Buscar la línea correspondiente al ID_var
    for i, line in enumerate(lines):
        data = line.strip().split(',')
        if data[0] == ID_var_pieza.get():
            # Modificar los campos con los valores actuales
            data[1] = descripcion.get() 
            data[2] = stock.get()
            lines[i] = ','.join(data) + '\n'
            break

    # Escribir las líneas modificadas de vuelta al archivo
    with open('piezas.txt', 'w') as file:
        file.writelines(lines)

    # Deshabilitar la edición después de guardar los cambios
    descripcion.config(state='disabled') 
    stock.config(state='disabled')
    id_pieza.config(state='disabled')

    # Escribir las líneas modificadas de vuelta al archivo
    with open('piezas.txt', 'w') as file:
        file.writelines(lines)

    # Deshabilitar la edición después de guardar los cambios
    descripcion.config(state='disabled') 
    stock.config(state='disabled')
    id_pieza.config(state='disabled')

    messagebox.showinfo("Éxito", "Vehículo editado correctamente")

def eliminar_pieza(ID_var_pieza, id_pieza, descripcion, stock):
    # Leer el archivo de usuarios
    with open('piezas.txt', 'r') as file:
        lines = file.readlines()

    # Buscar la línea correspondiente al ID_var
    for i, line in enumerate(lines):
        data = line.strip().split(',')
        if data[0] == ID_var_pieza.get():
            # Eliminar el usuario
            del lines[i]
            break
    else:
        # Si el bucle no se rompió, el usuario no se encontró
        messagebox.showerror("Error", "No se pudo encontrar la reparación para eliminar")
        return

    # Escribir las líneas modificadas de vuelta al archivo
    with open('piezas.txt', 'w') as file:
        file.writelines(lines)

    habilitar_edicion_pieza(id_pieza, descripcion, stock)

    # Limpiar y deshabilitar los campos después de eliminar el usuario
    descripcion.delete(0, tk.END)
    stock.delete(0, tk.END)
    id_pieza.delete(0, tk.END)

    
    descripcion.config(state='disabled')
    stock.config(state='disabled')
    id_pieza.config(state='disabled')

    # Mostrar ventana de alerta
    messagebox.showinfo("Éxito", "Reparación eliminada correctamente")