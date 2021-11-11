# Program to find the maximum of two numbers #

def maxnum(n1, n2):
    if n1 > n2:
        return n1
    elif n1 == n2:
        return "Both the numbers are equal"
    else:
        return n2


print("The maximum of the two numbers is ", maxnum(4, 4))
