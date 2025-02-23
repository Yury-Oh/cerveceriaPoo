from time import sleep #Función para retardar la ejecución de un programa
#Programación modular - Importación de modulos necesarios
from baseDatos import conectar_bd, crear_tablas
from productos import crear_nuevo_producto, actualizar_producto, consultar_producto
from clientes import crear_nuevo_cliente, actualizar_direccion_cliente, consultar_cliente
from compras import finalizar_compra, quitar_producto, añadir_producto, mostrar_productos

class Menu:
    def __init__(self, con=None, titulo="", color="\033[0m"):
        # Conexión a la base de datos y atributos visuales comunes
        self.con = con
        self.titulo = titulo  # Título del menú
        self.color = color    # Color para presentación en consola
        self.opciones = []    # Lista de opciones

    def mostrar_encabezado(self):
        # Muestra un encabezado basado en el título y el color definidos
        print(self.color)
        if self.titulo:
            print(f"===== {self.titulo} =====")
        print("\033[0m", end="")  # Reinicia el color de la consola

    def solicitar_opcion(self):
        # Solicita una opción al usuario
        return input("\nSeleccione una opción: ")

    def run(self):
        # Método para elevar cuando no se ha implementado un método o función
        raise NotImplementedError("El método run debe ser implementado en la subclase.")

class MenuPrincipal(Menu):
    def __init__(self):
        # Establece la conexión y prepara la base de datos
        con = conectar_bd()
        if con:
            crear_tablas(con)
        super().__init__(con, titulo="Bienvenido a la Cervecería Artesanal", color="\033[1;33m")

    def imprimir_bienvenida(self):
        print(self.color)
        print("🍺════════════════════════════════════════════════════🍺")
        print("      ✨ Bienvenido a la Cervecería Artesanal ✨       ")
        print("🍺════════════════════════════════════════════════════🍺\033[0m")

    def run(self):
        # Bucle principal para el acceso a los diferentes menús
        while True:
            self.imprimir_bienvenida()
            print("\n📌 Opciones disponibles:")
            print("1️⃣   Iniciar sesión como administrador")
            print("2️⃣   Iniciar sesión como cliente")
            print("3️⃣   Salir del sistema")
            seleccion = input("\nSeleccione una opción: ")
            #Validación de credenciales de administrador
            if seleccion == "1":
                pwd = input("\n🔑 Ingrese la contraseña de administrador: ")
                if pwd == "admin123":
                    MenuAdmin(self.con).run()
                else:
                    print("❌ Contraseña incorrecta")
            elif seleccion == "2":
                MenuCliente(self.con).run()
            elif seleccion == "3":
                print("👋 Gracias por visitarnos. ¡Salud! 🍻")
                self.con.close()
                break
            else:
                print("⚠️ Seleccione una opción válida.")

class MenuAdmin(Menu):
    def __init__(self, con):
        # Configura el menú de administrador con sus atributos heredados
        super().__init__(con, titulo="Menú Administrador", color="\033[1;34m")

    def run(self):
        while True:
            print(self.color)
            print("\n════════════════════════════════")
            print("      🛠 MENÚ ADMINISTRADOR      ")
            print("════════════════════════════════\033[0m")
            print("1️⃣   Menú de Productos")
            print("2️⃣   Menú de Clientes")
            print("3️⃣  🔙 Volver")
            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                MenuProductos(self.con).run()
            elif opcion == "2":
                MenuClientes(self.con).run()
            elif opcion == "3":
                print("👋 Volviendo al menú principal...")
                sleep(1)
                break
            else:
                print("⚠️ Opción no válida, intente nuevamente.")

class MenuCliente(Menu):
    def __init__(self, con):
        # Configura el menú para clientes 
        super().__init__(con, titulo="Menú Cliente", color="\033[1;32m")

    def run(self):
        # Gestiona registro, actualización y compra
        while True:
            print(self.color)
            print("\n════════════════════════════=")
            print("        👤 MENÚ CLIENTE        ")
            print("════════════════════════════=\033[0m")
            print("1️⃣   Registrarse")
            print("2️⃣   Actualizar dirección")
            print("3️⃣   Hacer una compra")
            print("4️⃣  🔙 Volver")
            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                crear_nuevo_cliente(self.con)
            elif opcion == "2":
                actualizar_direccion_cliente(self.con)
            elif opcion == "3":
                MenuCompras(self.con).run()
            elif opcion == "4":
                print("👋 Volviendo al menú principal...")
                sleep(1)
                break
            else:
                print("⚠️ Opción no válida, intente nuevamente.")

class MenuProductos(Menu):
    def __init__(self, con):
        #Atributos heredados de Menu()
        super().__init__(con, titulo="Menú de Productos", color="\033[1;35m")

    def run(self):
        while True:
            print(self.color)
            print("\n═════════════════════════════════")
            print("       📦 MENÚ DE PRODUCTOS       ")
            print("═════════════════════════════════\033[0m")
            print("1️⃣   Agregar producto")
            print("2️⃣   Actualizar producto")
            print("3️⃣  🔍 Consultar producto")
            print("4️⃣  🔙 Volver al Menú Principal")
            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                crear_nuevo_producto(self.con)
            elif opcion == "2":
                actualizar_producto(self.con)
            elif opcion == "3":
                consultar_producto(self.con)
            elif opcion == "4":
                break
            else:
                print("⚠️ Opción no válida.")

class MenuClientes(Menu):
    def __init__(self, con):
        # Configura el menú de clientes (administrador)
        super().__init__(con, titulo="Menú de Clientes", color="\033[1;36m")

    def run(self):
        # Permite al administrador gestionar clientes
        while True:
            print(self.color)
            print("\n════════════════════════════")
            print("       👥 MENÚ DE CLIENTES       ")
            print("════════════════════════════\033[0m")
            print("1️⃣   Agregar cliente")
            print("2️⃣   Actualizar dirección")
            print("3️⃣  🔍 Consultar cliente")
            print("4️⃣  🔙 Volver al Menú Principal")
            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                crear_nuevo_cliente(self.con)
            elif opcion == "2":
                actualizar_direccion_cliente(self.con)
            elif opcion == "3":
                consultar_cliente(self.con)
            elif opcion == "4":
                break
            else:
                print("⚠️ Opción no válida, intente nuevamente.")

class MenuCompras(Menu):
    def __init__(self, con):
        #Se inicializan atributos heredados y carrito de compras
        super().__init__(con, titulo="Menú de Compras", color="\033[1;31m")
        self.carrito = []

    def run(self):
        while True:
            if self.carrito:
                print("\n🛒 Productos en el carrito:")
                for i, item in enumerate(self.carrito):
                    print(f"{i + 1}. {item[1]} unidades de {item[0]} a ${item[2]} cada una.")
            print(self.color)
            print("\n════════════════════════════=")
            print("       🛍 MENÚ DE COMPRAS       ")
            print("════════════════════════════=\033[0m")
            print("1️⃣  ➕ Añadir producto")
            print("2️⃣  ➖ Quitar producto")
            print("3️⃣  ✅ Finalizar compra")
            print("4️⃣  🔙 Volver")
            opcion = input("\nSeleccione una opción: ")

            if opcion == '1':
                añadir_producto(self.carrito, self.con)
            elif opcion == '2':
                quitar_producto(self.carrito)
            elif opcion == '3':
                finalizar_compra(self.carrito, self.con)
            elif opcion == '4':
                print("🎉 Gracias por su compra 🍻")
                break
            else:
                print("⚠️ Opción no válida.")

if __name__ == "__main__":
    MenuPrincipal().run()
