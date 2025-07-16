
'''
Dictionary 

# ORDERED
# cHANGABLE
# NOT ALLOW DUPLICATES

'''

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Accessing value using key
print(my_dict['name'])  # Output: Alice

# Using .get() method (safer, returns None if key not found)
print(my_dict.get('age'))   # Output: 25
print(my_dict.get('country')) # Output: None
print(my_dict.get('country', 'USA')) # Output: USA (default value if key not found)


my_dict = {'name': 'Alice', 'age': 25}

# Adding a new key-value pair
my_dict['city'] = 'New York'
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Adding multiple items (less direct, usually done with update)
my_dict.update({'occupation': 'Engineer', 'zip': '10001'})
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'occupation': 'Engineer', 'zip': '10001'}

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Modifying an existing value
my_dict['age'] = 26
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# Using .update() to modify existing keys or add new ones
my_dict.update({'city': 'San Francisco', 'occupation': 'Data Scientist'})
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'San Francisco', 'occupation': 'Data Scientist'}


key = my_dict.keys()
print(key)

value = my_dict.values()
print(value)



## if you are trying ot access the key and value if else then the asnwer will be deffferent from default 

## copy

newdict = my_dict.copy()
print(newdict)


newdict1 = dict(newdict)
print(newdict1)


## remove

# x = newdict.pop("height")
# print(x)
# print(newdict)

my_dict.popitem()
print(my_dict)


## pop()  and  popitem()

my_dict.clear()  ### { }
print(my_dict)



my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York', 'occupation': 'Engineer'}

# 1. Using del keyword
del my_dict['occupation']
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# If you try to delete a non-existent key, it will raise a KeyError
# del my_dict['country'] # This would raise a KeyError

# 2. Using pop() method
age = my_dict.pop('age')
print(age)      # Output: 25
print(my_dict)  # Output: {'name': 'Alice', 'city': 'New York'}

# pop() can also take a default value if the key is not found
country = my_dict.pop('country', 'Not Found')
print(country)  # Output: Not Found
print(my_dict)  # Output: {'name': 'Alice', 'city': 'New York'}

# 3. Using popitem() method
item = my_dict.popitem() # In Python 3.7+, removes the last inserted item
print(item)     # Output: ('city', 'New York') (Example, could be different in older Python versions)
print(my_dict)  # Output: {'name': 'Alice'}

# 4. Using clear() method
my_dict.clear()
print(my_dict)  # Output: {}

# Deleting the entire dictionary (the variable itself)
# my_dict = {'a': 1, 'b': 2}
# del my_dict
# print(my_dict) # This would raise a NameError because my_dict no longer exists



my_family = {
    'dad': {
        'name': 'Rajesh',
        'age': 55,
        'occupation': 'Engineer'
    },
    'mom': {
        'name': 'Priya',
        'age': 52,
        'occupation': 'Teacher'
    },
    'sister': {
        'name': 'Anjali',
        'age': 28,
        'occupation': 'Doctor',
        'hobbies': ['reading', 'painting']
    },
    'me': {
        'name': 'Rahul', # You can change this to your actual name
        'age': 30,
        'occupation': 'Software Developer',
        'hobbies': ['coding', 'hiking', 'photography']
    }
}

# --- Examples of how you can use this dictionary ---

print("My Family Details:")
for relation, details in my_family.items():
    print(f"\n{relation.capitalize()}:")
    for key, value in details.items():
        print(f"  {key.replace('_', ' ').capitalize()}: {value}")

print("\n--- Let's modify and add some data! ---")

# Add a new family member (e.g., a brother)
my_family['brother'] = {
    'name': 'Amit',
    'age': 22,
    'occupation': 'Student'
}
print("\nAfter adding brother:")
print(my_family['brother'])

# Modify an existing detail (e.g., dad's age)
my_family['dad']['age'] = 56
print("\nDad's new age:", my_family['dad']['age'])

# Add a new hobby for yourself
my_family['me']['hobbies'].append('cooking')
print("\nMy updated hobbies:", my_family['me']['hobbies'])

# Remove a family member (e.g., if a family member moves out)
if 'sister' in my_family:
    del my_family['sister']
    print("\nAfter removing sister from the dictionary.")
