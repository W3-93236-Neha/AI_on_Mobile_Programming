#Write a Python program to calculate the average value
# of the numbers in a given tuple of tuples.
#   - Input: ((10, 10, 10, 12), (30, 45, 56, 45),
#    (81, 80, 39, 32), (1, 2, 3, 4))
#   - Output: [30.5, 34.25, 27.0, 23.25]
def function1():
    Input= ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
    average=[]
    for tup in Input:
        result=sum(tup)
        count=len(tup)
        average.append(result/count)
        print(average)

function1()