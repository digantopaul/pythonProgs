# fibonacci series using WHILE loop ##
def fibonacci(limit):
    n0, n1 = 0, 1
    print(n0)
    print(n1)
    while limit >= 0:
        n0 = n0 + n1
        n1 = n1 + n0
        print(n0)
        print(n1)
        limit -= 1

fibonacci(10)