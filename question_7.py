#question_7
#you are given with a comma seperated natural numbers 1 to 10 print only the even numbers
#my_list=list(map(int,input().split(",")))
#for i in range(1,10):
#    print(i,ends="i")
#for i in range()


#QUESTIONS 7.2
#take a space separted input from a user and print alternate elements for(0,n,1)
#my_list=list(map(int,input().split()))
#for i in range(1,len(my_list),2):
#    print(my_list[i])


#QUESTIONS 7.3
#how many even questions are there in above question
my_list=list(map(int,input().split()))
count=0
for i in range(1,len(my_list),2):
    count+=1
    print(count)    
  
