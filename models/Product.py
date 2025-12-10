

class Product:
    # Inicializar Producto con atributos básicos
    def __init__(self, name, price, description, id=None):
        self.id = id
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
            return f"Product(id={self.id}, name='{self.name}', price={self.price}, description='{self.description}')"
    # def update_stock(self, quantity):
    #     if quantity < 0 and abs(quantity) > self.stock:
    #         raise ValueError("Insufficient stock to reduce")
    #     self.stock += quantity

    # def apply_discount(self, percentage):
    #     if not (0 <= percentage <= 100):
    #         raise ValueError("Discount percentage must be between 0 and 100")
    #     discount_amount = self.price * (percentage / 100)
    #     self.price -= discount_amount