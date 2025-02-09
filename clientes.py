from sqlite3 import Error

def crear_nuevo_cliente(con):
    try:
        cursor = con.cursor()
        noIdCliente = int(input("Número de identificación del cliente: "))
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        direccion = input("Dirección: ").strip()
        telefono = input("Teléfono: ").strip()
        correo = input("Correo electrónico: ").strip()
        
        cursor.execute('''
            INSERT INTO clientes (noIdCliente, nombre, apellido, direccion, telefono, correo)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (noIdCliente, nombre, apellido, direccion, telefono, correo))
        con.commit()
        print("Cliente agregado correctamente.")
    except Error as e:
        print("Error al agregar el cliente:", e)

def actualizar_direccion_cliente(con):
    try:
        cursor = con.cursor()
        noIdCliente = int(input("Número de identificación del cliente a actualizar: "))

        cursor.execute("SELECT * FROM clientes WHERE noIdCliente = ?", (noIdCliente,))
        cliente = cursor.fetchone()
        if not cliente:
            print("Error: El cliente con ese identificador no existe.")
            return

        nueva_direccion = input("Ingrese la nueva dirección: ").strip()
        
        cursor.execute('''
            UPDATE clientes SET direccion = ? WHERE noIdCliente = ?
        ''', (nueva_direccion, noIdCliente))
        con.commit()
        print("Dirección actualizada correctamente.")
    except Error as e:
        print("Error al actualizar la dirección del cliente:", e)

def consultar_cliente(con):
    try:
        cursor = con.cursor()
        noIdCliente = int(input("Número de identificación del cliente a consultar: "))
        cursor.execute("SELECT * FROM clientes WHERE noIdCliente = ?", (noIdCliente,))
        cliente = cursor.fetchone()
        if cliente:
            print("Número de identificación:", cliente[0])
            print("Nombre:", cliente[1])
            print("Apellido:", cliente[2])
            print("Dirección:", cliente[3])
            print("Teléfono:", cliente[4])
            print("Correo electrónico:", cliente[5])
        else:
            print("Cliente no encontrado.")
    except Error as e:
        print("Error al consultar el cliente:", e)
