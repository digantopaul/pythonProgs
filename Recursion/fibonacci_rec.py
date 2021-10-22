## fibonacci series with recursion

def fibonacci_rec(limit):
    if limit <= 1:
        return limit
    else:
        return fibonacci_rec(limit-1) + fibonacci_rec(limit-2)


nterms = int(input("Enter the number of terms: "))

if nterms <=0:
    print("Please enter the number of terms more than 1.")
else:
    for i in range(nterms):
        print(fibonacci_rec(i))
