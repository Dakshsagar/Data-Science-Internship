# Import seaborn
import seaborn as sns
import pandas as pd


# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a visualization
sns.relplot(           # designed to visualize many different statistical relationships.
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size"
)

'''Statistical analyses require knowledge about the distribution of variables in your dataset.
The seaborn function displot() supports several approaches to visualizing distributions.
These include classic techniques like histograms and computationally-intensive approaches like kernel density estimation:'''
sns.displot(data=tips, x="total_bill", col="time", kde=True)

#Reading the iris data set and performing instructions

df=pd.read_csv("Iris.csv")
print(df)

print(df.shape)

print(df.head())
print(df.tail())

print(df.loc[df["Species"] == "Iris-setosa"]) #The “loc” functions use
#the index name of the row to display the particular row of the dataset.

print(df["Species"].value_counts())  #The value_counts() function,
#counts the number of times a particular instance or data has occurred.

print(df.describe()) #to view basic statistical details of a data frame or a series of numeric values



#Calculating sum mean median
sum_data = df["SepalLengthCm"].sum()
mean_data = df["SepalLengthCm"].mean()
median_data = df["SepalLengthCm"].median()

print("Sum:", sum_data, "\nMean:", mean_data, "\nMedian:", median_data)


#Minimum and Maximum
min_data = df["SepalLengthCm"].min()
max_data = df["SepalLengthCm"].max()

print("Minimum:", min_data, "\nMaximum:", max_data)

#steps for handling the data set
# Loading the Data: The data is loaded into a DataFrame and printed to verify its contents.
# Handling Missing Values: Missing values in the 'Age' and 'Salary' columns are filled with the mean and median respectively,
# and the DataFrame is printed to confirm the changes.
# Converting Data Types: The data types of 'Age' and 'Salary' columns are converted to numeric if they aren't already,
# and the data types are printed to confirm.
# Normalizing Values: The 'Age' and 'Salary' columns are normalized using Min-Max scaling,
# and the DataFrame is printed to verify the normalized values.
from sklearn.preprocessing import MinMaxScaler

# Step 1: Load the Data
df = pd.read_csv('Data.csv')
print("Initial DataFrame:")
print(df)

# Step 2: Handle Missing Values
print("\nMissing values before handling:")
print(df.isnull().sum())

# Fill missing Age with mean age
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill missing Salary with median salary
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

print("\nDataFrame after handling missing values:")
print(df)

# Step 3: Convert Data Types
# Ensure that Age and Salary columns are of numeric type.
df['Age'] = pd.to_numeric(df['Age'])
df['Salary'] = pd.to_numeric(df['Salary'])

print("\nData types after conversion:")
print(df.dtypes)

# Step 4: Normalize/Scale Numerical Values
scaler = MinMaxScaler()

# Normalize Age and Salary
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

print("\nDataFrame after normalization:")
print(df)

# Sample data
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = {
    'Name': ['John', 'Jane', 'Doe', 'Alice', 'Bob'],
    'Age': [28, 35, None, 30, 25],
    'Salary': [50000, None, 40000, 70000, 45000],
    'Department': ['IT', 'HR', 'Marketing', 'IT', 'HR']
}

df = pd.DataFrame(data)

# Fill missing Age with mean age
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill missing Salary with median salary
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

# Convert Age and Salary to numeric types if they are not already
df['Age'] = pd.to_numeric(df['Age'])
df['Salary'] = pd.to_numeric(df['Salary'])

# Normalize Age and Salary
scaler = MinMaxScaler()
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

# Convert the Department column into dummy variables
df = pd.get_dummies(df, columns=['Department'], prefix='Dept')
# pd.get_dummies: Converts categorical variable(s) into dummy/indicator variables.
# columns=['Department']: Specifies the column to be converted.
# prefix='Dept': Adds a prefix to the new dummy variable columns for clarity.
# This transformation creates new binary columns for each unique value in the 'Department' column,
# making the data suitable for machine learning algorithms that require numerical input.
print(df)


####ExpRemaining####

#Binarisation
# In the below example, we used threshold value = 0.5 and that is why, all the values
# above 0.5 would be converted to 1, and all the values below 0.5 would be converted to 0.
import numpy as np
from sklearn import preprocessing
Input_data = np.array([[2.1, -1.9, 5.5],
 [-1.5, 2.4, 3.5],
 [0.5, -7.9, 5.6],
 [5.9, 2.3, -5.8]])
data_binarized = preprocessing.Binarizer(threshold=0.5).transform(Input_data)
print("\nBinarized data:\n", data_binarized)
#in this we have used sklearn preprocessing function and transformed the Input_data, setting the threshhold for 0.5.

#Mean Removal
input_data = np.array([[2.1, -1.9, 5.5],

 [-1.5, 2.4, 3.5],
 [0.5, -7.9, 5.6],
 [5.9, 2.3, -5.8]])
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print ("\nMin max scaled data:\n", data_scaled_minmax)

#displaying the mean and the standard deviation of the input data
print("Mean =", input_data.mean(axis=0))
print("Stddeviation = ", input_data.std(axis=0))
#Removing the mean and the standard deviation of the input data
data_scaled = preprocessing.scale(input_data)
print("Mean_removed =", data_scaled.mean(axis=0))
print("Stddeviation_removed =", data_scaled.std(axis=0))

#Scaling

data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print ("\nMin max scaled data:\n", data_scaled_minmax)

#l1 Normalisation
data_normalized_l1 = preprocessing.normalize(input_data, norm='l1')
print("\nL1 normalized data:\n", data_normalized_l1)

#l2 Normalisation
data_normalized_l2 = preprocessing.normalize(input_data, norm='l2')
print("\nL2 normalized data:\n", data_normalized_l2)

#Storing datasets into dataframes
from sklearn.datasets import fetch_openml  #fetch openml functionality
df=fetch_openml('titanic',version=1,as_frame=True)['data']
df.info()


####ExpRemaining####


# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values   #integer location based indexing
y = dataset.iloc[:, -1].values    #selecting rows and columns by their integer position
#This line selects all the columns except the last one
#(which typically contain the features or predictors in the dataset) and stores them in X as a NumPy array.

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Data Preprocessing Tools

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(X)
print(y)

# Taking care of missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
print(X)

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
print(X)
# Encoding the Dependent Variable
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print(y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)
print(X_train)
print(X_test)
print(y_train)
print(y_test)




