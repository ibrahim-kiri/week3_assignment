def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False
    
# Test the function
print(large_power(10, 3)) #Output: False
print(large_power(2, 10)) #Output: True
print(large_power(5, 4)) #Output: False

def divisible_by_ten(num):
    return num % 10 == 0

# Test the function
print(divisible_by_ten(20)) #Output: True
print(divisible_by_ten(25)) #Output: False
print(divisible_by_ten(100)) #Output: True