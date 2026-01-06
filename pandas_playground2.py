#DAY 6 — PANDAS WITH REAL CSV DATA (DATA CLEANING DAY)

# Target time: ~2–2.5 hours

# Goal: Load real data, inspect it, clean it, and prepare it for ML

#TASK 1: Create a CSV & Read It 
import pandas as pd
import numpy as np
print("Task 1:\n")

df = pd.read_csv(r"C:\Users\Anagha Ghewari\OneDrive\Desktop\students.csv")
print("The data set is as follows:\n",df)
print("Shape:\n",df.shape)
df.info()

#TASK 2:Detect Missing Values
print("Task 2:\n")

print(df.isnull(),"\n")
print(df.isnull().sum(),"\n")
#Thus Age,score and city has null values

#TASK 3: Handle Missing Values
print("Task 3:\n")
 
df["Age"]=df["Age"].fillna(df["Age"].mean())
print(df,"\n\n\n")
df["Score"]=df["Score"].fillna(df["Score"].median())
print(df,"\n\n\n")
df["City"]=df["City"].fillna("Unknown")
print(df,"\n\n\n")

#TASK 4: Data Type Verification
print("Task 4:\n")
print(df.dtypes,"\n\n")

df["Age"]=df["Age"].astype(int)
df["Score"]=df["Score"].astype(int)
print(df,"\n\n\n\n")
print(df.dtypes)

#TASK 5: Rename Columns
print("Task 5:\n")
df.columns = ["name", "age", "score","city"]

print(df.columns)
print(df,"\n\n\n\n")

#TASK 6: Filtering Cleaned Data
print("Task 6:\n")
print(df[(df["score"]>85)],"\n")
print(df[(df["city"]=="Pune")],"\n")
print(df[(df["age"]>=21) & (df["score"]>=80)],"\n")

#TASK 7: Prepare Data for ML
X=df[["age","score"]]
print(X,"\n")
print(X.shape)

df["Passed"]=(df["score"]>=80)

y=df["Passed"]
print("Passed:\n",y)
print(y.shape)

#TASK 8: Thinking Task (IMPORTANT)
# 1. handling the missing values is one of the most important task as it helps  in improving the accuracy of the model as there is more clarified data available
# 2.it helps in incresing the efficiency of the training model
# 3.it make the data more clean
 

#DAY 7 — PANDAS EDA (EXPLORATORY DATA ANALYSIS)

#Target time: ~2–2.5 hours

#Goal: Learn how to understand patterns, distributions, and relationships in data

#TASK 1: Re-check the Cleaned Dataset
print(df,"\n\n")

print(df.shape)
df.info()
print("\n")

print(df.describe(),"\n")

#The mean for the the age is 20.600000 and that if the score is 85.800000 while the std tells that the other values are deviating from the mean for age by a difference of abour 0.89 while that of the score id deviating by 5.11
#25% include the data in the value id 20 for age and that of the score is 85, 50% of age includes 20 for age and 86 for score while that for the 75% for age is 21 and score is 88

#TASK 3: Value Counts

print(df["Passed"].value_counts(),"\n\n")
print(df["city"].value_counts())

#TASK 4: GroupBy
score_per_city=df.groupby('city')

score_sum = score_per_city['score'].mean()
print(score_sum)

stud_per_city=df.groupby('city')

count=stud_per_city['city'].count()
print(count)

passed_age_mean=df[df["Passed"]==True]["age"].mean()
print(df)

#TASK 5: Feature Relationship
#1 yes the students who are older have more score than the younger ones
#2 students from mumbai seem to have a higher score as compared to the other cities
print(df.describe())

#TASK 6: Prepare Final ML Dataset
X=df[["age","score"]]
print(X.head(2))
Y=df["Passed"]
print(Y.head(2))

#Exploratory Data Analysis (EDA) is a crucial first step in data science where analysts use visualization and summary statistics to understand a dataset's core features, find patterns, detect anomalies, test assumptions, and identify relationships between variables, essentially acting as detective work before formal modeling to guide subsequent analysis and ensure data quality. It's an iterative process of questioning, visualizing, transforming, and modeling the data to generate hypotheses and uncover insights. 









