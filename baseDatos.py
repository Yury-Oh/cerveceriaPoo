import sqlite3
from sqlite3 import Error

class GestorBD:
    def __init__(self, db_name="cerveceria.db"):
        self.db_name = db_name
        self.con = None

    def conectar_bd(self):
        try:
            self.con = sqlite3.connect(self.db_name)
            print("Conexión exitosa a la base de datos.")
        except Error as e:
            print("Error al conectar con la base de datos:", e)

    def crear_tablas(self):
        if self.con is not None:
            try:
                cursor = self.con.cursor()
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

                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS factura (
                        noIdFactura INTEGER PRIMARY KEY)
                ''')

                self.con.commit()
                print("Tablas creadas exitosamente.")
            except Error as e:
                print("Error al crear las tablas:", e)
        else:
            print("No hay conexión a la base de datos.")

    def cerrar_bd(self):
        if self.con:
            self.con.close()
            print("Conexión a la base de datos cerrada.")
