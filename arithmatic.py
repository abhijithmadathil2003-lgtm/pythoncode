a=float(input("enter the first number:"))
b=float(input("enter the second number:"))
c=input("enter a value:,\n 1.addition \n 2.subtration \n 3.multplication \n 4.divison \n 5.exponentiation \n 6.moduls \n 7.floordivison \n")
if c=="1":
 d=a+b
elif c=="2":
 d=a-b
elif c=="3":
 d=a*b
elif c=="4":
 d=a/b
elif c=="5":
 d=a**b
elif c=="6": 
 d=a%b
elif c=="7": 
 d=a//b
else:
 print("invalid option")
print("the result is:",d)
