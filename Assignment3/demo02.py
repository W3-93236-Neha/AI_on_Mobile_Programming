#  2. Define a function subtract() that takes two lists and returns difference (i.e. excess elements from list1). If list1 = [10, 20, 30, 40] and list2 = [30, 40, 50, 60], then result should be [10, 20].[Note : without using set]


list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]


def subtract(list1, list2):
    l1 = list()

    for e1 in list1:
        for e2 in list2:
            if(e1 == e2):
                l1.append(e1)
                break

     
    for e1 in l1:
        for e2 in list1:
            if(e2 == e1) : 
                list1.remove(e2)
                break
    
    print(list1)
 
subtract(list1, list2)
