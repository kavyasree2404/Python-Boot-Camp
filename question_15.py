#reverse the given number 123 to 321
#imp
n=123
sum=0
while n>0:
    r=n%10
    sum=sum+r    #imp step
    n=n//10
print(sum)    
