'''
# # 1. your application is bill splitter  write the function that takes the total bill amount and number of people  
# # and return how much each person should pay

# ## 2.email validator function to check if the email address is valid or not @ and .

# ## 3.you have to design the simple Shop cart that takes the list of total item price and return the total price including a 10% sales tax

# ## 4.Unit Convertor  km to miles 1 km == 0.621371 miles 

####
# # 1. Bill Splitter
print("#################  Bill Splitter #################################")
total_amount = int(input())
num_people = int(input())
def split_bill(total_amount, num_people):
    
    if num_people <= 0:
         return "Invalid number of people"
    return round(total_amount / num_people, 2)


print("Each should pay: ₹", split_bill(total_amount,num_people))


print("#################  Email Validator #################################")


emailcheck = input()
def valid(emailcheck):
    print("Task Started")
    if "@" not in emailcheck or "." not in emailcheck:
        return "Email is not Valid !! it must contain '@'"
    elif "@" in emailcheck or "."  in emailcheck:
        return "email is valid !!!"
    elif "@" not in emailcheck:
        return  "@ is missing !! it nust contain '@' "
    else:
        return "email is not Valid!!"
        
valid(emailcheck)


######### Shopping Cart
 
print("#################  Shopping Cart #################################")

total_item = int(input("Enter the total number of items: "))

def ItemList():
    total = 0
    for i in range(total_item):
        item = int(input(f"Enter amount for item {i + 1}: "))
        total += item
    return round(total*0.10)

# Calling the function and printing the result
print("Total price of all items: ₹", ItemList())


 
   
## 4 . Km to miles 
print("#################  Km to Miles  #################################")

def km_to_miles(km):
    return round(km*0.621371)

print(km_to_miles(5))
   

print("###################### Modules #####################################")
#### Modules 
# 1. Built-in Module (os , sys, math , date , random , datetime, json)
# 2. user defined modules ()'=
# 3. external or third party module (request , django , numpy , flask , pandas ,pygame , pytest)


import random
print(round(random.random()))
print(random.randint(10,20))

print(random.randrange(10,50,10))


### change the name of module 
import random as h1 
print(round(h1.random()))

from random import *
print(random())

print("#################### user defined modules ####################")

import userModule

userModule.info("Hello Anant!!")


# mutable 
# access list 
fruits = list(("apple","mango","Kiwi","Cherry","kiwi","orange" ,"kiwi"))
print(fruits)

print(fruits[0])
print(fruits[0:3])
print(fruits[2:])
print(fruits[:3])
print(fruits[-1])
print(fruits[-1:-3])



fruits[1:2] = ["apple","craneberry"]
print(fruits)

fruits[1:4] = ["apple","craneberry"]
print(fruits)


# fruits.remove("Kiwi")
# print(fruits)

# fruits.pop(2)
# print(fruits)

fruits.pop()
print(fruits)


# fruits.clear()
# print(fruits)


fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

newfruits = fruits.copy()
print(newfruits)


newfruits = list(fruits)
print(fruits)

print(fruits.count("apple"))


# data = fruits.index("kiwi")
# print(data)

fruits = tuple(("apple","mango","Kiwi","Cherry","kiwi","orange" ,"kiwi", True, 0))
print(fruits)
print(type(fruits))
print(len(fruits))

newfruits = list(fruits)
newfruits[1] = "berry"
fruits = tuple(newfruits)
print(fruits)
print(type(fruits))
print(len(fruits))
''' 
###### you have to create a to do list management 

# Task 1: Create a Todo List Manager 

# create a list of task 

# add new task 

# mark a Task by removing it 

# ----------------------------
# Task 1: Todo List Manager
# ----------------------------
todo_list = []

# Add new task
no_of_task = int(input("Enter the number of tasks: "))

def add_task():
    for i in range(no_of_task):
        task = input(f"Enter task {i+1}: ")
        todo_list.append(task)

add_task()

