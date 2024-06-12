class Carrito:
    def __init__(self):
        self.libros = []

    def is_empty(self):
        return len(self.libros) > 0
    
    def clear(self):
        self.libros = []
    
    def total(self):
        total = 0.0

        for l in self.libros:
            total += l.total()

        return total
    
    def add_book(self, book):
        self.libros.append(book)