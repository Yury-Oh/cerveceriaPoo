from baseDatos import conectar_bd, crear_tablas
from productos import crear_nuevo_producto, actualizar_producto, consultar_producto
from clientes import crear_nuevo_cliente, actualizar_direccion_cliente, consultar_cliente
from compras import finalizar_compra, quitar_producto, añadir_producto, mostrar_productos

def menu_principal():
    con = conectar_bd()
    if con:
        crear_tablas(con)
        
        while True:
            print("\nMenú Principal:")
            print("1. Menú de Productos")
            print("2. Menú de Clientes")
            print("3. Menú de compras")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                menu_productos(con)
            elif opcion == "2":
                menu_clientes(con)
            elif opcion == "3":
                menu_compras(con)
            elif opcion == "4":
                print("Saliendo del sistema...")
                con.close()
                break
            else:
                print("Opción no válida, intente nuevamente.")

def menu_productos(con):
    while True:
        print("\nMenú de Productos:")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Consultar producto")
        print("4. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_nuevo_producto(con)
        elif opcion == "2":
            actualizar_producto(con)
        elif opcion == "3":
            consultar_producto(con)
        elif opcion == "4":
            break

def menu_clientes(con):
    while True:
        print("\nMenú de Clientes:")
        print("1. Agregar cliente")
        print("2. Actualizar dirección de cliente")
        print("3. Consultar cliente")
        print("4. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_nuevo_cliente(con)
        elif opcion == "2":
            actualizar_direccion_cliente(con)
        elif opcion == "3":
            consultar_cliente(con)
        elif opcion == "4":
            break
        else:
            print("Opción no válida, intente nuevamente.")

    
def menu_compras(con):   
    carrito = [] 

    while True:
            if carrito:
                print("\nProductos en el carrito:")
                for i, item in enumerate(carrito):
                    print(f"{i + 1}. {item[1]} unidades de {item[0]} a ${item[2]} cada una.")
            print("\nMenú de compras")
            print("1. Añadir producto al carrito")
            print("2. Quitar producto del carrito")
            print("3. Finalizar compra")
            print("4. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                añadir_producto(carrito, con)
            elif opcion == '2':
                quitar_producto(carrito)
            elif opcion == '3':
                finalizar_compra(carrito, con)
            elif opcion == '4':
                print("Gracias por usar el sistema")
                break
            else:
                print("Opción no válida. Intente de nuevo.")




if __name__ == "__main__":
    menu_principal()
