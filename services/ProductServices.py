from models.ProductNode import ProductNode, BinaryTreeSearch
from models.Product import Product
from fastapi import FastAPI
import mysql.connector
from configuration.databaseConnection import DatabaseConnection

class ProductServices:
    def __init__(self):
        pass
    
    async def create_product(self, product:ProductNode):
        # Lógica para crear un producto en la base de datos
        db_connection = DatabaseConnection(
            host="localhost",
            user="root",
            password="Mininayara23",
            database="shop"
        )
        conn = await db_connection.connect()
        cursor = conn.cursor()
        insert_query = "INSERT INTO products (name, price, description) VALUES (%s, %s, %s)"
        values = (product.get_product().name, product.get_product().price, product.get_product().description)
        cursor.execute(insert_query, values)
        conn.commit()
        
        #obtener el id del producto insertado
        product_id = cursor.lastrowid
        
        cursor.close()
        conn.close()
        return {"message": "Product created successfully",
                "id": product_id}
    
    #metodo para leer un producto por id
    async def get_product_by_id(self, product_id: int):
        db_connection = DatabaseConnection(
            host="localhost",
            user="root",
            password="Mininayara23",
            database="shop"
        )
        conn = await db_connection.connect()
        cursor = conn.cursor()
        select_query = "SELECT id, name, price, description FROM products WHERE id = %s"
        cursor.execute(select_query, (product_id,))
        result = cursor.fetchone()
        conn.close()
        if result:
            product = Product(id=result[0], name=result[1], price=result[2], description=result[3])
            return product
        else:
            return {"message": "Product not found"}     

    

