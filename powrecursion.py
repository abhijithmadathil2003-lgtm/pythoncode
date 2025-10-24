def power(base,exponent):
    if exponent == 0:
        return 1
    elif exponent==1:
        return base
    else:
        return base*power(base,exponent-1)
base=float(input("enter the base: "))
exponent=int(input("enter the exponent: "))
result=power(base,exponent)
print(base, "raised to the power of",exponent,"is",result)





