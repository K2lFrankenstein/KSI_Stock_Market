import quandl 
import csv
import pandas as pd
# quandl config


def getdata(code):
    quandl.ApiConfig.api_key = "YOUR API KEY"
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
    print("getting data PLz wait........")
    data = quandl.get(code,start_date='2015-01-01')
    
    print(data.head())
    print("Data fetched successfully.......")
    return data

if __name__ == '__main__' :
    print("Populating the data please wait")
    getdata(code)
    print(" not populating completed")   
