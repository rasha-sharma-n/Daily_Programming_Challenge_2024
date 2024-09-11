def duplicate_number(array):
    
    original_sum = 0; duplicate_sum = 0
    
    for i in range(1, len(array)+1):
        original_sum += i
        
    for i in range(0, len(array)):
        duplicate_sum += array[i]

    difference = original_sum - duplicate_sum
    return len(array) - difference

#Test Cases
print(duplicate_number([1, 3, 4, 2, 2]))
print(duplicate_number([3, 1, 3, 4, 2]))
print(duplicate_number([1, 1]))
print(duplicate_number([1, 4, 4, 2, 3]))
print(duplicate_number((list(range(1, 100000)))+ [50000]))

        