print("Your Todo List:")
print(todo_list)


todo_list = ['Buy groceries', 'Study Python', 'Call mom']

removed_from_index = int(input("Enter the index of the task to remove: "))
print("Removed from the Index:", removed_from_index)

def remove_task(index):
    if 0 <= index < len(todo_list):
        removed = todo_list.pop(index)
        print("The Task removed:", removed)
    else:
        print("Invalid index!")

remove_task(removed_from_index)

print("Updated Todo List:", todo_list)

'''

print("Todo List:", todo_list)

# Mark task done (remove)
completed_task = todo_list.pop(0)  # removes the first task
print(f"Completed Task: {completed_task}")
print("Updated Todo List:", todo_list)

'''




# Task 2 : Student Scores 
# list of student scores : [88 , 45 ,76, 544]

# find the highest and the lowest score 

# calculate the average score 


# ----------------------------
# Task 2: Student Scores
# ----------------------------
scores = [88, 45, 76, 544]

# Highest and lowest
highest = max(scores)
lowest = min(scores)
average = sum(scores) / len(scores)

print("\nStudent Scores:", scores)
print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Average Score:", average)







# Task 3: Guest List for a Party 

# Create a Guest List 

# check if a guest is on the list

# Add a new guest 

# Remove a guest who cancels 


# ----------------------------
# Task 3: Guest List for a Party
# ----------------------------
guest_list = ["Alice", "Bob", "Charlie"]

# Check if a guest is in the list
guest_to_check = "Bob"
if guest_to_check in guest_list:
    print(f"\n{guest_to_check} is on the guest list.")
else:
    print(f"{guest_to_check} is not on the guest list.")

# Add a new guest
guest_list.append("Diana")

# Remove a guest
guest_list.remove("Charlie")

print("Updated Guest List:", guest_list)





# Task 4 : 
# 1. Flight Data Analysis
# given  a tuple of flights (flight_number , origin , destination ,duration_in_minute)

# flights = (
#    ("AA123","NYC","LAX",360),
#    ("BU123","CHI","NYC",544),
#    ("AA123","NYC","LAX",360),
#    ("Bw723","CHI","NYC",544),
#    ("AR523","LAX","CHI",360),
#    ("BT623","MIA","LAX",544),
# ) 

# Tasks 
 #  Print all the flights originated from the  NYC
 # sort flights by duration (shortest to longest) and print the sort list
 # find the flight with the largest duration 


# ----------------------------
# Task 4: Flight Data Analysis
# ----------------------------
flights = (
    ("AA123", "NYC", "LAX", 360),
    ("BU123", "CHI", "NYC", 544),
    ("AA123", "NYC", "LAX", 360),
    ("Bw723", "CHI", "NYC", 544),
    ("AR523", "LAX", "CHI", 360),
    ("BT623", "MIA", "LAX", 544),
)

# Flights from NYC
print("\nFlights from NYC:")
for flight in flights:
    if flight[1] == "NYC":
        print(flight)

# Sort by duration
sorted_flights = sorted(flights, key=lambda x: x[3])
print("\nFlights sorted by duration:")
for flight in sorted_flights:
    print(flight)

# Flight with longest duration
longest_flight = max(flights, key=lambda x: x[3])
print("\nFlight with longest duration:", longest_flight)


#### Sets 

## unordered
## unchangable 
## no dulpicates 


data = ("kiwi","orange",23,23,33,3,3,2,True,False,"Kiwi")
print(data)
print(type(data))
print(len(data))


for i  in data: 
   print(i)

data.add("mango")
print(data)

data1 = {1,2,3}
data.update(data1)
print(data)

data.remove("Kiwi")
data.remove("Cherry")
print(data)

data.discard("Kiwi")
data.discard("Cherry")
print(data)


data.clear()
print(data)   ## set()



del data 
print(data)


#set joins 
data  = {"a","b","c","d","e","f"}
data1 = {1,2,3,4,5,6}
data.union(data1)

