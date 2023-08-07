

class Clientes:
    base_de_datos = {}
    def __init__(self, numero_cliente, nombre, apellido, dni):
        self.numero_cliente = numero_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        Clientes.base_de_datos[self.numero_cliente] = self

    def __str__(self):
        return f"DATOS: {self.numero_cliente, self.nombre, self.apellido, self.dni}"
    
    def mostrar_cliente(self):
        print("*"*50)
        print(f"Numero de cliente: \n -- {self.numero_cliente} -- \n -Nombre: {self.nombre} \n -Apellido: {self.apellido} \n -Dni: {self.dni}")
    
    def editar_cliente(self, numero_cliente, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        Clientes.base_de_datos[self.numero_cliente] = self

    def mostrar_base_de_datos():
        print("Base de datos de clientes: ")
        for numero_cliente,cliente in Clientes.base_de_datos.items():
            cliente.mostrar_cliente()
            

    



    
    
