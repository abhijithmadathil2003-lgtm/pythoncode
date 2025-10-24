num=int(input("enter a number:"))
original_num = num
n= len(str(num))
sum_of_powers = 0
while num >0:
	digit=num%10
	sum_of_powers += digit ** n
	num //=10
if original_num == sum_of_powers:
	print(f"{original_num} is an armstrong number.")
else:
	print(f"{original_num} is not an armstrong number.")
