
a = [5,3,6]
def large(a): #function to idfentify the max interger in the list
    # if a[0] >= a[1]:
    #     max = a[0]
    # else:
    #     max = a[1]
    
    max = a[0]
    
    for i in range(1, len(a)):
        if max >= a[i]:
           max = max
        else:
            max = a[i]
    print(max)

large(a)
# def max_list(a):          
#     a_sorted = sorted(a)
#     return a_sorted.pop(len(a)-1)
