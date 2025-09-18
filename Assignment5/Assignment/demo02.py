import numpy as np

def function1():
    a1=np.array([1,2,3])
    a2=np.array([3,2,1])
    res=a1+a2
    print(f"{a1} + {a2} = {res}")
    print(f"{a1} * {a2} = {a1*a2}")

    res = a1==a2
    print(f"{a1} == {a2} = {res}")

#function1()
# broadcast operations
def function2():
    a1 = np.array([1, 2, 3])
    n = 10
    res = a1 + n 
    print(f"{a1} + {n} = {res}")

# function2()

#numpy Serching using where
def function3():
    arr1=np.array([11,22,33,44,55,66])
    idx=np.where(arr1 % 2== 0 )
    print("evens=",arr1[idx])
    print("odds=",arr1[np.where(arr1%2!=0)])
#function3()
def function4():
    arr1 = np.array([11, 22, 33, 44, 55, 66, 77, 88])
    print("arr > 30 =",arr1 [arr1 > 30])

function4()