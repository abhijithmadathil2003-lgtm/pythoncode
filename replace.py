string=input("enter a string:")
first_char=string[0]
new_char=first_char+string[1:].replace(first_char,'$')
print(new_char)
