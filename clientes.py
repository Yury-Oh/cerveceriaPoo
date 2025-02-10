import sqlite3
import re

def obtener_texto(mensaje, minimo=1):
    while True:
        valor = input(mensaje).strip()
        if len(valor) >= minimo:
            return valor
        print(f"Error: el campo debe tener al menos {minimo} caracteres.")

def obtener_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número válido.")

def obtener_correo(mensaje):
    while True:
        correo = input(mensaje).strip()
        if re.fullmatch(r"[\w.-]+@(gmail\.com|hotmail\.com)", correo):
            return correo
        print("Error: Ingrese un correo válido con dominio @gmail.com o @hotmail.com.")

def crear_nuevo_cliente(con):
    try:
        cursor = con.cursor()
        noIdCliente = obtener_entero("Número de identificación del cliente: ")
        nombre = obtener_texto("Nombre: ", 2)
        apellido = obtener_texto("Apellido: ", 2)
        direccion = obtener_texto("Dirección: ", 5)
        telefono = obtener_texto("Teléfono: ", 7)
        correo = obtener_correo("Correo electrónico: ")
        
        cursor.execute('''
            INSERT INTO clientes (noIdCliente, nombre, apellido, direccion, telefono, correo)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (noIdCliente, nombre, apellido, direccion, telefono, correo))
        con.commit()
        print("Cliente agregado correctamente.")
    except sqlite3.Error as e:
        print("Error al agregar el cliente:", e)

def actualizar_direccion_cliente(con):
    try:
        cursor = con.cursor()
        noIdCliente = obtener_entero("Número de identificación del cliente a actualizar: ")

        cursor.execute("SELECT * FROM clientes WHERE noIdCliente = ?", (noIdCliente,))
        cliente = cursor.fetchone()
        if not cliente:
            print("Error: El cliente con ese identificador no existe.")
            return

        nueva_direccion = obtener_texto("Ingrese la nueva dirección: ", 5)
        
        cursor.execute('''
            UPDATE clientes SET direccion = ? WHERE noIdCliente = ?
        ''', (nueva_direccion, noIdCliente))
        con.commit()
        print("Dirección actualizada correctamente.")
    except sqlite3.Error as e:
        print("Error al actualizar la dirección del cliente:", e)

def consultar_cliente(con):
    try:
        cursor = con.cursor()
        noIdCliente = obtener_entero("Número de identificación del cliente a consultar: ")
        cursor.execute("SELECT * FROM clientes WHERE noIdCliente = ?", (noIdCliente,))
        cliente = cursor.fetchone()
        if cliente:
            print("Número de identificación:", cliente[0])
            print("Nombre:", cliente[1])
            print("Apellido:", cliente[2])
            print("Dirección:", cliente[3])
            print("Teléfono:", cliente[4])
            print("Correo electrónico:", cliente[5])
        else:
            print("Cliente no encontrado.")
    except sqlite3.Error as e:
        print("Error al consultar el cliente:", e)
