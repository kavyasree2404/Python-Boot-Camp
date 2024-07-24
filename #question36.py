#question36
#print
#**********
#* ********
#** *******
#*** ******
#**** *****
#***** ****
#****** ***
#******* **
#******** *
#*********
row=10
column=10
for i in range(10):
    for j in range(10):
        if(i==j):
            print(" ",end="")
        else:
            print("*",end="")
    print()            

