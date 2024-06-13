from database.connection import get_db_connection

class Supplier:
    def __init__(self, name, contact_information):
        self._name = name
        self._contact_information = contact_information
        self._id = None

    @property
    def id(self):
        return self._id

    def save(self):
        existing_supplier = Supplier.get_by_name(self._name)
        if existing_supplier:
            self._id = existing_supplier.id
        else:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO suppliers (name, contact_information) VALUES (?, ?)', (self._name, self._contact_information))
            self._id = cursor.lastrowid
            conn.commit()
            conn.close()

    @classmethod
    def get_by_name(cls, name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM suppliers WHERE name = ?', (name,))
        supplier_data = cursor.fetchone()
        conn.close()
        if supplier_data:
            supplier = cls(supplier_data[1], supplier_data[2])
            supplier._id = supplier_data[0]
            return supplier
        return None

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM suppliers')
        suppliers_data = cursor.fetchall()
        conn.close()
        suppliers = []
        for row in suppliers_data:
            supplier = cls(row[1], row[2])
            supplier._id = row[0]
            suppliers.append(supplier)
        return suppliers

    def update_name(self, new_name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE suppliers SET name = ? WHERE id = ?', (new_name, self._id))
        conn.commit()
        conn.close()
        self._name = new_name

    @classmethod
    def delete_by_name(cls, name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM suppliers WHERE name = ?', (name,))
        conn.commit()
        conn.close()