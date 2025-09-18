#A function that call itself is called as recursive function. 
# Write a recursive function to calculate power.

def power(base, exponent):
    # Base case: any number to the power of 0 is 1
    if exponent == 0:
        return 1
    # Recursive case: multiply base by power(base, exponent - 1)
    return base * power(base, exponent - 1)


print(power(2, 3))  
