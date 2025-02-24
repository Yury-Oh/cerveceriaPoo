#Para procesos de impresión y busqueda de archivos en las carpetas de windows
import os, sqlite3
from sqlite3 import Error

#Esta función se encarga de generar un documento plano txt en el que se ponen los datos de la factura
#para despues imprimirla

class Factura:
    def __init__(self, con, nombre, apellido, direccion, telefono, productos, imprimir):
        self.conex = con
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.productos = productos
        self.imprimir = imprimir

    def generar_factura(self, num_factura, nombre, apellido, dic, tel, lista_productos):
        global numero_factura, comprador, direccion, telefono, total, relleno, titulos_tabla_formateado
        #agrega espacios antes de las lineas para centrar los textos
        def ajustador_de_linea():
            global numero_factura, comprador, direccion, telefono, total, relleno, titulos_tabla_formateado
            linea_mas_larga = 40
            #Fase 1, comprobar cual de todas las lineas tiene la mayor extensión
            if len(numero_factura) > linea_mas_larga:
                linea_mas_larga = len(numero_factura)
            if len(comprador) > linea_mas_larga:
                linea_mas_larga = len(comprador)
            if len(direccion) > linea_mas_larga:
                linea_mas_larga = len(direccion)
            if len(telefono) > linea_mas_larga:
                linea_mas_larga = len(telefono)
            if len(total) > linea_mas_larga:
                linea_mas_larga = len(total)
            
            #Formatea la lista de productos y prueba su extensión
            for i in lista_productos:
                cadena_actual = i[0] + " | " + str(i[1]) + " | " + str(i[2]) + " | " + str(i[1]*i[2])
                if len(cadena_actual) > linea_mas_larga:
                    linea_mas_larga = len(cadena_actual)
            
            #Fase 2, sabiendo la linea más larga, queda hallar el más largo de cada cartegoria del cuerpo
            largo_producto = 10
            largo_cantidad = 10
            largo_unidad = 8
            largo_subtotal = 10
            for i in producto:
                if len(i) > largo_producto:
                    largo_producto = len(i)

            for i in cantidad:
                if len(i) > largo_cantidad:
                    largo_cantidad = len(i)

            for i in precio_unidad:
                if len(i) > largo_unidad:
                    largo_unidad = len(i)
            
            for i in subtotal:
                if len(i) > largo_subtotal:
                    largo_subtotal = len(i)
            
            #fase 3, Agregar los espacios necesarios a cada linea para que quede centrada
            numero_factura = numero_factura.center(linea_mas_larga)
            comprador = comprador.center(linea_mas_larga)
            direccion = direccion.center(linea_mas_larga)
            telefono = telefono.center(linea_mas_larga)
            total = total.center(linea_mas_larga)
            relleno = relleno.center(linea_mas_larga+1, "-")

            #fase 4, Agregar espacios a los productos de la tabla para que la tabla no se deforme
            for i in range(len(producto)):
                producto[i] = producto[i].center(largo_producto)
            for i in range(len(cantidad)):
                cantidad[i] = cantidad[i].center(largo_cantidad)
            for i in range(len(precio_unidad)):
                precio_unidad[i] = precio_unidad[i].center(largo_unidad)
            for i in range(len(subtotal)):
                subtotal[i] = subtotal[i].center(largo_subtotal)
            
            titulos_tabla[0] = titulos_tabla[0].center(largo_producto)
            titulos_tabla[1] = titulos_tabla[1].center(largo_cantidad)
            titulos_tabla[2] = titulos_tabla[2].center(largo_unidad)
            titulos_tabla[3] = titulos_tabla[3].center(largo_subtotal)
            titulos_tabla_formateado = f"{titulos_tabla[0]}|{titulos_tabla[1]}|{titulos_tabla[2]}|{titulos_tabla[3]}".center(linea_mas_larga)

            #Colocamos los elementos del cuerpo en el formato
            for i in range(len(lista_productos)):
                lista_productos_formateada.append(producto[i] + "|" + cantidad[i] + "|" + precio_unidad[i] + "|" + subtotal[i])
                lista_productos_formateada[i] = lista_productos_formateada[i].center(linea_mas_larga)

        #calcula el valor total a pagar por el cliente al final
        def calculo_total():
            resultado = 0
            for i in lista_productos:
                resultado_actual = i[1]*i[2]
                resultado += resultado_actual
            return resultado
        
        #Crea un documento txt con la factura para imprimir
        def generar_txt():
            global cadena_factura
            cadena_factura = "factura" + str(num_factura+1)
            with open("Facturas\\" + cadena_factura + ".txt", "a") as file:
                #Creamos el encabezado de la factura
                file.write(f"{numero_factura}\n\n{comprador}\n{direccion}\n{telefono}\n\n{relleno}\n\n{titulos_tabla_formateado}\n")

                #Creamos el cuerpo de la factura
                for i in range(len(lista_productos)):
                    file.write(lista_productos_formateada[i] + "\n")
                
                #Creamos el pie de la factura
                file.write(f"\n{relleno}\n\n{total}")


        #Datos de encabezado de la factura
        numero_factura = "FACTURA No. " + str(num_factura+1)
        comprador = "COMPRADOR: " + nombre + " " + apellido
        direccion = "DIRECCION: " + dic
        telefono = "TEL: " + tel
        relleno = "-"

        #Datos de cuerpo de la factura
        producto = []
        cantidad = []
        precio_unidad = []
        subtotal = []
        titulos_tabla = ["PRODUCTO", "CANTIDAD", "UNIDAD", "SUBTOTAL"]
        titulos_tabla_formateado = None
        lista_productos_formateada = []

        for i in lista_productos:
            producto.append(i[0])
            cantidad.append(str(i[1]))
            precio_unidad.append(str(int(i[2])) + "$")
            subtotal.append(str(int(i[1]*i[2])) + "$")

        #Datos de pie de factura
        total = "TOTAL: " + str(int(calculo_total())) + "$"

        #agregamos espacios para centrar los textos
        ajustador_de_linea()
        
        #Creamos un documento txt con la factura
        generar_txt()

    #Esta función imprimira el documento txt que se le coloque en la ruta
    def imprimir_factura(self, ruta):
        try:
            os.startfile(ruta, "print")
            print("Impresión exitosa")
        except:
            print("Impresión fallida")

    def leer_factura(self):
        global cadena_factura
        def consultarNumeroFactura ():
            cursorObj = self.conex.cursor()
            #recorremos la BD con el objeto de conexion
            cad = f'''SELECT noIdFactura FROM factura'''
            #creamos la cadena con el sql a ejecutar
            cursorObj.execute(cad)
            #ejecutamos la cadena con el método execute
            filas = cursorObj.fetchall()
            return len(filas)
        
        def añadirFactura ():
            cursorObj = self.conex.cursor()
            #recorremos la BD con el objeto de conexion
            cad = f'''INSERT INTO factura VALUES ({numeroFactura+1})'''
            #creamos la cadena con el sql a ejecutar
            cursorObj.execute(cad)
            #ejecutamos la cadena con el método execute
            self.conex.commit()
            #guardamos los cambios

        numeroFactura = consultarNumeroFactura()
        try:
            self.generar_factura(numeroFactura, self.nombre, self.apellido, self.direccion, self.telefono, self.productos)
            añadirFactura()
            if self.imprimir:
                self.imprimir_factura("Facturas\\"+ cadena_factura +".txt")
        except:
            print("Error al generar la factura")
