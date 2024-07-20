#HOMEWORK
#write a program to find area of a circle
#write a program to find perimeter of a circle
#write a program to find area of triangle 
#write a program to find perimeter of triangle
 

# #write a program to find prime number using sqrt
num=int(input("enter the number"))
import math
a=int(math.sqrt(num))
b=0
for i in range(2,a):
    if a%i==0:
        b+=1
    if b==0:
        print(a,"is a prime")
else:
    print(a,"is not prime")

    

