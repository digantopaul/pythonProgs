def fibo(num1):
#     1 1 2 3 5 8 13 21 34 55
        f1 = 1
        f2 = 1
        print(str(f1) + " " + str(f2))
        while num1 > 0:
            f3 = f1 + f2
            f1 = f2
            f2 = f3
            num1 -= 1
            print(" " + str(f3))


fibo(10)
