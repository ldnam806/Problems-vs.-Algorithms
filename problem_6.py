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

### Additional Example Test Cases
import random

# Test case with 100 integers in random order
l = [i for i in range(0, 100)]  # a list containing 0 - 99
random.shuffle(l)

print("Pass" if ((0, 99) == get_min_max_value(l)) else "Fail")

# Test case with negative integers
print("Pass" if ((-10, 10) == get_min_max_value(list(range(-10, 11)))) else "Fail")

# Test case with duplicate integers
print("Pass" if ((0, 0) == get_min_max_value([0, 0, 0])) else "Fail")

# Test case with a single integer
print("Pass" if ((5, 5) == get_min_max_value([5])) else "Fail")

# Test case with an empty list
print("Pass" if (None == get_min_max_value([])) else "Fail")
