from database.connection import get_db_connection

class Product:
    def __init__(self, name, description, price, supplier_id, category_id, stock_quantity):
        self._name = name
        self._description = description
        self._price = price
        self._supplier_id = supplier_id
        self._category_id = category_id
        self._stock_quantity = stock_quantity
        self._id = None

    @property
    def id(self):
        return self._id

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO products (name, description, price, supplier_id, category_id, stock_quantity)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self._name, self._description, self._price, self._supplier_id, self._category_id, self._stock_quantity))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()

    @classmethod
    def get_by_name(cls, name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products WHERE name = ?', (name,))
        product_data = cursor.fetchone()
        conn.close()
        if product_data:
            product = cls(product_data[1], product_data[2], product_data[3], product_data[4], product_data[5], product_data[6])
            product._id = product_data[0]
            return product
        return None

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products')
        products_data = cursor.fetchall()
        conn.close()
        products = []
        for row in products_data:
            product = cls(row[1], row[2], row[3], row[4], row[5], row[6])
            product._id = row[0]
            products.append(product)
        return products

    def update_name(self, new_name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE products SET name = ? WHERE id = ?', (new_name, self._id))
        conn.commit()
        conn.close()
        self._name = new_name

    @classmethod
    def delete_by_name(cls, name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM products WHERE name = ?', (name,))
        conn.commit()
        conn.close()