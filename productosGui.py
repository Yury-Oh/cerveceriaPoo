# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'productos.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3
from sqlite3 import Error
from PyQt5 import QtWidgets, QtCore
from baseDatos import GestorBD


class Ui_MainWindow(object):
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 639)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_superior = QtWidgets.QFrame(self.frame)
        self.frame_superior.setMinimumSize(QtCore.QSize(0, 42))
        self.frame_superior.setStyleSheet("QFrame{\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #000000ff;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 20px;\n"
"\n"
"}")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_menu = QtWidgets.QPushButton(self.frame_superior)
        self.bt_menu.setMinimumSize(QtCore.QSize(200, 40))
        self.bt_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../imagenes/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QtCore.QSize(38, 38))
        self.bt_menu.setObjectName("bt_menu")
        self.horizontalLayout.addWidget(self.bt_menu)
        spacerItem = QtWidgets.QSpacerItem(477, 38, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bt_restaurar = QtWidgets.QPushButton(self.frame_superior)
        self.bt_restaurar.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_restaurar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../imagenes/minimizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_restaurar.setIcon(icon1)
        self.bt_restaurar.setIconSize(QtCore.QSize(38, 38))
        self.bt_restaurar.setObjectName("bt_restaurar")
        self.horizontalLayout.addWidget(self.bt_restaurar)
        self.bt_minimizar = QtWidgets.QPushButton(self.frame_superior)
        self.bt_minimizar.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_minimizar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../imagenes/reducir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_minimizar.setIcon(icon2)
        self.bt_minimizar.setIconSize(QtCore.QSize(38, 38))
        self.bt_minimizar.setObjectName("bt_minimizar")
        self.horizontalLayout.addWidget(self.bt_minimizar)
        self.bt_maximizar = QtWidgets.QPushButton(self.frame_superior)
        self.bt_maximizar.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_maximizar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../imagenes/ampliar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_maximizar.setIcon(icon3)
        self.bt_maximizar.setIconSize(QtCore.QSize(38, 38))
        self.bt_maximizar.setObjectName("bt_maximizar")
        self.horizontalLayout.addWidget(self.bt_maximizar)
        self.bt_cerrar = QtWidgets.QPushButton(self.frame_superior)
        self.bt_cerrar.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_cerrar.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../../imagenes/cerrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_cerrar.setIcon(icon4)
        self.bt_cerrar.setIconSize(QtCore.QSize(38, 38))
        self.bt_cerrar.setObjectName("bt_cerrar")
        self.horizontalLayout.addWidget(self.bt_cerrar)
        self.verticalLayout_2.addWidget(self.frame_superior)
        self.frame_contenido = QtWidgets.QFrame(self.frame)
        self.frame_contenido.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contenido.setObjectName("frame_contenido")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_contenido)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_control = QtWidgets.QFrame(self.frame_contenido)
        self.frame_control.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_control.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_control.setStyleSheet("QFrame{ \n"
"background-color: rgb(225, 161, 11);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(61, 61, 61);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"color: rgb(0, 0, 0);\n"
"font: 77 10pt \"Arial Black\";\n"
"}")
        self.frame_control.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_control.setObjectName("frame_control")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_control)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bt_datos = QtWidgets.QPushButton(self.frame_control)
        self.bt_datos.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_datos.setObjectName("bt_datos")
        self.verticalLayout_3.addWidget(self.bt_datos)
        self.bt_agregar_producto = QtWidgets.QPushButton(self.frame_control)
        self.bt_agregar_producto.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_agregar_producto.setObjectName("bt_agregar_producto")
        self.verticalLayout_3.addWidget(self.bt_agregar_producto)
        self.bt_actualizar_nombre = QtWidgets.QPushButton(self.frame_control)
        self.bt_actualizar_nombre.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_actualizar_nombre.setObjectName("bt_actualizar_nombre")
        self.verticalLayout_3.addWidget(self.bt_actualizar_nombre)
        self.horizontalLayout_2.addWidget(self.frame_control)
        self.frame_paginas = QtWidgets.QFrame(self.frame_contenido)
        self.frame_paginas.setStyleSheet("QFrame{\n"
"background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QLabel{\n"
"font: 87 12pt \"Arial Black\";\n"
"background-color: #000000ff;\n"
"color: rgb(225, 161, 11);\n"
"border:0px solid #14C8DC;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border:0px;\n"
"color: rgb(225, 161, 11);\n"
"border-bottom: 2px solid rgb(61, 61, 61);\n"
"font: 75 12pt \"Times New Roman\";\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(225, 161, 11);\n"
"border-radius: 15px;\n"
"color: rgb(0, 0, 0);\n"
"font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QTableWidget {\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 8pt;\n"
"gridline-color: rgb(0, 206, 151); \n"
"color: #000000;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: rgb(225, 161, 11);\n"
"border: 1px solid rgb(0, 0, 0);\n"
"font-size: 8pt;\n"
"}\n"
"\n"
"QTableWidget QTableComerButton::section {\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}")
        self.frame_paginas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_paginas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_paginas.setObjectName("frame_paginas")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_paginas)
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_paginas)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_actualizar = QtWidgets.QWidget()
        self.page_actualizar.setObjectName("page_actualizar")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_actualizar)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.page_actualizar)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_9.addWidget(self.label_10)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.page_actualizar)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.act_buscar = QtWidgets.QLineEdit(self.page_actualizar)
        self.act_buscar.setObjectName("act_buscar")
        self.horizontalLayout_8.addWidget(self.act_buscar)
        self.bt_actualiza_buscar = QtWidgets.QPushButton(self.page_actualizar)
        self.bt_actualiza_buscar.setMinimumSize(QtCore.QSize(120, 30))
        self.bt_actualiza_buscar.setObjectName("bt_actualiza_buscar")
        self.horizontalLayout_8.addWidget(self.bt_actualiza_buscar)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.page_actualizar)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.act_nombre = QtWidgets.QLineEdit(self.page_actualizar)
        self.act_nombre.setObjectName("act_nombre")
        self.horizontalLayout_6.addWidget(self.act_nombre)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.signal_actualizar = QtWidgets.QLabel(self.page_actualizar)
        self.signal_actualizar.setMinimumSize(QtCore.QSize(120, 30))
        self.signal_actualizar.setText("")
        self.signal_actualizar.setObjectName("signal_actualizar")
        self.horizontalLayout_7.addWidget(self.signal_actualizar)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.bt_actualizar = QtWidgets.QPushButton(self.page_actualizar)
        self.bt_actualizar.setMinimumSize(QtCore.QSize(120, 30))
        self.bt_actualizar.setObjectName("bt_actualizar")
        self.horizontalLayout_7.addWidget(self.bt_actualizar)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.stackedWidget.addWidget(self.page_actualizar)
        self.page_agregar = QtWidgets.QWidget()
        self.page_agregar.setObjectName("page_agregar")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_agregar)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.page_agregar)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(30)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.page_agregar)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.page_agregar)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.page_agregar)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.page_agregar)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.page_agregar)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.page_agregar)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.reg_id = QtWidgets.QLineEdit(self.page_agregar)
        self.reg_id.setObjectName("reg_id")
        self.verticalLayout_6.addWidget(self.reg_id)
        self.reg_nombre = QtWidgets.QLineEdit(self.page_agregar)
        self.reg_nombre.setObjectName("reg_nombre")
        self.verticalLayout_6.addWidget(self.reg_nombre)
        self.reg_peso = QtWidgets.QLineEdit(self.page_agregar)
        self.reg_peso.setObjectName("reg_peso")
        self.verticalLayout_6.addWidget(self.reg_peso)
        self.reg_vencimiento = QtWidgets.QLineEdit(self.page_agregar)
        self.reg_vencimiento.setObjectName("reg_vencimiento")
        self.verticalLayout_6.addWidget(self.reg_vencimiento)
        self.reg_produccion = QtWidgets.QLineEdit(self.page_agregar)
        self.reg_produccion.setObjectName("reg_produccion")
        self.verticalLayout_6.addWidget(self.reg_produccion)
        self.reg_venta = QtWidgets.QLineEdit(self.page_agregar)
        self.reg_venta.setObjectName("reg_venta")
        self.verticalLayout_6.addWidget(self.reg_venta)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.signal_agregar = QtWidgets.QLabel(self.page_agregar)
        self.signal_agregar.setMinimumSize(QtCore.QSize(200, 30))
        self.signal_agregar.setText("")
        self.signal_agregar.setAlignment(QtCore.Qt.AlignCenter)
        self.signal_agregar.setObjectName("signal_agregar")
        self.horizontalLayout_5.addWidget(self.signal_agregar)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.bt_agregar = QtWidgets.QPushButton(self.page_agregar)
        self.bt_agregar.setMinimumSize(QtCore.QSize(200, 30))
        self.bt_agregar.setObjectName("bt_agregar")
        self.horizontalLayout_5.addWidget(self.bt_agregar)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.stackedWidget.addWidget(self.page_agregar)
        self.page_datos = QtWidgets.QWidget()
        self.page_datos.setObjectName("page_datos")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_datos)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.page_datos)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.tabla_productos = QtWidgets.QTableWidget(self.page_datos)
        self.tabla_productos.setObjectName("tabla_productos")
        self.tabla_productos.setColumnCount(6)
        self.tabla_productos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(5, item)
        self.verticalLayout_5.addWidget(self.tabla_productos)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.bt_refrescar = QtWidgets.QPushButton(self.page_datos)
        self.bt_refrescar.setMinimumSize(QtCore.QSize(120, 30))
        self.bt_refrescar.setObjectName("bt_refrescar")
        self.horizontalLayout_3.addWidget(self.bt_refrescar)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.stackedWidget.addWidget(self.page_datos)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_paginas)
        self.verticalLayout_2.addWidget(self.frame_contenido)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_datos.setText(_translate("MainWindow", "Consultar Producto"))
        self.bt_agregar_producto.setText(_translate("MainWindow", "Agregar Producto"))
        self.bt_actualizar_nombre.setText(_translate("MainWindow", "Actualizar Nombre"))
        self.label_10.setText(_translate("MainWindow", "ACTUALIZAR NOMBRE PRODUCTO"))
        self.label_11.setText(_translate("MainWindow", "Id del Producto a Actualizar:"))
        self.bt_actualiza_buscar.setText(_translate("MainWindow", "BUSCAR"))
        self.label_12.setText(_translate("MainWindow", "Nuevo Nombre"))
        self.bt_actualizar.setText(_translate("MainWindow", "ACTUALIZAR"))
        self.label_8.setText(_translate("MainWindow", "AGREGAR PRODUCTO"))
        self.label_2.setText(_translate("MainWindow", "No Identificador"))
        self.label_3.setText(_translate("MainWindow", "Nombre"))
        self.label_4.setText(_translate("MainWindow", "Peso o Volumen"))
        self.label_5.setText(_translate("MainWindow", "Fecha Vencimiento"))
        self.label_6.setText(_translate("MainWindow", "Precio de Produccion"))
        self.label_7.setText(_translate("MainWindow", "Precio de Venta"))
        self.bt_agregar.setText(_translate("MainWindow", "AGREGAR"))
        self.label.setText(_translate("MainWindow", "PRODUCTOS"))
        item = self.tabla_productos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "noIdProducto"))
        item = self.tabla_productos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "nombreProducto"))
        item = self.tabla_productos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "pesoVolumen"))
        item = self.tabla_productos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "fechaVencimiento"))
        item = self.tabla_productos.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "precioProduccion"))
        item = self.tabla_productos.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "precioVenta"))
        self.bt_refrescar.setText(_translate("MainWindow", "Refrescar"))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect the refresh button to the update table method
        self.ui.bt_refrescar.clicked.connect(self.actualizar_tabla)

        # Initialize the database manager
        self.gestor_bd = GestorBD()
        self.gestor_bd.conectar_bd()
        self.gestor_bd.crear_tablas()

        # Initial table update
        self.actualizar_tabla()

    def actualizar_tabla(self):
        # Fetch data from the database
        productos = self.gestor_bd.obtener_productos()

        # Clear the table
        self.ui.tabla_productos.setRowCount(0)

        # Populate the table with data
        for row_index, producto in enumerate(productos):
            self.ui.tabla_productos.insertRow(row_index)
            for col_index, value in enumerate(producto):
                self.ui.tabla_productos.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(value)))

    def closeEvent(self, event):
        # Close the database connection when the application is closed
        self.gestor_bd.cerrar_bd()
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
