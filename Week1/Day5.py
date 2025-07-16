'''
 OOPS 
 POP
 Functional Programming

 

1. what is OOPS and hoew it is different from POP and functional programming  ?
2. what are the other  approaches present in market  similar to OOPS  ? 
3. when the OOPS evolve in the market  and why ? 
4. why python approaches only OOPS and is there any other approach in python that it supports  ?


'''

'''
class Dog:
    breed = "bulldog"  ## class variable


    # def __init__(self):     # default Contructor
    #     print("Dog class is Called!!")


    def __init__(self,name,age):     # intialiser   _new_ constructor is called Parametrised constructor
       self.name = name
       self.age = age 
       print(self.name)
       print(self.age)
     
       print("Dog is created")

    # def __str__(self):
    #     return(f"dog and data class")
    def Bark(self):
        print("dogs are barking")
    
d1 = Dog("Jack",5)
d2 = Dog("Coco",4)



d1.Bark()
d2.Bark()

print(d1.name)
print(d2.name)
print(d1.breed) 
print(d2.breed) 

print(d1.age)
print(d2.age)
'''

# print(d1)

   # <__main__.Dog object at 0x00000272995CA1E0> assign same memory location because the value is same


# encapsulation 
# is a feature where you can 
# restriction to hide the data 
# access modifiers 
# method should de public nd hide the variable throught access modifier 
# Public , Private , protected 

# __ privatevariable
# _ protected

'''

class Emp:
    cname = "lpu"

    def __init__(self, name , age , salary):
        self.name = name
        self.age = age
        self.__salary = salary

    def display(self):
     print(self.name)
     print(f"{self.name,self.age}")
     print(self.__salary)

e1 = Emp("john",34,50000)
e1.display()

'''

'''
## Task- 1 
Scenerio: 

Bank Balance applicaition 
3 methods 
 Balance is private 
1. Display 
2. Withdraw 
3  Credit


'''

class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def display(self):
        print(f"The Total Balance: {self.__balance}")

    def withdraw(self,balance,amountwithdraw):
        Amount = self.__balance - amountwithdraw
        print(f"Withdrawed Amount: {amountwithdraw}")
        print(f"The Amount After Withdrawal : {Amount}")

    def Credit(self,balance,amountcredit):
        Credited = self.__balance + amountcredit
        print(f"Credited Amount: {amountcredit}")
        print(f"The Amount After Credit : {Credited}")
        print(Credited)

bankamount = Bank(40000)
bankamount.display()
bankamount.withdraw(40000,10000)
bankamount.Credit(40000,10000)
        


'''
Problem 2 : car class with default values 
Problem:
Create a class Car that had attributes make , model ,year
the constructor should allow the default values 
if none is provided . Create few car objects using different sets of arguements 
'''

class Car:
   
    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year 

    def Display(self):
        print(self.name)
        print(self.model)
        print(self.year)

CarDetails = Car("AudiQ7","CCE4","2010")
CarDetails.Display()

'''
Problem 3: Student Imformation System
Scenerio :
Create a class Studnet with the following attributes name , roll ,grade 
Use a Constructor to initalise thes eviewa 
Create 2 Studnet object and display thier information 


'''

# class StudentDetails:
#     def __init__(self, name , roll, grade):
#         self.name = name 
#         self.roll = roll
#         self.grade = grade

#     def Display(self):
#         print(f"Name: {self.name} , Roll.No: {self.roll} , Grade: {self.grade}")
    

# Student1 = StudentDetails("Anant",1,70)
# Student2 = StudentDetails("Krishna",2,80)

# Student1.Display()
# Student2.Display()

## 

'''

INHERITENCE

1. SINGLE 
2. MULTIPLE 
3. MULTI LEVEL
4. HEIRARCY 
5. HYBRID 

'''



# single level inheritence 1- base class and 1 - child class 

