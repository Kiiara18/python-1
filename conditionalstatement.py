temperature = 13

if temperature > 25:
    print("It is hot")
else:
    print("It is cold")


# A programme that returns the largest number among three numbers
num1 = 45
num2 = 56
num3 = 21
if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")


# A programme that checks whether a number is even or odd
number = 45
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# A programme that checks whether a number is prime or not
def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)
# Test the function
num = 17
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")