import mysql.connector
import bcrypt
# Step 1: Connect and Create Database
con_temp = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    port=3307
)
cur_temp = con_temp.cursor()
cur_temp.execute("CREATE DATABASE IF NOT EXISTS LoginDB")
con_temp.close()

# Step 2: Connect to LoginDB
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="LoginDB",
    port=3307
)
cur = con.cursor()

# Step 3: Create users table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
)
""")
con.commit()

# Step 4: Insert Default Users (if table empty)
cur.execute("SELECT COUNT(*) FROM users")
if cur.fetchone()[0] == 0:
    cur.execute("""
    INSERT INTO users (username, password) VALUES
    ('admin', 'admin123'),
    ('anant', '12345678'),
    ('user1', 'pass1')
    """)
    con.commit()

# Step 5: Functionality
def register():
    print("\n🔐 Register New User")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
    try:
        cur.execute("insert into users(username,password) values(%s,%s)",(username,hashed_pw))
        con.commit()
    except mysql.connector.errors.IntegrityError:
        print("❌ Username already exists. Try another.\n")

def login():
    print("\n🔓 Login")
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cur.fetchone()
    
    if user:
        print(f"✅ Login successful! Welcome, {username}\n")
    else:
        print("❌ Invalid credentials. Try again.\n")

def show_users():
    print("\n👥 Registered Users:")
    cur.execute("SELECT user_id, username FROM users")
    for row in cur.fetchall():
        print(row)
    print()

# Step 6: Menu Loop
while True:
    print("======== Login Management System ========")
    print("1. Register")
    print("2. Login")
    print("3. Show All Users")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        show_users()
    elif choice == '4':
        print("👋 Exiting. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Enter 1-4.\n")

# Step 7: Close connection
con.close()

