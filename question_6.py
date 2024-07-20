#question_6
#take a space separted input from a user and print alternate elements for(0,n,1)
#my_list=list(map(int,input().split()))
#for i in range(1,len(my_list),2):
#    print(my_list[i])

#how many even questions are there in above question
my_list=list(map(int,input().split()))
count=0
for i in range(1,len(my_list),2):
    count+=1
    print(count)    
  
