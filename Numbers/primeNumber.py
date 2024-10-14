num1 = int(input("Enter the number: "))


def prime(num):
    mid = int(num/2)
    print("mid " + str(mid))
    if num > 1:
        for i in range(2, mid+1):
            if (num % i) == 0:
                print(str(i))
                print(str(num) + " is not a prime number")
                break
            else:
                print(str(num) + " is a prime number")
                break
    else:
        print("It is not a prime number.")


def PrimeChecker(a):  
    # Checking that given number is more than 1  
    if a > 1:  
        # Iterating over the given number with for loop  
        for j in range(2, int(a/2) + 1):  
            # If the given number is divisible or not  
            if (a % j) == 0:  
                print(a, "is not a prime number")  
                break  
        # Else it is a prime number  
        else:  
            print(a, "is a prime number")  
    # If the given number is 1  
    else:  
        print(a, "is not a prime number")

        
print(prime(21))
print(PrimeChecker(31))