print("\nCurrent family members:", list(my_family.keys()))


for i , obj in my_family.items():
    print(i)
    for j in obj:
        print(j,":", obj[j])


'''

## 1 .Contact Book 
Task : Store and retrieve contact information (name,phone email)


contacts = {
    # "Alice": {"Phone":"123-456-789"}
    # "Bob" : {"Phone":"989-766-655"}
    }

    ## 2 .Tasks : Store Student  Grades Recored  and calculate thrie average 
    grades = {
    # john : [44,3,323]
      Emma : [34,65,44]
      Alex : [70,77,78]
    }
 # Problem : Library Book Tracking System 
 # Senerio :

 # library wants to keep track ofthe boooks it has , how many copies of echa book are available 
 and which members have borrowed which book . Implement a Simple System that allows 

 # Adding a book to the library inventory

 Borrowing a book (decreasing the avail count)
 Returning a Book (increase in avail count )

 checking which books a member has borrowed 


'''


# Task- 1

# 1. Contact Book Application
# Task: Store and retrive contact information (name, phone number, email.
#
contacts = {
     "Alice": {"phone": "123-456-7890", "email": "alice@example.com"},
     "Bob": {"phone": "987-654-3210", "email": "bob@example.com"}    
}

set_contact = set(contacts.keys())
for i in contacts.items():
    print("Contact Name:", i[0])
    print("Phone Number:", i[1]["phone"])
    print("Email:", i[1]["email"])

# Task - 2 Average 

# Task: Store student grades and calculate average grade.

grades = {
    "John": [85, 90, 78],
    "Alice": [92, 88, 95],
    "Bob": [70, 75, 80],
    "Charlie": [88, 82, 84]
}
for i, j in grades.items():
    print("Student:", i, "Grades:", sum(j))
    print("Average Grade for", i, ":", sum(j) / len(j))


# Task Library Management System 

## Library 


library = {
    "books":{ "Your Name":5 , "Jujutsu Kaisen":9, "Demon Slayer":4},
   "returned_books":{""},
   "borrowed_books": {""}
}


library_inventory = {}       
member_borrowed_books = {}   



print("--- Initial State ---")
print("Library Inventory:", library_inventory)
print("Member Borrowed Books:", member_borrowed_books)



library_inventory.update({"The Great Gatsby": {'total_copies': 3, 'available_copies': 3}})
print("\n--- After adding 'The Great Gatsby' ---")
print("Library Inventory:", library_inventory)

# Adding "1984"
library_inventory.update({"1984": {'total_copies': 2, 'available_copies': 2}})
print("\n--- After adding '1984' ---")
print("Library Inventory:", library_inventory)



library_inventory.update({"The Great Gatsby": {'total_copies': 4, 'available_copies': 4}}) # Assume we're just setting a new total/available
print("\n--- After updating 'The Great Gatsby' total copies ---")
print("Library Inventory:", library_inventory)


print("\n--- Attempting to borrow books ---")

# Borrow "1984" by "Alice"
# This will crash if '1984' is not in library_inventory
# It will make available_copies negative if already 0
library_inventory["1984"].update({'available_copies': library_inventory["1984"]['available_copies'] - 1})
member_borrowed_books.update({"Alice": member_borrowed_books.get("Alice", []) + ["1984"]}) # Adds to list, creates if not exists


print("Library Inventory:", library_inventory)
print("Member Borrowed Books:", member_borrowed_books)


library_inventory["The Great Gatsby"].update({'available_copies': library_inventory["The Great Gatsby"]['available_copies'] - 1})
member_borrowed_books.update({"Bob": member_borrowed_books.get("Bob", []) + ["The Great Gatsby"]})

print("Library Inventory:", library_inventory)
print("Member Borrowed Books:", member_borrowed_books)


# 3. Returning a Book (increase in avail count)
print("\n--- Attempting to return books ---")

# Alice returns "1984"
# This will crash if '1984' is not in library_inventory
# This will crash if "Alice" is not in member_borrowed_books or if "1984" not in her list

