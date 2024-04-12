def rearrange_digits_max_sum(input_list):
    if len(input_list) <= 1:
        return input_list

    # Function to find the maximum and minimum elements in the array
    def find_max_min(arr):
        max_num, min_num = float('-inf'), float('inf')
        for num in arr:
            if num > max_num:
                max_num = num
            if num < min_num:
                min_num = num
        return max_num, min_num

    max_num, min_num = find_max_min(input_list)
    
    # Initialize frequency counters for each digit
    frequency = [0] * 10
    for num in input_list:
        frequency[num] += 1

    # Construct the two numbers based on their frequencies
    num1, num2 = 0, 0
    is_first_num = True
    for digit in range(9, -1, -1):
        while frequency[digit] > 0:
            if is_first_num:
                num1 = num1 * 10 + digit
            else:
                num2 = num2 * 10 + digit
            frequency[digit] -= 1
            is_first_num = not is_first_num

    return [num1, num2]


def test_rearrange_digits_max_sum():
    # Test cases
    test_cases = [
        [[1, 2, 3, 4, 5], [542, 31]],
        [[4, 6, 2, 5, 9, 8], [964, 852]],
        [[], []],
        [[1], [1]]
    ]

    for input_list, expected_output in test_cases:
        output = rearrange_digits_max_sum(input_list)
        if sum(output) == sum(expected_output):
            print("Pass")
        else:
            print("Fail")

# Call the test function
test_rearrange_digits_max_sum()
