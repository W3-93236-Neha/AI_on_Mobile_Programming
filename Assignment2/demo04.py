#Write a Python function to Convert Celsius To Fahrenheit vice versa.
 #  fahrenheit = (celsius * 1.8) + 32
#Celsius = (Fahrenheit - 32) / 1.8

def function1():
    try:
        cel=int(input("Enter celsius"))
        print("Celsius is:",cel)
        fahrenheit=(cel*1.8)+32
        print("fehrenheit",fahrenheit)
        cel= (fahrenheit - 32) / 1.8
        print("cel val=",cel)
    except:
        print("invalid input")    



function1()    
