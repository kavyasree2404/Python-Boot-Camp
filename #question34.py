#question34
#ip:hello-----wor----ld
#op:---------helloworld
inp=input()
count=0
ans=""
for i in inp:
    if(i=="-"):
        count+=1
    else:
        ans=ans+i
print("-"*count+ans)        


