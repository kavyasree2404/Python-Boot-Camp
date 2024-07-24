#question 26
##print the non-repeating char or unique char in a str
vowel="aeiou"
consonents="bcdfghjklmnpqrstvwxyz"
ans=""
i="kavyasree"
inp=i.lower()
for i in inp:
    if(i not in ans):
        ans+=i
print(ans)
 

