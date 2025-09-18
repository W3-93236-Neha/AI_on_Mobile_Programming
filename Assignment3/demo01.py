#1: Define a function union() that takes two lists and 
#returns another list that have union both lists. If list1 = 
#[10, 20, 30, 40] and list2 = [30, 40, 50, 60], then result 
#should be [10, 20, 30, 40, 50, 60]. [Note : without using set]



list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

def union(list1,list2):
    l1=list()

    for e1 in range(len(list1)):
        e=e1
        for e2 in list2:
            if(list1[e]==e2):
                l1.append(e2)
                break
    print(l1)  

    for i1 in l1:
        for i2 in list2:
            if(i2==i1):
                list2.remove(i2) 
    print(list2)                

    
    for i2 in list1:
             if(i2 == i1):
                list1.remove(i2)
                 
    print(list1)

    l1.extend(list1)
    l1.extend(list2)
    l1.sort()
    print(l1)

union(list1,list2)        


    





