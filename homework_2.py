#homework_2
# find greatest of three numbers
my_list=list(map(int,input().split(" ")))
great=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>great):
        great=my_list[i]
print("greatest of three numbers are:",great)
        
    