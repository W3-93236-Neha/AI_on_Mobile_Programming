#Refer the dataset "Salaries.csv" and perform following tasks.

  # - Read the dataset in dataframe.
   #- display first five records.
  # - display first ten records.
   #- display last five records.
   #- display last ten records.
   #- display the columns inside the dataset.
   #- display shape of data.
   #- describe the dataset.
   #- display the information about the dataset and analyse the data.
   #- display types of each columns.
   #- Find out maximum,minimum,mean,median,standard deviation value of each column.
   #- Replace all null values by mean or mode
import pandas as pd
def function1():
    df=pd.read_csv("assignment/Salaries.csv")
    print(df)
    print("display first five records=",df.head(5))
    print("--------------------------------------")
    print("display first Ten records=",df.head(10))
    print("--------------------------------------")
    print("display last five records=",df.tail(5))
    print("--------------------------------------")
    print("display last ten records=",df.tail(10))
    print("--------------------------------------")
    print("column in dataset:",df.columns)
    print("--------------------------------------")
    print("shape of the dataset=",df.shape)
    print("--------------------------------------")
    print("Description of the dataset:",df.describe())
    print("--------------------------------------")
    print("Information about the dataset",df.info())
    print("--------------------------------------")
    print("Datatype of each column=",df.dtypes)
    print("--------------------------------------")
    print("\nStatistical values for each column:")
    print("Maximum:\n", df.max())
    print("\nMinimum:\n", df.min())
    print("\nMean (for numeric columns):", df.mean(numeric_only=True))
    print("\nMedian (for numeric columns):", df.median(numeric_only=True))
    print("\nStandard Deviation (for numeric columns):", df.std(numeric_only=True))
    print("--------------------------------------")
    

function1()

    