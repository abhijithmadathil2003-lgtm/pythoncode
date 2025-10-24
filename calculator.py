def add(num1,num2):
    return num1 + num2
    
def subtract(num1,num2):
    return num1 - num2
    
def multiple(num1,num2):
    return num1 * num2
   
def divide(num1,num2):
    return num1 / num2
 
def power(num1,num2):
    return  num1 ** num2
    
def calculator(num1,opertor,num2):
    if opertor == "+":
       return add(num1,num2)
    elif opertor == "-":
        return subtract(num1,num2)
    elif opertor == "*":
        return multiple(num1,num2)
    elif opertor == "/":
        return divide(num1,num2)
    elif opertor == "**":
        return power(num1,num2)
    else:
        return"invalid opertor"
num1=float(input("enter the first number:"))
opertor=input("enter the opertor:\n+\n-\n*\n/\n**\n\n")
num2=float(input("enter the second number:"))
result=calculator(num1,opertor,num2)
print("result",result)
