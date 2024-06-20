#creating arrays using pythondataset list and tupple

import numpy as np
arr= np.array([1,2,3])
print(arr)
#printing differents aspects of array

#printing type of array
print('The type of array is:',type(arr))

#printing the dimension of array
print("The dimension of array is:",arr.ndim)

#Shape of the array
print("The shape of array is:",arr.shape)

#Size of the array
print("The size of the array is:",arr.size)

#Type of elements in the array
print("The type of elemnts are:",arr.dtype)

#2-Dimension array

arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)
#printing differents aspects of array

#printing type of array
print('The type of array is:',type(arr2))

#printing the dimension of array
print("The dimension of array is:",arr2.ndim)

#Shape of the array
print("The shape of array is:",arr2.shape)

#Size of the array
print("The size of the array is:",arr2.size)

#Type of elements in the array
print("The type of elemnts are:",arr2.dtype)

#Creatinga array from tupple
arrtup = np.array((1,5,6))
print("\nThis the array created by tupple\n",arrtup)

#creating an array and copying it
arrog = np.array([1,2,3,6,8,3,5])
arrcpy = arrog.copy()

#og and cpy have different id
print("id of arrog is:",id(arrog))
print("id of arrcpy is:",id(arrcpy))

#changes in original array does not affect its copy

arrog[1]= 36
#printing both arrays
print(arrog)
print(arrcpy)

#defining functions
#parameters :Input array
def sum(array):
#set variable for final answer
    sum=0
#parse through array
    for i in array:
        sum +=i
    return sum
testarray = [1,2,3,4,5,6,7,8,9]

#use function sum
print("\nThe sum of the array is\n"+ str(sum(testarray)))

#Creating a set of integers from 10 to 1 with a step of -2
a =np.arange(10,1,-2)
print("A array from 10 to 1 with a step of -2:\n",a)

#Creating a set of integers from 1 to 100 with a step of 5
b =np.arange(1,100,5)
print("A array from 1 to 100 with a step of 5:\n",b)

#Index are specified in the np.array method
newarr= b[np.array([4,5,6])]
print("\nThe elements on these indices are:\n",newarr)

#various types of ways to print array using indexes
narray = np.array([1,7,5,3,4,6,8])

print(narray[1:5])
#In this the element on 1 index to element till 4 index will printed the element on index 5 is excluded

print(narray[4:])
#In this the elements after 4th index will be printed including element on the 4th index

print(narray[:4])
#In this the elements before the 4th index will be printed excluding the element on 4th index

print(narray[-4:-1])
#In this the elements are indexed from negative and we go from right to left right most index is -1 and then normal rules are apllied

print(narray[1:6:2])
#In this the elements are printed by steping up 2 indexes

print(narray[::2])
#In this the elements will bre printed by stepping up index by 2


#various types of ways to print 2 dimensional array using indexes
arr3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print("\n\n")

print(arr3[1, 1:4])
#in this the second row will be printed from index 1 to 4

print(arr3[0:2, 2])
#in this the first row will be printed from index 0 to 2

print(arr3[0:2, 1:4])
#in this the both rows are printed from 0 to 2 and 1 to 4


#the copy of the array does not reflect any changes but if use view function the changes will be seen
#copy
arr69 = np.array([1, 2, 3, 4, 5])
x1 = arr69.copy()
arr[0] = 42
print(arr69)
print(x1)

#view
arr70 = np.array([1, 2, 3, 4, 5])
x2 = arr70.view()
arr70[0] = 369
print(arr)
print(x2)

#changes made to view does affect the original array
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31
print(arr)
print(x)

# Check if Array Owns its Data
# copies owns the data, and views does not own the data, but how can we check this?
#Every NumPy array has the attribute base that returns None if the array owns the data.
#Otherwise, the base  attribute refers to the original object.

arr12 = np.array([1, 2, 3, 4, 5])
x = arr12.copy()
y = arr12.view()
print(x.base)
print(y.base)


#printing the shape of array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)


