import mysql.connector
from datetime import date

# Step 1: Connect to MySQL & create database
con_temp = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    port=3307
)
cur_temp = con_temp.cursor()
cur_temp.execute("CREATE DATABASE IF NOT EXISTS ShopDB")
con_temp.close()

# Step 2: Connect to ShopDB
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="ShopDB",
    port=3307
)
cur = con.cursor()

# Step 3: Create Tables
cur.execute("""
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    product_name VARCHAR(100),
    amount DECIMAL(10,2),
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
)
""")

# Step 4: Insert Initial Data (only if table is empty)
cur.execute("SELECT COUNT(*) FROM Customers")
if cur.fetchone()[0] == 0:
    cur.execute("""
    INSERT INTO Customers (name, email) VALUES
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com'),
    ('Charlie', 'charlie@example.com')
    """)
    con.commit()

cur.execute("SELECT COUNT(*) FROM Orders")
if cur.fetchone()[0] == 0:
    cur.execute("""
    INSERT INTO Orders (customer_id, product_name, amount, order_date) VALUES
    (1, 'Laptop', 999.99, '2025-06-29'),
    (1, 'Mouse', 25.00, '2025-06-30'),
    (2, 'Keyboard', 45.00, '2025-06-30')
    """)
    con.commit()

# Step 5: Functionalities
def show_all_orders_with_customers():
    print("\n📦 All Orders with Customer Info (INNER JOIN):")
    cur.execute("""
    SELECT o.order_id, c.name, c.email, o.product_name, o.amount, o.order_date
    FROM Orders o
    INNER JOIN Customers c ON o.customer_id = c.customer_id
    """)
    for row in cur.fetchall():
        print(row)
    print()

def show_customers_without_orders():
    print("\n👤 Customers without Orders (LEFT JOIN + NULL):")
    cur.execute("""
    SELECT c.customer_id, c.name, c.email
    FROM Customers c
    LEFT JOIN Orders o ON c.customer_id = o.customer_id
    WHERE o.order_id IS NULL
    """)
    result = cur.fetchall()
    if result:
        for row in result:
            print(row)
    else:
        print("All customers have placed orders.\n")

def show_order_count_per_customer():
    print("\nTotal Orders Per Customer (GROUP BY):")
    cur.execute("""
    SELECT c.name, COUNT(o.order_id) AS total_orders
    FROM Customers c
    LEFT JOIN Orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.name
    """)
    for row in cur.fetchall():
        print(row)
    print()

# Step 6: Console Menu
while True:
    print("======== Customer Orders System ========")
    print("1. Show All Orders with Customer Info")
    print("2. Show Customers Without Orders")
    print("3. Show Total Orders Per Customer")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        show_all_orders_with_customers()
    elif choice == '2':
        show_customers_without_orders()
    elif choice == '3':
        show_order_count_per_customer()
    elif choice == '4':
        print("👋 Goodbye!")
        break
    else:
        print("Invalid input. Try 1–4.\n")

# Step 7: Close connection
con.close()


