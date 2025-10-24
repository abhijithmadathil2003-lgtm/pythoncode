def fibonacci(n):
    if n <= 1:
        return n
       
    else:
         return fibonacci(n-1) + fibonacci(n-2)	  
n=int(input("enter the fibonacci number to generate:"))
for i in range(n):
    print(fibonacci(i),end='')
    print("\n")
print("the",n,"fibonacci series is",fibonacci(n-1))
	
	
	
	
	
	


