
class Order:
    def __init__(self, id):
        self.init = None
        self.id = id
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def list_products(self):
        self.products = []
        current = self.init
        while current is not None:
            self.products.append(str(current))
            current = current.next
        return self.products 
    
