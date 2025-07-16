import mysql.connector
from datetime import date

# Step 1: Ensure database exists
con_temp = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    port=3307
)
mycursor_temp = con_temp.cursor()
mycursor_temp.execute("CREATE DATABASE IF NOT EXISTS API")
con_temp.close()

# Step 2: Connect to the correct database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="API",  # ✅ make sure this matches the actual database name (case-sensitive on some systems)
    port=3307
)
mycursor = con.cursor()

# Step 3: Create the table if it doesn't exist
mycursor.execute("""
CREATE TABLE IF NOT EXISTS product2 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    price DECIMAL(10,2),
    stock INT,
    created_at DATE
)
""")
print("Table 'product2' ready!")

# Step 4: Functions for menu options
def register_product():
    name = input("Enter product name: ")
    desc = input("Enter product description: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter stock quantity: "))
    today = date.today()

    query = """
    INSERT INTO product2 (name, description, price, stock, created_at)
    VALUES (%s, %s, %s, %s, %s)
    """
    data = (name, desc, price, stock, today)
    mycursor.execute(query, data)
    con.commit()
    print("✅ Product registered successfully!\n")

def show_products():
    mycursor.execute("SELECT * FROM product2")
    rows = mycursor.fetchall()

    if not rows:
        print("No products found.\n")
        return

    print("\nAll Products:")
    for row in rows:
        print(row)
    print()

# Step 5: Menu loop
while True:
    print("======== MENU ========")
    print("1. Register Product")
    print("2. Show All Products")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        register_product()
    elif choice == '2':
        show_products()
    elif choice == '3':
        print("Exiting program. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.\n")

# Step 6: Cleanup
con.close()
