#QUESTION_8
#given an space seperation list find the avg of elements present in the given LIST
my_list=list(map(int,input().split("i")))
total=0
lenght=len(my_list)-1
for i in my_list:
    if i%2==0:
        total+=1
average=total/lenght
print(average)    


#or second method
my_list=list(map(int,input().split(",")))
sum=0
count=0
n=len(my_list)
for i in range(len(my_list)):
 sum+=my_list[i]
 count+=1
print(sum/count)

