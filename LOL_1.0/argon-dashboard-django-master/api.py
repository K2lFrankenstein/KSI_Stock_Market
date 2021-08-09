import quandl 
import pandas as pd
from github import Github
# quandl config
quandl.ApiConfig.api_key = 'RATUYxBwY63sVF7F8PBQ'
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')

#github config

g = Github("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")
repo = g.get_user().get_repo('test')

# fetching data from api
data = quandl.get('BSE/BOM500057')
df = pd.DataFrame(data, columns = ['Open','High','Low','Close'])
df.to_json(r'D:\psudo_desktop\KSI\data.json',orient="table")

# Prepare files to upload to GitHub
files = ['D:\psudo_desktop\KSI\data.json']

# Make a commit and push
commit_message =
repo.commit(files)
origin = repo.remote('origin')
origin.push()
