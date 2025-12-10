from models.ProductNode import ProductNode, BinaryTreeSearch
from models.Product import Product
from fastapi import FastAPI
import mysql.connector


class ProductServices:
    def __init__(self):
        pass
    
    async def create_product(self, product:ProductNode):
        product = Product(product.get_product().name,product.get_product().name, product.get_product().price, product.get_product().description)
        
        return {"message: El producto ha sido creado de manera correcta"}
    
    #metodo para leer un producto por id
    async def get_product_by_id(self, product_id: int):
        return ""

    

