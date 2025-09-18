 #Write a NumPy program to test whether each 
 # element of a 1-D array is also present in 
 # a second array.

 #  - Input:
  #   - Array1: [ 0 10 20 40 60]
  #   - Array2: [0, 40]
  # - Output: [ True False False True False]

import numpy as np
def function1():
    Array1=np.array([0, 10 ,20 ,40, 60])
    Array2=np.array([0, 40])
    result=np.isin(Array1,Array2)
    print("Array1:",Array1)
    print("Array2",Array2)
    print("result is=",result)
function1()    

