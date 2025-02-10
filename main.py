from time import sleep
from baseDatos import conectar_bd, crear_tablas
from productos import crear_nuevo_producto, actualizar_producto, consultar_producto
from clientes import crear_nuevo_cliente, actualizar_direccion_cliente, consultar_cliente
from compras import finalizar_compra, quitar_producto, añadir_producto, mostrar_productos

def imprimir_bienvenida():
    print("\033[1;33m")
    print("🍺════════════════════════════════════════════════════🍺")
    print("      ✨ Bienvenido a la Cervecería Artesanal ✨       ")
    print("🍺════════════════════════════════════════════════════🍺\033[0m")

def menu_principal():
    con = conectar_bd()  
    if con:
        crear_tablas(con)
        while True:
            imprimir_bienvenida()
            print("\n📌 Opciones disponibles:")
            print("1️⃣   Iniciar sesión como administrador")
            print("2️⃣   Iniciar sesión como cliente")
            print("3️⃣   Salir del sistema")

            seleccion = input("\n Seleccione una opción: ")

            if seleccion == "1":
                pwd = input("\n🔑 Ingrese la contraseña de administrador: ")
                if pwd == "admin123": 
                    while True:
                        print("\033[1;34m\n ════════════════════════════")
                        print("      🛠 MENÚ ADMINISTRADOR      ")
                        print("══════════════════════════════ \033[0m")
                        print("1️⃣   Menú de Productos")
                        print("2️⃣   Menú de Clientes")
                        print("3️⃣  🔙 Volver")

                        opcion = input("\n Seleccione una opción: ")

                        if opcion == "1":
                            menu_productos(con)
                        elif opcion == "2":
                            menu_clientes(con)
                        elif opcion == "3":
                            print("👋 Volviendo al menú principal...")
                            sleep(1)
                            break
                        else:
                            print("⚠️ Opción no válida, intente nuevamente.")

                else:
                    print("❌ Contraseña incorrecta")

            elif seleccion == "2":
                while True:
                    print("\033[1;32m\n ═════════════════════════════")
                    print("        👤 MENÚ CLIENTE        ")
                    print("════════════════════════════ \033[0m")
                    print("1️⃣   Registrarse")
                    print("2️⃣   Actualizar dirección")
                    print("3️⃣   Hacer una compra")
                    print("4️⃣  🔙 Volver")

                    opcion = input("\n Seleccione una opción: ")

                    if opcion == "1":
                        crear_nuevo_cliente(con)
                    elif opcion == "2":
                        actualizar_direccion_cliente(con)
                    elif opcion == "3":
                        menu_compras(con)
                    elif opcion == "4":
                        print("👋 Volviendo al menú principal...")
                        sleep(1)
                        break
                    else:
                        print("⚠️ Opción no válida, intente nuevamente.")

            elif seleccion == "3":
                print("👋 Gracias por visitarnos. ¡Salud! 🍻")
                con.close()
                break
            else:
                print("⚠️ Seleccione una opción válida.")

# ================= MENÚ DE PRODUCTOS ==================
def menu_productos(con):
    while True:
        print("\033[1;35m\n ══════════════════════════════════")
        print("       📦 MENÚ DE PRODUCTOS       ")
        print("═════════════════════════════════ \033[0m")
        print("1️⃣   Agregar producto")
        print("2️⃣   Actualizar producto")
        print("3️⃣  🔍 Consultar producto")
        print("4️⃣  🔙 Volver al Menú Principal")

        opcion = input("\n Seleccione una opción: ")

        if opcion == "1":
            crear_nuevo_producto(con)
        elif opcion == "2":
            actualizar_producto(con)
        elif opcion == "3":
            consultar_producto(con)
        elif opcion == "4":
            break
        else:
            print("⚠️ Opción no válida.")

# ================= MENÚ DE CLIENTES ==================
def menu_clientes(con):
    while True:
        print("\033[1;36m\n ═════════════════════════════")
        print("       👥 MENÚ DE CLIENTES       ")
        print("════════════════════════════ \033[0m")
        print("1️⃣   Agregar cliente")
        print("2️⃣   Actualizar dirección")
        print("3️⃣  🔍 Consultar cliente")
        print("4️⃣  🔙 Volver al Menú Principal")

        opcion = input("\n Seleccione una opción: ")

        if opcion == "1":
            crear_nuevo_cliente(con)
        elif opcion == "2":
            actualizar_direccion_cliente(con)
        elif opcion == "3":
            consultar_cliente(con)
        elif opcion == "4":
            break
        else:
            print("⚠️ Opción no válida, intente nuevamente.")

# ================= MENÚ DE COMPRAS ==================
def menu_compras(con):   
    carrito = [] 

    while True:
        if carrito:
            print("\n🛒 Productos en el carrito:")
            for i, item in enumerate(carrito):
                print(f"{i + 1}. {item[1]} unidades de {item[0]} a ${item[2]} cada una.")
        print("\033[1;31m\n ═════════════════════════════")
        print("       🛍 MENÚ DE COMPRAS       ")
        print("════════════════════════════ \033[0m")
        print("1️⃣  ➕ Añadir producto")
        print("2️⃣  ➖ Quitar producto")
        print("3️⃣  ✅ Finalizar compra")
        print("4️⃣  🔙 Volver")

        opcion = input("\n Seleccione una opción: ")

        if opcion == '1':
            añadir_producto(carrito, con)
        elif opcion == '2':
            quitar_producto(carrito)
        elif opcion == '3':
            finalizar_compra(carrito, con)
        elif opcion == '4':
            print("🎉 Gracias por su compra 🍻")
            break
        else:
            print("⚠️ Opción no válida.")

if __name__ == "__main__":
    menu_principal()
