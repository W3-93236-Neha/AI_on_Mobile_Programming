# Input a string from user and display unique characters in it.
#  Hint: list(str) convert string to list of chars.


def function1():
    str=(input("Enter the  String"))
    result=set(str)
    unique_char=sorted(list(result))
    
    print(unique_char)
function1()    

