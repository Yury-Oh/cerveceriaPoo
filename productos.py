from datetime import datetime  # Importa la clase datetime para manejar fechas
from sqlite3 import Error  # Importa Error para manejar excepciones en SQLite

# Clase que representa un producto con atributos privados
class Producto:
    def __init__(self, noIdProducto, nombreProducto, pesoVolumen, fechaVencimiento, precioProduccion, precioVenta):
        self.__noIdProducto = noIdProducto
        self.__nombreProducto = nombreProducto
        self.__pesoVolumen = pesoVolumen
        self.__fechaVencimiento = fechaVencimiento
        self.__precioProduccion = precioProduccion
        self.__precioVenta = precioVenta

    # Métodos getter para obtener los valores de los atributos
    def get_noIdProducto(self):
        return self.__noIdProducto

    def get_nombreProducto(self):
        return self.__nombreProducto

    def get_pesoVolumen(self):
        return self.__pesoVolumen

    def get_fechaVencimiento(self):
        return self.__fechaVencimiento

    def get_precioProduccion(self):
        return self.__precioProduccion

    def get_precioVenta(self):
        return self.__precioVenta

    # Métodos setter para modificar los valores de los atributos
    def set_noIdProducto(self, noIdProducto):
        self.__noIdProducto = noIdProducto

    def set_nombreProducto(self, nombreProducto):
        self.__nombreProducto = nombreProducto

    def set_pesoVolumen(self, pesoVolumen):
        self.__pesoVolumen = pesoVolumen

    def set_fechaVencimiento(self, fechaVencimiento):
        self.__fechaVencimiento = fechaVencimiento

    def set_precioProduccion(self, precioProduccion):
        self.__precioProduccion = precioProduccion

    def set_precioVenta(self, precioVenta):
        self.__precioVenta = precioVenta


# Clase que gestiona los productos en la base de datos
class GestorProductos:
    def __init__(self, con):
        self.con = con  # Conexión a la base de datos

    # Método para obtener un número entero con validación
    def obtener_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))  # Intenta convertir la entrada en un número entero
            except ValueError:
                print("Error: Debe ingresar un número válido.")  # Muestra un mensaje de error si la conversión falla

    # Método para crear un nuevo producto y guardarlo en la base de datos
    def crear_nuevo_producto(self):
        try:
            cursor = self.con.cursor()  # Crea un cursor para ejecutar consultas SQL

            # Solicita los datos del producto al usuario
            noIdProducto = self.obtener_entero("Número de identificación del producto: ")
            nombreProducto = input("Nombre del producto: ").strip()
            pesoVolumen = input("Peso o volumen: ").strip()

            # Validación de la fecha de vencimiento
            while True:
                fechaVencimiento = input("Fecha de vencimiento (DD/MM/AAAA): ").strip()
                try:
                    fecha_venc = datetime.strptime(fechaVencimiento, "%d/%m/%Y")  # Convierte la entrada en una fecha
                    if fecha_venc > datetime.today():  # Verifica que la fecha sea futura
                        break
                    else:
                        print("Error: La fecha de vencimiento debe ser mayor a la fecha actual.")
                except ValueError:
                    print("Error: Formato de fecha inválido. Use DD/MM/AAAA.")

            # Solicita los precios del producto
            precioProduccion = float(input("Precio de producción: "))
            precioVenta = float(input("Precio de venta: "))

            # Inserta los datos en la base de datos
            cursor.execute('''
                INSERT INTO productos (noIdProducto, nombreProducto, pesoVolumen, fechaVencimiento, precioProduccion, precioVenta)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (noIdProducto, nombreProducto, pesoVolumen, fechaVencimiento, precioProduccion, precioVenta))

            self.con.commit()  # Guarda los cambios en la base de datos
            print("Producto agregado correctamente.")

        except Error as e:
            print("Error al agregar el producto:", e)  # Maneja cualquier error de SQLite

    # Método para actualizar el nombre de un producto existente
    def actualizar_producto(self):
        try:
            cursor = self.con.cursor()
            noIdProducto = self.obtener_entero("Número de identificación del producto a actualizar: ")

            # Verifica si el producto existe en la base de datos
            cursor.execute("SELECT * FROM productos WHERE noIdProducto = ?", (noIdProducto,))
            producto = cursor.fetchone()

            if not producto:  # Si no se encuentra el producto, muestra un mensaje de error
                print("Error: El producto con ese identificador no existe.")
                return

            # Solicita el nuevo nombre del producto
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ").strip()

            # Actualiza el nombre del producto en la base de datos
            cursor.execute('''
                UPDATE productos SET nombreProducto = ? WHERE noIdProducto = ?
            ''', (nuevo_nombre, noIdProducto))

            self.con.commit()  # Guarda los cambios
            print("Nombre del producto actualizado correctamente.")

        except Error as e:
            print("Error al actualizar el producto:", e)  # Maneja errores de SQLite

    # Método para consultar los datos de un producto en la base de datos
    def consultar_producto(self):
        try:
            cursor = self.con.cursor()
            noIdProducto = self.obtener_entero("Número de identificación del producto a consultar: ")

            # Consulta el producto en la base de datos
            cursor.execute("SELECT * FROM productos WHERE noIdProducto = ?", (noIdProducto,))
            producto = cursor.fetchone()

            if producto:  # Si se encuentra el producto, lo muestra en pantalla
                print("Número de identificación:", producto[0])
                print("Nombre del producto:", producto[1])
                print("Peso o volumen:", producto[2])
                print("Fecha de vencimiento:", producto[3])
                print("Precio de producción:", producto[4])
                print("Precio de venta:", producto[5])
            else:
                print("Producto no encontrado.")  # Muestra un mensaje si el producto no existe

        except Error as e:
            print("Error al consultar el producto:", e)  # Maneja errores de SQLite
