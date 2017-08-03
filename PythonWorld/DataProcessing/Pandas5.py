
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.options.display.max_rows = 7
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'

weather_2012 = pd.read_csv('data/weather_2012.csv', parse_dates=True, index_col='Date/Time')
print(weather_2012[:5])



#Операции над строками в pandas
weather_description = weather_2012['Weather']
is_snowing = weather_description.str.contains('Snow')

print(is_snowing)

is_snowing.plot()
plt.show()


#Находим снежные месяца
#resample(M) - медиана температуры
weather_2012['Temp (C)'].resample('M').median().plot(kind = 'bar')
plt.show()

print(is_snowing.astype(int)[:10])


#Используем resample , чтобы найти процент времени, когда шёл снег
print(is_snowing.astype(int).resample('M').mean())

is_snowing.astype(int).resample('M').mean().plot(kind = 'bar')
plt.show()



###Строим графики температур и снежности вместе
#Можно обьединить эти 2 статистики в 1 DataFrame

temperature = weather_2012['Temp (C)'].resample('M').median()
is_snowing = weather_2012['Weathe'].str.contains('Snow')
snowiness = is_snowing.astype(int).resample('M').mean()

#Name the columns
temperature.name = 'Temperature'
snowiness.name = 'Snowiness'

#Снова используем concat , чтобы обьединить колонки в 1 DataFrame

stats = pd.concat([temperature, snowiness], axis = 1)
print(stats)

stats.plot(kind = 'bar')
plt.show()

#Т.к. масштаб выбран не правильно , это не ОК
#построим на 2 разных графиках

stats.plot(kind = 'bar', subplots = True, figsize = (15, 10))

