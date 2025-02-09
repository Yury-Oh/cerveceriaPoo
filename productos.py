from datetime import datetime
from sqlite3 import Error

def crear_nuevo_producto(con):
    try:
        cursor = con.cursor()
        noIdProducto = int(input("Número de identificación del producto: "))
        nombreProducto = input("Nombre del producto: ").strip()
        pesoVolumen = input("Peso o volumen: ").strip()
        
        while True:
            fechaVencimiento = input("Fecha de vencimiento (DD/MM/AAAA): ").strip()
            try:
                fecha_venc = datetime.strptime(fechaVencimiento, "%d/%m/%Y")
                if fecha_venc > datetime.today():
                    break
                else:
                    print("Error: La fecha de vencimiento debe ser mayor a la fecha actual.")
            except ValueError:
                print("Error: Formato de fecha inválido. Use DD/MM/AAAA.")

        precioProduccion = float(input("Precio de producción: "))
        precioVenta = float(input("Precio de venta: "))
        
        cursor.execute('''
            INSERT INTO productos (noIdProducto, nombreProducto, pesoVolumen, fechaVencimiento, precioProduccion, precioVenta)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (noIdProducto, nombreProducto, pesoVolumen, fechaVencimiento, precioProduccion, precioVenta))
        con.commit()
        print("Producto agregado correctamente.")
    except Error as e:
        print("Error al agregar el producto:", e)

def actualizar_producto(con):
    try:
        cursor = con.cursor()
        noIdProducto = int(input("Número de identificación del producto a actualizar: "))

        cursor.execute("SELECT * FROM productos WHERE noIdProducto = ?", (noIdProducto,))
        producto = cursor.fetchone()
        if not producto:
            print("Error: El producto con ese identificador no existe.")
            return

        print("1. Nombre del producto")
        print("2. Peso o volumen")
        print("3. Fecha de vencimiento")
        print("4. Precio de producción")
        print("5. Precio de venta")
        opcion = input("Seleccione el número del campo que desea actualizar: ")

        campos = {
            "1": "nombreProducto",
            "2": "pesoVolumen",
            "3": "fechaVencimiento",
            "4": "precioProduccion",
            "5": "precioVenta"
        }

        if opcion in campos:
            if opcion == "3":
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

            cursor.execute(f'''
                UPDATE productos SET {campos[opcion]} = ? WHERE noIdProducto = ?
            ''', (nuevo_valor, noIdProducto))
            con.commit()
            print("Producto actualizado correctamente.")
        else:
            print("Opción no válida.")
    except Error as e:
        print("Error al actualizar el producto:", e)

def consultar_producto(con):
    try:
        cursor = con.cursor()
        noIdProducto = int(input("Número de identificación del producto a consultar: "))
        cursor.execute("SELECT * FROM productos WHERE noIdProducto = ?", (noIdProducto,))
        producto = cursor.fetchone()
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
        print("Error al consultar el producto:", e)
