def factorial(num1):
    fact = 1
    if num1 <= 1:
        return 1
    else:

        while num1 > 1:
            fact = fact * num1
            num1 -= 1

    print(str(fact))


factorial(10)
