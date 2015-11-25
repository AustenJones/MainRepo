"""
Function designed to calculate the factorial of an integer n.
First attempts to convert argument n to integer if possible; 
if n is not convertible to integer type, prints error message. 
If n is convertible to integer type, function continues by first
checking whether n is zero, in which case it returns 1.  This
is the only special case in the factorial calculation.  If n
is not zero, the function returns the product of n and every
incremental integer between n and zero inclusive.
"""

def factorial(n):
    try:
	    n = int(n)
	except ValueError:
	    print("Error: The factorial operation is valid only for \
		positive integers. Please provide a positive integer")
	if n == 0:
	    return 1
	elif n < 0:
	    print("Error: The factorial operation is valid only for \
		positive integers. Please provide a positive integer")
	else:
	    return n * factorial(n - 1)