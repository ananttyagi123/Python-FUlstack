## airthmetic operator (+,-,*,/,%)
## Assigment operator (+,+= , -= ,/=, *=, %=)
## logical (and or not)
## bitwise (| , & , ^ , << ,>> , ! )
## membership (in , not in)    
## identity (is , is not )    ## TO COMPARE 2 MEMORY ADDRESSES


## we are at  a grocery shop
print("############################  Arthematic operator  #############################")
item1 = 50
item2 = 30
total = item1 + item2      
difference = item1 - item2 
product = item1 * 2           
average = total / 2           
remainder = total % 7         

print("Total Bill:", total)           
print("Price Difference:", difference) 
print("Product:", product)            
print("Average:", average)             
print("Remainder:", remainder)         

print("############################  Arthematic operator  #############################")

wallet = 1000     
wallet -= 200        
wallet += 100 
wallet *= 2         
wallet %= 750         

print("Final wallet balance:", wallet)  

print("############################  Arthematic operator  #############################")

has_permission = True
paid_fees = False

can_go = has_permission and paid_fees
print("Can attend trip:", can_go)       

can_register = has_permission or paid_fees
print("Eligible to register:", can_register)  

print("Not eligible:", not can_register)      


print("############################  Bitwise operator  #############################")

bulb = 0b1010   
fan = 0b0101    

print("Bulb OR Fan:", bulb | fan)  
print("Bulb AND Fan:", bulb & fan)  
print("Bulb XOR Fan:", bulb ^ fan) 
print("Bulb Left Shift:", bulb << 1) 
print("Fan Right Shift:", fan >> 1)   



## membership operator

print("############################  membership operator  #############################")


menu = ["pizza", "burger", "pasta"] 


print("Is 'pizza' available?", "pizza" in menu)       
print("Is 'samosa' available?", "samosa" not in menu)   

## identity operator
print("############################## identity operator  #############################")

# Assume these are objects representing face data

registered_face = "QEW123"
scanned_face = registered_face       
other_face = "QEW123"

# Identity checks
print("Is same person (scanned)?", scanned_face is registered_face)   
print("Is same person (other face)?", other_face is registered_face)  
print("Is scanned NOT the same as registered?", scanned_face is not other_face) 


## expression evaluation 
## associativity precedence

units = 3
rate = 2

bill = rate * units ** 2
print("Total bill:", bill)  # Output: 18



distance = 2 ** 3 ** 1
print("Max distance:", distance, "km")  # Output: 8



price = 1000 - 200 + 50
print("Final payable:", price)  # Output: 850



age = 21
correct_pin = True

can_access = age > 18 and correct_pin
print("Access granted:", can_access)  # Output: True


# > has higher precedence than and
# So it first checks age > 18, then applies and correct_pin


# Real-life ATM-like logic
balance = 4800
pin = "1234"
max_withdrawal = 20000
attempts = 0

while attempts < 3:
    entered_pin = input("Enter your PIN: ")

    if entered_pin != pin:
        attempts += 1
        print(f"Incorrect PIN. Attempts left: {3 - attempts}")
        if attempts == 3:
            print("Your account has been locked. Please contact the bank.")
        continue

    amount = int(input("Enter amount to withdraw: "))

    if amount > max_withdrawal:
        print("Cannot withdraw more than ₹20,000 at once.")
    elif amount > balance:
        print("Insufficient balance.")
    elif balance < 5000:
        fee = 50
        balance -= (amount + fee)
        print(f"₹{amount} withdrawn with ₹{fee} low balance fee. Remaining balance: ₹{balance}")
    else:
        balance -= amount
        print(f"₹{amount} withdrawn successfully. Remaining balance: ₹{balance}")
    break

##### LOOPS #######

## WHILE LOOP   - mostly used to fetch on numerical data  
## FOR LOOP     - by default used to support to work on collection of data 




# i = 1
# while i<=10 :
#     print(i)
#     break
#     ## i+=2
# else:
#     print("end loop")


# i = 1
# while i==1 :
#     print(i)
#     break
    


# i = 1
# while i==1 :
#     print("HELLO")
#     print(i)
#     pass


# i = 1
# while i==1 :
#     print(i)
#     continue


name = "loveleen"
for i in name:
    print(i*2,end=" ")   ## ll oo vv ee ll ee ee nn


name = "loveleen"
for i in name:
    print(i*2)   ## ll oo vv ee ll ee ee nn
    


name = "loveleen"
for i in name:
    print(True*2)   ## 2 2 2 2 2 2 2   True = 1 False = 0






### Set , Dict , Tuples 

# Tuple
mytuple = (10, 20, 30)
print("Tuple elements:")
for item in mytuple:
    print(item)

# Set
my_set = {5, 10, 15}
print("\nSet elements:")
for item in my_set:
    print(item)

# Dictionary


my_dict = {'name': 'Shruti', 'age': 22, 'city': 'Delhi'}
print("\nDictionary keys and values:")
for key in my_dict:
    print(f"{key}: {my_dict[key]}")


print("----------------------- Printing Pattern -------------------------------")

rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()


import random

secret_number = 5     ## random.randint(1, 10)  
attempts = 10



print("Guess the number between 1 to 10. You have 3 attempts!")

for i in range(attempts):
    guess = int(input(f"Attempt {i+1}: Enter your guess: "))
    if guess > 10:
        print("The number is out of Range!!!")
        break
    else:
        pass
    if guess == secret_number:
        print("Congratulations! You guessed it right!")
        
        break
    else:

        print("Wrong guess.")
else:
    print(f"Sorry! The correct number was {secret_number}")



def daata():
    print("Hello")


##### create a recursion

def fact(n):
    if(n<=1):
        return 1
    else:
        return (n*fact(n-1))
print(fact(5))
