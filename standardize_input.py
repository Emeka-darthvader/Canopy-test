import pandas as pd 

#Function to standardize date format
#Input- This function takes the dataframe value for date (date)
#Output- This function returns the formatted date  (date)
def standardize_date(date):
    date = pd.to_datetime(date)
    date = date.dt.strftime('%Y/%m/%d')
    return date

#Function to standardize numbers
#Input - This function takes the dataframe value for number (number).
######- It also provides an argument for symbol which can help to trim the currency if need be
#Output - This function returns the formatted number (number)
def standardize_number(number,symbol='$'):
    number = number.str.replace(',','')
    number = number.str.replace(symbol,'')
    return number



