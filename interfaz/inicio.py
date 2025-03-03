
from PyQt5 import QtCore, QtGui, QtWidgets
from sesionAdministradores import Ui_sesionAdministradores

class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_sesionAdministradores()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Elephant")
        font.setPointSize(14)
        self.frame.setFont(font)
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame.setStyleSheet("background-color: rgb(52, 37, 30);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(160, 110, 491, 51))
        font = QtGui.QFont()
        font.setFamily("Elephant")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(225, 161, 11)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(250, 180, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Elephant")
        font.setPointSize(18)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(218, 194, 141)")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(300, 250, 211, 161))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../../imagenes/cerveza.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.BotonAdministradores = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.BotonAdministradores.setGeometry(QtCore.QRect(100, 460, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Elephant")
        font.setPointSize(14)
        self.BotonAdministradores.setFont(font)
        self.BotonAdministradores.setStyleSheet("background-color: rgb(225, 161, 11);\n"
"\n"
"border-radius:20px;\n"
"")
        self.BotonAdministradores.setAutoDefault(False)
        self.BotonAdministradores.setDefault(False)
        self.BotonAdministradores.setFlat(False)
        self.BotonAdministradores.setObjectName("BotonAdministradores")
        self.BotonClientes = QtWidgets.QPushButton(self.frame)
        self.BotonClientes.setGeometry(QtCore.QRect(510, 460, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Elephant")
        font.setPointSize(14)
        self.BotonClientes.setFont(font)
        self.BotonClientes.setStyleSheet("background-color: rgb(225, 161, 11);\n"
"\n"
"border-radius:20px;\n"
"")
        self.BotonClientes.setAutoDefault(False)
        self.BotonClientes.setDefault(False)
        self.BotonClientes.setFlat(False)
        self.BotonClientes.setObjectName("BotonClientes")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Bienvenido a BeBeer"))
        self.label_2.setText(_translate("MainWindow", "Tu Cervecería Artesanal"))
        self.BotonAdministradores.setText(_translate("MainWindow", "Administradores"))
        self.BotonClientes.setText(_translate("MainWindow", "Clientes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
