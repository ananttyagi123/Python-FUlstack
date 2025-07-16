import mysql.connector
from datetime import date

# Step 1: Connect to MySQL and ensure database
con_temp = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    port=3307
)
cur_temp = con_temp.cursor()
cur_temp.execute("CREATE DATABASE IF NOT EXISTS store")
con_temp.close()

# Step 2: Connect to store DB
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="store",
    port=3307
)
cur = con.cursor()

# Step 3: Create product table
cur.execute("""
CREATE TABLE IF NOT EXISTS product (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2),
    stock INT
)
""")

# Step 4: Create sales table for join demo
cur.execute("""
CREATE TABLE IF NOT EXISTS sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    quantity INT,
    sale_date DATE,
    FOREIGN KEY (product_id) REFERENCES product(product_id)
)
""")

# Step 5: Functions
def insert_product():
    name = input("Product name: ")
    price = float(input("Price: "))
    stock = int(input("Stock quantity: "))
    cur.execute("INSERT INTO product (name, price, stock) VALUES (%s, %s, %s)", (name, price, stock))
    con.commit()
    print("Product added.\n")

def update_stock_after_sale():
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Quantity sold: "))
    
    # Check current stock
    cur.execute("SELECT stock FROM product WHERE product_id = %s", (product_id,))
    result = cur.fetchone()
    
    if not result:
        print("Product not found.\n")
        return
    
    current_stock = result[0]
    if quantity > current_stock:
        print("Not enough stock.\n")
        return

    # Update stock
    new_stock = current_stock - quantity
    cur.execute("UPDATE product SET stock = %s WHERE product_id = %s", (new_stock, product_id))
    
    # Log sale in `sales` table
    cur.execute("INSERT INTO sales (product_id, quantity, sale_date) VALUES (%s, %s, %s)",
                (product_id, quantity, date.today()))
    
    con.commit()
    print("Stock updated & sale recorded.\n")

def view_low_stock():
    threshold = int(input("Enter stock threshold: "))
    cur.execute("SELECT * FROM product WHERE stock <= %s", (threshold,))
    rows = cur.fetchall()
    
    print("Products with Low Stock:")
    for row in rows:
        print(row)
    print()

def view_sales_with_product_details():
    print("Sales with Product Info (Using JOIN):")
    cur.execute("""
    SELECT s.sale_id, p.name, s.quantity, s.sale_date
    FROM sales s
    JOIN product p ON s.product_id = p.product_id
    ORDER BY s.sale_date DESC
    """)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print()

# Step 6: Menu
while True:
    print("====== Inventory Management Menu ======")
    print("1. Add Product")
    print("2. Sell Product (Update Stock)")
    print("3. View Low Stock Products")
    print("4. View Sales with Product Info (JOIN)")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        insert_product()
    elif choice == '2':
        update_stock_after_sale()
    elif choice == '3':
        view_low_stock()
    elif choice == '4':
        view_sales_with_product_details()
    elif choice == '5':
        print("👋 Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")

# Step 7: Close connection
con.close()
