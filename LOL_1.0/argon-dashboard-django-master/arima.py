import os
import warnings

from requests.models import codes
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from pylab import rcParams
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
import pmdarima as pm
from pmdarima.arima import auto_arima
from sklearn.metrics import mean_squared_error, mean_absolute_error
import math
import numpy as np
from statsmodels.tsa.stattools import adfuller
from api import getdata
from fill import getcode
import plotly
import plotly.express as px
import plotly.graph_objects as go

import plotly.offline as pof
import quandl

def arima_fun():

    # code = 'BSE/BOM500002'
    data = getdata()
    smort = math.ceil(len(data)*0.05)

    def test_stationarity(timeseries):
        #Determing rolling statistics
        rolmean = timeseries.rolling(12).mean()
        rolstd = timeseries.rolling(12).std()
    
        print("Results of dickey fuller test")
        adft = adfuller(timeseries,autolag='AIC')
        # output for dft will give us without defining what the values are.
        # hence we manually write what values does it explains using a for loop
        output = pd.Series(adft[0:4],index=['Test Statistics','p-value','No. of lags used','Number of observations used'])
        for key,values in adft[4].items():
            output['critical value (%s)'%key] =  values
        print(output)

    test_stationarity(data['Close'])

    df_log = np.log(data['Close'])
    train_data, test_data = df_log[:int(len(df_log)*0.95)], df_log[int(len(df_log)*0.95):]

    model_autoARIMA = auto_arima(train_data, start_p=0, start_q=0,
    test='adf',       # use adftest to find optimal 'd'
    max_p=5, max_q=5, # maximum p and q
    m=1,              # frequency of series
    d=None,           # let model determine 'd'
    seasonal=False,   # No Seasonality
    start_P=0, 
    D=0, 
    trace=True,
    error_action='ignore',  
    suppress_warnings=True)

    x=str(model_autoARIMA)
    p = int(x[7]) 
    d =int(x[9])
    q =int(x[11])
    model_autoARIMA.plot_diagnostics(figsize=(15,8))
    plt.savefig('Graphs/Diagnostics.png')
    model = ARIMA(train_data, order=(p, d, q))
    fitted = model.fit(disp=-1)
    
    fc, se, conf = fitted.forecast(smort, alpha=0.05)  # 95% confidence
    fc_series = pd.Series(fc, index=test_data.index)
    lower_series = pd.Series(conf[:, 0], index=test_data.index)
    upper_series = pd.Series(conf[:, 1], index=test_data.index)
    plt.figure(figsize=(12,5), dpi=100)
    plt.plot(train_data, label='training')
    plt.plot(test_data, color = 'blue', label='Actual Stock Price')
    plt.plot(fc_series, color = 'orange',label='Predicted Stock Price')
    plt.fill_between(lower_series.index, lower_series, upper_series, color='k', alpha=.10)
    plt.title('Stock Price Prediction')
    plt.xlabel('Time')
    plt.ylabel('Actual Stock Price')
    plt.legend(loc='upper left', fontsize=8)
    plt.savefig('Graphs/Prediction.png')   

def graphs_fun():

    # code = 'BSE/BOM500002'
    data = getdata()
    # graph_data = data.reset_index()
    # print(graph_data)
    graph_data = data

    # Line chart - Close
    fig = px.line(graph_data, x="Date", y="Close", title="Closing price")
    pof.plot(fig,filename='Graphs/graphs/Linechart-Close.html')

    # Histogram - Clsoe
    fig = px.histogram(graph_data, x="Date", y="Close")
    pof.plot(fig,filename='Graphs/graphs/Histogram-Close.html')

    # Claculating rolmean and rolstd
    rolmean = list(graph_data['Close'].rolling(12).mean())
    rolstd = list(graph_data['Close'].rolling(12).std())
    # print(rolmean)
    # print(rolstd)

    dataf = graph_data
    dataf['Rolmean'] = rolmean
    dataf['Rolstd'] = rolstd

    dataf = dataf.drop(['Open', 'High', 'Low', 'WAP','No. of Shares','No. of Trades','Total Turnover','Deliverable Quantity','% Deli. Qty to Traded Qty', 'Spread H-L', 'Spread C-O'],axis=1)
    # Rolling mean and Standard deviation 
    trace0 = go.Scatter(x = dataf.Date, y = dataf.Close, mode = 'lines', name = 'Close')

    trace1 = go.Scatter(x = dataf.Date, y = dataf.Rolmean, mode = 'lines', name = 'Rolmean')

    trace2 = go.Scatter(x = dataf.Date, y = dataf.Rolstd, mode = 'lines', name = 'Rolstd') 

    df = [trace0, trace1, trace2]
    layout = go.Layout(title = "Rolling Mean and Standard Deviation")
    figure = go.Figure(data = df, layout = layout)
    pof.plot(figure,filename='Graphs/graphs/RM-SD.html')

    df_close = graph_data['Close']
    result = seasonal_decompose(df_close, model='multiplicative', freq = 30)
    fig = result.plot()
    # fig.set_size_inches(16, 9)
    # fig.show()
    plt.savefig('Graphs/seasonal_decompose.png')   


if __name__ == '__main__' :
    print("calling arima")
    arima_fun()
    print(" calling graph")
    graphs_fun()
    print("successfully called evrything!!!")