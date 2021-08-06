import quandl 
import pandas as pd
quandl.ApiConfig.api_key = 'RATUYxBwY63sVF7F8PBQ'
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
data = quandl.get('BSE/BOM500180')
print(data)