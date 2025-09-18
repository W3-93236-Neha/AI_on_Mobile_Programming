#Write a function that prompts the user to input number of calls and calculate the monthly  
# telephone bills as per the following rule:
#   Minimum Rs. 200 for up to 100 calls.
#   Plus Rs. 0.60 per call for next 50 calls.
#   Plus Rs. 0.50 per call for next 50 calls.
#   Plus Rs. 0.40 per call for any call beyond 200 calls.

def calculate_telephone_bill():
    
    try:
        num_calls = int(input("Enter the number of calls: "))

        if num_calls <= 100:
            bill = 200
        elif num_calls <= 150:
            # 200 for the first 100 calls + 0.60 per call for the next 50
            bill = 200 + (num_calls - 100) * 0.60
        elif num_calls <= 200:
            # 200 for the first 100 + 30 for the next 50 + 0.50 per call for the next 50
            bill = 230 + (num_calls - 150) * 0.50
        else:
            # 200 for the first 100 + 30 for the next 50 + 25 for the next 50
            # + 0.40 per call for calls beyond 200
            bill = 255 + (num_calls - 200) * 0.40
        
        print(f"The monthly telephone bill is: Rs. {bill:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# To run the function, simply call it:
calculate_telephone_bill()