def is_palindrome(n):
    n_str=str(n)
    n_rev=n_str[::-1]
    return n_str==n_rev
n=int(input("Enter a number:"))
result=is_palindrome(n)
if result:
	print(f"The number {n} is palindrome")
else:
	print(f"The number {n} is not palindrome")
	
