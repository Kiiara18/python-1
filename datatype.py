# Data Types
number = 45 # int
num = 56.78  # float
greeting = "Hello there" # str
IsPythonInteresting = True # bool

# Variable storing multiple values
languages = ["python","php", "java"] # list
fruits = ("apple","banana", "pineapple") # tuple
countries = ("Kenya", "China", "USA") # set
# Dictionary
details = {
    "firstname" : "Grace",
    "age" : 17,
    "course" : "MIT",
    "nationality" : "North America"
}

print(number)
print(greeting)
print(countries)
print(IsPythonInteresting)
print(details["course"])
print(details["nationality"])

# Determining the data type
print(type(details))
print(type(countries))

# Type casting - Converting one data type to another
print(float(number))
print(int(num))
