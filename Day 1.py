def dutch_flag(array):
    start = 0; mid = 0; end = len(array)-1
   
    while mid <= end:
        if array[mid] == 0:
            array[start], array[mid] = array[mid], array[start]
            start += 1; mid +=1

        elif array[mid] == 1:
            mid += 1

        elif array[mid] == 2:
            array[mid], array[end] = array[end], array[mid]
            end -= 1

        else:
            print("Array element invalid")

      
    return array


print("Testing:")

print("Test Case 1:\nInput = [0, 1, 2, 1, 0, 2, 1, 0]\nRequired Output = [0, 0, 0, 1, 1, 1, 2, 2]")
out1 = dutch_flag([0, 1, 2, 1, 0, 2, 1, 0])
print("Output generated:", out1)

print("Test Case 2:\nInput = [2, 2, 2, 2]\nRequired Output = [2, 2, 2, 2]")
out2 = dutch_flag([2, 2, 2, 2])
print("Output generated:", out2)

print("Test Case 3:\nInput = [0, 0, 0, 0]\nRequired Output = [0, 0, 0, 0]")
out3 = dutch_flag([0, 0, 0, 0])
print("Output generated:", out3)

print("Test Case 4:\nInput = [1, 1, 1, 1]\nRequired Output = [1, 1, 1, 1]")
out4 = dutch_flag([1, 1, 1, 1])
print("Output generated:", out4)

print("Test Case 5:\nInput = [2, 0, 1]\nRequired Output = [0, 1, 2]")
out5 = dutch_flag([2, 0, 1])
print("Output generated:", out5)

print("Test Case 6:\nInput = []\nRequired Output = []")
out6 = dutch_flag([])
print("Output generated:", out6)
