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
    
# Test cases
test_case_1 = ([4, 5, 6, 7, 0, 1, 2], 1)  # General case
test_case_2 = ([], 5)                     # Edge case - Empty input
test_case_3 = (list(range(1000000)), 999999)  # Edge case - Very large array

# Expected outputs
expected_output_1 = 5
expected_output_2 = -1
expected_output_3 = 999999

# Testing the function with the test cases
print("Test Case 1:", "Pass" if rotated_array_search(*test_case_1) == expected_output_1 else "Fail")
print("Test Case 2:", "Pass" if rotated_array_search(*test_case_2) == expected_output_2 else "Fail")
print("Test Case 3:", "Pass" if rotated_array_search(*test_case_3) == expected_output_3 else "Fail")

