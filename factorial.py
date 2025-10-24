def factorial(n):
    if n <= 1:
         return 1
    else:
         result =factorial(n-1)
         return n * result
n=int(input("enter the element:"))
print(factorial(n))
