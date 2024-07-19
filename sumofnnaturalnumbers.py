#sumofnnaturalnumbers
# Using a loop
def sum_first_natural_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

n = 10
sum_first_10 = sum_first_natural_numbers(n)
print(f"The sum of the first {n} natural numbers is: {sum_first_10}")
