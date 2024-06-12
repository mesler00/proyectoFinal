from carrito import Carrito

class Cliente:
    def __init__(self, nombre, apellido, fecha_nacimiento, mail, ubicacion_compra):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.mail = mail
        self.carrito = Carrito()

    def get_carrito(self) -> Carrito:
        self.carrito