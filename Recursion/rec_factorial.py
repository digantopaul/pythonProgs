def recFactorial(num):
    f1 = 1
    f2 = 1

    if num > 0:
        return recFactorial(num - 1) + recFactorial(num - 2)
    else:
        return num


for i in range(10):
    print(recFactorial(i))
