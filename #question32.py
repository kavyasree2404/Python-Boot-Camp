#question32
#write a code to remove all the brackets from the algebric expression
#input 
inp=input()
for i in inp:
    if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==93 or ord(i)==123 or ord(i)==124 ):
        pass
    else:
        print(i,end=" ")
