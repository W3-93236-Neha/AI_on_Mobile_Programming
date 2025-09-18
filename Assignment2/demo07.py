#The marks obtained by a student in 3 different subjects are input by the user. Your
#    function should calculate the average of subjects and display the grade. The student
#    gets a grade as per the following rules:
#    Average Grade
  #  90-100 A
  #  80-89 B
   # 70-79 C
   # 60-69 D
    # 0-59 F
subject1=int(input("Enter the marks of English"))
subject2=int(input("Enter the marks of Hindi"))
subject3=int(input("Enter the marks of Marathi"))

def averagefun():
    average=(subject1+subject2+subject3)/3
    print("average is",average)

    if  average >= 90 :
        print("A") 
    elif average >= 80:
        print("B") 
    elif average >=70:
        print("c")
    elif average >=60:
        print("D")  
    elif  average >=50:
        print("E")    
    else:
        print("invalid input")        

averagefun()
