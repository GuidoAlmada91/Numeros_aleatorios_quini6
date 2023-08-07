from clientes import Clientes
from productos import Productos

cliente1 = Clientes("Guido", "Almada", "guido.almada.91@gmail.com")
cliente2 = Clientes("Mariano", "Barraco", "marianobarraco@gmail.com")
print(cliente1)
print(cliente2)

producto1 = Productos("Manzana", 50)
producto2 = Productos("Banana", 75)
producto3 = Productos("Pera", 45)
producto4 = Productos("Durazno", 90)


cliente1.agregar_al_carrito(producto1)

cliente1.agregar_al_carrito(producto4)

cliente2.agregar_al_carrito(producto3)

cliente2.agregar_al_carrito(producto2)

cliente1.eliminar_del_carrito(producto1)

cliente1.mostrar_carrito()
cliente2.mostrar_carrito()
cliente2.calcular_total()
cliente1.calcular_total()
