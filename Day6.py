import os 

print(os.getcwd())

os.chdir("Week2/")

print(os.getcwd())

## read is used to read the entire content 

file_obj = open("data.txt","rb")
content = file_obj.read()
print(content)


file_obj = open("data.txt","w")
file_obj.write("How are you ?? ")
print("data added")
## adding multiple lines 
file_obj.writelines("Hello how are you doing ? \n any updates regarding the interview ...")
# file_obj.writelines(input(),"a")
file_obj.close()


## append 


# file_obj = open("data4.txt","x")
# print("file is created !!")

with open("data.csv","r") as file: 
    content = file.read()
    print(content)
    file.close()

with open("data.csv","a") as file:
    file.write("4 , Kumar , 22")
    print("data added !! ")
    file.close()



## Exception handling 
# try , except , else , finally 
# raise exception 
# custom exception 


# built-in        
# zero divison , file not found , value error , module not found , key error  attribute error 


# user defined
    ## custom exception 
    class validate_age(Exception):
        def __init__(self, age, message="Age is Invalid !!"):
            self.age = age 
            self.message = message
            super.__init__(self,message)

def set_age(age):
    if age<0:
        raise validate_age(age)
    print(f"age is {age}")

try:
     set_age(-9)
except validate_age as v :
    print(f"validation error {v}")
 

try : 
    a = int(input())
    b = int(input())
    c = a/b 

except ZeroDivisionError:

  print("Can't be divisible by zero!!")

except TypeError: 
    print("trying to do the func with improper value")

except Exception as e: 
    print(f"detect the error !! {e}")

except validate_age as v:
     print("message")
else :
    print(f"result {c}")


## Raise Exception 

def set_age(age):
    if age <0:
        raise ValueError("Age can't be negative")
    print(f"age is {age}")

    set_age(-9)
    
## error logging in python is a typically handled using the inbuilt logging mobilr module
## this module provide a flexible framework for emminting log messsges from application 

## Key Concepts of error logging 

import logging 
logging.basicConfig(filename="app.log",level=logging.ERROR,format='%(asctime)s-%(levelname)s-%(message)s')

def divide(a,b):
    try:
        result = a/b
        logging.info(f"divison successful {result}")
        return result
    except ZeroDivisionError:
        logging.exception("number can't e divide by zero")
    except TypeError as e:
        logging.error(f"invalid number {e}",exc_info=True)

divide(12,4)
divide(12,0)






