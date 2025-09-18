 #Create a class Distance with two (public) attributes feet and inches. Add custom initializer in it.
 #  Now write a function (outside the class), to add two given distance objects. E.g. if d1=3'5" and d2=4'8", then
 #  addition method should return 8'1".

class Distance:
    
    def __init__(self, feet, inches):
       
        self.feet = feet
        self.inches = inches

    def __str__(self):
       
        return f"{self.feet}'{self.inches}\""


def add_distances(d1, d2):
   
    total_feet = d1.feet + d2.feet
    total_inches = d1.inches + d2.inches

    # Normalize the inches to account for every 12 inches forming a new foot
    if total_inches >= 12:
        extra_feet = total_inches // 12
        total_feet += extra_feet
        total_inches %= 12
    
    return Distance(total_feet, total_inches)


d1 = Distance(3, 5)
d2 = Distance(4, 8)


d3 = add_distances(d1, d2)

print(f"Distance 1: {d1}")
print(f"Distance 2: {d2}")
print(f"Sum: {d3}")