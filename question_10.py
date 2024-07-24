#question_9
#Print the element in a particular index
my_list=list(map(int,input().split(" ")))
k=int(input())
index=k%len(my_list)
print(my_list[index])

