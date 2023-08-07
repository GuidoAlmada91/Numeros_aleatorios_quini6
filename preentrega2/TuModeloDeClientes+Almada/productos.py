class Productos:
    def __init__ (self, producto, precio):
        self.producto = producto
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.producto} $:{self.precio}"
        