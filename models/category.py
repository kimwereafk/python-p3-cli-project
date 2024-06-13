from database.connection import get_db_connection

class Category:
    def __init__(self, name):
        self._name = name
        self._id = None

    @property
    def id(self):
        return self._id

    def save(self):
        existing_category = Category.get_by_name(self._name)
        if existing_category:
            self._id = existing_category.id
        else:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO categories (name) VALUES (?)', (self._name,))
            self._id = cursor.lastrowid
            conn.commit()
            conn.close()

    @classmethod
    def get_by_name(cls, name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM categories WHERE name = ?', (name,))
        category_data = cursor.fetchone()
        conn.close()
        if category_data:
            category = cls(category_data[1])
            category._id = category_data[0]
            return category
        return None

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM categories')
        categories_data = cursor.fetchall()
        conn.close()
        categories = []
        for row in categories_data:
            category = cls(row[1])
            category._id = row[0]
            categories.append(category)
        return categories

    def update_name(self, new_name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE categories SET name = ? WHERE id = ?', (new_name, self._id))
        conn.commit()
        conn.close()
        self._name = new_name

    @classmethod
    def delete_by_name(cls, name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM categories WHERE name = ?', (name,))
        conn.commit()
        conn.close()