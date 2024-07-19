#market mrx
cost_apples=15
cost_bananas=4
cost_oranges=8
#no. of fruits
print("enter no. of apples")
no_apples=int(input())
print("enter no. of bananas")
no_bananas=int(input())
print("enter no. of oranges")
no_oranges=int(input())
print("enter the ammount given by mother")
amount_given=int(input("enter gthe amount"))
sum=(no_apples*cost_apples)+(no_bananas*cost_bananas)+(no_oranges*cost_oranges)
if(sum>=700 and amount_given):
    print("cheated")
else:
    print("not cheated")
    