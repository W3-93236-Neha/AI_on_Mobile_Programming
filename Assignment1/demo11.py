#11. Write a program to find minimum of three numbers. Use appropriate logical operators.
num1=int(input("Enter the number 1"))
num2=int(input("Enter the number 2"))
num3=int(input ("Enter the number 3"))

if num1 >=num2 and num2>=num3:
    print ("num 1 is greater")
elif num2>= num3:
    print("num2 is greater")
else:
    print("num3 is greater")   

print("program Excuted") 