#Pandas Playground
#Day-1
import pandas as pd
#Task-1:TASK 1: Create & Inspect a DataFrame (Warm-up)
data={
    "Name":["Amit","Sara","Neha","Rohit","Krian"],
    "Age":[20,21,19,22,20],
    "Score":[85,90,78,88,92],
    "City":["Pune","Mumbai","Pune","Delhi","Mumbai"]

}
df=pd.DataFrame(data)
print("The data set is as follows:",df)
print("The shape of the above data set is as follows:",df.shape)
print(df.shape) #The shape attribute of the data frame tells us about the no of rows and the no of columns of the given data set
print(df.columns)
print(df.index)


#TASK 2: Series vs DataFrame
#Extract the Age column into a variable
print("The Age in the given data set is as follows:\n",df["Age"])
print(type(df["Age"]),"\n")
print(type(df),"\n")
print(df["Age"].values,"\n")
print(df.values,"\n")
#The difference is that Age.values gives the value of the age column while the df.values give the value of the entire data frames but not in the form of a data frame or a table but in the form of a 2d array


#TASK 3: Data Inspection (VERY IMPORTANT)
print(df.head(2),"\n")
print(df.tail(2),"\n")
df.info()
print(df.describe(),"\n")
#df.info will show the data type of the above data set
#df.decscribe will give the statistics
print(df.isnull(),"\n")
print("The total number of the missing values is as follows:\n",df.isnull().sum())


#TASK 4: Column Selection
data0=df["Score"]
print("Score:\n",data0)
data1=df[["Name","City"]]
print(data1,"\n")

#TASK 5: Row Selection
row_1=df.iloc[0]
print(row_1,"\n")
rows=df.iloc[1:4]
print(rows,"\n")
print(df.loc[df["Age"]>20],"\n")

#TASK 6: Conditional Filtering (IMPORTANT)
print(df.loc[df["Score"]>85],"\n")
print(df[(df["City"]=="Pune")],"\n")
print(df[(df["Score"]>=85) & (df["Age"]>=20)],"\n")
print(df[(df["City"]=="Mumbai") | (df["City"]=="Delhi")],"\n")

#TASK 7: Add a New Column
df["Passed"] = df["Score"]>=80
print(df["Passed"],"\n")
print(df)

#TASK 8: Sorting & Counting
df_sorted=df.sort_values(by="Score",ascending=False)
print(df_sorted,"\n")
print(df["City"].value_counts(),"\n")

#With the help of pandas we can easily visualize and analyase the data than in numpy
#Data can be visualize in the form of labeled data 
#helps in easy data manipulation and handling the missing data efficiently
a=3
print(type(a))