#homework_4
#peak element
my_list=list(map(int,input().split()))
count=0
for i in range(1,len(my_list)-1):
    if my_list[i]>my_list[i-1] and my_list[i]>my_list[i+1]:
        count=i
print(my_list[i],end=" ")
    
