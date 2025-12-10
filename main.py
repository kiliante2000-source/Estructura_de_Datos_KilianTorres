import json
import mysql.connector
from fastapi import FastAPI, Request
from models.Product import Product
from models.Order import Order
from models.ProductNode import ProductNode
from models.ProductNode import BinaryTreeSearch
from models.Order import Order
from models.OrderNode import OrderNode
from models.OrderNode import OrderList
from services.ProductServices import ProductServices
from pydantic import BaseModel
from typing import List


app = FastAPI()

@app.get("/")
async def read_root():
    return {"Bienvenido a la API de pedidos de Kilian Torres"}


#tenemos que crear el arbol bianrio que almacena los productos que vayamos creando
#y tambien tenemos que crear la conexion a la base de datos para almacenar los productos creados
#y poder listarlos desde la base de datos
binarytreesearch = BinaryTreeSearch()
#Crear algunos productos de ejemplo y agregarlos al árbol binario de búsqueda
product1 = Product(id=1, name="Producto A", price=10.99, description="Descripcion A")
product2 = Product(id=2, name="Producto B", price=5.49, description="Descripcion B")
product3 = Product(id=3, name="Producto C", price=7.99, description="Descripcion C")
binarytreesearch.insert(product1)
binarytreesearch.insert(product2)
binarytreesearch.insert(product3)

#ahora lo mismo para la lista enlazada de pedidos
# Crear órdenes de prueba
o1 = Order(id=100)
o1.products.append(product1)
o1.products.append(product2)

o2 = Order(id=200)
o2.products.append(product3)

orders_list = OrderList()

orders_list.insert(o1)
orders_list.insert(o2)



#peticion parar listar todos los productos desde el arbol binario de busqueda
@app.get("/list_products_bst")
async def list_products_bst():
    list_products = binarytreesearch.inorder_traversal()
    return list_products
    
#Petición para crear un producto en la base de datos y tambien agregarlo al árbol binario de búsqueda
@app.post("/create_product")
async def create_product_db(Request: Request):
    data = await Request.json()
    id= data.get("id")
    name = data.get("name")
    price = data.get("price")
    description = data.get("description")
    
    product = Product(id=id, name=name, price=price, description=description)
    binarytreesearch.insert(product)
    product_node = ProductNode(product)
    
    product_service = ProductServices()
    result = await product_service.create_product(product_node)
    if result:
        return {"message:ha sido creado correctamente"}
    
 
#Listar todos los productos en el árbol binario de búsqueda
@app.get("/list_products_bst")
async def list_products_bst():
    bst = BinaryTreeSearch()
    # Aquí deberíamos tener lógica para insertar productos en el árbol antes de listarlos
    # Por ahora, retornamos un mensaje indicando que esta funcionalidad está pendiente
    return {"message": "Functionality to list products in BST is pending implementation"}

#Listar producto por id usando el BinaryTreeSearch
@app.get("/get_product_bst/{product_id}")
async def get_product_bst(product_id: int):
    # Aquí deberíamos tener lógica para buscar el producto en el árbol binario de búsqueda
    # Por ahora, retornamos un mensaje indicando que esta funcionalidad está pendiente
    product = binarytreesearch.search_by_id(product_id)
    if product:
        return product
    else:  
        return {"message": "Product not found in BST"}

#Schema para poder obtener los ids de los objetos para el pedido
class CreateOrderRequest(BaseModel):
    id: int
    product_ids: List[int]

#Peticion para crear nuevo pedido con lop que tenmos almacenado en el binary tree search
@app.post("/create_order")
async def create_order(order_data: CreateOrderRequest):
# Crear el objeto Order
    order = Order(id=order_data.id)

    # Buscar cada producto en tu árbol binario
    for pid in order_data.product_ids:
        product = binarytreesearch.search_by_id(pid)
        if product:
            order.add_product(product)

    # Insertar en la lista enlazada de pedidos
    orders_list.insert(order)

    return {
        "message": "Order created",
        "order_id": order.id,
        "products": [
            {
                "id": p.id,
                "name": p.name,
                "price": p.price,
                "description": p.description
            } for p in order.products
        ]
    }
    
@app.get("/get_order_by_id/{order_id}")
def get_order_by_id(order_id:int):
    
    order = orders_list.search_by_id(order_id)
    if not order:
        return {"message": "Order not found"}

    return {
        "id": order.id,
        "products": [str(p) for p in order.products]
    }
    
@app.get("/get_all_orders")
def get_all_orders():
    return orders_list.list_orders()

@app.delete("/delete_order/{order_id}")
async def delete_order(order_id: int):
    deleted = orders_list.delete_order_by_id(order_id)
    if deleted:
        return {"message": f"Order {order_id} deleted successfully"}
    else:
        return {"message": f"Order {order_id} not found"}







#ProductNode contiene las clases de producto y el arbol binario de busqueda
#Lo que vamos a comprobar es que se pueda insertar productos en el arbol
# @app.get("/test_product_node")
# async def test_product_node():
#     # Crear algunos productos de ejemplo
#     product1 = Product(id=3, name="Producto A", price=10.99,description="Descripcion A")
#     product2 = Product(id=1, name="Producto B", price=5.49, description="Descripcion B")
#     product3 = Product(id=2, name="Producto C", price=7.99, description="Descripcion C")

#     # Crear el árbol binario de búsqueda
#     bst = BinaryTreeSearch()
#     bst.insert(product1)
#     bst.insert(product2)
#     bst.insert(product3)

#     # Retornar los productos insertados para verificar
#     return {
#         "Inserted Products": [
#             str(product1),
#             str(product2),
#             str(product3)
#         ]
#     }
    
    
    
        

# #Petición para crear un nodo de producto y agregarlo al árbol binario de búsqueda
# @app.post("/create_product_node_bst")
# async def create_product_node(Request: Request):
#     data = await Request.json()
#     name = data.get("name")
#     price = data.get("price")
#     description = data.get("description")
#     product = Product(name=name, price=price, description=description)
#     bst = BinaryTreeSearch()
#     bst.insert(product)
#     return {"message": "Product node created and inserted into binary search tree successfully"}




    