import sqlite3
import re

# Función para obtener un texto con una longitud mínima
def obtener_texto(mensaje, minimo=1):
    while True:
        valor = input(mensaje).strip()  # Elimina espacios al inicio y al final
        if len(valor) >= minimo:
            return valor  # Devuelve el texto si cumple con la longitud mínima
        print(f"Error: el campo debe tener al menos {minimo} caracteres.")

# Función para obtener un número entero validado
def obtener_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))  # Intenta convertir la entrada a entero
        except ValueError:
            print("Error: Debe ingresar un número válido.")  # Muestra un error si la conversión falla

# Función para obtener y validar un correo electrónico
def obtener_correo(mensaje):
    while True:
        correo = input(mensaje).strip()  # Elimina espacios adicionales
        # Verifica si el correo tiene un formato válido y pertenece a los dominios permitidos
        if re.fullmatch(r"[\w.-]+@(gmail\.com|hotmail\.com)", correo):
            return correo  # Retorna el correo si es válido
        print("Error: Ingrese un correo válido con dominio @gmail.com o @hotmail.com.")

# Función para agregar un nuevo cliente a la base de datos
def crear_nuevo_cliente(con):
    try:
        cursor = con.cursor()  # Obtiene un cursor para ejecutar comandos SQL

        # Solicita datos al usuario
        noIdCliente = obtener_entero("Número de identificación del cliente: ")
        nombre = obtener_texto("Nombre: ", 2)
        apellido = obtener_texto("Apellido: ", 2)
        direccion = obtener_texto("Dirección: ", 5)
        telefono = obtener_texto("Teléfono: ", 7)
        correo = obtener_correo("Correo electrónico: ")

        # Inserta los datos del cliente en la tabla 'clientes'
        cursor.execute('''
            INSERT INTO clientes (noIdCliente, nombre, apellido, direccion, telefono, correo)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (noIdCliente, nombre, apellido, direccion, telefono, correo))
        
        con.commit()  # Guarda los cambios en la base de datos
        print("Cliente agregado correctamente.")
    
    except sqlite3.IntegrityError:
        print("Error: Ya existe un cliente con ese número de identificación.")  # Maneja duplicados de ID
    
    except sqlite3.Error as e:
        print("Error al agregar el cliente:", e)  # Captura otros errores de SQLite

# Función para actualizar la dirección de un cliente existente
def actualizar_direccion_cliente(con):
    try:
        cursor = con.cursor()  # Obtiene un cursor para ejecutar comandos SQL

        # Solicita el número de identificación del cliente
        noIdCliente = obtener_entero("Número de identificación del cliente a actualizar: ")

        # Verifica si el cliente existe en la base de datos
        cursor.execute("SELECT * FROM clientes WHERE noIdCliente = ?", (noIdCliente,))
        cliente = cursor.fetchone()  # Obtiene el primer resultado

        if not cliente:
            print("Error: El cliente con ese identificador no existe.")  # Muestra un error si el cliente no existe
            return

        # Solicita la nueva dirección
        nueva_direccion = obtener_texto("Ingrese la nueva dirección: ", 5)

        # Actualiza la dirección en la base de datos
        cursor.execute('''
            UPDATE clientes SET direccion = ? WHERE noIdCliente = ?
        ''', (nueva_direccion, noIdCliente))
        
        con.commit()  # Guarda los cambios
        print("Dirección actualizada correctamente.")
    
    except sqlite3.Error as e:
        print("Error al actualizar la dirección del cliente:", e)  # Captura errores de SQLite

# Función para consultar la información de un cliente por su ID
def consultar_cliente(con):
    try:
        cursor = con.cursor()  # Obtiene un cursor para ejecutar comandos SQL

        # Solicita el número de identificación del cliente
        noIdCliente = obtener_entero("Número de identificación del cliente a consultar: ")

        # Busca el cliente en la base de datos
        cursor.execute("SELECT * FROM clientes WHERE noIdCliente = ?", (noIdCliente,))
        cliente = cursor.fetchone()  # Obtiene el primer resultado

        if cliente:
            # Muestra la información del cliente si se encontró en la base de datos
            print("\nInformación del Cliente:")
            print("Número de identificación:", cliente[0])
            print("Nombre:", cliente[1])
            print("Apellido:", cliente[2])
            print("Dirección:", cliente[3])
            print("Teléfono:", cliente[4])
            print("Correo electrónico:", cliente[5])
        else:
            print("Cliente no encontrado.")  # Mensaje si el cliente no existe en la base de datos
    
    except sqlite3.Error as e:
        print("Error al consultar el cliente:", e)  # Captura errores de SQLite
