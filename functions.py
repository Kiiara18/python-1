# In-built functions
number = max(89, 70,23,45,123)
print(number)

x = min(78,45,34,1)
print(x)

z = pow(2,3)
print(z)


# User-defined functions
def name():
    print("Melisa")
name() # Calling a function

def student():
    name = "Vincent"
    age = 18
    course = "MIT"
    print(name, age, course)


student()

# Parameters/variables and arguments/values

def students(name, age, course):
    print(name, age, course)

students("Vincent", 18, "MIT")
students("Vincent", 18, "MIT")
students("Vincent", 18, "MIT")
students("Vincent", 18, "MIT")
students("Vincent", 18, "MIT")
students("Vincent", 18, "MIT")
students("Vincent", 18, "MIT")
students("Vincent", 18, "MIT")


# Create a user-defined function called employees.It should display details of 5 employees parameters are;name,age,gender,position,salary
def employees(name, age, gender, position, salary):
    print(name, age, gender, position, salary)


employees("Melisa",26,"female", "CEO",1000000)
employees("David",48,"male", "CFO",100000)
employees("Roselyn",46,"female", "CTO",50000)
employees("Jeremy",20,"male", "Assistant",100000)
employees("Tess",28,"female", "Manager",1000000)
