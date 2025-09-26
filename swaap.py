print("using temporary vairble")
a=int(input("enter the first value:"))
b=int(input("enter the second value:"))
print("a before swapping:",a)
print("b before swapping:",b)
temp=a
a=b
b=temp
print("a after swapping:",a)
print("b after swapping:",b)
print("\n")
print("without using temporary vairble")
x=int(input("enter the first value:"))
y=int(input("enter the second value:"))
print("befor swapping x=",x,"y=",y)
x=x+y
y=x-y
x=x-y
print("after swapping x=",x,"y=",y)

