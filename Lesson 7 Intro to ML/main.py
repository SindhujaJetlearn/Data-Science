# Data Preprocessing Tools
#pip install scikit-learn 

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
print(dataset.info())
print()

#Identify the features and Target.
#Target - wheather purchased or not
#Feature - country, age, salary
X = dataset.iloc[:, :-1].values #picked all expect last column
y = dataset.iloc[:, -1].values #picked last column
print("Features :\n",X)
print("Target :\n ",y)
print()

# Taking care of missing data - either remove it or replace it with appropritate value
#SimpleImputer - replaces missing values with someother value
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
#Transform the data for the entire dataset (age and salary alone)
#imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.fit_transform(X[:, 1:3])
print("After Imputing :\n",X)
print()

# Encoding categorical data to numerical value (ex : Replacing Country names with 0,1 and 2)
# Encoding the Independent Variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

#on the 0th column- country
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = pd.DataFrame(ct.fit_transform(X))
print("One hot encoding :\n ", X)
print()

# Encoding the Dependent Variable - Target has to be 1D so shouldnt use encoder
from sklearn.preprocessing import LabelEncoder 
#Yes - 1 and No - 0
le = LabelEncoder()
y = le.fit_transform(y)
print("Label Encoder :\n ", y)
print()

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)
print("Xtrain : \n",X_train)
print("Xtest : \n ",X_test)
print()

print("Ytrain : \n",y_train)
print("Xtest : \n ",y_test)
print()

# Feature Scaling - age and salary (trying to scale down as sys wll get affected with huge variation in the values)
#StandardScaler=(x-mean)/stdev (values will range from -1 to 1 with mean to be 0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train.iloc[:, 1:3] = sc.fit_transform(X_train.iloc[:, 1:3])
X_test.iloc[:, 1:3] = sc.transform(X_test.iloc[:, 1:3])

print("After scaling the values from -1 to 1 :\n ")
print(X_train)
print(X_test)
















