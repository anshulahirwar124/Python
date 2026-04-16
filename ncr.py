def factorial(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact

n = int(input("Enter n: "))
r = int(input("Enter r: "))

result = factorial(n) // (factorial(r) * factorial(n - r))

print("nCr =", result)