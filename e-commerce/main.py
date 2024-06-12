from cliente import Cliente
from carrito import Carrito
from defaults import BOOKS


cliente1 = Cliente('Marcos', 'Rojo', '30/03/1990', 'licha.lopez@bocajuniors.com')

carrito_compras = cliente1.get_carrito()
carrito_compras.add_book(BOOKS[0])
print("Total: ", carrito_compras.total())

carrito_compras.clear()
print("Total: ", carrito_compras.total())