import sqlite3

# ShopManagement class to handle product operations
class ShopManagement:
    def __init__(self):
        # Connect to the SQLite database
        self.conn = sqlite3.connect('shop.db')
        self.cursor = self.conn.cursor()

        # Create a table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT UNIQUE,
                                price REAL,
                                quantity INTEGER)''')
        self.conn.commit()

    # Add a new product to the shop
    def add_product(self):
        product_name = input("Enter the product name: ")
        price = float(input("Enter the product price: "))
        quantity = int(input("Enter the product quantity: "))

        try:
            self.cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
                                (product_name, price, quantity))
            self.conn.commit()
            print(f"Product {product_name} added successfully!")
        except sqlite3.IntegrityError:
            print(f"{product_name} already exists. Use update option to change stock.")

    # Display the available products in the shop
    def display_products(self):
        self.cursor.execute("SELECT * FROM products")
        products = self.cursor.fetchall()
        if not products:
            print("No products available in the shop.")
        else:
            print("\nAvailable Products in Shop:")
            for product in products:
                print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Quantity: {product[3]}")

    # Sell a product by specifying the quantity
    def sell_product(self):
        product_name = input("Enter the product name to sell: ")
        self.cursor.execute("SELECT * FROM products WHERE name=?", (product_name,))
        product = self.cursor.fetchone()

        if product:
            quantity_to_sell = int(input(f"How many {product_name} do you want to sell? "))
            if quantity_to_sell <= product[3]:
                new_quantity = product[3] - quantity_to_sell
                self.cursor.execute("UPDATE products SET quantity=? WHERE name=?", (new_quantity, product_name))
                self.conn.commit()
                print(f"Sold {quantity_to_sell} of {product_name}. Remaining stock: {new_quantity}")
            else:
                print(f"Not enough stock. Only {product[3]} available.")
        else:
            print(f"Product {product_name} not found.")

    # Remove a specified quantity from a product
    def remove_product(self):
        product_name = input("Enter the product name to remove: ")
        self.cursor.execute("SELECT * FROM products WHERE name=?", (product_name,))
        product = self.cursor.fetchone()

        if product:
            quantity_to_remove = int(input(f"How many {product_name} do you want to remove from stock? "))
            if quantity_to_remove <= product[3]:
                new_quantity = product[3] - quantity_to_remove
                if new_quantity == 0:
                    self.cursor.execute("DELETE FROM products WHERE name=?", (product_name,))
                    self.conn.commit()
                    print(f"Removed {product_name} from stock completely.")
                else:
                    self.cursor.execute("UPDATE products SET quantity=? WHERE name=?", (new_quantity, product_name))
                    self.conn.commit()
                    print(f"Removed {quantity_to_remove} of {product_name}. Remaining stock: {new_quantity}")
            else:
                print(f"Cannot remove more than the available quantity of {product[3]}.")
        else:
            print(f"Product {product_name} not found.")

    # Close the database connection
    def close_connection(self):
        self.conn.close()

# Main menu for interacting with the shop management system
def main_menu():
    shop = ShopManagement()
    while True:
        print("\n--- Shop Management System ---")
        print("1. Add Product")
        print("2. Display Products")
        print("3. Sell Product")
        print("4. Remove Product")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            shop.add_product()
        elif choice == '2':
            shop.display_products()
        elif choice == '3':
            shop.sell_product()
        elif choice == '4':
            shop.remove_product()
        elif choice == '5':
            shop.close_connection()
            print("Exiting the system.")
            break
        else:
            print("Invalid choice! Please select again.")

if __name__ == "__main__":
    main_menu()

