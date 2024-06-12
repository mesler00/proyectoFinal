class Libro:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def total(self) -> float:
        return self.price