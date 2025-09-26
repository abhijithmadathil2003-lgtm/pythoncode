print("program to find largest among three numbers")
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if a>=b and a>=c:
  print("a is the largest:",a)
elif b>=a and b>=c:
  print("b is the largest:",b)
else:
  print("c is the largest:",c)

