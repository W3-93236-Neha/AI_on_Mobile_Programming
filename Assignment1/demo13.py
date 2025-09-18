#13. Write a program to check if given number is prime or not. Hint: Number is prime if not divisible by any number from 2 to that number-1.
# Check if a number is prime

# Input
num = int(input("Enter a number: "))

if num <= 1:
    print(" not a prime number.",(num))
else:
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(" prime number.",(num))
    else:
        print("not a prime number.",(num))
   
