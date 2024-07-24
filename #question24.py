#question24                      day5
#check how many vowels are in a string

check=["a","e","i","o","u"]
count=0
input="kavyasree"
for i in input:
    if(i in check):
        count+=1
print(count)        

#check hw many consonants in a sting
check=["a","e","i","o","u"]
consonent="bcdfghjklmnpqrstvwzyz"
count=0
c=0
i="kavyasree"
inp=i.lower()
for i in inp:
    if(i  not in check):
        count+=1
print(count)        

