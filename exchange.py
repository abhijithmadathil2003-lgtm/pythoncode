print("Exchange")
def swap(a):
	s=a[0]
	e=a[-1]
	x=e+a[1:-1]+s
	print(x)
a=input("enter the word\n")
swap(a)
