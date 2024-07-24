#question_11
#my_list=list(map(int,input().split(" ")))
#max_num=max(my_list)
#print("the max number in element is:",max_num)


#max elements
my_list=list(map(int,input().split(" ")))
maxi=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>maxi):
        maxi=my_list[i]
print(maxi)        

#min elemnts
my_list=list(map(int,input().split(" ")))
mini=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]<mini):
        mini=my_list[i]
print(mini)        