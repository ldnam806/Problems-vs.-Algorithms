def rotated_array_search(input_list, number):
    left, right = 0, len(input_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # If the middle element is the target, return its index
        if input_list[mid] == number:
            return mid
        
        # If the left half is sorted
        if input_list[left] <= input_list[mid]:
            # If the target is within the sorted left half
            if input_list[left] <= number and number < input_list[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # If the right half is sorted
        else:
            # If the target is within the sorted right half
            if input_list[mid] < number and number <= input_list[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1
    
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Test cases
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])  # Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])  # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])          # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])          # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])         # Pass

# Test cases 100
test_function([[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100], 100])  # Pass

