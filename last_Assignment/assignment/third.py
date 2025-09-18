 #Follow the given steps.
  # - Create a list of empids and names (10 employees).
  # - Convert list into Series.
  # - Print type of Series.
   #- Convert Series into DataFrame.
   #  - Display all records.
   #- Save the record in csv file (MyRecord.csv).
   #  - Hint: to_csv()

import pandas as pd
def employee():
    employee_data = [
    (101, 'Neha'),
    (102, 'Abhi'),
    (103, 'Gaurav'),
    (104, 'Kunal'),
    (105, 'minal'),
    (106, 'priya'),
    (107, 'shivam'),
    (108, 'riya'),
    (109, 'ayan'),
    (110, 'yash')
                 ]
    id = pd.Series([emp[0] for emp in employee_data])
    names = pd.Series([emp[1] for emp in employee_data])
    
    print("Type of id=",type(id))
    print("Type of names=",type(names))

    df=pd.DataFrame({
        "id":id,
        "name":names
    })
    print("display all the records=",df)

    df.to_csv('Myrecord.csv',index=False)

employee()    
