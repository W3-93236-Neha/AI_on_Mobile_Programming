#Input a 4 digit int from user and print sum of its digits.

num = int(input("Enter a 4-digit number: "))

if 1000 <= num <= 9999:

    sum = sum(int(digit) for digit in str(num))
    print("Sum of digits of is ",(sum))
else:
    print("Invalid Input.")
