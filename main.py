from models import Product, Supplier, Category
from database.connection import setup_db

def add_supplier():
    supplier_name = input("Enter supplier's name: ")
    supplier = Supplier.get_by_name(supplier_name)
    if not supplier:
        contact_information = input("Enter supplier's contact information: ")
        supplier = Supplier(supplier_name, contact_information)
        supplier.save()
        print("Supplier added successfully!")
    return supplier

def add_category():
    category_name = input("Enter category's name: ")
    category = Category.get_by_name(category_name)
    if not category:
        category = Category(category_name)
        category.save()
        print("Category added successfully!")
    return category

def add_product():
    product_name = input("Enter product's name: ")
    description = input("Enter product's description: ")
    price = float(input("Enter product's price: "))
    stock_quantity = int(input("Enter product's stock quantity: "))

    supplier = add_supplier()
    category = add_category()

    product = Product(product_name, description, price, supplier.id, category.id, stock_quantity)
    product.save()
    print("Product added successfully!")

def view_products():
    products = Product.get_all()
    print("\nProducts:")
    for product in products:
        print(f"ID: {product.id}, Name: {product._name}, Description: {product._description}, Price: {product._price}, Supplier ID: {product._supplier_id}, Category ID: {product._category_id}, Stock Quantity: {product._stock_quantity}")

def view_suppliers():
    suppliers = Supplier.get_all()
    print("\nSuppliers:")
    for supplier in suppliers:
        print(f"ID: {supplier.id}, Name: {supplier._name}, Contact Information: {supplier._contact_information}")

def view_categories():
    categories = Category.get_all()
    print("\nCategories:")
    for category in categories:
        print(f"ID: {category.id}, Name: {category._name}")

def delete_product():
    product_name = input("Enter product's name to delete: ")
    Product.delete_by_name(product_name)
    print("Product deleted successfully!")

def delete_supplier():
    supplier_name = input("Enter supplier's name to delete: ")
    Supplier.delete_by_name(supplier_name)
    print("Supplier deleted successfully!")

def delete_category():
    category_name = input("Enter category's name to delete: ")
    Category.delete_by_name(category_name)
    print("Category deleted successfully!")

def main():
    setup_db()

    while True:
        print("\nMenu:")
        print("1. Add Product")
        print("2. View Products")
        print("3. View Suppliers")
        print("4. View Categories")
        print("5. Delete Product by Name")
        print("6. Delete Supplier by Name")
        print("7. Delete Category by Name")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            view_products()
        elif choice == '3':
            view_suppliers()
        elif choice == '4':
            view_categories()
        elif choice == '5':
            delete_product()
        elif choice == '6':
            delete_supplier()
        elif choice == '7':
            delete_category()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()