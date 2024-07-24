#question_20
#squareroot of prime number
a=int(input("enter 1st number:"))
sqrt=a**0.5
count=[0]
if a==1:
    print("not a prime number")
elif a==2:
    print("is a prima number")
for i in range(2,int(sqrt+1)):
    if a%i==0:
        count=1
        break
print("prime")    


