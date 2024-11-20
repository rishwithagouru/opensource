def reverse_integer(n):
    # Define the 32-bit signed integer range
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    
    # Determine if the number is negative
    is_negative = n < 0
    n = abs(n)  # Work with the absolute value for reversal
    
    # Reverse the digits
    reversed_n = int(str(n)[::-1])
    
    # Reapply the negative sign if necessary
    if is_negative:
        reversed_n = -reversed_n
    
    # Check for overflow
    if reversed_n < INT_MIN or reversed_n > INT_MAX:
        return 0
    
    return reversed_n

# Read the input
n = int(input().strip())

# Get the reversed integer
result = reverse_integer(n)

# Print the result
print(result)
