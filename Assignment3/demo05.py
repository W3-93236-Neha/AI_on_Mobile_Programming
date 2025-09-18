#You have sensor readings (some may be faulty):
  # - readings = [12, 15, 11, 120, 14, 16, 13, 200, 12, 15]
   #- Remove the top 2 and bottom 2 values (assume the list
   #  is large, and slicing helps).

def function1():

    readings = [12, 15, 11, 120, 14, 16, 13, 200, 12, 15]
    readings.sort()
    result=readings[2:-2]
    print("sorted list:",readings)
    print("top2 and bottom 2 removed",result)

function1()
