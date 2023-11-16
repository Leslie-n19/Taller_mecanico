import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Variable global para el ID
global_id = 1

def crear_ventana_registro(ventana):
    # Función para manejar el botón Sign Up y abrir una nueva ventana de registro
    ventana_registro = tk.Toplevel(ventana)
    ventana_registro.title("Registro de Usuario")

    # Variables para almacenar la información del nuevo usuario
    nombre_var = tk.StringVar()
    ap_paterno_var = tk.StringVar()
    ap_materno_var = tk.StringVar()
    perfil_var = tk.StringVar()
    telefono_var = tk.StringVar()
    direccion_var = tk.StringVar()
    usuario_var = tk.StringVar()
    contraseña_var = tk.StringVar()

    # Función para guardar la información en un archivo de texto
    def guardar_usuario():
        global global_id  # Indica que estamos utilizando la variable global_id definida fuera de esta función
        with open("usuarios.txt", "a") as archivo:
            archivo.write(f"{global_id},")
            archivo.write(f"{nombre_var.get()},")
            archivo.write(f"{ap_paterno_var.get()},")
            archivo.write(f"{ap_materno_var.get()},")
            archivo.write(f"{perfil_var.get()},")
            archivo.write(f"{telefono_var.get()},")
            archivo.write(f"{direccion_var.get()},")
            archivo.write(f"{usuario_var.get()},")
            archivo.write(f"{contraseña_var.get()}\n")
        global_id += 1
        ventana_registro.destroy()

    # Interfaz de la ventana de registro
    ttk.Label(ventana_registro, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
    ttk.Entry(ventana_registro, textvariable=nombre_var).grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(ventana_registro, text="Apellido Paterno:").grid(row=1, column=0, padx=10, pady=10)
    ttk.Entry(ventana_registro, textvariable=ap_paterno_var).grid(row=1, column=1, padx=10, pady=10)

    ttk.Label(ventana_registro, text="Apellido Materno:").grid(row=2, column=0, padx=10, pady=10)
    ttk.Entry(ventana_registro, textvariable=ap_materno_var).grid(row=2, column=1, padx=10, pady=10)

    # Etiqueta y combobox para el perfil
    ttk.Label(ventana_registro, text="Perfil:").grid(row=2, column=2, padx=10, pady=10)
    perfiles = ["--Selecciona perfil--", "Administrador", "Gerente", "Secretarix", "Mecanico"]  # Agrega más perfiles si es necesario
    perfil_combobox = ttk.Combobox(ventana_registro,textvariable=perfil_var, values=perfiles, state="readonly")
    perfil_combobox.current(0)  # Establece el valor por defecto
    perfil_combobox.grid(row=2, column=3, padx=10, pady=10)

    ttk.Label(ventana_registro, text="Teléfono:").grid(row=3, column=0, padx=10, pady=10)
    ttk.Entry(ventana_registro, textvariable=telefono_var).grid(row=3, column=1, padx=10, pady=10)

    ttk.Label(ventana_registro, text="Dirección:").grid(row=3, column=2, padx=10, pady=10)
    ttk.Entry(ventana_registro, textvariable=direccion_var).grid(row=3, column=3, padx=10, pady=10)

    ttk.Label(ventana_registro, text="Usuario:").grid(row=4, column=0, padx=10, pady=10)
    ttk.Entry(ventana_registro, textvariable=usuario_var).grid(row=4, column=1, padx=10, pady=10)

    ttk.Label(ventana_registro, text="Contraseña:").grid(row=4, column=2, padx=10, pady=10)
    ttk.Entry(ventana_registro, textvariable=contraseña_var, show="*").grid(row=4, column=3, padx=10, pady=10)

    ttk.Button(ventana_registro, text="Guardar", command=guardar_usuario).grid(row=5, column=0, columnspan=4, pady=10)

def iniciar_sesion(usuario_var, contraseña_var):
    usuario = usuario_var.get() if usuario_var else None
    contraseña = contraseña_var.get() if contraseña_var else None

    # Imprime los valores después de obtenerlos
    print(f"Usuario={usuario}, Contraseña={contraseña}")

    if validar_login(usuario, contraseña):
        messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def validar_login(usuario, contraseña):
    # Función para validar el inicio de sesión con los datos almacenados en el archivo
    with open("usuarios.txt", "r") as archivo:
        for linea in archivo:
            # Divide la línea en campos usando comas como separadores
            campos = linea.strip().split(',')
            
            # Verifica que haya suficientes elementos en la lista antes de acceder a los índices
            if len(campos) == 9:
                if campos[7].strip() == usuario and campos[8].strip() == contraseña:
                    return True
    return False


