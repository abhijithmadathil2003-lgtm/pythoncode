a=[]
n=int(input("enter the number of elements in list:"))
for x in range(n):
	element=input("enter element" +str(x+1)+":")
	a.append(element)
max1=len(a[0])
temp=a[0]
for i in a:
	if len(i)>max1:
	 max1=len(i)
	 temp=i
print("the word with the longest length is:")
print(temp)	
print("length of the word",(temp),"is",len(temp))





