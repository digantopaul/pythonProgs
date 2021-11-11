## Program to find the maximum of two numbers ##

def numMax(n1, n2):
    if n1 > n2:
        return n1
    elif n1 == n2:
        return "Both the numbers are equal"
    else:
        return n2


print("The maximum of the two numbers is ", numMax(4, 4))
