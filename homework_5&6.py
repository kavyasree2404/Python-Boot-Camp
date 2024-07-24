#homework_4&5
#find max number
#my_list=list(map(int,input().split(" ")))
#maxi=my_list[0]
#for i in range(len(my_list)):
 #   if(my_list[i]>maxi):
  #      maxi=my_list[i]
#print(maxi)        

#find the second max number
my_list2=list(map(int,input().split()))
max1=max(my_list2[0],my_list2[1])
maxi2=min(my_list2[0],my_list2[1])
for i in range(2,len(my_list2)):
    if(my_list2[i]>max1):
        maxi2=max1
        max1=my_list2[i]
    elif my_list2[i]> maxi2 and max1 != my_list2[i]:
        maxi2 = my_list2[i]
    elif max1 == maxi2 and \
        maxi2 != my_list2[i]:
          maxi2 = my_list2[i]
 
print("Second highest number is : ",\
      str(maxi2))


print(maxi2)        

