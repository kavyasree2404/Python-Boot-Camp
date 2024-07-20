#QUESTION_7.3
#U R GIVEN WITH A SPACE SEPERATED  INTEGER LIST FIND NO. OF EVEN AND NO. OF ODD ELEMENTS IN GIVEN list 
my_list=list(map(int,input().split(",")))
even=0
odd=0
for i in range(0,len(my_list)):
    if(my_list[i]%2==0):
        even+=1    
    else:
        odd+=1
print(even)
print(odd)
 
