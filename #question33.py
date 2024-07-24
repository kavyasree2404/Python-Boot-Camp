#question33
##ABC input string 
#Skip value 4 
#Op:EFG
#xyz
#x=120+3=123   ------------>a=97
#chr(123)
#y=121=3=124   ------------->b=98
#chr(124)=}
#z=122=3=125   ------------->c=99
#chr(125)=~
inp=input()
for i in inp:
    print(chr(ord(i)==4),end=" ")
print()