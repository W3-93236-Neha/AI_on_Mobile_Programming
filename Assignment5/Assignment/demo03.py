import pandas as pd
import numpy as np

def function1():
    s1 = pd.Series([10, 20 ,30, 40,50])
    print("s1 = ",s1)
    print("type of s1 =",type(s1))
    print(f"s1.size = {s1.size}")
    print(f"s1 nbytes = {s1.nbytes}")
    print(f"s1 shape = {s1.shape}")
    print(f"s1 dtype= {s1.dtype}")
    print(f"s1 ndim = {s1.ndim}")
    print(f"s1 values = {s1.values}")
    print(f"s1 keys = {s1.keys()}")
    

#function1()

def function2():
    students = ["st1", "st2", "st3", "st4", "st5"]
    marks = [11, 77, 44, 33, 87]
    stud_marks=pd.Series(data = marks , index = students)
    print("stud_marks=",stud_marks)

#function2()

# series from collections
def function4():
    # series from tuple
    s1 = pd.Series((1.2, 2.3, 4.3, 4.5),dtype=np.float32)
    print("s1 = ",s1)

    # s2 = pd.Series({22, 33, 44, 55})   TypeError: 'set' type is unordered

    s2 = pd.Series({
        "name" : "Ravi",
        "age"  :  34
    })
    print("s2 = ",s2)

function4()