import mysql.connector 
import bcrypt 

con = mysql.connector.connect(host="localhost",user="root",password="12345678",database="api" ,port=3307)
mycursor = con.cursor()
print(con)

mycursor.execute("create database loginapp")
mycursor.execute("""
                #  create table users(id INT AUTO_INCREMENT PRIMARY KEY,
                #  username VARCHAR(100) UNIQUE NOT NULL,
                #  password VARCHAR(255) NOT NULL)
                #  """)
print("table created")

def sign_up(username,password):
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
    try:
        mycursor.execute("insert into users(username,password) values(%s,%s)",(username,hashed_pw))
        con.commit()
        print("user registered successfuly")
    except mysql.connector.IntegrityError:
        print("user already registered!try different one.")


def login(username,password):
    mycursor.execute("select password from users where username=%s",(username,))
    result = mycursor.fetchone()
    if result:
        stored_hash = result[0].encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'),stored_hash):
            print("login successfuly")
        else:
            print("incorrect password")
    else:
        print("username not found")

def main():
    while True:
        print("\n-------Login System------")
        print("1.Sign up")
        print("2.Login")
        print("3.Exit")
        choice = input("choose an option")
        if choice=="1":
            u = input("username: ")
            p = input("password: ")
            sign_up(u,p)
        elif choice=="2":
            u = input("username: ")
            p = input("password: ")
            login(u,p)
        elif choice=="3":
            print("Goodbye")
            break
        else:
            print("invalid choice try agian!")


if __name__=="__main__":
    main()
            

