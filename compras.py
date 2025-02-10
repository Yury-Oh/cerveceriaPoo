from sqlite3 import Error
import sqlite3
from imprimir_factura import leer_factura

# Función para mostrar los productos disponibles en la base de datos
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

    mostrar_productos(con)  # Muestra los productos antes de seleccionar uno
    id_producto = int(input("\nIngrese el ID del producto que desea añadir al carrito: "))
    cantidad = int(input("Ingrese la cantidad: "))

    # Consulta el nombre y precio del producto seleccionado
    cursor.execute('SELECT nombreProducto, precioVenta FROM productos WHERE noIdProducto = ?', (id_producto,))
    producto = cursor.fetchone()

    if producto:
        carrito.append((producto[0], cantidad, producto[1]))  # Añade el producto al carrito
        print(f"{cantidad} unidades de {producto[0]} añadidas al carrito.")
    else:
        print("Producto no encontrado.")  # Mensaje si el producto no existe en la BD

# Función para quitar un producto del carrito
def quitar_producto(carrito):
    if not carrito:
        print("El carrito está vacío.")  # Mensaje si no hay productos en el carrito
        return
    
    print("\nProductos en el carrito:")
    for i, item in enumerate(carrito):
        print(f"{i + 1}. {item[1]} unidades de {item[0]} a ${item[2]} cada una.")
    
    try:
        indice = int(input("Ingrese el número del producto que desea quitar: ")) - 1
        if 0 <= indice < len(carrito):
            producto_eliminado = carrito.pop(indice)  # Elimina el producto del carrito
            print(f"{producto_eliminado[1]} unidades de {producto_eliminado[0]} eliminadas del carrito.")
        else:
            print("Número inválido.")  # Si el número no está en la lista
    except ValueError:
        print("Entrada inválida.")  # Si el usuario ingresa algo que no es un número

# Función para finalizar la compra y generar factura
def finalizar_compra(carrito, con):
    if not carrito:
        print("El carrito está vacío.")  # No permite finalizar la compra si no hay productos
        return
    
    total = sum(item[1] * item[2] for item in carrito)  # Calcula el total a pagar

    print("\nResumen de la compra:")
    for item in carrito:
        print(f"{item[1]} unidades de {item[0]} a ${item[2]} cada una.")
    print(f"Total a pagar: ${total:.2f}")

    # Solicita el ID del cliente y valida que exista en la base de datos
    while True:
        noIdCliente = input("Ingrese su ID de cliente >> ")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM clientes WHERE noIdCliente = ?", (noIdCliente,))
        cliente = cursor.fetchone()

        if cliente:
            nombre, apellido, direccion, telefono = cliente[1], cliente[2], cliente[3], cliente[4]
            print(nombre, apellido, direccion, telefono)  # Muestra los datos del cliente
            break
        else:
            print("Ingrese un ID de cliente válido.")  # Si el cliente no existe

    # Pregunta si se desea generar la factura
    while True:
        opcion = input("Generar factura? (si o no): ").strip().lower()
        if opcion == "si":
            while True:
                opcion2 = input("Imprimir factura? (si o no): ").strip().lower()
                if opcion2 == "si":
                    leer_factura(con, nombre, apellido, direccion, telefono, carrito, True)  # Genera e imprime factura
                    break
                elif opcion2 == "no":
                    leer_factura(con, nombre, apellido, direccion, telefono, carrito, False)  # Solo genera factura
                    break
                else:
                    print("Opción inválida.")  # Validación de entrada
            break
        elif opcion == "no":
            break
        else:
            print("Opción inválida.")  # Validación de entrada

    carrito.clear()  # Vacía el carrito después de finalizar la compra
