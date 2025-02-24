from sqlite3 import Error
import sqlite3
from imprimir_factura import Factura

class Carrito:
    def __init__(self):
        self.items = []  # Lista para almacenar los productos en el carrito

    def agregar_item(self, producto, cantidad):
        """Agrega un item al carrito"""
        self.items.append((producto[0], cantidad, producto[1]))

    def quitar_item(self, indice):
        """Quita un item del carrito por su índice"""
        if 0 <= indice < len(self.items):
            return self.items.pop(indice)
        return None

    def obtener_total(self):
        """Calcula el total de la compra"""
        return sum(item[1] * item[2] for item in self.items)

    def esta_vacio(self):
        """Verifica si el carrito está vacío"""
        return len(self.items) == 0

    def limpiar(self):
        """Vacía el carrito"""
        self.items.clear()

    def listar_items(self):
        """Muestra los items en el carrito"""
        for i, item in enumerate(self.items):
            print(f"{i + 1}. {item[1]} unidades de {item[0]} a ${item[2]} cada una.")

class GestorCompras:
    def __init__(self, conexion):
        self.conexion = conexion
        self.carrito = Carrito()

    def mostrar_productos(self):
        """Muestra los productos disponibles en la base de datos"""
        cursor = self.conexion.cursor()
        cursor.execute('SELECT noIdProducto, nombreProducto, pesoVolumen, fechaVencimiento FROM productos')
        productos = cursor.fetchall()

        print("\nProductos disponibles:")
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Volumen: {producto[2]}, Fecha de vencimiento: {producto[3]}")

    def añadir_producto(self):
        """Añade un producto al carrito"""
        cursor = self.conexion.cursor()

        self.mostrar_productos()
        while True:
            try:
                id_producto = int(input("\nIngrese el ID del producto que desea añadir al carrito: "))
                cantidad = int(input("Ingrese la cantidad: "))
                if cantidad <= 0:
                    raise ValueError("La cantidad debe ser un número positivo.")
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero positivo para la cantidad.")

        cursor.execute('SELECT nombreProducto, precioVenta FROM productos WHERE noIdProducto = ?', (id_producto,))
        producto = cursor.fetchone()

        if producto:
            self.carrito.agregar_item(producto, cantidad)
            print(f"{cantidad} unidades de {producto[0]} añadidas al carrito.")
        else:
            print("Producto no encontrado.")

    def quitar_producto(self):
        """Quita un producto del carrito"""
        if self.carrito.esta_vacio():
            print("El carrito está vacío.")
            return

        print("\nProductos en el carrito:")
        self.carrito.listar_items()

        try:
            indice = int(input("Ingrese el número del producto que desea quitar: ")) - 1
            producto_eliminado = self.carrito.quitar_item(indice)
            if producto_eliminado:
                print(f"{producto_eliminado[1]} unidades de {producto_eliminado[0]} eliminadas del carrito.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")

    def finalizar_compra(self):
        """Finaliza la compra y genera la factura"""
        if self.carrito.esta_vacio():
            print("El carrito está vacío.")
            return

        total = self.carrito.obtener_total()

        print("\nResumen de la compra:")
        self.carrito.listar_items()
        print(f"Total a pagar: ${total:.2f}")

        # Solicita y valida el ID del cliente
        while True:
            noIdCliente = input("Ingrese su ID de cliente >> ")
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM clientes WHERE noIdCliente = ?", (noIdCliente,))
            cliente = cursor.fetchone()

            if cliente:
                nombre, apellido, direccion, telefono = cliente[1], cliente[2], cliente[3], cliente[4]
                print(nombre, apellido, direccion, telefono)
                break
            else:
                print("Ingrese un ID de cliente válido.")

        # Gestión de factura
        while True:
            opcion = input("Generar factura? (si o no): ").strip().lower()
            if opcion == "si":
                while True:
                    opcion2 = input("Imprimir factura? (si o no): ").strip().lower()
                    if opcion2 == "si":
                        facturita = Factura(self.conexion, nombre, apellido, direccion, telefono, self.carrito.items, True)
                        facturita.leer_factura()
                        break
                    elif opcion2 == "no":
                        facturita = Factura(self.conexion, nombre, apellido, direccion, telefono, self.carrito.items, False)
                        facturita.leer_factura()
                        break
                    else:
                        print("Opción inválida.")
                break
            elif opcion == "no":
                break
            else:
                print("Opción inválida.")

        self.carrito.limpiar()
