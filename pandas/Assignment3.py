#q1
import pandas as pd
import numpy as np
data = {
    "Tid": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Refund": ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
    "Marital Status": ["Single", "Married", "Single", "Married", "Divorced",
                       "Married", "Divorced", "Single", "Married", "Single"],
    "Taxable Income": ["125K", "100K", "70K", "120K", "95K",
                       "60K", "220K", "85K", "75K", "90K"],
    "Cheat": ["No", "No", "No", "No", "Yes", "No", "No", "Yes", "No", "Yes"]
}
df=pd.DataFrame(data)
print(df)
#q2
print(df.loc[[0, 4, 7, 8]])
#q3
print(df.iloc[3:8])     
print(df.loc[3:7])       
print(df.iloc[4:9, 2:5])
print(df.iloc[:, 1:4])
#q4
df = pd.read_csv("Iris.csv")
print(df.head())
#q5
df_new = df.drop(index=4)                         # delete row with index label 4
df_new = df_new.drop(columns=df_new.columns[3])   # delete column at position 3

print(df_new.head(7))
print(df_new.shape)     # (149, 5)
#q6


data1 = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": ["2020-03-15","2017-07-19","2013-06-01","2021-02-10","2010-11-25"],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5],
}
df = pd.DataFrame(data1)
df.to_csv("employees.csv", index=False)

df = pd.read_csv("employees.csv", parse_dates=["Joining_Date"])
#(a)
print(df.shape)  
#(b)
df.info() 
#(c)
print(df.describe()) 
#(d)
print(df.head())      # head(5) is the default
print(df.tail(3))
#(e)
print("Average salary :", df["Salary"].mean())      # 60000.0
print("Total bonus    :", df["Bonus"].sum())        # 27500
print("Youngest age   :", df["Age"].min())          # 28
print("Highest rating :", df["Rating"].max())       # 4.7
#(f)
print(df.sort_values(by="Salary", ascending=False))
#(g)
conditions = [df["Rating"] >= 4.5, df["Rating"] >= 4.0]
choices = ["Excellent", "Good"]
df["Performance_Category"] = np.select(conditions, choices, default="Average")
#(h)
print(df.isnull().sum())
#(i)
df = df.rename(columns={"Employee_ID": "ID"})
#(j)
df[df["Years_of_Experience"] > 5]        # Bob, Charlie, Edward
df[df["Department"] == "IT"]             # Bob, Charlie
df[(df["Years_of_Experience"] > 5) & (df["Department"] == "IT")]   # Bob, Charlie
#(k)
df["Tax"] = df["Salary"] * 0.10
#(l)
df.to_csv("modified_employees.csv", index=False)
