from sqlite3 import Error  # Importa la clase de manejo de errores de SQLite
import sqlite3  # Importa la librería para manejar bases de datos SQLite
from imprimir_factura import Factura  # Importa la clase Factura para generar comprobantes de compra

class Carrito:
    def __init__(self):
        self.items = []  # Lista para almacenar los productos en el carrito

    def agregar_item(self, producto, cantidad):
        self.items.append((producto[0], cantidad, producto[1]))  # Guarda el nombre, cantidad y precio del producto

    def quitar_item(self, indice):
        if 0 <= indice < len(self.items):  # Verifica si el índice es válido
            return self.items.pop(indice)  # Elimina el producto del carrito y lo devuelve
        return None  # Retorna None si el índice no es válido

    def obtener_total(self):
        return sum(item[1] * item[2] for item in self.items)  # Multiplica cantidad por precio y suma los totales

    def esta_vacio(self):
        return len(self.items) == 0  # Retorna True si no hay productos en el carrito

    def limpiar(self):
        self.items.clear()  # Borra todos los elementos de la lista

    def listar_items(self):
        for i, item in enumerate(self.items):  # Recorre la lista de productos en el carrito
            print(f"{i + 1}. {item[1]} unidades de {item[0]} a ${item[2]} cada una.")  # Muestra los detalles de cada producto

class GestorCompras:
    def __init__(self, conexion):
        self.conexion = conexion  # Almacena la conexión a la base de datos
        self.carrito = Carrito()  # Crea una instancia del carrito de compras

    def mostrar_productos(self):
        """Consulta y muestra los productos disponibles en la base de datos"""
        cursor = self.conexion.cursor()  # Crea un cursor para ejecutar consultas SQL
        cursor.execute('SELECT noIdProducto, nombreProducto, pesoVolumen, fechaVencimiento FROM productos')  # Consulta los productos
        productos = cursor.fetchall()  # Obtiene los resultados de la consulta

        print("\nProductos disponibles:")
        for producto in productos:  # Recorre los productos obtenidos de la base de datos
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Volumen: {producto[2]}, Fecha de vencimiento: {producto[3]}")

    def añadir_producto(self):
        """Permite seleccionar un producto y añadirlo al carrito"""
        cursor = self.conexion.cursor()  # Crea un cursor para ejecutar consultas

        self.mostrar_productos()  # Muestra la lista de productos disponibles
        while True:
            try:
                id_producto = int(input("\nIngrese el ID del producto que desea añadir al carrito: "))  # Pide el ID del producto
                cantidad = int(input("Ingrese la cantidad: "))  # Pide la cantidad de unidades
                if cantidad <= 0:  # Verifica que la cantidad sea positiva
                    raise ValueError("La cantidad debe ser un número positivo.")
                break  # Sale del bucle si los datos son correctos
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero positivo para la cantidad.")

        cursor.execute('SELECT nombreProducto, precioVenta FROM productos WHERE noIdProducto = ?', (id_producto,))  # Busca el producto en la base de datos
        producto = cursor.fetchone()  # Obtiene el resultado de la consulta

        if producto:  # Si el producto existe
            self.carrito.agregar_item(producto, cantidad)  # Lo añade al carrito
            print(f"{cantidad} unidades de {producto[0]} añadidas al carrito.")
        else:
            print("Producto no encontrado.")  # Mensaje si el ID del producto no es válido

    def quitar_producto(self):
        """Permite eliminar un producto del carrito"""
        if self.carrito.esta_vacio():  # Verifica si el carrito está vacío
            print("El carrito está vacío.")
            return

        print("\nProductos en el carrito:")
        self.carrito.listar_items()  # Muestra los productos en el carrito

        try:
            indice = int(input("Ingrese el número del producto que desea quitar: ")) - 1  # Pide el número del producto a eliminar
            producto_eliminado = self.carrito.quitar_item(indice)  # Elimina el producto del carrito
            if producto_eliminado:
                print(f"{producto_eliminado[1]} unidades de {producto_eliminado[0]} eliminadas del carrito.")
            else:
                print("Número inválido.")  # Mensaje si el número ingresado no es válido
        except ValueError:
            print("Entrada inválida.")  # Mensaje de error si la entrada no es un número válido

    def finalizar_compra(self):
        """Finaliza la compra, muestra el total y permite generar una factura"""
        if self.carrito.esta_vacio():  # Verifica si el carrito está vacío antes de proceder
            print("El carrito está vacío.")
            return

        total = self.carrito.obtener_total()  # Calcula el total de la compra

        print("\nResumen de la compra:")
        self.carrito.listar_items()  # Muestra los productos en el carrito
        print(f"Total a pagar: ${total:.2f}")  # Muestra el total a pagar

        # Solicita y valida el ID del cliente
        while True:
            noIdCliente = input("Ingrese su ID de cliente >> ")  # Pide el ID del cliente
            cursor = self.conexion.cursor()  # Crea un cursor para consultar la base de datos
            cursor.execute("SELECT * FROM clientes WHERE noIdCliente = ?", (noIdCliente,))  # Busca el cliente en la base de datos
            cliente = cursor.fetchone()  # Obtiene los datos del cliente

            if cliente:  # Si el cliente existe
                nombre, apellido, direccion, telefono = cliente[1], cliente[2], cliente[3], cliente[4]  # Extrae los datos del cliente
                print(nombre, apellido, direccion, telefono)  # Muestra los datos del cliente
                break  # Sale del bucle si el cliente es válido
            else:
                print("Ingrese un ID de cliente válido.")  # Mensaje si el ID no es válido

        # Gestión de factura
        while True:
            opcion = input("Generar factura? (si o no): ").strip().lower()  # Pregunta si desea generar factura
            if opcion == "si":
                while True:
                    opcion2 = input("Imprimir factura? (si o no): ").strip().lower()  # Pregunta si desea imprimir la factura
                    if opcion2 == "si":
                        facturita = Factura(noIdCliente, nombre, apellido, direccion, telefono, self.carrito.items, True)  # Crea la factura con opción de imprimir
                        facturita.leer_factura()  # Muestra la factura
                        break
                    elif opcion2 == "no":
                        facturita = Factura(noIdCliente, nombre, apellido, direccion, telefono, self.carrito.items, False)  # Crea la factura sin imprimir
                        facturita.leer_factura()
                        break
                    else:
                        print("Opción inválida.")  # Mensaje si la opción no es válida
                break
            elif opcion == "no":
                break  # Sale si no se quiere generar factura
            else:
                print("Opción inválida.")  # Mensaje si la opción no es válida

        self.carrito.limpiar()  # Vacía el carrito después de finalizar la compra
