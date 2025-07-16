'''

## Personal Expense Tracker 
build a python based personal expense tracker with file storage
which includes features
add new expense 

search / filter xpense by catagory or date 

store data in csv file for persistence 

Project Strucute


expense tracker/
|
|
|----- expense_tracker.py
------expense.csv

datetime module
strike method 
split method 
format method 


'''


import os 

print(os.getcwd())

os.chdir("Week2/expense_tracker/")

print(os.getcwd())

# date = input("Enter the date: ")
# catagory = input("Enter the Catagory: ")
# discription = input("Enter the Discription: ")
# amount = input("Enter the Amount: ")

# file_obj = open("store.csv","a")
# #file_obj.write(f"{date} , {catagory} ,{discription} , {amount}")

# file_obj.close()
# file_obj = open("store.csv","r")
# content = file_obj.read()
# print("your current Expenses ")
# print(content)
# file_obj.close()



def add_new_expenses():
     a = int(input('enter date'))
     b = input('Cate...')
     c = input('Name ... ')
     d = int(input('enter the amount'))
     f = open("expenses.csv", "a")
     c = f.writelines(f"{a}, {b}, {c}, {d}\n")
     f.close()

def view_all_expenses():
    f = open("expenses.csv", "r")
    c = f.read()
    print(c)
    f.close()

def search(val):
   f = open("expenses.csv", "r")
   c = f.readlines()
   for i in c:
       if (i.strip() == ""):
           continue
       pp = i.strip().split(",")
       if pp[0] == val:
           print(i)
# add_new_expenses()
# add_new_expenses()
view_all_expenses()

print("Search for the expense on the basis of date :")
search(int(input()))
search('11')



### method - 2

import os 
from datetime import datetime

FILENAME = "expense.csv"
FILENAME = "expenses.csv"
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as file:
            file.write("Date,Category,Description,Amount\n")
            
def add_expense(date, category, description, amount):
    data = input("Enter the date (YYYY-MM-DD) or leave blank for today: ").strip()
    if not data:
        data = datetime.today().strftime("%Y-%m-%d")
    category = input("Enter the category: ").strip()
    description = input("Enter the description: ").strip()
    amount = input("Enter the amount: ").strip()
    
    
    try:
        float(amount)  # Validate amount is a number
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return
    
    line = f"{data},{category},{description},{amount}\n"
    with open(FILENAME, "a") as file:
        file.write(line)
    print("Expense added successfully.")


def view_expense():
    try:
        with open(FILENAME,'r') as file
             for line in file:
                 parts = line.strip().split()
                 if len(parts) == 4:
                     print("{:<12} {:<15} , rs{:<7}".format(*parts))
    except FileNotFoundError :
        print("no expense recorded yet")

def search_expense():
    if not os.path.exists(FILENAME):
        print("NO ESPENSE FOUND")
        return
    choice = input("Search by (1) Date or (2) catagory? ")
    keyword = input("Enter the value to search :").strip().lower()
    found = False

    with open(FILENAME,'r') as file:
        next(file) 
        for line in file:
            parts = line.strip().split(',')
            if len(parts) !=4:
             continue
        date,catagory,discription,amount = parts 
        if(choice == '1' and date == keyword ) or (choice == '2' and catagory.lower() == keyword):
            print("{:<12} {:<15} {<30} ${:<7}".format(date,catagory,discription,amount))
            found = True
    if not found:
        print("No matching recored found .")




import os
from datetime import datetime

FILENAME = "expenses.csv"
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as file:
            file.write("Date,Category,Description,Amount\n")
            

def add_expense():
    date = input("Enter the date (YYYY-MM-DD) or leave blank for today: ").strip()
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")
        
    category = input("Enter the category: ").strip()
    description = input("Enter the description: ").strip()
    amount = input("Enter the amount: ").strip()
    
    try:
        float(amount)  # Validate amount is a number
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return
    
    line = f"{date},{category},{description},{amount}\n"
    with open(FILENAME, "a") as file:
        file.write(line)
    print("✅ Expense added successfully.")

    
def view_expenses():
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 4:
                    print("{:<12} {:<15} {:<30} rs{:>7}".format(*parts))
    except FileNotFoundError:
        print("No expenses found. Please add some expenses first.")


def search_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses found. Please add some expenses first.")
        return

    choice = input("Search by (1) Date or (2) Category:")
    keyword = input("Enter the value to search: ").strip().lower()
    
    found = False
    
    with open(FILENAME, "r") as file:
        next(file)  # Skip header
        for line in file:
            parts = line.strip().split(',')
            if len(parts) < 4:
                continue
            
            date, category, description, amount = parts
            
            if (choice == "1" and date == keyword) or (choice == "2" and category.lower() == keyword):
                print("{:<12} {:<15} {:<30} rs{:>7}".format(date, category, description, amount))
                found = True
    
    if not found:
        print(f"No expenses found for {keyword} in {('date' if choice == '1' else 'category')} search.")


def main():
    initialize_file()
    
    while True:
        print("\n📊 Personal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_expenses()
        elif choice == "4":
            print("Exiting the tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
if _name_ == "_main_":
    main()