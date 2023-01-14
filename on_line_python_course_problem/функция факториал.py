def factorial(n=13):
    z = 1
    for i in range(n):
        x = z * (i + 1)
        z = x
    return x

x = factorial()

print(x)