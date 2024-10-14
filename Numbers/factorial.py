# Calculate Factorial without recursion#

def factorial(num):
    fact = 1
    while num >= 1:
        fact = fact * num
        num -= 1
    print(fact)


print("factorial of number ", 10, " is ", factorial(10))
