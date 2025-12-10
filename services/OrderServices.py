class OrderService:

    async def create_order(self, order_data: OrderCreateSchema):
        db = DatabaseConnection(
            host="localhost",
            user="root",
            password="Mininayara23",
            database="shop"
        )
        conn = await db.connect()
        cursor = conn.cursor()

        # Crear pedido
        insert_order = "INSERT INTO orders (customer_name) VALUES (%s)"
        cursor.execute(insert_order, (order_data.customer_name,))
        order_id = cursor.lastrowid

        # Insertar items
        insert_item = "INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)"
        for item in order_data.items:
            cursor.execute(insert_item, (order_id, item.product_id, item.quantity))

        conn.commit()
        conn.close()

        return {"message": "Order created", "order_id": order_id}

    async def get_order(self, order_id: int):
        db = DatabaseConnection(
            host="localhost",
            user="root",
            password="Mininayara23",
            database="shop"
        )
        conn = await db.connect()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM orders WHERE id = %s", (order_id,))
        order = cursor.fetchone()

        cursor.execute("SELECT * FROM order_items WHERE order_id = %s", (order_id,))
        items = cursor.fetchall()

        conn.close()

        return {"order": order, "items": items}
