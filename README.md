# API de Gestión de Productos y Órdenes

Este proyecto es una API desarrollada con **FastAPI** que permite gestionar productos y órdenes utilizando **un árbol binario de búsqueda (BST) para productos** y **una lista enlazada para pedidos**. Además, se integra con una base de datos (MySQL) para persistir los productos.

---

## 📦 Estructura del Proyecto

- `models/`: Contiene las clases de **Product**, **Order**, y los nodos para BST y listas enlazadas.
  - `ProductNode.py` → Implementa `ProductNode` y `BinaryTreeSearch`.
  - `OrderNode.py` → Implementa `OrderNode` y `OrderList`.
- `services/`: Servicios para manejar la persistencia de productos en la base de datos.
  - `ProductServices.py` → Función `create_product` para guardar productos en DB.
- `main.py`: Archivo principal que expone los endpoints de la API.

---

## 🌳 Árbol Binario de Búsqueda para Productos

Se utiliza un **BST** para almacenar los productos y permitir búsquedas eficientes por `id`.

- `ProductNode`:
  - `product` → Objeto `Product`.
  - `left` → Nodo hijo izquierdo.
  - `right` → Nodo hijo derecho.
- `BinaryTreeSearch`:
  - `insert(product)` → Inserta un producto en el árbol respetando la propiedad BST.
  - `search_by_id(product_id)` → Busca un producto por ID.
  - `inorder_traversal()` → Devuelve la lista de productos ordenados por ID.

---

## 🔗 Lista Enlazada para Órdenes

Se utiliza `OrderList` como una **lista enlazada simple** para almacenar los pedidos:

- `OrderNode` → Nodo que contiene un `Order`.
- `OrderList`:
  - `insert(order)` → Inserta un pedido al final de la lista.
  - `search_by_id(order_id)` → Busca un pedido por ID.
  - `delete_order_by_id(order_id)` → Elimina un pedido por ID.
  - `list_orders()` → Lista todos los pedidos almacenados.

---

## 🚀 Endpoints de la API

### 1. **Root**
```http
GET /
Devuelve un mensaje de bienvenida.
{"Bienvenido a la API de pedidos de Kilian Torres"}
2. Listar productos en BST
GET /list_products_bst
Retorna todos los productos insertados en el árbol binario de búsqueda, en orden ascendente por id.
[
    {"id": 1, "name": "Producto A", "price": 10.99, "description": "Descripcion A"},
    {"id": 2, "name": "Producto B", "price": 5.49, "description": "Descripcion B"}
]
3. Crear producto
POST /create_product
Crea un producto y lo agrega al BST y a la base de datos.
Request JSON:
{
    "id": 4,
    "name": "Producto D",
    "price": 12.50,
    "description": "Descripcion D"
}
Response:
{"message:ha sido creado correctamente"}
4. Obtener producto por ID
GET /get_product_bst/{product_id}
Busca un producto en el BST por su id.
Ejemplo:
GET /get_product_bst/2
Response:
{"id": 2, "name": "Producto B", "price": 5.49, "description": "Descripcion B"}
5. Crear un pedido
POST /create_order
Crea un pedido usando productos existentes en el BST.
Request JSON:
{
    "id": 101,
    "product_ids": [1, 3]
}
Response:
{
    "message": "Order created",
    "order_id": 101,
    "products": [
        {"id": 1, "name": "Producto A", "price": 10.99, "description": "Descripcion A"},
        {"id": 3, "name": "Producto C", "price": 7.99, "description": "Descripcion C"}
    ]
}
6. Obtener pedido por ID
GET /get_order_by_id/{order_id}
Devuelve el pedido con los productos asociados.
Response:
{
    "id": 101,
    "products": ["Producto A", "Producto C"]
}
7. Listar todos los pedidos
GET /get_all_orders
Devuelve todos los pedidos almacenados en la lista enlazada.
Response:
[
    {"id": 100, "products": ["Producto A", "Producto B"]},
    {"id": 200, "products": ["Producto C"]}
]
8. Eliminar un pedido
DELETE /delete_order/{order_id}
Elimina un pedido por su ID.
Response:
{"message": "Order 101 deleted successfully"}