print("#################### single inheitence ##################")
class Animal:

    def __init__(self,name,age):
         self.name = name
         self.age = age
         print(self.name)
         print(self.age)

    def speak(self):
        print("Animal class")



class Dog(Animal):
       def __init__(self,breed,name,age):
         super().__init__(name,age)
         self.breed = breed
         print(self.breed)

         

       def speak(self):
        super().speak()
        print("Dog class")


d1 = Dog("Coco",4,"Bulldog")
d1.speak()

# multi level 
print("###################### multi level ##################")
class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal:", self.name)

class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print("Mammal Age:", self.age)

class Dog(Mammal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
        print("Dog Breed:", self.breed)

    def speak(self):
        print(f"{self.name} says Woof!")

d1 = Dog("Bruno", 3, "Labrador")
d1.speak()


## multiple 
print("################# multiple inheritence ##################")
class Father:
    def __init__(self):
        print("Father Constructor")

    def speak(self):
        print("Father speaks.")
    
class Mother:
    def __init__(self):
        print("Mother Constructor")

    def speak(self):
        print("Mother speaks.")

class Child(Father, Mother):
    def __init__(self):
        super().__init__()           # Calls Father's constructor (first in MRO)
        Mother.__init__(self)        # Manually calling Mother's constructor
        print("Child Constructor")

    def speak(self):
        super().speak()
        Mother.speak(self)
        print("Child speaks.")

c = Child()
c.speak()



# heirarcy 
print("############### heirarcy inheritence ##################")
class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal:", self.name)

    def speak(self):
        print(f"{self.name} is an animal.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print("Dog Breed:", self.breed)

    def speak(self):
        super().speak()
        print(f"{self.name} barks.")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        print("Cat Color:", self.color)

    def speak(self):
        super().speak()
        print(f"{self.name} meows.")

d = Dog("Rocky", "Pug")
d.speak()

c = Cat("Kitty", "White")
c.speak()




# hybrid 
print("################## HYbrid Inheritence ###################")
class LivingBeing:
    def __init__(self):
        print("LivingBeing Constructor")

    def speak(self):
        print("LivingBeing makes a sound.")

class Animal(LivingBeing):
    def __init__(self):
        super().__init__()
        print("Animal Constructor")

    def speak(self):
        super().speak()
        print("Animal speaks.")

class Canine:
    def __init__(self):
        print("Canine Constructor")

    def speak(self):
        print("Canine growls.")

class Dog(Animal, Canine):
    def __init__(self):
        Animal.__init__(self)   # Explicitly calling due to multiple inheritance
        Canine.__init__(self)
        print("Dog Constructor")

    def speak(self):
        Animal.speak(self)
        Canine.speak(self)
        print("Dog barks.")

d = Dog()
d.speak()


'''
Polymorphism
1.built in 
2.user defined 
3.on operators 
4.oops
'''

print("################## Polymorphism ###################")


# built in 

def add(a,b):
    print(a+b)

add("hello"," world")
add(3,2)


print(5*4)
print("hello "*5)

## method overloading is not supported in python but we can achieve it using *args and **kwargs

# completime polymorhism 
# runtime polymorphism  

#### with the help of method overriding 

## Polymorphism

class Animal:
    def speak(self):
        print("Animal Class")

class Cat(Animal):
    def speak(self):
        print("meow meow")

class Dog(Animal):
    def speak(self):
        print("Woof Woof")

def makeSound(animal):
    animal.speak()

d1=Dog()
c1=Cat()
a1=Animal()
d1.makeSound()
c1.makeSound()
a1.makeSound()

# animal = [Animal(),Cat(),Dog()]
# for a in animal:
#     a.speak()


### Python Duck Typing


class Bird:
    def fly(self):
        print("fly with wings !!")
    
class Aero:
    def fly(self):
        print("fly with fuel !!")

class Fish:
    def swim(self):
        print("swim in the water")

for obj in Bird() , Aero() , Fish():
    obj.fly()
