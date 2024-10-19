Shop Management System
This project is a Shop Management System implemented in Python, utilizing SQLite as the database for storing product information. The system allows users to manage a small shop's inventory efficiently through a simple command-line interface.

Features
Add Products: Users can add new products to the inventory, specifying the product name, price, and quantity.
Display Products: The system displays all available products in the shop, including their ID, name, price, and remaining quantity.
Sell Products: Users can sell specified quantities of products, with the system ensuring sufficient stock is available before completing the sale.
Remove Products: Users can remove a specified quantity of products from stock. If the quantity becomes zero, the product will be deleted from the inventory.
Database Management: The application stores product information in an SQLite database, ensuring persistent data storage across sessions.
Technologies Used
Python
SQLite3
Installation
To run this project, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/shop-management-system.git
cd shop-management-system
Make sure you have Python installed on your system.

Run the script:

bash
Copy code
python shop_management.py
Usage
Upon running the program, users will see a menu with the following options:

Add Product
Display Products
Sell Product
Remove Product
Exit
Simply enter the corresponding number to perform the desired action.
