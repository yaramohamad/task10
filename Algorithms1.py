numbers = [1, 2, 3, 4, 5]
def second_largest(list1):
    first_max= max(list1[0],list1[1])
    second_max= max(list1[0],list1[1])
    for i in range(2,len(list1)):
        if list1[i]>first_max :
            second_max=first_max
            first_max=list1[i]
        elif list1[i]>second_max:
            second_max=list1[i] 
    return second_max
print("second max no.:",second_largest(numbers))