print("program to find area of the triangle")
a=int(input("enter the length of side a:"))
b=int(input("enter the length of side b:"))
c=int(input("enter the length of side c:"))
s=(a+b+c)/2
print(s)
area=(s*(s-a)*(s-c))**0.5
print("area of the triangle",area)
