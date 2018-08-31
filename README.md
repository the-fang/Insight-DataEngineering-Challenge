# Insight-DataEngineering-Challenge

### Challenge:

Finding the average error values between the actual stock prices and predicted values for a sliding window of specified size.

### Programming Language Used:

Python 3.6

### Packages used:

No external packages were used

### Funtions and Approach:

The program typically uses nested dictionaries for comparision and matching of stock price and stock id respectively.
There are a total of 4 functions in this program:

#### 1) reader(n):

This function reads the lines of input files, strips them of \n characters and splits them at the occurence of pipeline.  
It takes file name as input.
Returns a list of lists.

#### 2) nested_Dict(list,max):

This function converts the nested list into a nested dictionary in the form {1:{"Stock_ID1": Value1,...},2:{"Stock_ID2": Value2,...},...}.
It takes a nested list(like the one returned above) and the highest time(Integer Value) of the predictions.
Returns a nested dictionary.

#### 3) error_List(a,b,max):

This function generates a error list of lists, where each list comprises of difference of stock prices for a give time hour.
It takes the nested dictionaries of actual values and predicted values and the max value.
Returns the error list.

#### 4) average_Error(a,window,max):

This function calculates the average error and prints to output file.
It takes the error list generated in previous function, sliding window width, and max value.
Writes to the output file comparison.txt.

