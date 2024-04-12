def get_min_max_value(ints):
    if not ints:
        return None

    min_value = max_value = ints[0]

    for num in ints[1:]:
        if num < min_value:
            min_value = num
        elif num > max_value:
            max_value = num

    return (min_value, max_value)

# Test cases
print(get_min_max_value([3, 5, 2, 1, 4]))  # Expected output: (1, 5)
print(get_min_max_value([7]))             # Expected output: (7, 7)
print(get_min_max_value([]))              # Expected output: None

