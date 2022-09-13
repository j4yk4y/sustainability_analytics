import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error
import numpy as np
from pmdarima.arima import auto_arima
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import warnings
warnings.filterwarnings("ignore")
sns.set()

def monthToNum(shortMonth):
    return {
        'Januar': 1,
        'Februar': 2,
        'Maerz': 3,
        'April':4,
        'Mai':5,
        'Juni':6,
        'Juli':7,
        'August':8,
        'September':9,
        'Oktober':10,
        'November':11,
        'Dezember':12
    }[shortMonth]

def check_stationarity(ts):
    dftest = adfuller(ts)
    adf = dftest[0]
    pvalue = dftest[1]
    critical_value = dftest[4]['5%']
    if (pvalue < 0.05) and (adf < critical_value):
        print('The series is stationary')
    else:
        print('The series is NOT stationary')



#Overview
df = pd.read_csv("px-x-1003020000_201_20220907-163118.csv", sep=";")
for i, row in df.iterrows():
    df.at[i,'Monat'] = monthToNum(row["Monat"])
df["Date"] = df["Jahr"].astype(str)+"."+df["Monat"].astype(str)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
for i, row in df.iterrows():
    if row["Monat"] in {11, 12, 1, 2, 3, 4}:
        df.at[i, "Saison"] = "Winter"
    else:
        df.at[i, "Saison"] = "Summer"
sns.lineplot(data=df["Logiernaechte"])
plt.ylabel('Overnight Stays')
plt.show()

#Decomposition
df = df.rename(columns={"Logiernaechte": "Overnight Stays"})
ts = df["Overnight Stays"]
result = seasonal_decompose(ts, model='multiplicative')
result.plot()
plt.show()

#ARIMA, SARIMA
train = ts[ts.index <= pd.to_datetime("2021-08-01", format='%Y-%m-%d')]
test = ts[ts.index >= pd.to_datetime("2021-08-01", format='%Y-%m-%d')]
y = train

#Auto-arima
model = auto_arima(y)
print(model)
p = 3
d = 1
q = 2

#D-Order
seasonal = result.seasonal
check_stationarity(seasonal)
D = 2

#P-Order
plot_pacf(seasonal, lags=50)
plt.show()
P = 3

#Q-Order
plot_acf(seasonal, lags=50)
plt.show()
Q = 1

ARIMAmodel = ARIMA(y, order=(p, d, q))
ARIMAmodel = ARIMAmodel.fit()

y_arima_pred = ARIMAmodel.get_forecast(len(test.index))
y_arima_pred_df = y_arima_pred.conf_int(alpha=0.05)
y_arima_pred_df["Predictions"] = ARIMAmodel.predict(start=y_arima_pred_df.index[0], end=y_arima_pred_df.index[-1])
y_arima_pred_df.index = test.index
y_arima_pred_out = y_arima_pred_df["Predictions"]

arma_rmse = np.sqrt(mean_squared_error(test.values, y_arima_pred_df["Predictions"]))
print("RMSE: ", arma_rmse)

SARIMAXmodel = SARIMAX(y, order=(p, d, q), seasonal_order=(P, D, Q, 12))
SARIMAXmodel = SARIMAXmodel.fit()

y_sarima_pred = SARIMAXmodel.get_forecast(len(test.index))
y_sarima_pred_df = y_sarima_pred.conf_int(alpha=0.05)
y_sarima_pred_df["Predictions"] = SARIMAXmodel.predict(start=y_sarima_pred_df.index[0], end=y_sarima_pred_df.index[-1])
y_sarima_pred_df.index = test.index
y_sarima_pred_out = y_sarima_pred_df["Predictions"]

#Visualisation
plt.plot(train, color = "black", label='Train')
plt.plot(test, color = "red", label='Test')
plt.plot(y_arima_pred_out, color='Blue', label='ARIMA Predictions')
plt.plot(y_sarima_pred_out, color='Yellow', label='SARIMA Predictions')
plt.ylabel('Overnight Stays')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.title("Train/Test split for Overnight Stays in Meiringen")
plt.legend()
plt.show()

#Summer-Winter Trendline
df_saison = pd.read_csv("px-x-1003020000_201_20220907-163118.csv", sep=";")
for i, row in df_saison.iterrows():
    df_saison.at[i,'Monat'] = monthToNum(row["Monat"])
df_saison["Date"] = df_saison["Jahr"].astype(str)+"."+df_saison["Monat"].astype(str)
df_saison['Date'] = pd.to_datetime(df_saison['Date'])
for i, row in df_saison.iterrows():
    if row["Monat"] in {11, 12, 1, 2, 3, 4}:
        df_saison.at[i, "Saison"] = "Winter"
    else:
        df_saison.at[i, "Saison"] = "Summer"
sns.lineplot(x="Date", y="Logiernaechte", data=df_saison, hue="Saison")
plt.show()

years = list(range(2013, 2023))

df_winter = df_saison[df_saison["Saison"] == "Winter"]
df_winter = df_winter.resample('Y', on='Date').sum()
df_winter['Jahr'] = years
df_winter = df_winter.drop(["2022-12-31", "2021-12-31", "2020-12-31"])
sns.barplot(x="Jahr", y="Logiernaechte", data=df_winter, color="#1f77b4")
plt.ylabel('Overnight Stays')
plt.xlabel('Year')
plt.show()
sns.regplot(x="Jahr", y="Logiernaechte", data=df_winter, color="#1f77b4")
plt.ylim(0,)
plt.ylabel('Overnight Stays')
plt.xlabel('Year')
plt.tight_layout()
plt.show()

df_summer = df_saison[df_saison["Saison"] == "Summer"]
df_summer = df_summer.resample('Y', on='Date').sum()
df_summer['Jahr'] = years
df_summer = df_summer.drop(["2022-12-31", "2021-12-31", "2020-12-31"])
sns.barplot(x="Jahr", y="Logiernaechte", data=df_summer, color="#ff7f0e")
plt.ylabel('Overnight Stays')
plt.xlabel('Year')
plt.show()
sns.regplot(x="Jahr", y="Logiernaechte", data=df_summer, color="#ff7f0e")
plt.ylabel('Overnight Stays')
plt.xlabel('Year')
plt.ylim(0,)
plt.tight_layout()
plt.show()
