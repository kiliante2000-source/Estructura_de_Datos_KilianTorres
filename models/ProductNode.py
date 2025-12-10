from models.Product import Product


# Vamos a crear el nodo para los productos como nodos

class ProductNode:
    def __init__(self, product: Product):
        self.product = product
        self.next = None
    
    def __str__(self):
        return str(self.product)
    
    def get_product(self) -> Product:
        return self.product 
    
class BinaryTreeSearch:
    def __init__(self):
        self.root = None
    
    def insert(self, product: Product):
        new_node = ProductNode(product)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursively(self.root, new_node)
    
    def _insert_recursively(self, current_node: ProductNode, new_node: ProductNode):
        if new_node.product.id < current_node.product.id:
            if current_node.next is None:
                current_node.next = new_node
            else:
                self._insert_recursively(current_node.next, new_node)
        else:
            if current_node.next is None:
                current_node.next = new_node
            else:
                self._insert_recursively(current_node.next, new_node)
                
    def search_by_id(self, product_id: int):
        return self._search_recursively(self.root, product_id)

    def _search_recursively(self, current_node: ProductNode, product_id: int):
        if current_node is None:
            return None  # No encontrado

        if current_node.product.id == product_id:
            return current_node.product

        if product_id < current_node.product.id:
            return self._search_recursively(current_node.next, product_id)
        else:
            return self._search_recursively(current_node.next, product_id)
    
    # def inorder_traversal(self):
    #     products = []
    #     self._inorder_recursively(self.root, products)
    #     return products
    
    # def _inorder_recursively(self, node: ProductNode, products: list):
    #     if node is not None:
    #         self._inorder_recursively(node.next, products)
    #         products.append(node.product)
    #         self._inorder_recursively(node.next, products)