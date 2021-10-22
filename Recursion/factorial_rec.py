## Program to calculate factorial of a number using Recursion ##

def factorial_rec(num):
    if num < 1:
        return 1
    else:
        return num * factorial_rec(num - 1)


fac_num = int(input("Enter the number to calculate factorial: "))

factorial = factorial_rec(fac_num)
print(factorial)