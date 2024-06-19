from models.Cliente import Cliente
from models.Producto import Producto
from models.Carrito import Carrito
from controllers.ClienteController import clienteController
from controllers.ProductoController import productoController
from controllers.CarritoController import carritoController

cliente1 = Cliente("rodri","rodri.08gabriel.perez",600)
#cliente2 = Cliente("Juan","Juan_correo@gmail.com",600)
#cliente3 = Cliente("Ignacio","nacho-23.@hotmail.com",60)
#clinete4 = Cliente("Yo","Salame@gmail.com",899)

#producto1 = Producto(2054,"Harina",100,1)
#producto2 = Producto(20,"Tomate",100)
#producto3 = Producto(20523,"Azucar",100,5)
#producto4 = Producto(20765,"Yerba",200,9)


#cliente1.insertar()

#cliente2.insertar()

#cliente3.insertar()

#clinete4.insertar()

#producto1.insertar()

#p#roducto2.insertar()

#producto3.insertar()

#producto4.insertar() 

#producto5 = productoController.nuevo("Arroz",1000,10)

#producto1=Producto(201,"Yerba",299,9)
#producto1.actualizar()
#print(producto1)

#print(Cliente.obtener_uno('rodri.08gabriel.perez'))

#print(Producto.obtener(201))

#print(Producto.obtener_todo())

#print(Cliente.obtener_todo()) 




#cliente1 = clienteController.nuevo("roberto","gato@gmail.com",10)

#cliente1 = clienteController.actualizar("gato@gmail.com","dylan",30)
#print(cliente1)
#producto1 = productoController.actualizar(201,"Bowls",1200,9)
#print(productoController.borrar(205))
#cliente1 = clienteController.borrar("ahgdg")
#cliente1 = clienteController.obtener("n")
#print(clienteController.obtener("Salame@gmail.com"))
producto1 = carritoController.agregar_producto()