import pandas as pd
data = pd.read_csv("titanic.csv")

# Get the particular column out of a condition
adult_names = data.loc[data["Age"] > 18, "Name"]
print(adult_names)

#Slicing - Same as numpy 2D slicing
# The first index is for rows and the second is for columns
#last number is exclusive
print(data.iloc[9:25, 2:5])

# Changing the value in the dataset
data.iloc[0:3, 2] = "Sindhuja"
print(data.iloc[0:3, 2])

# Save the data to local to verify changes
data.to_csv("changedData.csv")

# Creating a new column in the dataFrame
data["Test"] = data["Fare"] + 2
data["Test2"] = data["Fare"] * data["Pclass"]
print(data.head())


# Renaming the column names
data_renamed = data.rename(
    columns = {
        "Pclass": "Passenger Class",
    }
)

print(data_renamed.info())


# Performing mathematical operation on multiple columns together
print(data["Age"].mean())

print(data[["Age", "Fare"]].mean())


print(data.agg({
    "Age": ["min", "max", "median"],
    "Fare": ["min", "max"]
}))

# Group by data categorically

print(data[["Sex", "Age"]].groupby("Sex").mean())

print(data.groupby("Sex")["Age"].mean())

# Task - Get the mean fare for each of sex and passenger class combination
print(data.groupby(["Sex", "Pclass"])["Fare"].mean())


# Get the count of rows in each category
print(data["Pclass"].value_counts())

# Sorting the data
a = data.sort_values(by = "Age")
print(a[["Name","Age"]])

b = data.sort_values(by = "Age",ascending=False)
print(b[["Name","Age"]])

# Operations on Text Data
data["NameLowercase"] = data["Name"].str.lower()
print(data.head())

data["Sex_short"] = data["Sex"].replace({"male": "M", "female": "F"})
print(data.head())
