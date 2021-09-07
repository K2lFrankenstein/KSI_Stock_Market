# pip install pmdarima

# pip install quandl


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import math
import numpy as np
import plotly
import plotly.express as px
import plotly.graph_objects as go

import plotly.offline as pof
import quandl

# quandl.ApiConfig.api_key = 'RATUYxBwY63sVF7F8PBQ'
# dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
# data = quandl.get('BSE/BOM500325')
data = pd.read_csv('data.csv')

data = data.reset_index()



# Line chart - Close
fig = px.line(data, x="Date", y="Close", title="Closing price")
pof.plot(fig,filename='Linechart-Close')


# Histogram - Clsoe
fig = px.histogram(data, x="Date", y="Close")
pof.plot(fig,filename='Histogram-Clsoe')

# from statsmodels.tsa.stattools import adfuller
# def test_stationarity(timeseries):
#     #Determing rolling statistics
#     rolmean = timeseries.rolling(12).mean()
#     rolstd = timeseries.rolling(12).std()
#     #Plot rolling statistics:
#     plt.plot(timeseries, color='yellow',label='Original')
#     plt.plot(rolmean, color='red', label='Rolling Mean')
#     plt.plot(rolstd, color='black', label = 'Rolling Std')
#     plt.legend(loc='best')
#     plt.title('Rolling Mean and Standard Deviation')
#     plt.show(block=False)
#     print("Results of dickey fuller test")
#     adft = adfuller(timeseries,autolag='AIC')
#     # output for dft will give us without defining what the values are.
#     #hence we manually write what values does it explains using a for loop
#     output = pd.Series(adft[0:4],index=['Test Statistics','p-value','No. of lags used','Number of observations used'])
#     for key,values in adft[4].items():
#         output['critical value (%s)'%key] =  values
#     print(output)

# test_stationarity(data['Close'])


# Claculating rolmean and rolstd
rolmean = list(data['Close'].rolling(12).mean())
rolstd = list(data['Close'].rolling(12).std())
# print(rolmean)
# print(rolstd)

dataf = data
dataf['Rolmean'] = rolmean
dataf['Rolstd'] = rolstd

dataf = dataf.drop(['Open', 'High', 'Low', 'WAP','No. of Shares','No. of Trades',	'Total Turnover',	'Deliverable Quantity',	'% Deli. Qty to Traded Qty', 'Spread H-L', 'Spread C-O'],axis=1)
# dataf.head(5)


# Rolling mean and Standard deviation 
trace0 = go.Scatter(
  x = dataf.Date,
  y = dataf.Close,
  mode = 'lines',
  name = 'Close')

trace1 = go.Scatter(
  x = dataf.Date,
  y = dataf.Rolmean,
  mode = 'lines',
  name = 'Rolmean')

trace2 = go.Scatter(
  x = dataf.Date,
  y = dataf.Rolstd,
  mode = 'lines',
  name = "Rolstd")

df = [trace0, trace1, trace2]
layout = go.Layout(title = "Rolling Mean and Standard Deviation")
figure = go.Figure(data = df, layout = layout)
pof.plot(figure,filename='RM-SD')


df_close = data['Close']
result = seasonal_decompose(df_close, model='multiplicative', freq = 30)
fig = result.plot()  
fig.set_size_inches(16, 9)
pof.plot(fig,filename='seadec')


# train_data, test_data = df_log[3:int(len(df_log)*0.9)], df_log[int(len(df_log)*0.9):]
# plt.figure(figsize=(10,6))
# plt.grid(True)
# plt.xlabel('Dates')
# plt.ylabel('Closing Prices')
# plt.plot(df_log, 'green', label='Train data')
# plt.plot(test_data, 'blue', label='Test data')
# plt.legend()

# model_autoARIMA = auto_arima(train_data, start_p=0, start_q=0,
# test='adf',       # use adftest to find optimal 'd'
# max_p=3, max_q=3, # maximum p and q
# m=1,              # frequency of series
# d=None,           # let model determine 'd'
# seasonal=False,   # No Seasonality
# start_P=0, 
# D=0, 
# trace=True,
# error_action='ignore',  
# suppress_warnings=True, 
# stepwise=True)
# print(model_autoARIMA.summary())

# model_autoARIMA.plot_diagnostics(figsize=(15,8))
# plt.show()

# model = ARIMA(train_data, order=(0,1,1))
# fitted = model.fit(disp=-1)
# print(fitted.summary())

# # Forecast

# fc, se, conf = fitted.forecast(742, alpha=0.05)  # 90% confidence

# fc_series = pd.Series(fc, index=test_data.index)
# lower_series = pd.Series(conf[:, 0], index=test_data.index)
# upper_series = pd.Series(conf[:, 1], index=test_data.index)
# plt.figure(figsize=(12,5), dpi=100)
# plt.plot(train_data, label='training')
# plt.plot(test_data, color = 'blue', label='Actual Stock Price')
# plt.plot(fc_series, color = 'orange',label='Predicted Stock Price')
# plt.fill_between(lower_series.index, lower_series, upper_series, color='k', alpha=.10)
# plt.title('Stock Price Prediction')
# plt.xlabel('Time')
# plt.ylabel('Actual Stock Price')
# plt.legend(loc='upper left', fontsize=8)
# plt.show()
# plt.savefig('books_read.png')