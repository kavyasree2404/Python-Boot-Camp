#question_17
#password verifier
#Mr X is trying to create a new password for his insta account.these are the required conditions for creating a new password
# condition 1. min leng is 8
#max len is 15
#condition 2. only @,/is allowed in password  /  for loop count i= @ or /
#con3. no spaces are allowed
#con4.only alpha numeric are allowed
#you are supposed to print weak if len is exact 8 med when len is between 8 to 12
#strong if len is between 12 to 15

password=input()
n=len(password)
count=0
if n>8 and n<15  : 
    for i in password:
        if i=="@" or i=="/":
            count+=1
if n==8:
    print("password is weak")
if n>8 and n<12:
    print("print password id medium ")
if  n>12 and n<=15:
    print("password is strong")
    

