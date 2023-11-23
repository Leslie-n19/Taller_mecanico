import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from login import crear_ventana_registro, iniciar_sesion
from usuarios import buscar_usuario, habilitar_edicion, guardar_cambios, eliminar_usuario
from clientes import crear_ventana_registro_cliente, buscar_cliente, habilitar_edicion_cliente, guardar_cambios_cliente, eliminar_cliente
from vehiculos import crear_ventana_registro_vehiculo, buscar_vehiculo, habilitar_edicion_vehiculo, guardar_cambios_vehiculo, eliminar_vehiculo
from reparaciones import crear_ventana_registro_reparacion, buscar_reparacion

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
        ttk.Button(pestaña, text="Buscar", command=lambda: buscar_usuario(ID_var, id_entry, nombre_entry, apellidoP_entry, apellidoM_entry,
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


        ttk.Button(pestaña, text="Editar", command=lambda: habilitar_edicion(id_entry, nombre_entry, apellidoP_entry, apellidoM_entry,
                                                                           perfil_entry, telefono_entry, direccion_entry, usuario_entry, 
                                                                           contraseña_entry)).grid(row=10, column=0, pady=10)
        ttk.Button(pestaña, text="Eliminar", command=lambda: eliminar_usuario(ID_var, id_entry, nombre_entry, apellidoP_entry, apellidoM_entry,
                                                                     perfil_entry, telefono_entry, direccion_entry, usuario_entry, 
                                                                     contraseña_entry)).grid(row=10, column=1, pady=10)
        ttk.Button(pestaña, text="Guardar", command=lambda: guardar_cambios(ID_var, id_entry, nombre_entry, apellidoP_entry, apellidoM_entry,
                                                                             perfil_entry, telefono_entry, direccion_entry, usuario_entry, 
                                                                             contraseña_entry)).grid(row=10, column=2, pady=10)
    elif nombre == "Clientes":
        ttk.Label(pestaña, text="Buscar por ID:").grid(row=0, column=0, padx=10, pady=10)
        ttk.Entry(pestaña, textvariable=ID_var_cliente, state='normal').grid(row=0, column=1, padx=10, pady=10)
        ttk.Button(pestaña, text="Buscar", command=lambda: buscar_cliente(ID_var_cliente, id_usu, id_cliente, nombre_cliente, apellidoP_cliente, apellidoM_cliente,
                                                                          telefono_cliente)).grid(row=0, column=2, columnspan=2, pady=10)

        ttk.Label(pestaña, text="ID usuario:").grid(row=1, column=0, padx=10, pady=10)
        id_usu = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        id_usu.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(pestaña, text="ID:").grid(row=2, column=0, padx=10, pady=10)
        id_cliente = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        id_cliente.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(pestaña, text="Nombre:").grid(row=3, column=0, padx=10, pady=10)
        nombre_cliente = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        nombre_cliente.grid(row=3, column=1, padx=10, pady=10)

        ttk.Label(pestaña, text="Apellido Paterno:").grid(row=4, column=0, padx=10, pady=10)
        apellidoP_cliente = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        apellidoP_cliente.grid(row=4, column=1, padx=10, pady=10)

        ttk.Label(pestaña, text="Apellido Materno:").grid(row=5, column=0, padx=10, pady=10)
        apellidoM_cliente = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        apellidoM_cliente.grid(row=5, column=1, padx=10, pady=10)    

        ttk.Label(pestaña, text="Teléfono:").grid(row=6, column=0, padx=10, pady=10)
        telefono_cliente = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        telefono_cliente.grid(row=6, column=1, padx=10, pady=10)    

        ttk.Button(pestaña, text="Editar", command=lambda: habilitar_edicion_cliente(id_usu, id_cliente, nombre_cliente, apellidoP_cliente, apellidoM_cliente,
                                                                          telefono_cliente)).grid(row=7, column=0, pady=10)
        ttk.Button(pestaña, text="Eliminar", command=lambda: eliminar_cliente(ID_var_cliente, id_usu, id_cliente, nombre_cliente, apellidoP_cliente, apellidoM_cliente,
                                                                          telefono_cliente)).grid(row=7, column=1, pady=10)
        ttk.Button(pestaña, text="Guardar", command=lambda: guardar_cambios_cliente(ID_var_cliente, id_usu, id_cliente, nombre_cliente, apellidoP_cliente, apellidoM_cliente,
                                                                          telefono_cliente)).grid(row=7, column=2, pady=10)
        ttk.Button(pestaña, text="Nuevo", command=lambda: crear_ventana_registro_cliente(ventana)).grid(row=7, column=3, pady=10)
    elif nombre == "Vehículos":
        ttk.Label(pestaña, text="Buscar por ID:").grid(row=0, column=0, padx=10, pady=10)
        ttk.Entry(pestaña, textvariable=ID_var_vehiculo, state='normal').grid(row=0, column=1, padx=10, pady=10)
        ttk.Button(pestaña, text="Buscar", command=lambda: buscar_vehiculo(ID_var_vehiculo, id_cli, id_vehiculo, matricula, fecha, marca, modelo)).grid(row=0, column=2, columnspan=2, pady=10)

        ttk.Label(pestaña, text="ID cliente:").grid(row=1, column=0, padx=10, pady=10)
        id_cli = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        id_cli.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(pestaña, text="Vehículo ID:").grid(row=2, column=0, padx=10, pady=10)
        id_vehiculo = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        id_vehiculo.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(pestaña, text="Matrícula:").grid(row=3, column=0, padx=10, pady=10)
        matricula = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        matricula.grid(row=3, column=1, padx=10, pady=10)

        ttk.Label(pestaña, text="Fecha:").grid(row=4, column=0, padx=10, pady=10)
        fecha = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        fecha.grid(row=4, column=1, padx=10, pady=10)

        ttk.Label(pestaña, text="Marca:").grid(row=5, column=0, padx=10, pady=10)
        marca = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        marca.grid(row=5, column=1, padx=10, pady=10)    

        ttk.Label(pestaña, text="Módelo:").grid(row=5, column=2, padx=10, pady=10)
        modelo = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        modelo.grid(row=5, column=3, padx=10, pady=10)    

        ttk.Button(pestaña, text="Editar", command=lambda: habilitar_edicion_vehiculo(id_cli, id_vehiculo, matricula, 
                                                                                      fecha, marca, modelo)).grid(row=7, column=0, pady=10)
        ttk.Button(pestaña, text="Eliminar", command=lambda: eliminar_vehiculo(ID_var_vehiculo, id_cli, id_vehiculo, matricula, 
                                                                               fecha, marca, modelo)).grid(row=7, column=1, pady=10)
        ttk.Button(pestaña, text="Guardar", command=lambda: guardar_cambios_vehiculo(ID_var_vehiculo, id_cli, id_vehiculo, matricula, 
                                                                                     fecha, marca, modelo)).grid(row=7, column=2, pady=10)
        ttk.Button(pestaña, text="Nuevo", command=lambda: crear_ventana_registro_vehiculo(ventana)).grid(row=7, column=3, pady=10)
    elif nombre == "Reparaciones":
        ttk.Label(pestaña, text="Buscar reparación por ID:").grid(row=0, column=0, padx=10, pady=10)
        ttk.Entry(pestaña, textvariable=ID_var_repa, state='normal').grid(row=0, column=1, padx=10, pady=10)
        ttk.Button(pestaña, text="Buscar", command=lambda: buscar_reparacion (ID_var_repa, id_veh, id_pie, id_reparacion, fechaEn, fechaSal, 
                                                                              falla, cantidad)).grid(row=0, column=2, columnspan=2, pady=10)

        ttk.Label(pestaña, text="Vehículo ID:").grid(row=1, column=0, padx=10, pady=10)
        id_veh = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        id_veh.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(pestaña, text="Pieza ID:").grid(row=1, column=2, padx=10, pady=10)
        id_pie = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        id_pie.grid(row=1, column=3, padx=10, pady=10)

        ttk.Label(pestaña, text="Reparación ID:").grid(row=3, column=0, padx=10, pady=10)
        id_reparacion = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        id_reparacion.grid(row=3, column=1, padx=10, pady=10)

        ttk.Label(pestaña, text="Fecha Entrada:").grid(row=4, column=0, padx=10, pady=10)
        fechaEn = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        fechaEn.grid(row=4, column=1, padx=10, pady=10)

        ttk.Label(pestaña, text="Fecha salida:").grid(row=4, column=2, padx=10, pady=10)
        fechaSal = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        fechaSal.grid(row=4, column=3, padx=10, pady=10)    

        ttk.Label(pestaña, text="Falla:").grid(row=5, column=0, padx=10, pady=10)
        falla = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        falla.grid(row=5, column=1, padx=10, pady=10)    

        ttk.Label(pestaña, text="Cantidad de piezas:").grid(row=6, column=0, padx=10, pady=10)
        cantidad = ttk.Entry(pestaña, state='disabled', textvariable=tk.StringVar())
        cantidad.grid(row=6, column=1, padx=10, pady=10)  

        ttk.Button(pestaña, text="Editar", command=lambda: habilitar_edicion_vehiculo(id_cli, id_vehiculo, matricula, 
                                                                                      fecha, marca, modelo)).grid(row=7, column=0, pady=10)
        ttk.Button(pestaña, text="Eliminar", command=lambda: eliminar_vehiculo(ID_var_vehiculo, id_cli, id_vehiculo, matricula, 
                                                                               fecha, marca, modelo)).grid(row=7, column=1, pady=10)
        ttk.Button(pestaña, text="Guardar", command=lambda: guardar_cambios_vehiculo(ID_var_vehiculo, id_cli, id_vehiculo, matricula, 
                                                                                     fecha, marca, modelo)).grid(row=7, column=2, pady=10)
        ttk.Button(pestaña, text="Nuevo", command=lambda: crear_ventana_registro_reparacion(ventana)).grid(row=7, column=3, pady=10)
            # Agrega más etiquetas, entradas y botones según tus necesidades
    
    controlador.add(pestaña, text=nombre)

# Crea la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación con Pestañas")

# Crea el controlador de pestañas
controlador = ttk.Notebook(ventana)

# Variables para almacenar la información
ID_var_cliente = tk.StringVar()
ID_var = tk.StringVar()
ID_var_vehiculo = tk.StringVar()
ID_var_repa = tk.StringVar()
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
