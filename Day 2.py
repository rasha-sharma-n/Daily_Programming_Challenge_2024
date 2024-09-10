def missing_number(array):
    for i in range(len(array)):
        flag = 1
        if array[i] != i+1:
            print(i+1)
            flag = 0
            break
    if flag == 1:
        print(i+2)

missing_number([1, 2, 4, 5])
missing_number([2, 3, 4, 5])
missing_number([1, 2, 3, 4])
missing_number([1])
missing_number(list(range(1, 1000000)))
    
