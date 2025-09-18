6 #Write a function that prompts the user to input a year and determine whether the year is a leap  year or not. Leap Years are any year that can be evenly divided by 4.
   #A year that is evenly divisible by 100 is a leap year only if it is also evenly divisible by    400.
   #Example :
   #1992 Leap Year
   #2000 Leap Year
   #1900 NOT a Leap Year
   #1995 NOT a Leap Year

def leap_function():
    try:
        leap_year=int(input("Enter the year"))
        print("year is :",leap_year)
    except ValueError:
        print("Enter the valid year")
    if (leap_year % 400==0) or (leap_year % 4==0 and leap_year % 100!=0): 
        print("Leap year")
    else:
        print("Not a Leap year")     

leap_function()       

    

   