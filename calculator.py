# Calculator
x = float(input("Enter First Number:"))
y = float(input("Enter second number:"))

operator = input("Enter operator:")
if operator == "+":
    print("Result is",x+y)
elif operator == "-":
    print("Result is",x-y)
elif operator == "*":
    print("Result is",x*y)
elif operator == "/":
    print("Result is",x/y)
else:
    print("Invalid Operator")
