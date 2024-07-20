#my_list=list(map(str,input().split(" ")))
#my_list.pop()
#print(*my_list)

#take input from user 4 choices 1append,2pop,3sort,4print hello,lenght
my_list=list(map(str,input().split(" ")))
choice=int(input())
if( choice == 1):
    print(my_list.append())
elif(choice == 2):
    print(my_list.pop())
elif(choice == 3):
    print(my_list.sort())
    print(*my_list)
elif(choice == 4):
    print(len(my_list))



