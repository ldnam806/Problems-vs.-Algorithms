def sqrt(number):
    if number == 0 or number == 1:
        return number

    start = 1
    end = number
    result = 0

    while start <= end:
        mid = (start + end) // 2
        if mid * mid == number:
            return mid
        elif mid * mid < number:
            start = mid + 1
            result = mid
        else:
            end = mid - 1

    return result

# Test cases normal
print("Pass" if (10 == sqrt(100)) else "Fail")     # Expected output: Pass (sqrt(100) = 10)
print("Pass" if (77 == sqrt(5929)) else "Fail")    # Expected output: Pass (sqrt(5929) = 77)
print("Pass" if (91 == sqrt(8281)) else "Fail")    # Expected output: Pass (sqrt(8281) = 91)
print("Pass" if (25 == sqrt(625)) else "Fail")     # Expected output: Pass (sqrt(625) = 25)
print("Pass" if (9 == sqrt(100)) else "Fail")      # Expected output: Fail (sqrt(100) = 10)
print("Pass" if (0 == sqrt(1)) else "Fail")        # Expected output: Pass (sqrt(1) = 1)
print("Pass" if (1 == sqrt(1)) else "Fail")        # Expected output: Pass (sqrt(1) = 1)
# Test for a large input number
print("Pass" if (1000 == sqrt(1000000)) else "Fail")  # Expected output: Pass (sqrt(1000000) = 1000)
# Test for a null input
print("Pass" if (0 == sqrt(0)) else "Fail")          # Expected output: Pass (sqrt(0) = 0)
# TTest for a negative input number 
print("Pass" if (-1 == sqrt(-100)) else "Fail")      # Expected output: Pass (sqrt(-100) = -1)

