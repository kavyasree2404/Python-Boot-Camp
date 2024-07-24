#homework2
# patterns
#print lower triangular matrix
print("pattern 2: ")
for i in range(10):
    for j in range(10):
        if(i==j or i<j):
            print("*",end="")
    print()            
