import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def buscar_usuario(ID_var, id_entry, nombre_entry, apellidoP_entry, apellidoM_entry, perfil_entry, telefono_entry, direccion_entry, usuario_entry, contraseña_entry):
    usuario_encontrado = False
    print(ID_var.get())
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
                
                usuario_encontrado = True
                break

        if not usuario_encontrado:
                messagebox.showinfo("Alerta", "Usuario no encontrado")

def habilitar_edicion(id_entry, nombre_entry, apellidoP_entry, apellidoM_entry, perfil_entry, telefono_entry, direccion_entry, usuario_entry, contraseña_entry):
    id_entry.config(state='normal')
    nombre_entry.config(state='normal')
    apellidoP_entry.config(state='normal')
    apellidoM_entry.config(state='normal')
    perfil_entry.config(state='normal')
    telefono_entry.config(state='normal')
    direccion_entry.config(state='normal')
    usuario_entry.config(state='normal')
    contraseña_entry.config(state='normal')

def guardar_cambios(ID_var, id_entry, nombre_entry, apellidoP_entry, apellidoM_entry, perfil_entry, telefono_entry, direccion_entry, usuario_entry, contraseña_entry):
    # Leer el archivo de usuarios
    with open('usuarios.txt', 'r') as file:
        lines = file.readlines()

    # Buscar la línea correspondiente al ID_var
    for i, line in enumerate(lines):
        data = line.strip().split(',')
        if data[0] == ID_var.get():
            # Modificar los campos con los valores actuales
            data[1] = nombre_entry.get()
            data[2] = apellidoP_entry.get()
            data[3] = apellidoM_entry.get()
            data[4] = perfil_entry.get()
            data[5] = telefono_entry.get()
            data[6] = direccion_entry.get()
            data[7] = usuario_entry.get()
            data[8] = contraseña_entry.get()
            lines[i] = ','.join(data) + '\n'
            break

    # Escribir las líneas modificadas de vuelta al archivo
    with open('usuarios.txt', 'w') as file:
        file.writelines(lines)

    # Deshabilitar la edición después de guardar los cambios
    id_entry.config(state='disabled')
    nombre_entry.config(state='disabled')
    apellidoP_entry.config(state='disabled')
    apellidoM_entry.config(state='disabled')
    perfil_entry.config(state='disabled')
    telefono_entry.config(state='disabled')
    direccion_entry.config(state='disabled')
    usuario_entry.config(state='disabled')
    contraseña_entry.config(state='disabled')

    # Escribir las líneas modificadas de vuelta al archivo
    with open('usuarios.txt', 'w') as file:
        file.writelines(lines)

    # Deshabilitar la edición después de guardar los cambios
    id_entry.config(state='disabled')
    nombre_entry.config(state='disabled')
    apellidoP_entry.config(state='disabled')
    apellidoM_entry.config(state='disabled')
    perfil_entry.config(state='disabled')
    telefono_entry.config(state='disabled')
    direccion_entry.config(state='disabled')
    usuario_entry.config(state='disabled')
    contraseña_entry.config(state='disabled')

    messagebox.showinfo("Éxito", "Usuario editado correctamente")

def eliminar_usuario(ID_var, id_entry, nombre_entry, apellidoP_entry, apellidoM_entry, perfil_entry, telefono_entry, direccion_entry, usuario_entry, contraseña_entry):
    # Leer el archivo de usuarios
    with open('usuarios.txt', 'r') as file:
        lines = file.readlines()

    # Buscar la línea correspondiente al ID_var
    for i, line in enumerate(lines):
        data = line.strip().split(',')
        if data[0] == ID_var.get():
            # Eliminar el usuario
            del lines[i]
            break
    else:
        # Si el bucle no se rompió, el usuario no se encontró
        messagebox.showerror("Error", "No se pudo encontrar el usuario para eliminar")
        return

    # Escribir las líneas modificadas de vuelta al archivo
    with open('usuarios.txt', 'w') as file:
        file.writelines(lines)

    habilitar_edicion(id_entry, nombre_entry, apellidoP_entry, apellidoM_entry, perfil_entry, telefono_entry, direccion_entry, usuario_entry, contraseña_entry)

    # Limpiar y deshabilitar los campos después de eliminar el usuario
    id_entry.delete(0, tk.END)
    nombre_entry.delete(0, tk.END)
    apellidoP_entry.delete(0, tk.END)
    apellidoM_entry.delete(0, tk.END)
    perfil_entry.delete(0, tk.END)
    telefono_entry.delete(0, tk.END)
    direccion_entry.delete(0, tk.END)
    usuario_entry.delete(0, tk.END)
    contraseña_entry.delete(0, tk.END)

    id_entry.config(state='disabled')
    nombre_entry.config(state='disabled')
    apellidoP_entry.config(state='disabled')
    apellidoM_entry.config(state='disabled')
    perfil_entry.config(state='disabled')
    telefono_entry.config(state='disabled')
    direccion_entry.config(state='disabled')
    usuario_entry.config(state='disabled')
    contraseña_entry.config(state='disabled')

    # Mostrar ventana de alerta
    messagebox.showinfo("Éxito", "Usuario eliminado correctamente")