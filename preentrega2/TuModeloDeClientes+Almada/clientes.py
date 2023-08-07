
from productos import Productos

class Clientes:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.carrito = []

    def __str__(self):
        return f"Se creo exitosamente el cliente {self.nombre, self.apellido}" 
    def agregar_al_carrito(self, producto):
        self.carrito.append(producto)
        print(f"Se agrego al carrito de {self.nombre}\n {producto}")
    def eliminar_del_carrito(self, producto):
        self.carrito.remove(producto)
        print(f"Se elimino el producto\n {producto}")
    def mostrar_carrito(self):
        print("*"*50)
        print (f"Carrito de: {self.nombre} {self.apellido}")
        for producto in self.carrito:
            print(producto)
    def calcular_total(self):
        print("*"*50)
        total = 0
        for producto in self.carrito:
            total += producto.precio
        print(f"Valor total del carrito de {self.nombre} es $:{total}")
        




    
    
