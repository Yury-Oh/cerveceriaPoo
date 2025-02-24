import sqlite3  # Importa la biblioteca para manejar bases de datos SQLite
import re  # Importa la biblioteca para manejar expresiones regulares

# Definición de la clase base Persona
class Persona:
    def __init__(self, nombre, apellido, direccion, telefono, correo):
        # Atributos privados de la clase Persona
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__telefono = telefono
        self.__correo = correo

    # Métodos getter para acceder a los atributos privados
    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_direccion(self):
        return self.__direccion

    def get_telefono(self):
        return self.__telefono

    def get_correo(self):
        return self.__correo

    # Métodos setter para modificar los atributos privados

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_correo(self, correo):
        self.__correo = correo

# Definición de la clase Cliente, que hereda de Persona
class Cliente(Persona):
    def __init__(self, noIdCliente, nombre, apellido, direccion, telefono, correo):
        super().__init__(nombre, apellido, direccion, telefono, correo)
        self.__noIdCliente = noIdCliente

    # Métodos getter y setter para noIdCliente
    def get_noIdCliente(self):
        return self.__noIdCliente

    def set_noIdCliente(self, noIdCliente):
        self.__noIdCliente = noIdCliente

# Clase GestorClientes para gestionar la base de datos y la interacción con el usuario
class GestorClientes:
    def __init__(self, con):
        self.con = con  # Almacena la conexión a la base de datos SQLite

    # Método para solicitar un texto con una longitud mínima
    def obtener_texto(self, mensaje, minimo=1):
        while True:
            valor = input(mensaje).strip()  # Elimina espacios en blanco al inicio y final
            if len(valor) >= minimo:  # Verifica que el texto tenga la longitud mínima
                return valor
            print(f"Error: el campo debe tener al menos {minimo} caracteres.")

    # Método para solicitar un número entero
    def obtener_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))  # Intenta convertir la entrada en un entero
            except ValueError:
                print("Error: Debe ingresar un número válido.")

    # Método para solicitar un número de teléfono con validación de formato
    def obtener_telefono(self, mensaje):
        while True:
            telefono = input(mensaje).strip()
            # Expresión regular para validar un número de teléfono (entre 7 y 15 dígitos)
            if re.fullmatch(r"\d{7,15}", telefono):
                return telefono
            print("Error: Ingrese un número de teléfono válido (7 a 15 dígitos).")

    # Método para solicitar un correo electrónico con validación de formato
    def obtener_correo(self, mensaje):
        while True:
            correo = input(mensaje).strip()
            # Expresión regular básica para validar el correo
            if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", correo):
                return correo
            print("Error: Ingrese un correo electrónico válido.")

    # Método para crear un nuevo cliente en la base de datos
    def crear_nuevo_cliente(self):
        try:
            cursor = self.con.cursor()  # Crea un cursor para interactuar con la base de datos

            # Solicita los datos del cliente con validación
            noIdCliente = self.obtener_entero("Número de identificación del cliente: ")
            nombre = self.obtener_texto("Nombre: ", 2)
            apellido = self.obtener_texto("Apellido: ", 2)
            direccion = self.obtener_texto("Dirección: ", 5)
            telefono = self.obtener_telefono("Teléfono: ")
            correo = self.obtener_correo("Correo electrónico: ")

            # Inserta los datos en la base de datos
            cursor.execute('''
                INSERT INTO clientes (noIdCliente, nombre, apellido, direccion, telefono, correo)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (noIdCliente, nombre, apellido, direccion, telefono, correo))

            self.con.commit()  # Guarda los cambios en la base de datos
            print("Cliente agregado correctamente.")

        except sqlite3.IntegrityError:
            print("Error: Ya existe un cliente con ese número de identificación.")  # Evita duplicados

        except sqlite3.Error as e:
            print("Error al agregar el cliente:", e)  # Captura cualquier otro error de SQLite

    # Método para actualizar la dirección de un cliente existente
    def actualizar_direccion_cliente(self):
        try:
            cursor = self.con.cursor()

            noIdCliente = self.obtener_entero("Número de identificación del cliente a actualizar: ")

            # Verifica si el cliente existe
            cursor.execute("SELECT * FROM clientes WHERE noIdCliente = ?", (noIdCliente,))
            cliente = cursor.fetchone()

            if not cliente:
                print("Error: El cliente con ese identificador no existe.")
                return  # Sale del método si el cliente no existe

            # Solicita la nueva dirección
            nueva_direccion = self.obtener_texto("Ingrese la nueva dirección: ", 5)

            # Actualiza la dirección en la base de datos
            cursor.execute('''
                UPDATE clientes SET direccion = ? WHERE noIdCliente = ?
            ''', (nueva_direccion, noIdCliente))

            self.con.commit()  # Guarda los cambios en la base de datos
            print("Dirección actualizada correctamente.")

        except sqlite3.Error as e:
            print("Error al actualizar la dirección del cliente:", e)

    # Método para consultar un cliente por su número de identificación
    def consultar_cliente(self):
        try:
            cursor = self.con.cursor()

            noIdCliente = self.obtener_entero("Número de identificación del cliente a consultar: ")

            # Busca el cliente en la base de datos
            cursor.execute("SELECT * FROM clientes WHERE noIdCliente = ?", (noIdCliente,))
            cliente = cursor.fetchone()

            if cliente:
                # Muestra la información del cliente si existe
                print("\nInformación del Cliente:")
                print("Número de identificación:", cliente[0])
                print("Nombre:", cliente[1])
                print("Apellido:", cliente[2])
                print("Dirección:", cliente[3])
                print("Teléfono:", cliente[4])
                print("Correo electrónico:", cliente[5])
            else:
                print("Cliente no encontrado.")

        except sqlite3.Error as e:
            print("Error al consultar el cliente:", e)
