import pandas as pd
import numpy as np

def print_df_info(df):
    print("df type:",type(df))
    print(f"size = {df.size}") # num of elems
    print(f"dtype = \n{df.dtypes}") # data type of elems -- int64 = 8 bytes
    print(f"ndims = {df.ndim}") # num of dims
    print(f"shape = {df.shape}") # dimensions
    print(f"values = {df.values}")
    print(f"keys = {df.keys()}") # 
    print(f"columns =\n{df.columns}") # Index(['name', 'age', 'addr'], dtype='object')



 # dataframe from list of dicts
def function1():
    # list of dicts
    heros = [
        {"name": "James", "age": 65, "addr": "London"},
        {"name": "Superman", "age": 60, "addr": "Crypton"},
        {"name": "Batman", "age": 45, "addr": "Gotham"},
        {"name": "Panther", "age": 50, "addr": "Wakhanda"}
    ]

    df=pd.DataFrame(heros)
    print(df)
    print_df_info(df)

#function1()
def function3():
    df = pd.read_csv("Assignment/dept.csv")
    print(df)
#function3()
def function4():
    df = pd.read_csv("F:\python\Assignments\Assignment5\Assignment\emps.csv")
    # print(df)
    # print(df.head(3))
    print(df.tail(3))

#function4()

def function5():
    df = pd.read_csv("F:\python\Assignments\Assignment5\Assignment\emps.csv")
    # print("check if nulls are present: ")

    # print("check if nulls are present: ")
    # print(df.isna())   # True => null values, False => non-null values
   
    # print("\ndropping all rows with null values: ")
    # print(df.dropna())  # delete row  default = 0
    
    # print("\ndropping all columns with null values: ")
    # print(df.dropna(axis=1))  # delete column

    print("\nreplace all nulls with 0.0: ")
    # print(df.fillna(0))
    print(df.fillna({"mgr":-1,"sal":0.0,"comm":0.0}))
#function5()

def function6():
    df = pd.read_csv("F:\python\Assignments\Assignment5\Assignment\emps.csv")
    print("\ncheck if duplicates are present or not...")
    print(df.duplicated("sal"))
    print("\ndelete the duplicate rows...")
    print(df.drop_duplicates("sal"))

#function6()

def function7():
    df = pd.read_csv("F:\python\Assignments\Assignment5\Assignment\emps.csv")
    # accessing column
    # names=df["ename"]
    # print(f"type of names = {type(names)},\n {names}")

    # accessing multiple columns
    # data=df[["ename","sal"]]
    # print(f"type of names = {type(data)},\n {data}")

    # accessing row
    emp_row=df.loc[4]
    print("emp_row =",emp_row)

    # access a cell --> ename of 4th emp
    emp_name=df.loc[4]["ename"]
    print("emp_name =",emp_name)

    # modify a cell
    # df.loc[9]["ename"] = "DON" # only for reading -- not for changing
    df.loc[9,"ename"] = "DON"
    print(df)
#function7()
# filtering -- internally uses numpy filtering
def function8():
    df = pd.read_csv("F:\python\Assignments\Assignment5\Assignment\emps.csv")
    print("get all emps with sal < 1000:")
    bool_index = df["sal"] < 1000
    poor_emps=df[bool_index]
    # print(poor_emps)

    print("\nget all emps with sal >= 3000:")
    rich_emp = df[df["sal"] >=3000 ]
    print(rich_emp)

#function8()
def function9():
    df=pd.read_csv("F:\python\Assignments\Assignment5\Assignment\emps.csv")
    print("\n add new column bonus=sal* 0.10")
    df["bonus"]=df["sal"]* 0.10
    print(df)
#function9()    
def function10():
    df=pd.read_csv("F:\python\Assignments\Assignment5\Assignment\emps.csv")
    df["ename"]=df["ename"].map(lambda x:x.lower())
    print(df)
#function10()
def function11():
    df=pd.read_csv("F:\python\Assignments\Assignment5\Assignment\emps.csv")
    print("add new col dnames:")
    df["dname"]=df["deptno"].map({
        10:"ACCOUNTING",
        20:"RESERCH",
        30:"SALES"
    })
    print(df)
#function11() 
def function12():
    df=pd.read_csv("F:\python\Assignments\Assignment5\Assignment\emps.csv")
    df.sort_values(by=["deptno","sal"],ascending=False,inplace=True)
    print(df)
#function12() 
# group by aggregation
def function13():
    df=pd.read_csv("F:\python\Assignments\Assignment5\Assignment\emps.csv")
    result=df.groupby("deptno").sum(True)
    print(result["sal"])
function13()    
 
   
