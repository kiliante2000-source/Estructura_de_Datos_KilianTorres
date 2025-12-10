from pydantic import BaseModel
from typing import List

#Vamos a tener un pedido que lo inicializamos con id aleatorio y le vamos agregando los prodcutos por un metodo que recoge el json de varios pedidos
class OrderItemSchema(BaseModel):
    product_id: int
    quantity: int

class OrderCreateSchema(BaseModel):
    customer_name: str
    items: List[OrderItemSchema]

class OrderItem:
    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity
