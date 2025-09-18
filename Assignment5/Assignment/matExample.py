#matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def function1():
    x=np.array([1,2,3,4,5,6,7])# year
    y=np.array([10,20,30,40,50,25,11]) #profit

    plt.scatter(x,y)
    plt.xlabel("Years")
    plt.ylabel("Profit")
    plt.tight_layout()
    plt.plot(x,y,color="red")
    plt.savefig("char1.png")
    plt.show()
#function1()  
def function2():
    df=pd.read_csv("F:\python\Assignments\Assignment5\Assignment\emps.csv")
    df.dropna(subset=["sal"],inplace=True)
    sals=df["sal"]
    plt.pie(sals,labels=df["ename"])
    plt.show()
function2()      
 