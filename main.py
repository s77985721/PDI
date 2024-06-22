from models.Carrito import Carrito
from models.Producto import Producto
from models.Cliente import Cliente
from controllers.ClienteController import ClienteController
from controllers.ProductoController import ProductoController
from controllers.CarritoController import CarritoController

"""
CLIENTES
"""


"""
Crea nuevos clientes

# cliente1 = ClienteController.nuevo("rodri.08gabriel.perez@gmail.com","rodri")
# cliente2 = ClienteController.nuevo("gato@gmail.com","roberto")
# cliente3 = ClienteController.nuevo("pepe@gmail.com","pepe")
# cliente4 = ClienteController.nuevo("agus@gmail.com","agus")
# cliente5 = ClienteController.nuevo("juan@gmail.com","juan")
# cliente6 = ClienteController.nuevo("pablo@gmail.com","pablo")
# cliente7 = ClienteController.nuevo("lucas@gmail.com","lucas")

"""

"""
Actualiza un cliente como clave su correo

cliente1 = ClienteController.actualizar("pepe@gmail.com","pepe",200)
print(cliente1)

"""

"""
Borra un cliente por su correo

print(ClienteController.borrar("gato@gmail.com"))

"""

"""

Obtener un cliente por su correo

cliente = ClienteController.obtener("juan@gmail.com")
print(cliente)

"""

"""
PRODUCTOS
"""

"""
Ingresar nuevo producto

producto = ProductoController.nuevo("Leche",200,8)
print(producto)


"""

"""
Actualiza un producto

producto = ProductoController.actualizar(205,"Azucar",200,8)
print(producto)

"""

"""
Borra un producto

producto = ProductoController.borrar(204)
print(producto)

"""

"""
Obtener un producto

producto = ProductoController.obtener(201)
print(producto)

Output: Nombre: Yerba Precio: 299

"""


"""
CARRITO
"""
cliente = ClienteController.obtener("rodri.08gabriel.perez@gmail.com")
# ClienteController.actualizar("rodri.08gabriel.perez@gmail.com","rodri",10000)
carrito = Carrito(cliente)
CarritoController.agregar_producto(carrito,205)
CarritoController.agregar_producto(carrito,205)
CarritoController.agregar_producto(carrito,201)
print(CarritoController.realizar_compra(carrito))