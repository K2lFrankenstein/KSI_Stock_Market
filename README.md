# Stock Market Prediction using ARIMA

## Abstract
The purpose and essence of Time Series Analysis is to provide the right information at the right time for better insights. This project uses a complex algorithm, specifically the ARIMA model, to find trends in market values and make predictions, helping investors make informed decisions.

## Introduction

### What is Time Series Analysis?
Time series analysis is a method of analyzing data points collected or recorded at specific time intervals. It helps in understanding how the data points evolve over time, making it crucial for forecasting future data points.

### Why Use Time Series Analysis?
Organizations use time series analysis to understand trends and patterns over time, which can be used for forecasting future events. This analysis is widely used in finance, economics, weather forecasting, and many other fields.

## Objective
The objective of this project is to make meaningful insights and help users make informed investment decisions.

## Tools and Technologies

- **Tools**: Visual Studio Code, Google Collaboratory, GitHub, Quandl API
- **Languages**: Python, HTML, CSS, JavaScript
- **Framework**: Django
- **Database**: MySQL, SQLite3
- **Libraries**: Asgiref, autopep8, Django, Pycodestyle, Pytz, Sqlparse, Unipath, dj-database-url, python-decouple, whitenoise, Quandl, Pmdarima, Sklearn, Statsmodels, Matplotlib, Plotly

## Program Analysis

### Program Planning
The program is divided into three main pipelines:
1. Search Module
2. Fetching Data using API Call
3. ARIMA Model Fitting and Prediction

### Problem Identification
The base ARIMA model used here is not optimized for seasonality in the data. Each time data is received, a seasonality check must be performed to ensure accurate predictions.


## System Design
![image](https://github.com/K2lFrankenstein/KSI_Stock_Market/assets/68675641/04715443-7a63-463a-80e0-da3e494914c2)


## Implementation: Pipeline for ARIMA Model

1. **Load the Data**: Load the dataset into the notebook.
2. **Pre-processing**: Transform the data as needed.
3. **Make Series Stationary**: Check and make the series stationary.
4. **Determine d-value**: Number of times differencing operation was performed.
5. **Create ACF and PACF Plots**: Determine the input parameters for ARIMA.
6. **Fit ARIMA Model**: Using the processed data and parameter values.
7. **Predict Values**: Make predictions on the validation set.
8. **Calculate RMSE**: Check the model performance.


![image](https://github.com/K2lFrankenstein/KSI_Stock_Market/assets/68675641/e2e257cf-bc15-40be-8841-138f62efd135)


## Using Auto ARIMA
Auto ARIMA simplifies the steps of implementing an ARIMA model by eliminating the need for manually making the series stationary and selecting p, d, and q values.

## Evaluation
We evaluate the ARIMA model by preparing it on a training dataset and evaluating predictions on a test dataset.

## Limitations and Future Extensions

### Limitations
- Computation takes longer for larger datasets.
- Not optimized for seasonal data.
- Limited features in the web application.

### Future Work
- Data analysis for seasonal data.
- Data formatting for better predictions.
- Improved computation time with better modeling and computational power.
- Additional features and functionalities.

## Conclusion
Time series analysis, especially using ARIMA models, is a powerful tool for forecasting and understanding trends over time. This project aims to provide insightful predictions to help users make informed investment decisions.

## References
- [Django Documentation](https://docs.djangoproject.com/en/3.2/)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [Plotly](https://plotly.com/)
- [GitHub](https://github.com/)
- [Pmdarima](https://pypi.org/project/pmdarima/)
- [Machine Learning Plus](https://www.machinelearningplus.com/time-series/arima-model-time-series-forecasting-python/)

## Screenshots

### Login Page
![image](https://github.com/K2lFrankenstein/KSI_Stock_Market/assets/68675641/750c7b1f-aade-40a6-b76c-1d673b10fb2e)


### Home Page
![image](https://github.com/K2lFrankenstein/KSI_Stock_Market/assets/68675641/3c77c4d1-7ad7-41bc-b499-ef25fb675ad8)


### Line Chart
![image](https://github.com/K2lFrankenstein/KSI_Stock_Market/assets/68675641/94afa00e-37f0-4d33-84a9-22c2c9a2a315)


### Histogram
![image](https://github.com/K2lFrankenstein/KSI_Stock_Market/assets/68675641/04abf040-d6d8-4f68-9ac2-8e9b9363ac88)

### Rolling Mean and Standard Deviation
![image](https://github.com/K2lFrankenstein/KSI_Stock_Market/assets/68675641/35aedfe1-0a09-453b-b15a-5313272911ab)

### Prediction
![image](https://github.com/K2lFrankenstein/KSI_Stock_Market/assets/68675641/36b3b42a-8def-445f-ab19-5127f6bd55df)

### Seasonal Decomposition
![image](https://github.com/K2lFrankenstein/KSI_Stock_Market/assets/68675641/16bf2555-48ba-4497-85fa-2265a13ef4f3)

### Model Diagnostics
![image](https://github.com/K2lFrankenstein/KSI_Stock_Market/assets/68675641/ac021447-f47b-49ab-9c56-e53a44324431)
