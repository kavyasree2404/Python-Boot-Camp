#day 5
#strings23
#String methods are :Is alpha :Is alium:Is upper:Is lower:Is digit
#Converting to lower,upper,title,swap
inp="hellaaaaa woRld"
print(inp.upper())#to get upper char
print(inp.lower())#to get lower char
print(inp.title())#title means to get first letter capital
print(inp.swapcase())#swap the upper to lower and vice versa
print(inp.strip())#make space
print(inp.replace('a','z'))#replaces
print(inp.split())#prints ',' in space
print(inp.split('a'))#prints ',' in given 
#
inp="12 "
print(inp.isalpha())# check space if space flase,if no space true
print(inp.isnumeric())#numeric are all numbers
print(inp.isascii())#whether input is ascii or not
print(inp.isalnum())
print(inp.isdigit())#digts are 0 to 9
print(inp.isupper())
print(inp.islower())
print(inp.istitle())
print(inp.isnumeric())
print(inp.isdigit())