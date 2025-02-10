from sqlite3 import Error
import sqlite3
from imprimir_factura import leer_factura



# Función para mostrar los productos disponibles
def mostrar_productos(con):
    cursor = con.cursor()
    cursor.execute('SELECT noIdProducto, nombreProducto, pesoVolumen, fechaVencimiento FROM productos')
    productos = cursor.fetchall()
    print("\nProductos disponibles:")
    for producto in productos:
        print(f"ID: {producto[0]}, Nombre: {producto[1]}, Volumen: {producto[2]}ml, Fecha de vencimiento: {producto[3]}")

# Función para añadir un producto al carrito
def añadir_producto(carrito, con):
    cursor = con.cursor()

    mostrar_productos(con)
    id_producto = int(input("\nIngrese el ID del producto que desea añadir al carrito: "))
    cantidad = int(input("Ingrese la cantidad: "))
    
    cursor.execute('SELECT nombreProducto, precioVenta FROM productos WHERE noIdProducto = ?', (id_producto,))
    producto = cursor.fetchone()
    
    if producto:
        carrito.append((producto[0], cantidad, producto[1]))
        print(f"{cantidad} unidades de {producto[0]} añadidas al carrito.")
    else:
        print("Producto no encontrado.")

# Función para quitar un producto del carrito
def quitar_producto(carrito):
    if not carrito:
        print("El carrito está vacío.")
        return
    
    print("\nProductos en el carrito:")
    for i, item in enumerate(carrito):
        print(f"{i + 1}. {item[1]} unidades de {item[0]} a ${item[2]} cada una.")
    
    try:
        indice = int(input("Ingrese el número del producto que desea quitar: ")) - 1
        if 0 <= indice < len(carrito):
            producto_eliminado = carrito.pop(indice)
            print(f"{producto_eliminado[1]} unidades de {producto_eliminado[0]} eliminadas del carrito.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

# Función para finalizar la compra
def finalizar_compra(carrito, con):
    if not carrito:
        print("El carrito está vacío.")
        return
    
    noIdCliente = None
    total = sum(item[1] * item[2] for item in carrito)
    print("\nResumen de la compra:")
    for item in carrito:
        print(f"{item[1]} unidades de {item[0]} a ${item[2]} cada una.")
    print(f"Total a pagar: ${total:.2f}")

    while True:
        noIdCliente = input("Ingrese su id de cliente >> ")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM clientes WHERE noIdCliente = ?", (noIdCliente,))
        cliente = cursor.fetchone()
        if cliente:
            nombre = cliente[1]
            apellido = cliente[2]
            direccion = cliente [3]
            telefono = cliente[4]
            print(nombre, apellido, direccion, telefono)
            break
        else: print("ingrese un ID de cliente valido")
    
    while True:
        opcion = input("Generar factura? (si o no): ")
        if opcion == "si":
            while True:
                opcion2 = input("Imprimir factura? (si o no): ")
                if opcion2 == "si":
                    leer_factura(con, nombre, apellido, direccion, telefono, carrito, True)
                    break
                elif opcion2 == "no":
                    leer_factura(con, nombre, apellido, direccion, telefono, carrito, False)
                    break
                else:
                    print("Opción invalida")
            break
        elif opcion == "no":
            break
        else:
            print("Opción invalida")
    carrito.clear()


