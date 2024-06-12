from carrito import Carrito
from libro import Libro

class Cliente:
    def __init__(self, nombre, apellido, fecha_nacimiento, mail):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.mail = mail
        self.carrito = Carrito()

    def get_carrito(self) -> Carrito:
        return self.carrito
    
    def __str__(self):
        return f"el nombre y apellido del cliente es {self.nombre} {self.apellido} y sus compra/s son: {self.libro} con un monto total de {self.carrito}"