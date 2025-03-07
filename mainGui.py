import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, Qt
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from baseDatos import GestorBD
from productos import Producto

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('Productos2.ui', self)

        self.bt_menu.clicked.connect(self.mover_menu)

        
        # Conectar a la base de datos
        self.base_datos = GestorBD()
        self.base_datos.conectar_bd()
        self.base_datos.crear_tablas()

        # Ocultamos los botones
        self.bt_restaurar.hide()

        # Conectar botones a funciones
        self.bt_refrescar.clicked.connect(self.mostrar_productos)
        self.bt_agregar.clicked.connect(self.agregar_productos)
        self.bt_actualiza_buscar.clicked.connect(self.buscar_por_id)
        self.bt_actualizar.clicked.connect(self.actualizar_nombre)

        # Control de ventana
        self.bt_minimizar.clicked.connect(self.showMinimized)
        self.bt_restaurar.clicked.connect(self.control_bt_normal)
        self.bt_maximizar.clicked.connect(self.control_bt_maximizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        # Configuración de UI
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # Permitir redimensionamiento
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # Permitir mover la ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana

        # Configurar las páginas del `stackedWidget`
        self.bt_datos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_datos))
        self.bt_agregar_producto.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_agregar))
        self.bt_actualizar_nombre.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))
        
        # Configurar tabla
        self.tabla_productos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def control_bt_normal(self):
        self.showNormal()
        self.bt_restaurar.hide()
        self.bt_maximizar.show()

    def control_bt_maximizar(self):
        self.showMaximized()
        self.bt_maximizar.hide()
        self.bt_restaurar.show()

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    def mousePressEvent(self, event):
        self.click_position = event.globalPos()

    def mover_ventana(self, event):
        if not self.isMaximized() and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.click_position)
            self.click_position = event.globalPos()
            event.accept()

    def mover_menu(self):
        width = self.frame_control.width()
        new_width = 200 if width == 0 else 0
        self.animacion = QPropertyAnimation(self.frame_control, b'minimumWidth')
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(new_width)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacion.start()
    
    def mostrar_productos(self):
        self.tabla_productos.setRowCount(0)  # Limpiar tabla
        self.base_datos.conectar_bd()
        productos = self.base_datos.obtener_productos()  # Obtener productos desde la BD

        for row_idx, producto in enumerate(productos):
            self.tabla_productos.insertRow(row_idx)
            self.tabla_productos.setItem(row_idx, 0, QTableWidgetItem(str(producto[0])))
            self.tabla_productos.setItem(row_idx, 1, QTableWidgetItem(producto[1]))
            self.tabla_productos.setItem(row_idx, 2, QTableWidgetItem(producto[2]))
            self.tabla_productos.setItem(row_idx, 3, QTableWidgetItem(producto[3]))
            self.tabla_productos.setItem(row_idx, 4, QTableWidgetItem(str(producto[4])))
            self.tabla_productos.setItem(row_idx, 5, QTableWidgetItem(str(producto[5])))

        self.signal_actualizar.setText("")
        self.signal_agregar.setText("")

    def agregar_productos(self):
        codigo = self.reg_id.text().strip().upper()
        nombre = self.reg_nombre.text().strip().upper()
        peso = self.reg_peso.text().strip().upper()
        produccion = self.reg_produccion.text().strip().upper()
        vencimiento = self.reg_vencimiento.text().strip().upper()
        venta = self.reg_venta.text().strip().upper()

        if all([codigo, nombre, peso, produccion, vencimiento, venta]):
            producto = Producto(codigo, nombre, peso, vencimiento, produccion, venta)
            self.base_datos.inserta_producto(producto)
            self.signal_agregar.setText('Producto Registrado')

            # Limpiar campos
            self.reg_id.clear()
            self.reg_nombre.clear()
            self.reg_peso.clear()
            self.reg_produccion.clear()
            self.reg_vencimiento.clear()
            self.reg_venta.clear()
        else:
            self.signal_agregar.setText('Hay Espacios Vacíos')

    def buscar_por_id(self):
        id_producto = self.act_buscar.text().strip().upper()

        if id_producto:
            producto = self.base_datos.buscar_producto_id(id_producto)  # Buscar en la BD
            
            if producto:  # Si el producto existe
                self.act_nombre.setText(producto[1])  # Nombre actual
                self.signal_actualizar.setText("Producto encontrado")
            else:
                self.signal_actualizar.setText("Producto no encontrado")
        else:
            self.signal_actualizar.setText("Ingrese un ID válido")


    def actualizar_nombre(self):
        id_producto = self.act_buscar.text().strip().upper()
        nuevo_nombre = self.act_nombre.text().strip().upper()

        if id_producto and nuevo_nombre:
            producto = self.base_datos.buscar_producto_id(id_producto)

            if producto:  # Si el producto existe, actualizar el nombre
                self.base_datos.actualizar_nombre_producto(id_producto, nuevo_nombre)
                self.signal_actualizar.setText("Nombre actualizado correctamente")
            else:
                self.signal_actualizar.setText("Producto no encontrado")
        else:
            self.signal_actualizar.setText("Ingrese ID y nuevo nombre")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec_())
