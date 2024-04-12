def sort_array(input_list):
    # Initialize three pointers
    low = 0  # Pointer for 0
    mid = 0  # Pointer for 1
    high = len(input_list) - 1  # Pointer for 2

    while mid <= high:
        if input_list[mid] == 0:
            # Swap the element at mid with the element at low
            input_list[low], input_list[mid] = input_list[mid], input_list[low]
            low += 1
            mid += 1
        elif input_list[mid] == 1:
            mid += 1
        else:  # input_list[mid] == 2
            # Swap the element at mid with the element at high
            input_list[mid], input_list[high] = input_list[high], input_list[mid]
            high -= 1

    return input_list

# Test cases
print(sort_array([2, 0, 1, 2, 0, 1]))  # Expected output: [0, 0, 1, 1, 2, 2]
print(sort_array([0]))                # Expected output: [0]
print(sort_array([]))                 # Expected output: []

