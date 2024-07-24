#question_21
# to print all prime numbers in given range #input=10 and 30
a=int(input("enter the 1st  number:"))
b=int(input("enter the 2nd number:"))
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
         print(i)
        

    


