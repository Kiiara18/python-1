try:
    print(x)
except:
    print("NameError occurred")
finally:
    print("Success")


num1 = 20
num2 = 0

try:
    print(num1/num2)
except:
    print("ZeroDivisionError occurred")

    print(num1 / num2)


# User defined function

try:
   def multiply(x,y):
       return x*y
except:
    print("Exception occurred")
finally:
    print("Success")

print(multiply(10,20))
