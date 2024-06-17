# Inventory Management System

This Inventory Management System is a Python CLI application designed to manage products, suppliers, and categories. The system allows you to add, view, and delete records of products, suppliers, and categories.

## Features

- Add, view, update, and delete products
- Add, view, update, and delete suppliers
- Add, view, update, and delete categories

## Project Structure

python-p3-cli-project/
│
├── models/
│ ├── init.py
│ ├── product.py
│ ├── supplier.py
│ └── category.py
├── database/
│ ├── init.py
│ ├── connection.py
│ └── database.db
├── Pipfile
├── Pipfile.lock



## Requirements

- Python 3.8
- pipenv

## Setup

1. **Clone the repository**:
2. **Install dependencies**:
3. **Activate the virtual environment**:
4. **Run the application**:
## Usage

When you run the application, you'll see a menu with options to add, view, and delete products, suppliers, and categories.

### Menu Options

1. **Add Product**: Add a new product along with its supplier and category.
2. **View Products**: Display all products in the inventory.
3. **View Suppliers**: Display all suppliers.
4. **View Categories**: Display all categories.
5. **Delete Product by Name**: Delete a product by its name.
6. **Delete Supplier by Name**: Delete a supplier by its name.
7. **Delete Category by Name**: Delete a category by its name.
8. **Exit**: Exit the application.

### Adding a Product

When you choose to add a product, you'll be prompted to enter the following details:

- Product's name
- Product's description
- Product's price
- Product's stock quantity
- Supplier's name (If the supplier doesn't exist, you'll be prompted to enter their contact information)
- Category's name (If the category doesn't exist, it will be added)

### Viewing Records

You can view all products, suppliers, or categories by selecting the corresponding menu option. The application will display the records in a formatted list.

### Deleting Records

To delete a product, supplier, or category, select the appropriate delete option from the menu and enter the name of the record you wish to delete.
