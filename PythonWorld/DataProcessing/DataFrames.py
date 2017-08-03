
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.options.display.max_rows = 7
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'

weather_2012_final = pd.read_csv('data/weather_2012.csv',
                                 index_col = 'Date/Time')

weather_2012_final['Temp (C)'].plot(figsize = (18, 6))

url_template = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID;=5415&Year;={year}&Month;={month}&timeframe;=1&submit;=Download+Data"

#Чтобы получить данные за март 2012
url = url_template.format(month = 3, year = 2012)
weather_mar2012 = pd.read_csv(url, skiprows = 15, index_col = 'Data/Time', parse_dates = True, encoding = 'latin1')

print(weather_mar2012)


#Построим график температуры
weather_mar2012["Temp (ÃÂ°C)"].plot(figsize = (15, 5))
plt.show()

weather_mar2012.columns = [
    u'Year', u'Month', u'Day', u'Time', u'Data Quality', u'Temp (C)',
    u'Temp Flag', u'Dew Point Temp (C)', u'Dew Point Temp Flag',
    u'Rel Hum (%)', u'Rel Hum Flag', u'Wind Dir (10s deg)', u'Wind Dir Flag',
    u'Wind Spd (km/h)', u'Wind Spd Flag', u'Visibility (km)', u'Visibility Flag',
    u'Stn Press (kPa)', u'Stn Press Flag', u'Hmdx', u'Hmdx Flag', u'Wind Chill',
    u'Wind Chill Flag', u'Weather']


#Много пустых столбцов можно удалить с помощью dropna

#axis = 1 означает удалить столбцы, а не строки. how = any удалить столбец, если хотя бы 1 значение пусто
#Остануться только столбцы с реальными данными

weather_mar2012 = weather_mar2012.dropna(axis = 1, how = 'any')
print(weather_mar2012[:5])

#Удалим Year/Month/Day/Time и DataQuality они нам не нужны

weather_mar2012 = weather_mar2012.drop(['Year', 'Month', 'Day', 'Time', 'Data Quality'], axis = 1)
print(weather_mar2012[:5])


#Дневной график температуры
temperatures = weather_mar2012[[u'Temp (C)']].copy()
temperatures.loc[:, 'Hour'] = weather_mar2012.index.hour
temperatures.groupby('Hour').aggregate(np.median).plot()
#Наибольшая температура по медиане приходится на 2 часа дня
plt.show()

###Получаем данные за год
#Берем данные за месяц

def download_weather_month(year, month):
    url = url_template.format(year=year, month=month)
    weather_data = pd.read_csv(url, skiprows=15, index_col='Date/Time', parse_dates=True)
    weather_data = weather_data.dropna(axis=1)
    weather_data.columns = [col.replace('\xb0', '') for col in weather_data.columns]
    weather_data = weather_data.drop(['Year', 'Day', 'Month', 'Time', 'Data Quality'], axis=1)
    return weather_data


print(download_weather_month(2012, 1)[:5])


#Теперь обьединим все месяца
data_by_month = [download_weather_month(2012, i) for i in range(1, 13)]

#обьединим dataframe с помощью pd.concat
#Теперь у нас будут данные за весь год

weather_2012 = pd.concat(data_by_month)
print(weather_2012)

#Сохраним результаты в CSV файл
weather_2012.to_csv('data/weather_2012.csv')



