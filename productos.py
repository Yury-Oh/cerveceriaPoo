from datetime import datetime  # Importa la clase datetime para manejar fechas
from sqlite3 import Error  # Importa Error para manejar excepciones de SQLite

def crear_nuevo_producto(con):
    """
    Función para agregar un nuevo producto a la base de datos.
    Solicita información al usuario y la inserta en la tabla `productos`.
    """
    try:
        cursor = con.cursor()  # Obtiene un cursor para ejecutar comandos SQL
        
        # Solicita los datos del producto al usuario
        noIdProducto = int(input("Número de identificación del producto: "))
        nombreProducto = input("Nombre del producto: ").strip()
        pesoVolumen = input("Peso o volumen: ").strip()
        
        # Solicita la fecha de vencimiento con validación de formato y lógica de fecha
        while True:
            fechaVencimiento = input("Fecha de vencimiento (DD/MM/AAAA): ").strip()
            try:
                fecha_venc = datetime.strptime(fechaVencimiento, "%d/%m/%Y")
                if fecha_venc > datetime.today():  # La fecha debe ser futura
                    break
                else:
                    print("Error: La fecha de vencimiento debe ser mayor a la fecha actual.")
            except ValueError:
                print("Error: Formato de fecha inválido. Use DD/MM/AAAA.")
        
        # Solicita precios
        precioProduccion = float(input("Precio de producción: "))
        precioVenta = float(input("Precio de venta: "))
        
        # Inserta los datos en la base de datos
        cursor.execute('''
            INSERT INTO productos (noIdProducto, nombreProducto, pesoVolumen, fechaVencimiento, precioProduccion, precioVenta)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (noIdProducto, nombreProducto, pesoVolumen, fechaVencimiento, precioProduccion, precioVenta))
        con.commit()  # Guarda los cambios en la base de datos
        print("Producto agregado correctamente.")
    except Error as e:
        print("Error al agregar el producto:", e)  # Manejo de errores

def actualizar_producto(con):
    """
    Función para actualizar un producto existente en la base de datos.
    Permite al usuario seleccionar el campo a modificar e ingresar el nuevo valor.
    """
    try:
        cursor = con.cursor()
        noIdProducto = int(input("Número de identificación del producto a actualizar: "))

        # Verifica si el producto existe
        cursor.execute("SELECT * FROM productos WHERE noIdProducto = ?", (noIdProducto,))
        producto = cursor.fetchone()
        if not producto:
            print("Error: El producto con ese identificador no existe.")
            return

        # Muestra las opciones de actualización
        print("1. Nombre del producto")
        print("2. Peso o volumen")
        print("3. Fecha de vencimiento")
        print("4. Precio de producción")
        print("5. Precio de venta")
        opcion = input("Seleccione el número del campo que desea actualizar: ")
        
        # Diccionario para mapear opciones a nombres de columnas
        campos = {
            "1": "nombreProducto",
            "2": "pesoVolumen",
            "3": "fechaVencimiento",
            "4": "precioProduccion",
            "5": "precioVenta"
        }
        
        # Si la opción es válida, solicita el nuevo valor
        if opcion in campos:
            if opcion == "3":  # Si es la fecha de vencimiento, validar formato
                while True:
                    nuevo_valor = input("Ingrese la nueva fecha de vencimiento (DD/MM/AAAA): ").strip()
                    try:
                        fecha_venc = datetime.strptime(nuevo_valor, "%d/%m/%Y")
                        if fecha_venc > datetime.today():
                            break
                        else:
                            print("Error: La fecha de vencimiento debe ser mayor a la fecha actual.")
                    except ValueError:
                        print("Error: Formato de fecha inválido. Use DD/MM/AAAA.")
            else:
                nuevo_valor = input(f"Ingrese el nuevo valor para {campos[opcion]}: ")

            # Ejecuta la actualización en la base de datos
            cursor.execute(f'''
                UPDATE productos SET {campos[opcion]} = ? WHERE noIdProducto = ?
            ''', (nuevo_valor, noIdProducto))
            con.commit()
            print("Producto actualizado correctamente.")
        else:
            print("Opción no válida.")
    except Error as e:
        print("Error al actualizar el producto:", e)  # Manejo de errores

def consultar_producto(con):
    """
    Función para consultar un producto en la base de datos por su ID.
    Muestra toda la información del producto si existe.
    """
    try:
        cursor = con.cursor()
        noIdProducto = int(input("Número de identificación del producto a consultar: "))
        
        # Consulta el producto en la base de datos
        cursor.execute("SELECT * FROM productos WHERE noIdProducto = ?", (noIdProducto,))
        producto = cursor.fetchone()
        
        # Muestra los datos si el producto existe
        if producto:
            print("Número de identificación:", producto[0])
            print("Nombre del producto:", producto[1])
            print("Peso o volumen:", producto[2])
            print("Fecha de vencimiento:", producto[3])
            print("Precio de producción:", producto[4])
            print("Precio de venta:", producto[5])
        else:
            print("Producto no encontrado.")
    except Error as e:
        print("Error al consultar el producto:", e)  # Manejo de errores