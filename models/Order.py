
class Order:
    def __init__(self):
        self.init = None
        self.id = None
        self.listproducts = []
    
    def add_product(self, product):
        if self.init is None:
            self.init = product
        else:
            current = self.init
            while current.next is not None:
                current = current.next
            current.next = product
    
    def list_products(self):
        self.listproducts = []
        current = self.init
        while current is not None:
            self.listproducts.append(str(current))
            current = current.next
        return self.listproducts 
    