library_inventory["1984"].update({'available_copies': library_inventory["1984"]['available_copies'] + 1})
member_borrowed_books["Alice"].remove("1984") # Remove from list (will ValueError if not found)
print("Alice returned 1984")
print("Library Inventory:", library_inventory)
print("Member Borrowed Books:", member_borrowed_books)


# 4. Checking which books a member has borrowed
print("\n--- Checking borrowed books for Alice ---")
# Using .get() for safety, as accessing member_borrowed_books['Alice'] directly would crash if Alice not found
alice_books = member_borrowed_books.get("Alice", [])
print(f"Alice's borrowed books: {alice_books}")

print("\n--- Checking borrowed books for Bob ---")
bob_books = member_borrowed_books.get("Bob", [])
print(f"Bob's borrowed books: {bob_books}")

print("\n--- Checking borrowed books for Charlie (non-existent member) ---")
charlie_books = member_borrowed_books.get("Charlie", [])
print(f"Charlie's borrowed books: {charlie_books}")


# 5. Deleting a book (using 'del' keyword, which is not a method but the direct delete operation)
print("\n--- Attempting to delete a book ---")
# This will crash if 'The Great Gatsby' is not in library_inventory
# del library_inventory["The Great Gatsby"]
# print("Deleted 'The Great Gatsby'")
# print("Library Inventory:", library_inventory)


print("Library Inventory:", library_inventory)
print("Member Borrowed Books:", member_borrowed_books)


#Scenario
# A library wants to track of books it has, how many copies of each book are available,
# and which books are borrowed by which books. Implements a simple system that allows
# Adding new books to the library inventory
# borrowig a book
# returning a book
# chech which book a member has borrowed

library = {
    "books": {"The Great Gatsby": 5, "1984": 3, "To Kill a Mockingbird": 4 , 
              "Pride and Prejudice": 2, "How to invest time": 7},
    "borrowed_books": {},
    "returned_books": {},
    
}
print(library)  
library["books"].update({"The Catcher in the Rye": 8, "Brave New World": 9})
print("Updated Library Inventory:", library["books"])

available_books = library["books"]
print("Available Books:", available_books)
# boorrowing a book
book = "Brave New World"
copy = library["books"].get(book, 0)

library["borrowed_books"][book] = copy - (copy > 0)

print("Borrowed Books:", library["borrowed_books"])

# returning a book
def return_book(book):
    if book in library["borrowed_books"]:
        library["returned_books"][book] = library["borrowed_books"].pop(book)
        library["books"][book] += 1
        print(f"Book '{book}' returned successfully.")
    else:
        print(f"Book '{book}' was not borrowed.")
return_book("Brave New World")

# Check which book a member has borrowed
def check_borrowed_books():
    if library["borrowed_books"]:
        print("Borrowed Books:")
        for book, copies in library["borrowed_books"].items():
            print(f"{book}: {copies} copies")
    else:
        print("No books are currently borrowed.")

check_borrowed_books()

books = {}
members = {}

def add_books(title,count=1):
    if title in books:
        books[title]["total"] += count
        books[title]["available"] += count
    else:
        books[title] = {"total": count, "available": count}
        print(f"Added {count} copies of '{title}' to the library.")



add_books("1989")
add_books("Bob", "The Great Gatsby")
add_books(input())
print(f"Updated library inventory: {books}")

def borrow_book(member, title):
    if title not in books:
        print(f"Sorry, '{title}' is not available in the library.")
        return
    if books[title]['available'] <= 0:
        print(f"Sorry, '{title}' is currently not available for borrowing.")
        return
    if member not in members:
        members[member] = []
    members[member].append(title)
    books[title]['available'] -= 1
    print(f"{member} borrowed '{title}'.")
borrow_book("Alice", "1984")
borrow_book("Bob", "The Great Gatsby")


print(f"Updated library inventory: {books}")

#

## Returning the book increasing the available count 

def return_book(member, title):
    if member not in members or title not in members[member]:
        print(f"Sorry, '{member}' has not borrowed '{title}'.")
        return 
    members[member].remove(title)
    books[title]['available'] += 1
    print(f"{member} returned '{title}'.")

return_book("Alice","1984")





### Task -3 

'''

1. task -1 
Scenerio : 
You have to write a simple programme to create grocery shopping list manager 
Add , remove , view item


'''


