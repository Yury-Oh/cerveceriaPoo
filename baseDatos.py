import sqlite3
from sqlite3 import Error

def conectar_bd():
    try:
        con = sqlite3.connect("cerveceria.db")
        return con
    except Error as e:
        print("Error al conectar con la base de datos:", e)
        return None

def crear_tablas(con):
    try:
        cursor = con.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                noIdProducto INTEGER PRIMARY KEY,
                nombreProducto TEXT NOT NULL,
                pesoVolumen TEXT NOT NULL,
                fechaVencimiento TEXT NOT NULL,
                precioProduccion REAL NOT NULL,
                precioVenta REAL NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                noIdCliente INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                direccion TEXT NOT NULL,
                telefono TEXT NOT NULL,
                correo TEXT NOT NULL
            )
        ''')

        con.commit()
    except Error as e:
        print("Error al crear las tablas:", e)

def cerrarBD(con):
    con.close()
