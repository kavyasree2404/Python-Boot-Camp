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

    

