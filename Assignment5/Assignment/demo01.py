# classwork

import mymodule

def function1():
    print("var1=",mymodule.var1)
    mymodule.func1()
    p1=mymodule.Person()
    p1.display()
    print(p1)
#function1() 
# 
# -------Function2

def function2():
    import my_maths as mt
    mt.add(2,4)
#function2()  
#------------------function3
def function3():
    import my_maths
    my_maths.sub(7,2)
#function3() 


#------------------function4

def function4():
    from my_maths import mul
    mul(9,2)
#function4() 

#-------------------- function5

from my_maths import *

def function5():
    add(4,5)
    sub(33,2)
    mul(4,2)
    divide(10,2)
#function5()   

def function6():
    from my_maths import mul as m
    m(3,2)
#function6() 

import math
import random as r
def function7():
    print(f"squaere root of num={math.sqrt(16)}") 
    num=r.randint(10,99)
    print(f"random number ={num}")
#function7()
# 
#     
import numpy as np
def print_info(arr1):
    print(f"arr1.size = {arr1.size}")
    print(f"type of arr1 = {type(arr1)}")
    print(f"arr1 nbytes = {arr1.nbytes}")
    print(f"arr1 shape = {arr1.shape}")
    print(f"arr1 dtype= {arr1.dtype}")
    print(f"arr1 ndim = {arr1.ndim}")
    print(f"arr1 flags= {arr1.flags}")
    

def function8():
    arr1=np.array([11,22,33,444,55,66,77])
    print(f"arra1={arr1}")
    print_info(arr1)

    arr2 = np.array([[1,2,3],[4,5,6]])
    print(f"arr2 = {arr2}")
    print_info(arr2)

    arr3 = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
    print(f"arr3 = {arr3}")
    print_info(arr3)

    arr4 = np.array([1, 2.2, True, "Pune"])
    print(f"arr4 = {arr4}")
    print_info(arr4)

#function8()

def function9():
    arr1=np.array([11,22,33,44,55,66,77])
    print(f"arr1={arr1},of bytes={arr1.nbytes}")

    arr2=np.array([11,22,33,44,55,66,77],dtype=np.int16)
    print(f"arra2={arr2},of bytes={arr2.nbytes}")

    arr3=np.arange(1,10)
    print(f"arr3 = {arr3} ")
     # ndarray of ones or zeros
    arr4=np.ones(5,dtype=np.int8)
    print(f"arr4 = {arr4} ")

    arr5=np.zeros(5,dtype=np.int8)
    print(f"arr5 = {arr5} ")

    arr6=np.zeros((3,4),dtype=np.int8) # array of 3 rows & 4 cols
    print(f"arr6 = {arr6} ")

    # ndarray from random nums
    arr7=np.random.randint(10, 99, size=6)
    print(f"arr7 = {arr7} ")

#function9()
def function10():
    arr1=np.array([11,22,33,44,55,66,77,88])
    arr2=arr1.copy()
    print(f"original arr1={arr1}")
    print(f"original arr2={arr2}")
    arr1[1]=10
    arr1[0]=5
    print(f"modified arr1={arr1}")
    print(f"modified arr2 is={arr2}")
    print_info(arr1)
    print_info(arr2)
#function10()

# numpy array view
def function11():
    arr1 = np.array([11, 22, 33, 44, 55])
    arr2 = arr1.view()
    print(f"original arr1 = {arr1} ")
    print(f"original arr2 = {arr2} ")
    arr1[0] = 10
    arr1[1] = 20
    print(f"modified arr1 = {arr1} ")
    print(f"modified arr2 = {arr2} ")
    print_info(arr1)
    print_info(arr2)
#function11()

def function12():
    arr1=np.array([11,22,33,44,55,66,77,88,99])
    print(f"arr1 shape={arr1}")
    print(f"arr1 shape={arr1.shape}")
    arr2=arr1.reshape(3,2)
    print(f"arr2,{arr2}")
    print(f"arr1 shape={arr2.shape}")
    arr3=arr1.reshape(6,)
    print(f"arr2,{arr3}")
    print(f"arr1 shape={arr3.shape}")
    arr4=arr1.reshape(2,2)
#function12()    
def function13():
    arr1 = np.array([[11, 22, 33], [44, 55,66]])
    print(f"arr1 = {arr1} ")
    a2=arr1.flatten()   # changes in copy will not reflect in a1
    print(f"a2 = {a2} ")

#function13()
def function14():
    arr1 = np.array([[11, 22, 33], [44, 55,66]])
    print(f"arr1 = {arr1} ")
    arr1.resize((3,2))   # resizing the current array itself
    print(f"arr1 = {arr1} ")
    arr1.resize((2,2))   # resizing - size reduced - array is truncated
    print(f"arr1 = {arr1} ")
    arr1.resize((4,2))   # resizing - size increased - zeros added in array
    print(f"arr1 = {arr1} ")
#function14() 
def function15():
    arr1 = np.array([11, 22, 33, 44, 55, 66])
    print(f"arr1 = {arr1}")
    print(f" arr1[2] = {arr1[2]}") #33
    print(f" arr1[-2] = {arr1[-2]}")  #55
     # slicing
    print(f" arr1[1:4] = {arr1[1:4]}")  #[22 33 44]
    for n in arr1:
        print(n)
# function15()   
def function16():
    arr1 = np.array([11, 22, 33, 44, 55, 66, 77, 88])
    id = [2, 5, 3, 7]
    print(f"arr1[id] = {arr1[id]}")

#function16()
def function17():
    arr1 = np.array([11, 22, 33, 44, 55, 66, 77, 88])
    id = [True,False,True,True,False,False,False,True]
    print(f"arr1[id] = {arr1[id]}")
function17()