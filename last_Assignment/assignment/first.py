#1. Write a NumPy program to convert Centigrade degrees into
#  Fahrenheit degrees. Centigrade values are stored in a NumPy
#  array.
#  - Input (°C): [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]
# - Output (°F): [0, 12, 45.21, 34, 99.91]

import numpy as np
def function1():
    celsius=np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0. ],dtype=np.float64)
    fehrenheit=(celsius * 9/5) + 32
    result=np.round(fehrenheit,2)
    print("Centigrade degrees:", celsius)
    print("Fahrenheit degrees:", fehrenheit)
    print("final Output",result)

function1()   