data4 = {"A","B","C"}

data3 = data | data1 | data4
print(data3)



# intersection ()
data5 = data.intersection(data1)
print(data5)

data5 = data & data1


data6 = data.difference(data1)


data7 = data.symmetric_difference(data1)   # make a set of un common element from both sets 
data7 = data^data1
#include everything which does not common   

'''
##### Practice Task 
    # Use Cases Cleaning a Contact List 
 
## contact = ["alicegmail.com","bob@gmail.com","carol@gmail.com"]


## 2. Finding  Common Elemets 


Use Cases : Find user who are subscribed to both newsletters 
newsletter_A = {"alice ","bob","carol"}
newsletter_B = {"bob,"dave","carol}


#3 Finding Differences 
lastMonth_A = {"alice ","bob","carol"}
lastMonth_B = {"bob,"dave","carol"}


4. Checking the Membership 
Use Cases : Check if a user has already regustered 
registered_list = {"alice ","bob","carol"}

5. Tags of Label in an App
Use Cases :  Collect all the unique tags used in blog posts 

# tags = {"python ", "web","coding ", "tutorial","web" }

Problem: Detecting Duplicate Email Address in a Signup System 

Scenerio:
#you are managing a web application where users sign up with their email addresses
# you want to ensure that each user registers only once using a unique email address



# you recieve a list of new signups and need to find out which email address are dupllicates 
# (i.e) have aleardy signed up before 
 

'''

# Existing registered users
registered_users = {"alice@example.com", "bob@example.com", "carol@example.com", "david@example.com"}

# New signups (can contain duplicates or already registered emails)
new_signups_list = ["carol@example.com", "eve@example.com", "frank@example.com", "bob@example.com", "grace@example.com", "eve@example.com", "carol@example.com"]

print(f"Existing registered users: {registered_users}")
print(f"New signups list (raw): {new_signups_list}")

# Convert new signups list to a set. This automatically removes any duplicates within the new_signups_list itself.
# The unique new signups are now ready for set operations.
new_signups_set = set(new_signups_list)
print(f"Unique new signups (after set conversion): {new_signups_set}")

# --- Detecting Duplicates against existing registrations ---

# Emails in new signups that are ALREADY REGISTERED:
# Use set intersection to find common elements between registered_users and new_signups_set.
# These are the "duplicates" in the sense that they tried to sign up again.
already_registered_duplicates = registered_users.intersection(new_signups_set)
print(f"Emails in new signups that are already registered: {already_registered_duplicates}")

# --- Finding Truly New Signups ---

# Emails in new signups that are TRULY NEW and not already registered:
# Use set difference to find elements in new_signups_set that are NOT in registered_users.
truly_new_users = new_signups_set.difference(registered_users)
print(f"Truly new unique users (not previously registered): {truly_new_users}")

# --- Updating Registered Users ---

# Add the truly new users to the registered users set:
# Use set union to combine the existing registered users with the truly new unique signups.
updated_registered_users = registered_users.union(truly_new_users)
print(f"Updated registered users after adding new unique signups: {updated_registered_users}")

# --- Optional: Identifying duplicates attempted within the new signups batch itself ---
# While sets inherently remove duplicates upon creation, you can infer if duplicates
# were present in the *original list* by comparing the length of the list vs its set conversion.
# This does not use an 'if/else' but demonstrates the concept of duplicates in the initial list.
if len(new_signups_list) > len(new_signups_set):
    print("\nNote: Duplicates were present within the new signups list itself (e.g., 'eve@example.com' appeared twice).")
    print("These were automatically handled by converting the list to a set.")

# If you specifically wanted to list these internal duplicates without iteration,
# it would typically involve iterating and tracking seen items, which goes against the
# "no if/else" and "only set inbuilt methods" for individual list processing.
# Set methods excel at comparing *different* sets, not directly finding repeated items *within* one original list without loops.



## solution

