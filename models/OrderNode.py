from models.Order import Order

# Nodo de pedido
class OrderNode:
    def __init__(self, order):
        self.order = order  # tipo Order
        self.next = None

    def __str__(self):
        return str(self.order)

    def get_order(self):
        return self.order


# Lista enlazada para manejar pedidos
class OrderList:
    def __init__(self):
        self.head = None

    # Insertar un pedido en la lista
    def insert(self, order):
        new_node = OrderNode(order)
        if self.head is None:
            self.head = new_node
        else:
            self._insert_recursively(self.head, new_node)

    # Lógica de inserción basada en id (para mantener orden)
    def _insert_recursively(self, current_node: OrderNode, new_node: OrderNode):
        if new_node.order.id < current_node.order.id:
            if current_node.next is None:
                current_node.next = new_node
            else:
                self._insert_recursively(current_node.next, new_node)
        else:
            if current_node.next is None:
                current_node.next = new_node
            else:
                self._insert_recursively(current_node.next, new_node)

    # Buscar un pedido por id
    def search_by_id(self, order_id: int):
        return self._search_recursively(self.head, order_id)

    def _search_recursively(self, current_node: OrderNode, order_id: int):
        if current_node is None:
            return None  # No encontrado

        if current_node.order.id == order_id:
            return current_node.order

        return self._search_recursively(current_node.next, order_id)

    # Obtener todos los pedidos (para mostrar en Postman)
    def list_orders(self):
        orders = []
        current = self.head
        while current:
            orders.append({
                "id": current.order.id,
                "products": [
                    {
                        "id": p.id,
                        "name": p.name,
                        "price": p.price,
                        "description": p.description
                    } for p in current.order.products
                ]
            })
            current = current.next
        return orders
    
    def delete_order_by_id(self, order_id: int):
        current = self.head
        prev = None
        while current:
            if current.order.id == order_id:
                # Si es el primer nodo
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return True  # Pedido eliminado
            prev = current
            current = current.next

        return False  # Pedido no encontrado