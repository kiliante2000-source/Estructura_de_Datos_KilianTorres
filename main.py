import json
import mysql.connector
from fastapi import FastAPI, Request
from configuration.databaseConnection import DatabaseConnection
from models.Product import Product
from models.Order import Order
from models.ProductNode import ProductNode
from models.ProductNode import BinaryTreeSearch
from services.ProductServices import ProductServices

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


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

#Peticion para listar todos los productos desde la base de datos
@app.get("/list_orders")
async def list_orders():
    db_connection = DatabaseConnection(
        host="localhost",
        user="root",
        password="Mininayara23",
        database="shop"
    )
    conn = await db_connection.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()  
    conn.close()
    return orders

#peticion parar listar todos los productos desde el arbol binario de busqueda
@app.get("/list_products_bst")
async def list_products_bst():
    products = []
    def inorder_traversal(node):
        if node is not None:
            inorder_traversal(node.next)
            products.append(str(node.get_product()))
            inorder_traversal(node.next)
    inorder_traversal(binarytreesearch.root)
    return {"products": products}

#Petición para crear un producto en la base de datos y tambien agregarlo al árbol binario de búsqueda
@app.post("/create_product")
async def create_product_db(Request: Request):
    data = await Request.json()
    name = data.get("name")
    price = data.get("price")
    description = data.get("description")
    
    product = Product(name=name, price=price, description=description)
    product_node = ProductNode(product)
    
    product_service = ProductServices()
    result = await product_service.create_product(product_node)
    if result.get("message") == "Product created successfully":
        product.id = result.get("id")  # Asignar el ID generado al producto
        binarytreesearch.insert(product)
        return result
    else:
        return {"message": "Failed to create product"}
    
#Peticion para crear nuevo pedido con lop que tenmos almacenado en el binary tree search
@app.post("/create_order")
async def create_order():
    order = Order()
    def inorder_traversal(node):
        if node is not None:
            inorder_traversal(node.next)
            order.add_product(node.get_product())
            inorder_traversal(node.next)
    inorder_traversal(binarytreesearch.root)
    return {"products_in_order": order.list_products()}
    

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

 
#Listar todos los productos en el árbol binario de búsqueda
@app.get("/list_products_bst")
async def list_products_bst():
    bst = BinaryTreeSearch()
    # Aquí deberíamos tener lógica para insertar productos en el árbol antes de listarlos
    # Por ahora, retornamos un mensaje indicando que esta funcionalidad está pendiente
    return {"message": "Functionality to list products in BST is pending implementation"}

#Listar productos por id desde la base de datos
@app.get("/get_product/{product_id}")
async def get_product(product_id: int):
    ProductServices_instance = ProductServices()
    product = await ProductServices_instance.get_product_by_id(product_id)
    return product

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
    



    