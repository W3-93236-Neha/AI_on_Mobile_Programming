# Write functions to convert kilometers to meters, meters to centimeters, centimeters to millimeters,
#  feets to inches, and inches to centimeter. Write a function distance_converter() that takes a distance,
#  conversion type as a string (e.g. km to m, m to cm, etc.) and a conversion function as argument. This function does
#  the conversion using given function and print the result. Input a distance from user and print all conversions.

def km_to_m(kilometers):
    """Converts kilometers to meters."""
    return kilometers * 1000

def m_to_cm(meters):
    """Converts meters to centimeters."""
    return meters * 100

def cm_to_mm(centimeters):
    """Converts centimeters to millimeters."""
    return centimeters * 10

def feets_to_inches(feets):
    """Converts feets to inches."""
    return feets * 12

def inches_to_cm(inches):
    """Converts inches to centimeters."""
    return inches * 2.54

def distance_converter(distance, conversion_type, conversion_function):
   
    converted_distance = conversion_function(distance)
    print(f"{distance} {conversion_type.split(' ')[0]} is equal to {converted_distance} {conversion_type.split(' ')[-1]}")

if __name__ == "__main__":
    try:
        user_distance = float(input("Enter a distance: "))

        print("\nPerforming conversions:")
        distance_converter(user_distance, "km to m", km_to_m)
        distance_converter(user_distance, "m to cm", m_to_cm)
        distance_converter(user_distance, "cm to mm", cm_to_mm)
        distance_converter(user_distance, "feets to inches", feets_to_inches)
        distance_converter(user_distance, "inches to cm", inches_to_cm)

    except ValueError:
        print("Invalid input. Please enter a numerical value for the distance.")
        
