import quandl 
import csv
import pandas as pd
# quandl config


#github config
# g = Github("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")
# repo = g.get_user().get_repo('test')
# fetching data from api
#  df.to_json(r'D:\psudo_desktop\KSI\data.json',orient="table")
#Prepare files to upload to GitHub
#files = ['D:\psudo_desktop\KSI\data.json']
# Make a commit and push
# commit_message =
# repo.commit(files)
# origin = repo.remote('origin')
# origin.push()
# code = BSE/ BSE.....

# mydict = {}
# with open('BSE_metadata.csv', mode='r') as inp:
#     reader = csv.reader(inp)
#     dict_from_csv = {rows[1]:rows[0] for rows in reader}

# print(dict_from_csv) 

def getdata():
    # quandl.ApiConfig.api_key = 'RATUYxBwY63sVF7F8PBQ'
    # dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
    print("getting data PLz wait........")
    # data = quandl.get(code,start_date='2015-01-01')
    data = pd.read_csv("data.csv")
    
    # df = pd.DataFrame(data, columns = ['Date','Open','High','Low','Close'])
    print(data.head())
    print("Data fetched successfully.......")
    return data

if __name__ == '__main__' :
    print("Populating the data please wait")
    # code = input("enter  :")
    getdata()
    print(" not populating completed")   