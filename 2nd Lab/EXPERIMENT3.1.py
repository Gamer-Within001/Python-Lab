def factorial(n):
    result = 1
    for i in range (2, n + 1):
        result *= i
    return result

num = int(input("Enter A Number :"))
print(f"factorial of {num} is {factorial(num)}")