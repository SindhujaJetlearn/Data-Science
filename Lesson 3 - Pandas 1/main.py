#titanic dataset - https://drive.google.com/file/d/14b7_hSbbGISLX1YLe6zudyU-M0-PTmfX/view?usp=sharing

import pandas as pd

# Create a dataFrame from scratch to relate a dataFrame with a dictionary
df=pd.DataFrame({
    "Name":["Sana","Sindhuja","A","B","C","D","E"],
    "Age":[15,26,12,34,23,45,12],
    "City":["Fremomt","Madurai","x","y","z","q","r"]
})

# Show the number of rows in the head could be limited by passing a number in head
print(df.head())
print(df.shape)
# Show the way of accessing the column is same as that as of a dictionary
print(df["Name"])
# Also all numpy operations are applicable to the column (pd.Series)
print(df["Age"].max())
print(type(df["Age"]))
print(df["Age"].shape)

# Gives the typical summary of the data
print(df.info())
# Gives the important calculations on the numerical columns
print(df.describe())

# Loading the data from a file
data = pd.read_csv("titanic.csv")
print(data.head())
print(data.info())
# Prints the datatypes of each column
print(data.dtypes())

# Selecting multiple columns together
nameAndAge = data[["Name", "Age"]]

print(nameAndAge.head())
print(nameAndAge.shape)


# Filtering out rows
above35 = data[data["Age"] > 35]
print(above35.head())
print(above35.shape) # To confirm the number of rows, open the csv in excel and filter on the same column

# Combining multiple conditions together
class2And3 = data[data["Pclass"].isin([2, 3])]
print(class2And3[["Name", "Pclass"]].head())
print(class2And3.shape)

# Combining condition by OR (|), by AND (&) 
class2And3 = data[(data["Pclass"] == 2) | (data["Pclass"] == 3)] 
print(class2And3[["Name", "Pclass"]].head())
print(class2And3.shape)

# Task - Get the mean fare of Male travelling in Pclass 1

maleFirstClass = data[(data["Sex"] == "male") & (data["Pclass"] == 1)]
print("The mean age of male first class passenger is", maleFirstClass["Fare"].mean())

# Repeat for other 5 combinations namely
# femaleFirstClass
# maleSecondClass
# femaleSecondClass
# maleThirdClass
# femaleThirdClass





