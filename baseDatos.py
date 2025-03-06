import sqlite3
from sqlite3 import Error

class GestorBD:
    def __init__(self, db_name="cerveceria.db"):
        self.db_name = db_name
        self.con = None  # Inicializa la conexión en None

    def conectar_bd(self):
        """Establece la conexión con la base de datos y la devuelve."""
        try:
            self.con = sqlite3.connect(self.db_name)
            print("✅ Conexión exitosa a la base de datos.")
            return self.con  # Devuelve la conexión
        except sqlite3.Error as e:
            print("❌ Error al conectar con la base de datos:", e)
            return None  # Evita que sea None sin control

    def execute_query(self, query, values=None):
        """Ejecuta una consulta SQL con o sin valores."""
        if self.con is None:
            self.conectar_bd()  # Reintenta la conexión si está cerrada

        try:
            cursor = self.con.cursor()
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            self.con.commit()
            print("Consulta ejecutada con éxito.")
        except sqlite3.Error as e:
            print(f"Error al ejecutar la consulta: {e}")

    def crear_tablas(self):
        if self.con is not None:
            try:
                cursor = self.con.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS productos (
                        noIdProducto INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombreProducto TEXT NOT NULL,
                        pesoVolumen TEXT NOT NULL,
                        fechaVencimiento TEXT NOT NULL,
                        precioProduccion REAL NOT NULL,
                        precioVenta REAL NOT NULL
                    )
                ''')
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS clientes (
                        noIdCliente INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        apellido TEXT NOT NULL,
                        direccion TEXT NOT NULL,
                        telefono TEXT NOT NULL,
                        correo TEXT NOT NULL
                    )
                ''')
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS factura (
                        noIdFactura INTEGER PRIMARY KEY AUTOINCREMENT
                    )
                ''')
                self.con.commit()
                print("Tablas creadas exitosamente.")
            except Error as e:
                print("Error al crear las tablas:", e)
        else:
            print("No hay conexión a la base de datos.")

    def obtener_productos(self):
        """Obtiene todos los productos de la base de datos."""
        if self.con is None:
            self.conectar_bd()  # Reintenta la conexión si está cerrada

        try:
            cursor = self.con.cursor()
            cursor.execute("SELECT * FROM productos")
            return cursor.fetchall()
        except sqlite3.Error as e:
            print("❌ Error al obtener productos:", e)
            return []

    def inserta_producto(self, producto):
        query = """
        INSERT INTO productos (noIdProducto, nombreProducto, pesoVolumen, fechaVencimiento, precioProduccion, precioVenta)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        values = (
            producto.get_noIdProducto(),
            producto.get_nombreProducto(),
            producto.get_pesoVolumen(),
            producto.get_fechaVencimiento(),
            producto.get_precioProduccion(),
            producto.get_precioVenta()
        )
        self.execute_query(query, values)

    def buscar_producto_id(self, id_producto):
        """Busca un producto por ID."""
        if self.con:
            cursor = self.con.cursor()
            cursor.execute("SELECT * FROM productos WHERE noIdProducto = ?", (id_producto,))
            return cursor.fetchone()
        return None

    def actualizar_nombre_producto(self, id_producto, nuevo_nombre):
        query = "UPDATE productos SET nombreProducto = ? WHERE noIdProducto = ?"
        self.execute_query(query, (nuevo_nombre, id_producto))

    def cerrar_bd(self):
        if self.con:
            self.con.close()
            print("Conexión a la base de datos cerrada.")
