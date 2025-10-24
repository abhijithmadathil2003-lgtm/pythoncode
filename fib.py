def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter how many Fibonacci numbers to generate: "))

print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i), end=' ')
print("\nThe Fibonacci number is:"fibonacci(i))

