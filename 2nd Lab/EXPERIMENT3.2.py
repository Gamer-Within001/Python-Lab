import math

n = int(input("Enter A Number: "))

if n < 0 :
    print("Factorial is not defined for negative numbers")
elif n == 0:
    print("Factorial of the number is 1")
else:
    factorial = math.factorial(n)
    print("The factorial of ", n , "is", factorial)