# Create an array with 5 dimensions using ndmin
#using a vector with values 1,2,3,4 and verify that last dimension has value 4:

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)


#In this we convert the following 1-D array with 12 elements into a 2-D array.

#The outermost dimension will have 4 arrays, each with 3 elements:
arr13 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr1 = arr13.reshape(4, 3)

print(newarr1)

#The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:
newarr2 = arr13.reshape(2, 3, 2)
print(newarr2)


# Python code to demonstrate matrix operations
# add(), subtract() and divide()
# initializing matrices
x = np.array([[1, 2], [4, 5]])
y = np.array([[7, 8], [9, 10]])

# using add() to add matrices
print ("The element wise addition of matrix is : ")
print (np.add(x,y))

# using subtract() to subtract matrices
print ("The element wise subtraction of matrix is : ")
print (np.subtract(x,y))

# using divide() to divide matrices
print ("The element wise division of matrix is : ")
print (np.divide(x,y))


#panda library

import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

#The version string is stored under __version__ attribute.
print(pd.__version__)

#A Pandas Series is like a column in a table.
#It is a one-dimensional array holding data of any type.

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
#If nothing else  is specified, the values are labeled with their index number.
#First value has index 0, second value has index 1 etc.
#This label can be used to access a specified value.
#Return the first value of the Series:

print(myvar[0])

#In this we have changed the index values or we can say we have specified the index values

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

print(myvar["y"])

#A pandas DataFrame is like a 2-D datastructure just like an 2-D array or a table with columns and rows

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#loading the data into a DataFrame object named df:
df = pd.DataFrame(data)
print("\n",df)

#Pandas use the loc attribute to return one or more specified row(s)
#referring to the row index:
print("\n",df.loc[0])
#Returns a pandas series

#use a list of indexes:
print("\n",df.loc[[0, 1]])
#When using [], the result is a Pandas DataFrame.

# here the csv file is loaded using the pd.read_csv('') function
df = pd.read_csv('data.csv')
#to_string() this function is used to print the entire dataframe
print("\n",df.to_string())
#If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows
print(pd.options.display.max_rows)
#The number of rows returned is defined in Pandas option settings.
#You can check your system's maximum rows with the pd.options.display.max_rows statement.
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df)
print(pd.options.display.max_rows)
#here we modified the number of maximum rows

#Creating a dataframe using dictionary
#Load a Python Dictionary into a DataFrame   JSON= Python Dictionary
import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df)


#here we wil create two dataframes and join them
# creating the first DataFrame

df1 = pd.DataFrame({"fruit" : ["apple", "banana", "avocado"],
                    "market_price" : [21, 14, 35]})
print("The first DataFrame")
print(df1)

# creating the second DataFrame
df2 = pd.DataFrame({"fruit" : ["banana", "apple", "avocado"],
                    "wholesaler_price" : [65, 68, 75]})
print("The second DataFrame")
print(df2)

# joining the DataFrames
print("The merged DataFrame")
df3= pd.merge(df1, df2, on = "fruit", how = "inner")
#hwere using the pd.merge() function is used to join the coloumns in data frame
print(df3)
# how : {‘left’, ‘right’, ‘outer’, ‘inner’}, default ‘inner’

#different examples for merging with different number of elements

# creating the first DataFrame
df1 = pd.DataFrame({"fruit" : ["apple", "banana",
                               "avocado", "grape"],
                    "market_price" : [21, 14, 35, 38]})
("The first DataFrame")
print(df1)

# creating the second DataFrame
df2 = pd.DataFrame({"fruit" : ["apple", "banana", "grape"],
                    "wholesaler_price" : [65, 68, 71]})
print("The second DataFrame")
print(df2)

# joining the DataFrames
# here both common DataFrame elements are in df1 and df2,
# so it extracts apple, banana, grapes from df1 and df2.
print("The merged DataFrame")
df1= pd.merge(df1, df2, on = "fruit", how = "inner")
print(df1)
print(pd.merge(df1, df2, on = "fruit", how = "outer"))






