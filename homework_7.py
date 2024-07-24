#homework_6
# #find reverse in array without using  built in functions
my_list=list(map(int,input().split(" ")))
y=my_list[::-1]
for revert in range(1, len(my_list) +1 ):
    y.append(my_list[-revert])
print(y)    
