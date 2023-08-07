from clientes import Clientes

base_de_datos = {}

cliente1 = Clientes("001", "Guido", "Almada","35447741")
cliente2 = Clientes("002", "Mariano", "Barraco", "34355864")

cliente2.editar_cliente("002", "Roman", "Riquelme", "34355864")

Clientes.mostrar_base_de_datos()