#question_22
#leap year
#LOGIC:number should be div by 400 or num should be div by 4 but not 100
#a=int(input("enter a number"))
#if a//400==0:
#    print(a,"is laep year")
#else:
#    print(a,"not a leap year")
    
#leap year sequence in given  range
a=int(input())
for i in range(2000,2025):
    if(i%4==0 or i%100!=0):
        print(i)
        