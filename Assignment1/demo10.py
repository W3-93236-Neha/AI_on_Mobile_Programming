#Using a loop, write a program to find factorials from 0 to 10.
# Factorial from 0 to 10 using a loop
fact = 1

for i in range(0, 11):
    if i == 0:
        fact = 1
    else:
        fact *= i
    print("factorial is",(fact))
