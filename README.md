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
