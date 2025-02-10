Sistema de Gestión para Cervecería Artesanal 
UNIVERSIDAD NACIONAL DE COLOMBIA

🍻 Descripción

Este proyecto es una aplicación de gestión para una cervecería artesanal, desarrollada en Python 3.9.10 utilizando SQLite como base de datos. Permite la administración de productos, clientes y compras de manera sencilla e intuitiva.

Autores:

Juana Saavedra
Yury Muñoz
SImón Becerra
Nicolás Ramirez

🚀 Características

Gestión de productos (agregar, actualizar, consultar).

Administración de clientes (registrar, actualizar dirección, consultar).

Funcionalidad de compras con carrito y finalización de transacción.

Diferenciación entre usuario administrador y cliente.

🔑 Acceso como Administrador

Para acceder al sistema como administrador, utilice la siguiente contraseña predeterminada:

Contraseña: admin123

Si desea cambiar la contraseña, edite la siguiente línea en el código del archivo principal:

if seleccion == "1":
    pwd = input("\n🔑 Ingrese la contraseña de administrador: ")
    if pwd == "admin123":

Reemplace admin123 por la contraseña de su elección.

